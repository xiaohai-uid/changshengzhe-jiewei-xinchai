#!/usr/bin/env python3
"""Executable fail-closed validator for chapter Candidates.

This script does NOT try to replace literary judgment. It enforces what can be
enforced mechanically and verifies that the judgment-based reports actually
exist, PASS, and refer to the exact same Candidate bytes.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

RULE_ID_RE = re.compile(r"\b(?:WF|CAN|KNOW|CHAR|CAUSAL|POWER|SCENE|CAP|STYLE|END|PAY|ALG|MEM|PLOT|REV|LEN|FINAL)-\d{3}\b")
STATUS_ROW_RE = re.compile(r"^\|\s*([A-Z]+-\d{3})\s*\|\s*(PASS|NA|FAIL|UNKNOWN)\s*\|", re.M)
ASCII_LEFT = r"(?<![A-Za-z0-9_])"
ASCII_RIGHT = r"(?![A-Za-z0-9_])"

BACKEND_PATTERNS = {
    "chapter_id": re.compile(ASCII_LEFT + r"CH\d{3}" + ASCII_RIGHT, re.I),
    "canon": re.compile(ASCII_LEFT + r"CANON" + ASCII_RIGHT, re.I),
    "ledger": re.compile(ASCII_LEFT + r"Ledger" + ASCII_RIGHT, re.I),
    "state_diff": re.compile(r"State\s*Diff", re.I),
    "snapshot": re.compile(ASCII_LEFT + r"Snapshot" + ASCII_RIGHT, re.I),
    "author_chapter_ref": re.compile(r"(?:上一章|本章|前文|第[一二三四五六七八九十百0-9]+章)"),
}

AI_FINGERPRINTS = [
    "陈缺心里一沉",
    "他忽然明白",
    "原来如此",
    "真正的问题是",
    "深吸一口气",
    "微微一怔",
    "心头一颤",
    "意味深长",
    "空气仿佛凝固",
    "时间仿佛静止",
    "这不能证明",
    "这只能证明",
    "至少说明",
    "这不代表",
]

REQUIRED_GATE_REPORTS = {
    "post_draft": "quality/reviews/{chapter}_POST_DRAFT_AUDIT.md",
    "publication": "quality/reviews/{chapter}_PUBLICATION_GATE.md",
    "payoff": "quality/reviews/{chapter}_EXPECTATION_PAYOFF_GATE.md",
    "continuity": "quality/reviews/{chapter}_CONTINUITY_PRECOMMIT.md",
    "final": "quality/reviews/{chapter}_FINAL_DELIVERY.md",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def metadata(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for raw in text.splitlines():
        m = re.match(r"^\s*([A-Za-z][A-Za-z0-9_ /-]*):\s*(.*?)\s*$", raw)
        if m:
            key = re.sub(r"[^A-Za-z0-9]+", "_", m.group(1)).strip("_").upper()
            out[key] = m.group(2).strip()
    return out


def manifest_value(text: str, key: str) -> str | None:
    m = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", text, re.M)
    return m.group(1).strip() if m else None


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def prose_text(text: str) -> str:
    """Return prose-only text for scans that must ignore markdown titles."""
    return "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("#"))


def body_for_count(text: str) -> str:
    body = prose_text(text)
    return re.sub(r"[\s#*_>`~\-]", "", body)


def paragraphs(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip() and not p.lstrip().startswith("#")]


def is_dialogue(p: str) -> bool:
    s = p.lstrip()
    return s.startswith(("“", "‘", "「", "『", '"', "'"))


def sentence_count(p: str) -> int:
    n = len(re.findall(r"[。！？!?]", p)) + p.count("……")
    return max(n, 1)


def max_consecutive_one_sentence_narrative(paras: list[str]) -> int:
    best = cur = 0
    for p in paras:
        if not is_dialogue(p) and sentence_count(p) <= 1 and len(p) <= 90:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return best


def rule_ids_from_matrix(text: str) -> set[str]:
    return set(RULE_ID_RE.findall(text))


def coverage_from_audit(text: str) -> dict[str, str]:
    return {rid: status for rid, status in STATUS_ROW_RE.findall(text)}


def report_result(text: str) -> str | None:
    meta = metadata(text)
    for key in ("RESULT", "GATE_RESULT", "STATUS"):
        if key in meta and meta[key].upper() in {"PASS", "REWRITE", "BLOCKED", "FAIL"}:
            return meta[key].upper()
    m = re.search(r"(?:^|\n)\s*(?:result|gate_result)\s*:\s*(PASS|REWRITE|BLOCKED|FAIL)\b", text, re.I)
    return m.group(1).upper() if m else None


def check_report_binding(path: Path, revision: str, digest: str, errors: list[str]) -> None:
    text = read(path)
    meta = metadata(text)
    rev = meta.get("CANDIDATE_REVISION_ID")
    sha = meta.get("CANDIDATE_SHA256")
    result = report_result(text)
    if rev != revision:
        errors.append(f"{path}: candidate_revision_id={rev!r}, expected {revision!r}")
    if sha != digest:
        errors.append(f"{path}: candidate_sha256 mismatch")
    if result != "PASS":
        errors.append(f"{path}: result={result!r}, expected PASS")


def validate(chapter: str, candidate: Path, strict_delivery: bool) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    manifest_path = ROOT / "MANIFEST.md"
    workflow_path = ROOT / f"quality/workflow/{chapter}_WORKFLOW.md"
    matrix_path = ROOT / "quality/RULE_COVERAGE_MATRIX.md"
    memory_system_path = ROOT / "quality/MEMORY_ANCHOR_SYSTEM.md"
    memory_ledger_path = ROOT / "tracking/MEMORY_ANCHOR_LEDGER.md"
    receipt_path = ROOT / f"quality/receipts/{chapter}_CONTEXT_RECEIPT.md"
    scene_path = ROOT / f"quality/scene-cards/{chapter}_SCENE_CARD.md"

    for p in (manifest_path, workflow_path, matrix_path, memory_system_path, memory_ledger_path):
        if not p.exists():
            errors.append(f"missing required control file: {p.relative_to(ROOT)}")
    if errors:
        return errors, warnings

    manifest = read(manifest_path)
    if manifest_value(manifest, "PLANNING_ARCHITECTURE") != "SERIES_V2_8V_2M":
        errors.append("MANIFEST planning architecture is not SERIES_V2_8V_2M")

    if not candidate.exists():
        errors.append(f"missing Candidate: {candidate.relative_to(ROOT) if candidate.is_absolute() else candidate}")
        return errors, warnings

    text = read(candidate)
    scan_text = prose_text(text)
    digest = sha256_text(text)
    wc = len(body_for_count(text))
    if wc < 2800 or wc > 4000:
        errors.append(f"CAP-001: Candidate size {wc}, required 2800-4000")
    elif not 3200 <= wc <= 3600:
        warnings.append(f"Candidate size {wc}: valid hard range, outside normal 3200-3600 target")

    paras = paragraphs(text)
    run = max_consecutive_one_sentence_narrative(paras)
    if run >= 3:
        errors.append(f"STYLE-001/FM-003: max consecutive one-sentence narrative paragraphs = {run}")

    for name, pattern in BACKEND_PATTERNS.items():
        hits = list(pattern.finditer(scan_text))
        if hits:
            preview = ", ".join(repr(h.group(0)) for h in hits[:3])
            errors.append(f"STYLE-003 backend leak [{name}]: {preview}")

    ai_hits = {phrase: scan_text.count(phrase) for phrase in AI_FINGERPRINTS if phrase in scan_text}
    if ai_hits:
        warnings.append("AI/style fingerprint hits require human context review: " + str(ai_hits))

    workflow = metadata(read(workflow_path))
    revision = workflow.get("CANDIDATE_REVISION_ID", "")
    if not revision or revision.upper() in {"NONE", "PENDING"}:
        errors.append("WF-004: workflow has no frozen CANDIDATE_REVISION_ID")

    if strict_delivery:
        if not receipt_path.exists():
            errors.append(f"WF-001: missing {receipt_path.relative_to(ROOT)}")
        if not scene_path.exists():
            errors.append(f"WF-002: missing {scene_path.relative_to(ROOT)}")

        expected_workflow = {
            "POST_DRAFT_AUDIT": "PASS",
            "RULE_COVERAGE": "PASS",
            "FAILURE_REGRESSION": "PASS",
            "PUBLICATION_GATE": "PASS",
            "EXPECTATION_PAYOFF_GATE": "PASS",
            "CONTINUITY_PRECOMMIT": "PASS",
            "FINAL_DELIVERY_GATE": "PASS",
        }
        for key, expected in expected_workflow.items():
            if workflow.get(key, "").upper() != expected:
                errors.append(f"WF-003: {key}={workflow.get(key)!r}, expected PASS")
        if workflow.get("CURRENT_STATE", "").upper() not in {"FINAL_DELIVERY_PASS", "USER_REVIEW"}:
            errors.append(f"FINAL-005: CURRENT_STATE={workflow.get('CURRENT_STATE')!r}, not ready for delivery")

        reports: dict[str, Path] = {}
        for name, template in REQUIRED_GATE_REPORTS.items():
            p = ROOT / template.format(chapter=chapter)
            reports[name] = p
            if not p.exists():
                errors.append(f"missing gate report: {p.relative_to(ROOT)}")

        if revision and revision.upper() not in {"NONE", "PENDING"}:
            for p in reports.values():
                if p.exists():
                    check_report_binding(p, revision, digest, errors)

        post_path = reports.get("post_draft")
        if post_path and post_path.exists():
            matrix_rules = rule_ids_from_matrix(read(matrix_path))
            coverage = coverage_from_audit(read(post_path))
            missing = sorted(matrix_rules - set(coverage))
            bad = sorted(rid for rid, status in coverage.items() if status in {"FAIL", "UNKNOWN"})
            if missing:
                errors.append("FINAL-002: Rule Coverage missing Rule IDs: " + ", ".join(missing))
            if bad:
                errors.append("FINAL-002: Rule Coverage has FAIL/UNKNOWN: " + ", ".join(bad))

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chapter", help="e.g. CH007; defaults to MANIFEST NEXT_CHAPTER")
    parser.add_argument("--candidate", help="Candidate path; defaults to candidate/<CHAPTER>.md")
    parser.add_argument("--strict-delivery", action="store_true", help="require every delivery artifact and PASS")
    args = parser.parse_args()

    manifest = read(ROOT / "MANIFEST.md")
    chapter = args.chapter or manifest_value(manifest, "NEXT_CHAPTER")
    if not chapter or not re.fullmatch(r"CH\d{3}", chapter):
        print("ERROR: cannot resolve valid chapter id", file=sys.stderr)
        return 2

    candidate = Path(args.candidate) if args.candidate else ROOT / f"candidate/{chapter}.md"
    if not candidate.is_absolute():
        candidate = ROOT / candidate

    errors, warnings = validate(chapter, candidate, args.strict_delivery)
    print(f"chapter={chapter}")
    print(f"candidate={candidate.relative_to(ROOT) if candidate.is_relative_to(ROOT) else candidate}")
    for w in warnings:
        print(f"WARNING: {w}")
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        print("RESULT=FAIL")
        return 1
    print("RESULT=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
