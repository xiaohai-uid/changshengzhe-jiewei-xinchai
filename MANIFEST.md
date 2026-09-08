# MANIFEST

SCHEMA_VERSION: V10
PLANNING_ARCHITECTURE: SERIES_V2_8V_2M
TARGET_TOTAL_WORDS: ~2000000_CN_CHARS
PLANNING_RANGE_WORDS: 1900000-2100000_CN_CHARS
TARGET_VOLUMES: 8
TARGET_CHAPTERS: ~580-620
CURRENT_BOOK: 《长生者皆为薪柴》
CURRENT_PHASE: PHASE_I_我为什么会被吃
CURRENT_VOLUME: 第一卷·白骨山
CURRENT_ARC: ARC-V01-03_WORKING_AFTER_CH026_CANDIDATE
CANON_HORIZON: CH025
CURRENT_CANON_CHAPTER: CH025
CURRENT_SNAPSHOT: canon/snapshots/STATE_SNAPSHOT_V3.0.md
LATEST_STATE_DIFF: state/diffs/CH025_STATE_DIFF.md
LATEST_CONTINUITY_AUDIT: quality/reviews/CONTINUITY_AUDIT_CH020.md
CANON_KERNEL: canon/kernel/
CANON_KERNEL_COMPACTED_THROUGH: CH007
CANON_KERNEL_PATCH_DIR: canon/kernel/patches/
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
CHAPTER_LEDGER_BASE: state/CHAPTER_LEDGER.md
CHAPTER_LEDGER_APPEND_DIR: state/ledger-appends/
MEMORY_ANCHOR_SYSTEM: quality/MEMORY_ANCHOR_SYSTEM.md
MEMORY_ANCHOR_LEDGER: tracking/MEMORY_ANCHOR_LEDGER.md
CHAPTER_TITLE_STANDARD: quality/CHAPTER_TITLE_STANDARD.md
SCENE_CARD_TEMPLATE: quality/SCENE_CARD_TEMPLATE.md
RULE_COVERAGE_MATRIX: quality/RULE_COVERAGE_MATRIX.md
POST_DRAFT_AUDIT: quality/POST_DRAFT_AUDIT.md
PUBLICATION_GATE: quality/PUBLICATION_GATE.md
EXPECTATION_PAYOFF_GATE: quality/EXPECTATION_PAYOFF_GATE.md
FINAL_DELIVERY_GATE: quality/FINAL_DELIVERY_GATE.md
FAILURE_MEMORY: quality/FAILURE_MEMORY.md
CHAPTER_GATE: quality/CHAPTER_GATE.md
WORKFLOW_STATE_MACHINE: quality/WORKFLOW_STATE_MACHINE.md
CURRENT_WORKFLOW: quality/workflow/CH027_WORKFLOW.md
NARRATIVE_PATTERN_LEDGER: quality/NARRATIVE_PATTERN_LEDGER.md
COMMERCIAL_RESEARCH_BASELINE: quality/research/FANQIE_ZHIHU_COMMERCIAL_RESEARCH_2026-08-29.md
STYLE_GUIDE: style/STYLE_GUIDE.md
CHAPTER_VALIDATOR: tools/chapter_gate.py
CHAPTER_VALIDATOR_TESTS: tools/test_chapter_gate.py
CHAPTER_CI_WORKFLOW: .github/workflows/chapter-quality.yml
CANDIDATE_PATH_PATTERN: candidate/CHxxx.md
NEXT_CHAPTER: CH027
CANON_BRANCH: main
CANDIDATE_BRANCH: chapter/CH027
TRACKING_STATE_ROLE: projection

## Series Scale Decision

- 全书目标约200万字；8卷、约580—620章。
- 常规单章3200—3600字，硬区间2800—4000字。
- 不为凑字数重复已完成的世界观证明、修炼验证或情绪循环。
- 若自然终局早于190万字，不人为扩写；若规划将突破约210万字，先做Macro Drift Audit。

## Authority Order

1. 用户当前明确决定/修订。
2. `main` 已确认正文 + `canon/CANON_CORE.md`。
3. `canon/WORLD_BIBLE.md` / `canon/CULTIVATION_SYSTEM.md` 等作者层硬规则。
4. `canon/kernel/` 压实Canon + `canon/kernel/patches/` 未压实增量 + `state/CHAPTER_LEDGER.md` + `state/ledger-appends/`。
5. Snapshot / State Diff。
6. state/tracking人类可读投影。
7. planning：约束未来，不覆盖过去正文。
8. quality/research：校准阅读体验，不拥有Canon权威。

### Canon Kernel Overlay

- 压实Kernel当前截至CH007。
- 未压实Canonical patches：CH008—CH025，均位于 `canon/kernel/patches/CHxxx.jsonl`。
- 冷启动必须加载从 `CANON_KERNEL_COMPACTED_THROUGH` 之后到 `CANON_HORIZON` 的全部patch。
- patch不是第二套Canon，而是已确认正文的规范化增量。
- `state/CHAPTER_LEDGER.md` 为早期基础Ledger；CH012以后新增不可撤销事实使用 `state/ledger-appends/CHxxx.md` 追加，逻辑上仍是同一Append-Only Chapter Ledger。
- 只读主Kernel而漏patch，或只读基础Ledger而漏append，均视为LOAD失败。

## Planning Authority

**Series Master终点/底层命题 > Volume Blueprint卷级功能 > Current Volume Detail > ARC_MAP当前Arc > ROLLING_OUTLINE短期章纲。**

短期因果与旧章号冲突时允许调整；人物真实发展优先于过时规划。

## Writing Authority

默认Assistant新章必须经过：

