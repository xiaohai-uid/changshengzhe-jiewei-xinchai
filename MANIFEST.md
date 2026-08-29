# MANIFEST

SCHEMA_VERSION: V9
PLANNING_ARCHITECTURE: SERIES_V2_8V_2M
TARGET_TOTAL_WORDS: ~2000000_CN_CHARS
PLANNING_RANGE_WORDS: 1900000-2100000_CN_CHARS
TARGET_VOLUMES: 8
TARGET_CHAPTERS: ~580-620
CURRENT_BOOK: 《长生者皆为薪柴》
CURRENT_PHASE: PHASE_I_我为什么会被吃
CURRENT_VOLUME: 第一卷·白骨山
CURRENT_ARC: ARC-V01-01
CANON_HORIZON: CH009
CURRENT_CANON_CHAPTER: CH009
CURRENT_SNAPSHOT: canon/snapshots/STATE_SNAPSHOT_V2.2.md
LATEST_STATE_DIFF: state/diffs/CH009_STATE_DIFF.md
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
MEMORY_ANCHOR_SYSTEM: quality/MEMORY_ANCHOR_SYSTEM.md
MEMORY_ANCHOR_LEDGER: tracking/MEMORY_ANCHOR_LEDGER.md
SCENE_CARD_TEMPLATE: quality/SCENE_CARD_TEMPLATE.md
RULE_COVERAGE_MATRIX: quality/RULE_COVERAGE_MATRIX.md
POST_DRAFT_AUDIT: quality/POST_DRAFT_AUDIT.md
PUBLICATION_GATE: quality/PUBLICATION_GATE.md
EXPECTATION_PAYOFF_GATE: quality/EXPECTATION_PAYOFF_GATE.md
FINAL_DELIVERY_GATE: quality/FINAL_DELIVERY_GATE.md
FAILURE_MEMORY: quality/FAILURE_MEMORY.md
CHAPTER_GATE: quality/CHAPTER_GATE.md
WORKFLOW_STATE_MACHINE: quality/WORKFLOW_STATE_MACHINE.md
CURRENT_WORKFLOW: NONE_UNTIL_CH010_START
NARRATIVE_PATTERN_LEDGER: quality/NARRATIVE_PATTERN_LEDGER.md
COMMERCIAL_RESEARCH_BASELINE: quality/research/FANQIE_ZHIHU_COMMERCIAL_RESEARCH_2026-08-29.md
STYLE_GUIDE: style/STYLE_GUIDE.md
CHAPTER_VALIDATOR: tools/chapter_gate.py
CHAPTER_VALIDATOR_TESTS: tools/test_chapter_gate.py
CHAPTER_CI_WORKFLOW: .github/workflows/chapter-quality.yml
CANDIDATE_PATH_PATTERN: candidate/CHxxx.md
NEXT_CHAPTER: CH010
CANON_BRANCH: main
CANDIDATE_BRANCH: NONE_UNTIL_CH010_START
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
4. `canon/kernel/` 压实Canon + `canon/kernel/patches/` 未压实增量 + `state/CHAPTER_LEDGER.md`。
5. Snapshot / State Diff。
6. state/tracking人类可读投影。
7. planning：约束未来，不覆盖过去正文。
8. quality/research：校准阅读体验，不拥有Canon权威。

### Canon Kernel Overlay

- 压实Kernel当前截至CH007。
- 未压实Canonical patches：`CH008.jsonl`、`CH009.jsonl`。
- 冷启动必须加载从 `CANON_KERNEL_COMPACTED_THROUGH` 之后到 `CANON_HORIZON` 的全部patch。
- patch不是第二套Canon，而是已确认正文的规范化增量。
- 只读主Kernel而漏patch，视为LOAD失败。

## Planning Authority

**Series Master终点/底层命题 > Volume Blueprint卷级功能 > Current Volume Detail > ARC_MAP当前Arc > ROLLING_OUTLINE短期章纲。**

短期因果与旧章号冲突时允许调整；人物真实发展优先于过时规划。

## Writing Authority

每章必须经过：

**Rolling Outline → Context Receipt → Scene Card（含Memory第9问） → Published Prose Anchor → Write → Freeze Revision → Post-Draft Audit（含Memory） → Publication Gate → Expectation/Payoff Gate → Continuity Precommit → Final Delivery Gate → Candidate Branch Commit → External CI Success on Exact HEAD → User Review。**

任何关键步骤缺失即FAIL CLOSED。

所有写后PASS必须绑定同一 `candidate_revision_id` 与 `candidate_sha256`；正文改动后旧PASS失效。

### External CI

展示完整Candidate前必须实际确认：
1. workflow=`Chapter Quality Gate`；
2. branch=当前候选分支；
3. conclusion=`success`；
4. run.head_sha=候选分支当前HEAD；
5. CI通过后候选正文/报告未再修改。

## Rule Audit Authority

- `quality/RULE_COVERAGE_MATRIX.md`：交稿级硬规则总登记。
- `quality/FAILURE_MEMORY.md`：ACTIVE历史失败每章强制回归。
- `quality/POST_DRAFT_AUDIT.md`：写后证据化自审。
- `quality/FINAL_DELIVERY_GATE.md`：验证最终稿就是被审版本。
- `quality/MEMORY_ANCHOR_SYSTEM.md`：记忆锚与反强造规则。
- `tracking/MEMORY_ANCHOR_LEDGER.md`：只记录已进入Canon、值得保护/回响的锚。
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
- 代价可以污染收益，但不能习惯性清零。
- 信息不能长期成为唯一主奖励。
- 没有Context Receipt / Scene Card / Post-Draft / Rule Coverage / Final Delivery / exact-head CI success，不允许交正文。

## Current Canon / Next Status

- CH009《先借半日》：用户在通过门禁的候选后回复“好的，写下一章”，视为确认上一章并继续，已晋升Canon。
- Canon Horizon：CH009。
- CH009确认资产/变化：
  - 陈缺南二工作入口继续并承担木筹/废料记录；
  - 赵石主动争工作，原本即时药房方向被南二借下半日，午后最终处置未解；
  - 陈缺二验未再耗真气伪装，获得“先留南二、三日后复验”的具体阶段处置；
  - TARGET在陈缺二验期间与老马随废料下去，章末老马已回而TARGET尚未回；是否逃脱成功UNKNOWN。
- 韩鸦CH009未出场，因此截至CH009章末并不知道赵石借工、陈缺二验结果或TARGET未归，后续必须建立消息渠道。
- Memory：MA-005在CH009增值为ECHOED；MA-009“先借半日”新增PLANTED。Arc强行动场面缺口明显缩小，但待收束审计。
- 下一章：CH010。
- CH010必须先处理TARGET未归这一现实后果；不得跳过直接进入新测试。

## Canon Policy

- `main`只承认用户已确认/已发布正文和对应Canon。
- Candidate在用户确认前不得推进Canon Horizon。
- 已发布正文不得因规划调整静默Retcon。
- UNKNOWN / SUSPECTS不得自动升级成事实。
- 作者层长期真相严格服从Truth Reveal Ladder。
- 每章晋升写Kernel patch；每5章Snapshot/每10章Audit可执行Kernel Compaction。

核心原则：**正文决定过去；Canon描述真实世界；Tracking描述现在；Outline约束未来；Scene Card隔离后台与小说；Post-Draft Audit负责写后找错；Expectation/Payoff保证追读与累积；Memory Anchor保证人物/场面/关系能被记住；Rule Coverage保证无孤儿规则；Failure Memory防止同错复发；Final Delivery + External CI保证交稿版本就是被审版本。**
