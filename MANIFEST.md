# MANIFEST

SCHEMA_VERSION: V7
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
RULE_COVERAGE_MATRIX: quality/RULE_COVERAGE_MATRIX.md
POST_DRAFT_AUDIT: quality/POST_DRAFT_AUDIT.md
PUBLICATION_GATE: quality/PUBLICATION_GATE.md
EXPECTATION_PAYOFF_GATE: quality/EXPECTATION_PAYOFF_GATE.md
FINAL_DELIVERY_GATE: quality/FINAL_DELIVERY_GATE.md
FAILURE_MEMORY: quality/FAILURE_MEMORY.md
CHAPTER_GATE: quality/CHAPTER_GATE.md
WORKFLOW_STATE_MACHINE: quality/WORKFLOW_STATE_MACHINE.md
CURRENT_WORKFLOW: quality/workflow/CH007_WORKFLOW.md
NARRATIVE_PATTERN_LEDGER: quality/NARRATIVE_PATTERN_LEDGER.md
COMMERCIAL_RESEARCH_BASELINE: quality/research/FANQIE_ZHIHU_COMMERCIAL_RESEARCH_2026-08-29.md
STYLE_GUIDE: style/STYLE_GUIDE.md
CHAPTER_VALIDATOR: tools/chapter_gate.py
CHAPTER_VALIDATOR_TESTS: tools/test_chapter_gate.py
CHAPTER_CI_WORKFLOW: .github/workflows/chapter-quality.yml
CANDIDATE_PATH_PATTERN: candidate/CHxxx.md
NEXT_CHAPTER: CH007
CANON_BRANCH: main
CANDIDATE_BRANCH: chapter/CH007-v2
TRACKING_STATE_ROLE: projection

## Series Scale Decision

- 全书目标约200万字，不再采用旧350万—500万/12卷规划。
- 当前结构为8卷，约580—620章；单章仍以3200—3600字为常规目标。
- 若自然终局早于190万字，不为凑字数扩写重复Arc。
- 若规划将突破约210万字，必须先做Macro Drift Audit。
- 压缩优先合并重复证明和相邻理念卷，不删除核心真相链与已承诺人物弧。

## Authority Order

1. 用户在当前交互中的明确决定/修订。
2. `main` 已确认正文 + `canon/CANON_CORE.md`。
3. `canon/WORLD_BIBLE.md` / `canon/CULTIVATION_SYSTEM.md` 等作者层硬世界规则。
4. `canon/kernel/` 规范化Canon + `state/CHAPTER_LEDGER.md`。
5. Snapshot / State Diff。
6. state/tracking人类可读投影。
7. planning：约束未来，不覆盖过去正文。
8. quality/research：只校准阅读体验，不拥有Canon权威。

## Planning Authority

**Series Master终点/底层命题 > Volume Blueprint卷级功能 > Current Volume Detail > ARC_MAP当前Arc > ROLLING_OUTLINE短期章纲。**

短期因果与旧章号冲突时允许改章号/Arc节奏；连续偏离卷级功能必须显式重算。

商业阅读体验可以改变未来事件节奏、收益结构、卷长和场景选择，但不能覆盖已发布事实、人物利益或世界硬规则。

## Writing Authority

规划层不能直接生成正文。正文必须经过：

**Rolling Outline → Context Receipt → Scene Card → Published Prose Anchor → Write → Freeze Revision → Post-Draft Audit → Publication Gate → Expectation/Payoff Gate → Continuity Precommit → Final Delivery Gate → Candidate Branch Commit → External CI Success on Exact HEAD → User Review。**

并同步 `quality/WORKFLOW_STATE_MACHINE.md`。

以下均为交稿硬门：
- Post-Draft Audit
- Publication Gate
- Expectation/Payoff Gate
- Continuity Precommit
- Final Delivery Gate
- **GitHub Actions `Chapter Quality Gate` 对候选分支当前精确 HEAD commit 的 conclusion = success**

任何一项未PASS不得交Candidate。

