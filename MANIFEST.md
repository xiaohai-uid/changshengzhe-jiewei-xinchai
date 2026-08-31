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
CANON_HORIZON: CH015
CURRENT_CANON_CHAPTER: CH015
CURRENT_SNAPSHOT: canon/snapshots/STATE_SNAPSHOT_V2.4.md
LATEST_STATE_DIFF: state/diffs/CH015_STATE_DIFF.md
LATEST_CONTINUITY_AUDIT: quality/reviews/CONTINUITY_AUDIT_CH010.md
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
CURRENT_WORKFLOW: NONE_UNTIL_CH016_START
NARRATIVE_PATTERN_LEDGER: quality/NARRATIVE_PATTERN_LEDGER.md
COMMERCIAL_RESEARCH_BASELINE: quality/research/FANQIE_ZHIHU_COMMERCIAL_RESEARCH_2026-08-29.md
STYLE_GUIDE: style/STYLE_GUIDE.md
CHAPTER_VALIDATOR: tools/chapter_gate.py
CHAPTER_VALIDATOR_TESTS: tools/test_chapter_gate.py
CHAPTER_CI_WORKFLOW: .github/workflows/chapter-quality.yml
CANDIDATE_PATH_PATTERN: candidate/CHxxx.md
NEXT_CHAPTER: CH016
CANON_BRANCH: main
CANDIDATE_BRANCH: NONE_UNTIL_CH016_START
TRACKING_STATE_ROLE: projection

## Series Scale Decision

- 全书目标约200万字；8卷、约580—620章。
- 常规单章3200—3600字，硬区间2800—4000字。
- 不为凑字数重复已经完成的世界观证明或情绪循环。
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
- 未压实Canonical patches：`CH008.jsonl`、`CH009.jsonl`、`CH010.jsonl`、`CH011.jsonl`、`CH012.jsonl`、`CH013.jsonl`、`CH014.jsonl`、`CH015.jsonl`。
- 冷启动必须加载从 `CANON_KERNEL_COMPACTED_THROUGH` 之后到 `CANON_HORIZON` 的全部patch。
- patch不是第二套Canon，而是已确认正文的规范化增量。
- `state/CHAPTER_LEDGER.md` 为早期基础Ledger；CH012以后新增不可撤销事实使用 `state/ledger-appends/CHxxx.md` 追加，逻辑上仍是同一Append-Only Chapter Ledger。
- 只读主Kernel而漏patch，或只读基础Ledger而漏append，均视为LOAD失败。

## Planning Authority

**Series Master终点/底层命题 > Volume Blueprint卷级功能 > Current Volume Detail > ARC_MAP当前Arc > ROLLING_OUTLINE短期章纲。**

短期因果与旧章号冲突时允许调整；人物真实发展优先于过时规划。

## Writing Authority

默认每章必须经过：

**Rolling Outline → Context Receipt → Scene Card（含Memory第9问） → Published Prose Anchor → Write → Freeze Revision → Post-Draft Audit（含Memory） → Book Identity Gate → Publication Gate（含Title Attraction Review） → Expectation/Payoff Gate → Continuity Precommit → Final Delivery Gate → Candidate Branch Commit → External CI Success on Exact HEAD → User Review。**

任何关键步骤缺失即FAIL CLOSED。

**用户直接提供并明确声明为最终定稿的完整章节文本属于 Authority Order 第1级。此时正文不得被Gate静默改写；质量系统只记录偏离与未来回归风险，Canonical promotion以用户明确最终文本为准。**

所有写后PASS必须绑定同一 `candidate_revision_id` 与正文SHA；正文或最终标题改动后旧PASS失效。

### External CI

展示完整Assistant Candidate前必须实际确认：
1. workflow=`Chapter Quality Gate`；
2. branch=当前候选分支；
3. conclusion=`success`；
4. run.head_sha=候选分支当前HEAD；
5. CI通过后候选正文/报告未再修改。

用户直接提供最终正文时，该CI规则不用于否决用户已经明确发布的文字；但应在记录中标记 `USER_FINAL_OVERRIDE`，后续章节继续恢复正常Gate。

## Rule Audit Authority

- `quality/RULE_COVERAGE_MATRIX.md`：交稿级硬规则总登记。
- `quality/FAILURE_MEMORY.md`：ACTIVE历史失败每章强制回归。
- `quality/POST_DRAFT_AUDIT.md`：写后证据化自审。
- `quality/FINAL_DELIVERY_GATE.md`：验证最终稿就是被审版本。
- `quality/MEMORY_ANCHOR_SYSTEM.md`：记忆锚与反强造规则。
- `tracking/MEMORY_ANCHOR_LEDGER.md`：只记录已进入Canon、值得保护/回响的锚。
- `quality/CHAPTER_TITLE_STANDARD.md`：章节名质量与商业点击欲；最终标题属于交稿版本的一部分。
- `tools/chapter_gate.py` + GitHub Actions：机械规则、产物、版本一致性和伪PASS拦截。

