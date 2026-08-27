# LOAD ORDER V3

每次用户说“继续 / 写下一章”时，采用分层冷启动，不整书重读。

## 必读 HOT

1. `PROJECT_RULES.md`
2. `MANIFEST.md`
3. `canon/CANON_CORE.md`
4. `tracking/CONTEXT_CARD.md`
5. `planning/ARC_MAP.md` 当前 Arc + `planning/ROLLING_OUTLINE.md` 当前章
6. 最近 1—3 个 `tracking/chapter-records/`，必要时读取上章结尾全文
7. `style/STYLE_GUIDE.md`
8. `quality/CHAPTER_GATE.md`

## 定点读取 PERMANENT/WARM

根据本章合同中的永久 ID，只读取相关：
- `canon/kernel/ENTITIES.jsonl`
- `FACTS.jsonl`
- `KNOWLEDGE.jsonl`
- `TIMELINE.jsonl`
- `RELATIONSHIPS.jsonl`
- `PLOTS.jsonl`
- `PROMISES.jsonl`
- `INFO_GAPS.jsonl`

遇到旧事实争议，再按 `source_chapter` / Fact ID / Entity ID / FP-P-S ID 回查 Chapter Record 或正式正文。禁止因为“不确定”就默认补全。

## Context Receipt

起草 Candidate 前创建/刷新 `quality/receipts/CHxxx_CONTEXT_RECEIPT.md`，记录实际读取依赖。关键 Canon 源缺失时，本章标 BLOCKED/UNSAFE，不能假装已完成连续性检查。

## 写作流程

LOAD → CONTEXT RECEIPT → CAUSAL CHECK → REPETITION/PATTERN CHECK → PREWRITE GATE → WRITE → PRECOMMIT → EXTRACT CANDIDATE → 用户确认 → CANON PROMOTION → POSTCOMMIT → NEXT CAUSAL HOOK。

旧卷纲与真实正文因果冲突时，以已发生正文和当前 Canon 为准。