所有写后PASS必须绑定同一 `candidate_revision_id` 与 `candidate_sha256`。正文修改后按Final Delivery失效规则重跑；候选分支HEAD一旦发生变化，旧CI success自动失效，必须等待新HEAD重新验证。

### External CI 不是自我证明

候选工作流文件不能自行填写“CI通过”来获得交稿权。

在把完整正文展示给用户前，作者系统必须读取GitHub Actions实际运行结果，并确认：

1. workflow = `Chapter Quality Gate`；
2. branch = 当前 `CANDIDATE_BRANCH`；
3. conclusion = `success`；
4. workflow run `head_sha` = 候选分支当前HEAD；
5. CI通过后候选正文/报告未再修改。

只有上述外部证据成立，运行时才允许从 `FINAL_DELIVERY_PASS` 进入 `USER_REVIEW`。为了保持CI验证的HEAD不变，这个运行时转换不要求在交稿前再提交一次workflow文件。

## Rule Audit Authority

- `quality/RULE_COVERAGE_MATRIX.md`：交稿级硬规则总登记；每条规则必须有责任Gate和证据。
- `quality/FAILURE_MEMORY.md`：用户已指出/系统已识别的漏检失败，ACTIVE项每章强制回归测试。
- `quality/POST_DRAFT_AUDIT.md`：写完后的证据化自审。
- `quality/FINAL_DELIVERY_GATE.md`：验证最终交给用户的版本确实是被审过的版本。
- `tools/chapter_gate.py`：机械规则与产物/版本一致性校验器。
- `.github/workflows/chapter-quality.yml`：外部执行环境，防止只靠作者自报PASS。

规则新增但未进入Rule Coverage Matrix，视为流程配置不完整。

## Current Publication Safeguards

- 正文禁止章节编号/Canon/FP等后台语言泄漏。
- 正常自然段优先2—5句；连续3个一句式叙述段默认FAIL。
- 禁止把Rolling Outline逐项扩写成正文。
- 每章写前回读Published Prose Anchor。
- 检查高层胜利算法重复。
- 配角必须有独立目标。
- 每章/小周期检查“期待→兑现→升级”。
- 代价可以污染收益，但不能习惯性清零。
- 信息不能长期成为唯一主奖励。
- 没有Context Receipt / Scene Card / Post-Draft Audit / Rule Coverage / Final Delivery PASS，不允许交完整正文。
- Gate只能通过证据，不接受“脑内检查过”。
- Gate通过后改正文，旧PASS按影响范围自动失效。
- **没有候选分支精确HEAD的绿色GitHub Actions，不允许交完整正文。**

## Current Candidate Status

- CH007前一Candidate：`REWRITE`，未进入Canon。
- 旧 `chapter/CH007` 分支属于此前失败Candidate时代的历史分支，不再作为当前候选工作面。
- 当前候选分支：`chapter/CH007-v2`，从当前main重新建立。
- 当前CH007工作流：`BLOCKED`。
- 前一Candidate中新姓名、编号、南二具体器物/流程、逃亡执行细节没有Canon权威。
- CH007必须从CH006 Canon Horizon重新执行V3+Executable完整门禁。

## Canon Policy

- `main`只放已确认有效Canon。
- Candidate章节在用户确认前不得推进Canon Horizon。
- 已发布正文不因后续规划改变而偷偷重写。
- Canon状态改变优先关闭旧temporal fact并新增new fact，不抹掉历史。
- UNKNOWN / SUSPECTS不得自动升级成事实。
- Revision必须执行Change Impact Protocol。
- 作者层锁定的未来世界真相只能按`TRUTH_REVEAL_LADDER`分层进入正文。

核心原则：**正文决定过去；Canon描述真实世界；Tracking描述现在；Outline约束未来；Scene Card隔离后台与小说；Post-Draft Audit负责写后找错；Rule Coverage保证没有孤儿规则；Failure Memory防止同错复发；Final Delivery保证交稿版本就是审查版本；Executable Validator + GitHub Actions阻断可机械识别的漏检与伪PASS；200万目标防止情绪与理念被过度拉长。**