## Current Publication Safeguards

- 正文禁止后台语言泄漏。
- 正常自然段优先2—5句；连续3个一句叙述段默认FAIL。
- 禁止Rolling Outline逐项扩写。
- 每章写前回读Published Prose Anchor。
- 配角必须有独立目标和行动。
- 检查最近高层破局算法重复。
- 每章/短周期检查“期待→兑现→升级”。
- 每章检查Memory第9问，允许 `NO NEW ANCHOR`；Arc收束执行MEM-006。
- 记忆锚回响必须增值；禁止为名场面硬造金句/口头禅/象征物。
- **章节名不得只概括“本章发生了什么”；最终标题必须至少生成8个跨家族候选并执行Title Attraction Review。默认优先危险台词、异常事实、冲突结果、具体悬念或直接问句。用户已明确要求后续标题持续采用CH014/CH015这种更具点击欲的方向。**
- 代价可以污染收益，但不能习惯性清零。
- 信息不能长期成为唯一主奖励。
- Book Identity Gate：去掉专名后仍应明显承载本书的成长/生存博弈/规则破解/世界真相中的至少两项，核心冲突应来自本世界既有规则。
- Assistant Candidate没有Context Receipt / Scene Card / Post-Draft / Rule Coverage / Final Delivery / exact-head CI success，不允许交正文。
- 用户最终定稿可以覆盖上述交稿偏好，但覆盖只对该已明确章节有效，不自动修改未来写作标准；用户明确提出的长期标题方向除外，已写入Title标准和本Manifest。

## Current Canon / Next Status

- CH015《虫没长，伤倒先好了》：Assistant候选通过 exact-head CI 后，用户提供完整改写版并明确声明“最终版，把它提交了”。因此以**用户最终文本**作为唯一Canonical正文，Assistant候选不得覆盖。
- Canon manuscript：`manuscript/volume-01-baigushan/CH015-虫没长，伤倒先好了.md`。
- Canon Horizon：CH015。
- Latest Snapshot：`canon/snapshots/STATE_SNAPSHOT_V2.4.md`（CH015五章边界Snapshot）。
- 当前Arc：ARC-V01-02 · 药圃与真炼身。
- CH015确认变化：
  - 三日复验正式执行，银针两次仍只有极轻微反应，延续“体内动静极弱但非完全无反应”；
  - 陈缺右臂可举过肩约半寸，筋肉恢复被顾长槐亲自确认，重负能力仍弱；
  - 顾长槐没有把陈缺扣回药房里间，而是将其从三日候工正式转为药圃外棚药工；
  - 陈缺获得带“外棚”字样与药房暗红印的小木牌，以及正式药工食额；午时已实际吃到新增粗面饼与温热药粥；
  - 白绳不摘、黑点保留，未来七日改由药圃连续记录腕检与伤势脉案并送药房；
  - 赵石较此前更枯瘦，黑陶罐经过时右腕暗痕加深、右手明显抽搐；具体刺激物/机制仍UNKNOWN；
  - 赵石主动用南二借工记录争取离开药房里间，被准去西侧药渣棚三日试用，仍受药房控制；
  - 赵石“南二半日抬过几十只重药篓”为角色当场自述，不升级为客观精确数量事实；
  - 陈缺无虫真修、活木截气和真气→肉身工作假设仍未被药房确认。
- 下一章：CH016。最自然因果是处理“正式药工身份 + 稳定食额 + 七日连续恢复记录”形成的新资源闭环与暴露矛盾；不再重复三日复验、同类微截实验或单纯右臂再抬高一点。

## Canon Policy

- `main`只承认用户已确认/已发布正文和对应Canon。
- Candidate在用户确认前不得推进Canon Horizon；用户直接提供并明确标注最终正文除外。
- 已发布正文不得因规划调整静默Retcon。
- UNKNOWN / SUSPECTS不得自动升级成事实。
- 人物自述与客观事实分层记录；角色说出的精确数字不因进入最终正文自动升级为作者层事实，除非叙事/其他证据确认。
- 作者层长期真相严格服从Truth Reveal Ladder。
- 每章晋升写Kernel patch；每5章Snapshot；每10章Continuity Audit。
- 已发布旧章标题不因风格统一批量追改，除非用户明确要求。

核心原则：**正文决定过去；用户明确最终文本拥有最高发布权威；Canon描述真实世界；Tracking描述现在；Outline约束未来；Scene Card隔离后台与小说；Book Identity保证每章仍然属于《长生者皆为薪柴》；Title Attraction保证目录本身有追读欲；Post-Draft/Payoff/Continuity/Final Delivery/External CI共同保证交付质量。**
