# MANIFEST

SCHEMA_VERSION: V3
PLANNING_ARCHITECTURE: SERIES_V1_12V
CURRENT_BOOK: 《长生者皆为薪柴》
CURRENT_PHASE: PHASE_I_我为什么会被吃
CURRENT_VOLUME: 第一卷·白骨山
CURRENT_ARC: ARC-V01-01
CANON_HORIZON: CH006
CURRENT_CANON_CHAPTER: CH006
CURRENT_SNAPSHOT: canon/snapshots/STATE_SNAPSHOT_V2.2.md
LATEST_STATE_DIFF: state/diffs/CH006_STATE_DIFF.md
CANON_KERNEL: canon/kernel/
WORLD_BIBLE: canon/WORLD_BIBLE.md
CULTIVATION_SYSTEM: canon/CULTIVATION_SYSTEM.md
FACTIONS_GEOGRAPHY: canon/FACTIONS_GEOGRAPHY.md
AUTHOR_TRUTH: tracking/AUTHOR_TRUTH.md
SERIES_MASTER_OUTLINE: planning/SERIES_MASTER_OUTLINE.md
VOLUME_BLUEPRINTS: planning/VOLUME_BLUEPRINTS.md
CURRENT_VOLUME_DETAIL: planning/volumes/V01_DETAIL.md
TRUTH_REVEAL_LADDER: planning/TRUTH_REVEAL_LADDER.md
CHARACTER_LONG_ARCS: planning/CHARACTER_LONG_ARCS.md
CURRENT_CONTEXT_CARD: tracking/CONTEXT_CARD.md
CURRENT_ROLLING_OUTLINE: planning/ROLLING_OUTLINE.md
SCENE_CARD_TEMPLATE: quality/SCENE_CARD_TEMPLATE.md
PUBLICATION_GATE: quality/PUBLICATION_GATE.md
CHAPTER_GATE: quality/CHAPTER_GATE.md
STYLE_GUIDE: style/STYLE_GUIDE.md
NEXT_CHAPTER: CH007
CANON_BRANCH: main
CANDIDATE_BRANCH: chapter/CH007
TRACKING_STATE_ROLE: projection

## Authority Order

1. 用户在当前交互中的明确决定/修订。
2. `main` 已确认正文 + `canon/CANON_CORE.md`。
3. `canon/WORLD_BIBLE.md` / `canon/CULTIVATION_SYSTEM.md` 等作者层硬世界规则。
4. `canon/kernel/` 规范化 Canon + `state/CHAPTER_LEDGER.md`。
5. Snapshot / State Diff（历史恢复与迁移依据）。
6. state/tracking 人类可读投影。
7. planning：总纲约束未来方向，但不得覆盖过去正文。

## Planning Authority

规划层内部优先级：

**Series Master 终点/底层命题 > Volume Blueprint 卷级功能 > Current Volume Detail > ARC_MAP 当前Arc > ROLLING_OUTLINE 短期章纲。**

如果短期因果与旧章号计划冲突，允许改章号/Arc节奏；如果连续剧情正在偏离卷级核心功能，必须显式重算而不是自然漂移。

## Writing Authority

规划层不能直接生成正文。正文必须经过：

**Rolling Outline → Scene Card → Published Prose Anchor → Write → Publication Gate → Continuity Precommit。**

Publication Gate 与 Continuity Gate 同为硬门；任一失败都不得交 Candidate。

## Current Publication Safeguards

- 正文禁止章节编号/Canon/FP等后台语言泄漏。
- 正常自然段优先2—5句；连续3个一句式叙述段默认 Publication FAIL。
- 禁止把 Rolling Outline 逐项扩写成测试报告式正文。
- 每章写前必须回读已发布正文作为 prose anchor。
- 必须检查高层胜利算法重复，不只检查具体招式重复。
- 配角必须拥有独立目标；进入场景前要能回答“如果陈缺不在，他今天会做什么”。

## Canon Policy

- `main` 只放已确认有效 Canon。
- Candidate 章节在用户确认前不得推进 Canon Horizon。
- 已发布正文不因后续规划改变而偷偷重写。
- Canon 状态改变优先关闭旧 temporal fact 并新增新 fact，不抹掉历史。
- UNKNOWN / SUSPECTS 不得自动升级成事实。
- Revision 必须执行 Change Impact Protocol。
- 作者层已经锁定的未来世界真相只能按 `TRUTH_REVEAL_LADDER` 分层进入正文，不能因为仓库里已经写明就让角色提前知道。

核心原则：**正文决定过去；Canon 描述真实世界；Tracking 描述现在；Outline 约束未来方向；Scene Card 隔离后台与小说；Publication Gate 保证成品像小说；Rolling Outline 服从真实因果。**
