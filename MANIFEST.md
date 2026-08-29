# MANIFEST

SCHEMA_VERSION: V5
PLANNING_ARCHITECTURE: SERIES_V2_8V_2M
TARGET_TOTAL_WORDS: ~2000000_CN_CHARS
PLANNING_RANGE_WORDS: 1900000-2100000_CN_CHARS
TARGET_VOLUMES: 8
TARGET_CHAPTERS: ~580-620
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
EXPECTATION_PAYOFF_GATE: quality/EXPECTATION_PAYOFF_GATE.md
CHAPTER_GATE: quality/CHAPTER_GATE.md
WORKFLOW_STATE_MACHINE: quality/WORKFLOW_STATE_MACHINE.md
CURRENT_WORKFLOW: quality/workflow/CH007_WORKFLOW.md
NARRATIVE_PATTERN_LEDGER: quality/NARRATIVE_PATTERN_LEDGER.md
COMMERCIAL_RESEARCH_BASELINE: quality/research/FANQIE_ZHIHU_COMMERCIAL_RESEARCH_2026-08-29.md
STYLE_GUIDE: style/STYLE_GUIDE.md
NEXT_CHAPTER: CH007
CANON_BRANCH: main
CANDIDATE_BRANCH: chapter/CH007
TRACKING_STATE_ROLE: projection

## Series Scale Decision

- 全书目标约200万字，不再采用旧350万—500万/12卷规划。
- 当前结构为8卷，约580—620章；单章仍以3200—3600字为常规目标。
- 若自然终局早于190万字，不为凑字数扩写重复Arc。
- 若规划将突破约210万字，必须先做Macro Drift Audit，证明新增篇幅来自真实人物/因果需要，而不是“还能写”。
- 压缩优先合并重复证明和相邻理念卷，不删除核心真相链与已承诺人物弧。

## Authority Order

1. 用户在当前交互中的明确决定/修订。
2. `main` 已确认正文 + `canon/CANON_CORE.md`。
3. `canon/WORLD_BIBLE.md` / `canon/CULTIVATION_SYSTEM.md` 等作者层硬世界规则。
4. `canon/kernel/` 规范化 Canon + `state/CHAPTER_LEDGER.md`。
5. Snapshot / State Diff（历史恢复与迁移依据）。
6. state/tracking 人类可读投影。
7. planning：总纲约束未来方向，但不得覆盖过去正文。
8. quality/research：只校准阅读体验与规划方法，不拥有 Canon 权威。

## Planning Authority

规划层内部优先级：

**Series Master终点/底层命题 > Volume Blueprint卷级功能 > Current Volume Detail > ARC_MAP当前Arc > ROLLING_OUTLINE短期章纲。**

如果短期因果与旧章号计划冲突，允许改章号/Arc节奏；如果连续剧情偏离卷级功能，必须显式重算。

商业阅读体验属于planning/quality层约束：可以改变未来事件节奏、收益结构、卷长和场景选择，但不能覆盖已发布事实、人物真实利益或世界硬规则。

## Writing Authority

规划层不能直接生成正文。正文必须经过：

**Rolling Outline → Context Receipt → Scene Card → Published Prose Anchor → Write → Publication Gate → Expectation/Payoff Gate → Continuity Precommit → User Review。**

并同步 `quality/WORKFLOW_STATE_MACHINE.md`。

Publication Gate、Expectation/Payoff Gate、Continuity Precommit三者同为硬门；任一失败都不得交Candidate。

## Current Publication Safeguards

- 正文禁止章节编号/Canon/FP等后台语言泄漏。
- 正常自然段优先2—5句；连续3个一句式叙述段默认Publication FAIL。
- 禁止把Rolling Outline逐项扩写成测试报告式正文。
- 每章写前必须回读已发布正文作为prose anchor。
- 必须检查高层胜利算法重复，不只检查具体招式重复。
- 配角必须拥有独立目标；进入场景前能回答“如果陈缺不在，他今天会做什么”。
- 每章/小周期检查“期待→兑现→升级”，避免长期只留下秘密与危险。
- 代价可以污染收益，但禁止习惯性把重大获得立即清零。
- 信息可以是奖励，但不能长期成为唯一主奖励。
- 没有Context Receipt / Scene Card / Gate PASS记录，不允许交完整正文。

## Current Candidate Status

- CH007前一Candidate：`REWRITE`，未进入Canon。
- 当前CH007工作流：`BLOCKED`。
- 前一Candidate中新姓名、编号、南二具体器物/流程、逃亡执行细节没有Canon权威。
- CH007必须从CH006 Canon Horizon重新执行完整冷启动与门禁。

## Canon Policy

- `main`只放已确认有效Canon。
- Candidate章节在用户确认前不得推进Canon Horizon。
- 已发布正文不因后续规划改变而偷偷重写。
- Canon状态改变优先关闭旧temporal fact并新增新fact，不抹掉历史。
- UNKNOWN / SUSPECTS不得自动升级成事实。
- Revision必须执行Change Impact Protocol。
- 作者层锁定的未来世界真相只能按`TRUTH_REVEAL_LADDER`分层进入正文。

核心原则：**正文决定过去；Canon描述真实世界；Tracking描述现在；Outline约束未来；Scene Card隔离后台与小说；Publication Gate保证成品像小说；Expectation/Payoff Gate保证高压之后有真实累计；Rolling Outline服从真实因果；Workflow State Machine防止跳步交稿；200万目标防止情绪与理念被过度拉长。**
