#!/usr/bin/env python3
import tempfile
import unittest
from pathlib import Path

import chapter_gate as gate


class ChapterGateTests(unittest.TestCase):
    def test_detects_short_paragraph_waterfall(self):
        text = "第一句。\n\n第二句。\n\n第三句。\n\n第四段有两句。这里继续。"
        self.assertEqual(gate.max_consecutive_one_sentence_narrative(gate.paragraphs(text)), 3)

    def test_dialogue_does_not_count_as_narrative_waterfall(self):
        text = "“一句。”\n\n“第二句。”\n\n“第三句。”\n\n叙述有两句。这里继续。"
        self.assertEqual(gate.max_consecutive_one_sentence_narrative(gate.paragraphs(text)), 0)

    def test_rule_matrix_extracts_rule_ids(self):
        text = "| WF-001 | a |\n| STYLE-003 | b |\n| PAY-004 | c |"
        self.assertEqual(gate.rule_ids_from_matrix(text), {"WF-001", "STYLE-003", "PAY-004"})

    def test_coverage_extracts_status(self):
        text = "| WF-001 | PASS | evidence |\n| PAY-004 | NA | no power use |"
        self.assertEqual(gate.coverage_from_audit(text), {"WF-001": "PASS", "PAY-004": "NA"})

    def test_candidate_hash_changes_on_edit(self):
        self.assertNotEqual(gate.sha256_text("甲"), gate.sha256_text("乙"))

    def test_backend_patterns_detect_repository_language(self):
        text = "本章里出现了CH007和Canon。"
        hit_names = {name for name, pattern in gate.BACKEND_PATTERNS.items() if pattern.search(text)}
        self.assertIn("chapter_id", hit_names)
        self.assertIn("canon", hit_names)
        self.assertIn("author_chapter_ref", hit_names)

    def test_markdown_chapter_heading_is_not_scanned_as_prose_backend_reference(self):
        text = "# 《长生者皆为薪柴》\n\n## 第八章：好药不能当废料\n\n陈缺把药篓放下。"
        prose = gate.prose_without_headings(text)
        self.assertNotIn("第八章", prose)
        hit_names = {name for name, pattern in gate.BACKEND_PATTERNS.items() if pattern.search(prose)}
        self.assertNotIn("author_chapter_ref", hit_names)

    def _write(self, root: Path, rel: str, content: str) -> Path:
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def _strict_fixture(self, root: Path) -> Path:
        chapter = "CH007"
        revision = "CH007-R01"
        candidate_text = "药香贴着石壁散开，少年没有停步。" * 190
        candidate = self._write(root, f"candidate/{chapter}.md", candidate_text)
        digest = gate.sha256_text(candidate_text)

        self._write(root, "MANIFEST.md", "PLANNING_ARCHITECTURE: SERIES_V2_8V_2M\nNEXT_CHAPTER: CH007\n")
        self._write(
            root,
            f"quality/workflow/{chapter}_WORKFLOW.md",
            "\n".join(
                [
                    "CHAPTER: CH007",
                    "CURRENT_STATE: FINAL_DELIVERY_PASS",
                    f"CANDIDATE_REVISION_ID: {revision}",
                    "POST_DRAFT_AUDIT: PASS",
                    "RULE_COVERAGE: PASS",
                    "FAILURE_REGRESSION: PASS",
                    "PUBLICATION_GATE: PASS",
                    "EXPECTATION_PAYOFF_GATE: PASS",
                    "CONTINUITY_PRECOMMIT: PASS",
                    "FINAL_DELIVERY_GATE: PASS",
                ]
            )
            + "\n",
        )
        self._write(
            root,
            "quality/RULE_COVERAGE_MATRIX.md",
            "| Rule ID | hard rule |\n|---|---|\n| WF-001 | receipt |\n| STYLE-003 | no backend leakage |\n",
        )
        self._write(root, f"quality/receipts/{chapter}_CONTEXT_RECEIPT.md", "chapter: CH007\nstatus: PASS\n")
        self._write(root, f"quality/scene-cards/{chapter}_SCENE_CARD.md", "scene: test\nstatus: PASS\n")

        common = f"candidate_revision_id: {revision}\ncandidate_sha256: {digest}\nresult: PASS\n"
        post = common + "\n| Rule ID | Status | Evidence | Note |\n|---|---|---|---|\n| WF-001 | PASS | receipt | ok |\n| STYLE-003 | PASS | 0 hit | ok |\n"
        self._write(root, f"quality/reviews/{chapter}_POST_DRAFT_AUDIT.md", post)
        self._write(root, f"quality/reviews/{chapter}_PUBLICATION_GATE.md", common)
        self._write(root, f"quality/reviews/{chapter}_EXPECTATION_PAYOFF_GATE.md", common)
        self._write(root, f"quality/reviews/{chapter}_CONTINUITY_PRECOMMIT.md", common)
        self._write(root, f"quality/reviews/{chapter}_FINAL_DELIVERY.md", common)
        return candidate

    def test_strict_delivery_end_to_end_passes_complete_fixture(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            candidate = self._strict_fixture(root)
            old_root = gate.ROOT
            gate.ROOT = root
            try:
                errors, _warnings = gate.validate("CH007", candidate, strict_delivery=True)
            finally:
                gate.ROOT = old_root
            self.assertEqual(errors, [])

    def test_strict_delivery_rejects_stale_report_hash_after_edit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            candidate = self._strict_fixture(root)
            candidate.write_text(candidate.read_text(encoding="utf-8") + "石门又响了一声。", encoding="utf-8")
            old_root = gate.ROOT
            gate.ROOT = root
            try:
                errors, _warnings = gate.validate("CH007", candidate, strict_delivery=True)
            finally:
                gate.ROOT = old_root
            self.assertTrue(any("candidate_sha256 mismatch" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