**Rolling Outline → Context Receipt → Scene Card（含Memory第9问） → Published Prose Anchor → Write → Freeze Revision → Post-Draft Audit（含Memory） → Book Identity Gate → Publication Gate（含Title Attraction Review） → Expectation/Payoff Gate → Continuity Precommit → Final Delivery Gate → Candidate Branch Commit → External CI Success on Exact HEAD → User Review。**

任何关键步骤缺失默认FAIL CLOSED。

用户对完整正文作出明确最终决定，或在连续审阅后以“今天任务结束/全部提交”等明确发布指令要求晋升当前已展示版本时，按 Authority Order #1 处理：正文不得被Gate静默改写；Canonical promotion以用户最终发布意图为准，后续章节恢复正常Gate。

## External CI Boundary

- Assistant Candidate正常交稿时必须真实确认 `Chapter Quality Gate` 对候选分支精确HEAD成功。
- 用户明确最终发布的正文/当前版本不因缺少此前候选CI而被否决，但不得伪造CI成功记录。
- 任何未实际运行的CI不得声称PASS。

## Rule Audit Authority

- `quality/RULE_COVERAGE_MATRIX.md`：交稿级硬规则总登记。
- `quality/FAILURE_MEMORY.md`：ACTIVE历史失败回归。
- `quality/POST_DRAFT_AUDIT.md`：写后证据化自审。
- `quality/FINAL_DELIVERY_GATE.md`：验证最终稿与被审版本一致。
- `quality/MEMORY_ANCHOR_SYSTEM.md` / `tracking/MEMORY_ANCHOR_LEDGER.md`：记忆锚与反强造规则。
- `quality/CHAPTER_TITLE_STANDARD.md`：章节名质量与点击欲。
- `tools/chapter_gate.py` + GitHub Actions：机械规则、产物、版本一致性校验。

## Current Publication Safeguards

- 正文禁止后台语言泄漏。
- 正常自然段优先2—5句；连续3个无必要一句叙述段默认FAIL。
- 禁止Rolling Outline逐项扩写。
- 每章写前回读Published Prose Anchor。
- 配角必须有独立目标与行动。
- 检查最近高层破局算法重复。
- 每章/短周期检查“期待→兑现→升级”。
- 代价可以污染收益，但不能习惯性清零。
- 信息不能长期成为唯一主奖励。
- UNKNOWN / SUSPECTS / BELIEVES必须分层；角色自述不能自动升级为世界事实。
- Book Identity Gate必须保持成长/生存博弈/规则破解/世界真相至少两项同时成立。

## Current Canon / Publication Status

- CH016《我就给你单开一行》：Assistant版本经用户结束当日工作并要求提交后晋升Canonical。
- CH017《现在不值这块地》：用户直接改写最终版，Canonical。
- CH018《这车，我不碰》：用户直接改写最终版，Canonical。
- CH019《干得快，就再多干一畦》：Assistant版本经用户结束当日工作并要求提交后晋升Canonical。
- CH020《这点力气，已经记进去了》：用户直接改写最终版，Canonical。
- CH021《看他能撑多久》：原Candidate文本在后续连续写作中作为上一章基线使用，并于用户明确结束工作并要求提交后晋升Canonical。
- CH022《这块牌，不必还了》：Assistant修订版随后晋升Canonical。
- CH023《废根也得湿着送》：Canonical。
- CH024《雨水没这个味》：Canonical。
- CH025《别让这筐死透了》：Canonical。
- CH026《第九趟》：当前会话已展示、exact-head CI通过的Working Candidate；用户已要求继续下一章，因此作为CH027直接工作前章，但尚未写入main Canon。

### Canon manuscript latest

`manuscript/volume-01-baigushan/CH025-别让这筐死透了.md`

### Working predecessor

`candidate/CH026.md` on `chapter/CH026`, revision CH026-R1-5C14075E, external CI run 34177034887 success on exact head fc327787bd3c1b6442d9c71164ae38f5878e28bf.

## Current Arc / Next Status

- main Canon仍处于ARC-V01-02末段，Canon Horizon=CH025。
- 连续写作工作状态：CH026 Candidate已经完成“无新气也能越过旧第六趟衰竭阈值”的阶段兑现，并以三包同日青须根在药房出现不同虫反应开启ARC-V01-03接口。
- CH027主驱动力：MYSTERY + IMPACT + STATUS USE。
- CH027只允许把异常推进到一个可追溯生产差异进入正式封样；禁止确认石缸水为元凶、灵脉衰竭、返灵/归息或母虫根因。
- 西山湿料、赵石再次发作、完整三转实验、南坡纯验货继续冷却。
- 下一次Snapshot边界：CH030。
- 下一次Continuity Audit边界：CH030。

## Canon Policy

- `main`只承认用户已确认/已发布正文和对应Canon。
- 已发布正文不得因规划调整静默Retcon。
- UNKNOWN / SUSPECTS / BELIEVES不得自动升级成事实。
- 人物自述与客观事实分层记录。
- 作者层长期真相严格服从Truth Reveal Ladder。
- 每章晋升写Kernel patch；每5章Snapshot；每10章Continuity Audit。
- 已发布旧章标题不因风格统一批量追改，除非用户明确要求。
- Working Candidate可作为用户明确“继续”后的下一章直接因果基线，但不得在用户最终发布前伪装成main Canon；若前章Candidate被否决/重写，所有依赖它的后续Candidate必须失效重算。

核心原则：**正文决定过去；用户明确最终发布拥有最高权威；Canon描述真实世界；Tracking描述现在；Outline约束未来；人物只知道他们该知道的东西。**