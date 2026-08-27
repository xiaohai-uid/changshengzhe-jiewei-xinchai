# MANIFEST

CURRENT_BOOK: 《长生者皆为薪柴》
ARCHITECTURE_VERSION: 2.0
CURRENT_VOLUME: 第一卷·白骨山
CURRENT_CANON_CHAPTER: CH004
CURRENT_SNAPSHOT: canon/snapshots/STATE_SNAPSHOT_V2.0.md
LATEST_STATE_DIFF: state/diffs/CH004_STATE_DIFF.md
AUTHORITATIVE_TRACKING_STATE: tracking/TRACKING_STATE.json
CURRENT_CONTEXT_CARD: tracking/CONTEXT_CARD.md
AUTHOR_TRUTH_VIEW: tracking/AUTHOR_TRUTH.md
READER_KNOWN_VIEW: tracking/READER_KNOWN.md
CURRENT_ROLLING_OUTLINE: planning/ROLLING_OUTLINE.md
CHAPTER_GATE: quality/CHAPTER_GATE.md
NEXT_CHAPTER: CH005
CANON_BRANCH: main
WORK_BRANCH: chapter/CH005

## Canon Policy

- `main` 只放已确认有效 Canon。
- 正文一旦进入 `main`，不因后续规划改变而偷偷重写事实。
- 章节修改必须同步检查状态增量、知识矩阵、关系、伏笔和后续影响。
- Snapshot 是阶段完整状态；Snapshot 之后的最新有效状态 = Snapshot + 所有后续 State Diff。

## Tracking Policy

- 已发布正文与只追加 Chapter Ledger 是最高事实依据。
- `tracking/TRACKING_STATE.json` 是当前状态的单一结构化权威；LIVE / KNOWLEDGE / RELATIONSHIP / PLOT 和 tracking Markdown 为人类可读视图。
- `AUTHOR_TRUTH.md` 中 UNKNOWN 不得为了续写方便被临时补成答案。
- `READER_KNOWN.md` 与 `KNOWLEDGE_MATRIX.md` 分工：前者追踪读者知道什么，后者追踪角色知道什么。
- 每章认可后必须完成 POSTCOMMIT 才允许开始下一章。
