# MANIFEST

SCHEMA_VERSION: V3
CURRENT_BOOK: 《长生者皆为薪柴》
CURRENT_VOLUME: 第一卷·白骨山
CURRENT_ARC: ARC-V01-01
CANON_HORIZON: CH004
CURRENT_CANON_CHAPTER: CH004
CURRENT_SNAPSHOT: canon/snapshots/STATE_SNAPSHOT_V2.0.md
LATEST_STATE_DIFF: state/diffs/CH004_STATE_DIFF.md
CANON_KERNEL: canon/kernel/
CURRENT_CONTEXT_CARD: tracking/CONTEXT_CARD.md
CURRENT_ROLLING_OUTLINE: planning/ROLLING_OUTLINE.md
NEXT_CHAPTER: CH005
CANON_BRANCH: main
CANDIDATE_BRANCH: chapter/CH005
TRACKING_STATE_ROLE: projection

## Authority Order

1. 用户在当前交互中的明确决定/修订。
2. `main` 已确认正文 + `canon/CANON_CORE.md`。
3. `canon/kernel/` 规范化 Canon + `state/CHAPTER_LEDGER.md`。
4. Snapshot / State Diff（历史恢复与迁移依据）。
5. state/tracking 人类可读投影。
6. planning（只建议未来，从不覆盖过去）。

## Canon Policy

- `main` 只放已确认有效 Canon。
- Candidate 章节在用户确认前不得推进 Canon Horizon。
- 已发布正文不因后续规划改变而偷偷重写。
- Canon 状态改变优先关闭旧 temporal fact 并新增新 fact，不抹掉历史。
- UNKNOWN / SUSPECTS 不得自动升级成事实。
- Revision 必须执行 Change Impact Protocol。

核心原则：**正文决定过去；Canon Kernel描述可查询事实；Tracking描述现在；Planning只建议未来。**