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
CURRENT_ARC: ARC-V01-02
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
CURRENT_WORKFLOW: NONE_UNTIL_CH026_START
NARRATIVE_PATTERN_LEDGER: quality/NARRATIVE_PATTERN_LEDGER.md
COMMERCIAL_RESEARCH_BASELINE: quality/research/FANQIE_ZHIHU_COMMERCIAL_RESEARCH_2026-08-29.md
STYLE_GUIDE: style/STYLE_GUIDE.md
CHAPTER_VALIDATOR: tools/chapter_gate.py
CHAPTER_VALIDATOR_TESTS: tools/test_chapter_gate.py
CHAPTER_CI_WORKFLOW: .github/workflows/chapter-quality.yml
CANDIDATE_PATH_PATTERN: candidate/CHxxx.md
NEXT_CHAPTER: CH026
CANON_BRANCH: main
CANDIDATE_BRANCH: NONE_UNTIL_CH026_START
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
- CH021《看他能撑多久》：原Candidate文本在后续连续写作中作为上一章基线使用，并于本次用户明确“今天的任务结束了，把它们都提交了”后晋升Canonical。
- CH022《这块牌，不必还了》：Assistant按用户审阅意见修订后的版本，用户继续后续章节并于本次结束工作指令中正式晋升Canonical。
- CH023《废根也得湿着送》：Assistant版本经用户继续后续章节并在本次结束工作指令中晋升Canonical。
- CH024《雨水没这个味》：Assistant版本经用户继续后续章节并在本次结束工作指令中晋升Canonical。
- CH025《别让这筐死透了》：Assistant版本经用户结束当日工作并要求全部提交后晋升Canonical。

### Canon manuscript latest

`manuscript/volume-01-baigushan/CH025-别让这筐死透了.md`

### CH021—CH025 核心变化

- CH020七日底账后果兑现：顾长槐已看记录，并通过灰衣弟子启动三日南坡资源隔离观察。
- 三日不碰活苗/后棚、暂停药粥且无新截气，陈缺已有腰腿/整体耐劳仍未退回早期水平；累计性身体资产成立，但正式炼身机制仍UNKNOWN。
- 顾长槐没有清退陈缺，而把异常稳定产出重新定价为周期性南坡验工用途；陈缺现持外棚木牌+“验”牌，南坡半日从外棚折工。
- 南坡验工形成真实签单追责；CH024陈缺首次验出返软根并触发整篓返工。
- 关键青须草完成后棚→东畦→起收纵向链：木气逐步收敛、苦味/药性变重；木气强度≠当前药性价值已确认，完整机制仍UNKNOWN。
- 新鲜青篓边损仍短暂保留木气；CH025多株分散微取可勉强聚出极薄一层，但气散、难收束、会分神/针麻并险些造成工作错分。
- 青篓边损有明确西山下游用途，要求保持湿润；黑盆死透腐料无木气且直接倒坑。
- CH024亲见黑陶壶苦腥液用于重新浇湿青料；CH025反证其不是赵石反应唯一条件：未新浇黑壶液的隔夜湿边根也会让赵石轻度右手僵紧。
- “西山怕湿料死透”目前只是反复出现的生产事实/赵石工作解释；最终用途、触发成分、是否涉及木气全部UNKNOWN。

## Current Arc / Next Status

- 当前Arc：ARC-V01-02 · 药圃与真炼身，接近阶段收束。
- CH026主驱动力：GROWTH + PAYOFF + STATUS。
- 最自然下一步：把已有累计性真炼身兑现成第一项更具体、可持续使用的身体能力/工作阈值，同时保留食物、经络、资源或监督成本。
- CH026不得连续第四章追黑壶/湿料；赵石湿料发作、南坡纯验货、完整三转实验均进入短期冷却。
- 若CH026自然完成“真炼身可见、可持续但不安全”的阶段兑现，可收束ARC-V01-02并向ARC-V01-03《坏掉的虫种》过渡。
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

核心原则：**正文决定过去；用户明确最终发布拥有最高权威；Canon描述真实世界；Tracking描述现在；Outline约束未来；人物只知道他们该知道的东西。**