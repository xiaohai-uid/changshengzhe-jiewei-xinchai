# LOAD ORDER V10

每次用户说“继续 / 写下一章”时采用分层冷启动。目标同时保证：上一章因果、当前Arc、当前卷终点、全书真相方向、正式小说文风、期待/兑现方向、**记忆锚与人物辨识度**，以及写后审查与可执行交稿门禁都被加载。

## A. 每章必读 HOT

1. `PROJECT_RULES.md`
2. `MANIFEST.md`
3. `tracking/CONTEXT_CARD.md`
4. `planning/ARC_MAP.md` 当前Arc
5. `planning/ROLLING_OUTLINE.md` 当前章
6. 当前卷细纲相关部分：`planning/volumes/V01_DETAIL.md`
7. 最近1—3个 `tracking/chapter-records/`；必要时回读上章结尾全文
8. `style/STYLE_GUIDE.md`
9. `quality/SCENE_CARD_TEMPLATE.md`
10. `quality/MEMORY_ANCHOR_SYSTEM.md`
11. `tracking/MEMORY_ANCHOR_LEDGER.md`
12. `quality/CHAPTER_GATE.md`
13. `quality/WORKFLOW_STATE_MACHINE.md`
14. `quality/RULE_COVERAGE_MATRIX.md`
15. `quality/POST_DRAFT_AUDIT.md`
16. `quality/PUBLICATION_GATE.md`
17. `quality/EXPECTATION_PAYOFF_GATE.md`
18. `quality/FINAL_DELIVERY_GATE.md`
19. `quality/FAILURE_MEMORY.md`
20. `quality/NARRATIVE_PATTERN_LEDGER.md`

当前卷发生重要商业节奏重算时，定点读取：
`quality/research/FANQIE_ZHIHU_COMMERCIAL_RESEARCH_2026-08-29.md`。

### HOT完整性硬规则

Context Receipt必须记录上述质量规则的版本/路径。缺失 `MEMORY_ANCHOR_SYSTEM / MEMORY_ANCHOR_LEDGER / RULE_COVERAGE / POST_DRAFT / FINAL_DELIVERY / FAILURE_MEMORY` 任一项，本章不得进入LOADED。

---

## A2. Published Prose Anchor（每章强制）

起草前回读至少2段已发布且质量稳定的正文，优先最近章节与CH001—CH003。

校准：
- 自然段长度；
- 动作/观察/心理合段方式；
- 对话密度；
- 推理如何藏进行为；
- 世界内部语言。

Candidate出现短句瀑布、提纲扩写、研究报告腔时，必须重新回到Prose Anchor，不只靠抽象规则修补。

---

## A3. Expectation / Payoff Anchor（每章强制）

写前必须知道：
1. EXPECTATION：读者具体在等陈缺得到/做到/改变什么；
2. PAYOFF：本章负责兑现、部分兑现还是推进条件；
3. UPGRADE：兑现后新问题怎样从获得自然长出。

如果只能回答“别死 / 别暴露 / 看下一关”，且前面已连续高压，先回规划层重算。

---

## A4. Memory Anchor Check（每章强制检查，不强制新增）

写前读取 `quality/MEMORY_ANCHOR_SYSTEM.md` 与 `tracking/MEMORY_ANCHOR_LEDGER.md`。

必须知道：
1. 本章是否自然有记忆锚候选；
2. 若无，Scene Card明确写 `NO NEW ANCHOR`；
3. 若调用已有锚，为什么这次意义会增加/改变；
4. 当前Arc还缺哪个人物/场面记忆残余；
5. 是否存在“为了补记忆点硬造金句/口头禅/象征物”的风险。

普通章节允许没有新锚；Arc收束必须执行MEM-006四项检查。

---

## B. 书级 WARM / PERMANENT

Arc切换、每5章Snapshot、每10章Audit、新世界观/境界/势力时定点读取：

- `canon/CANON_CORE.md`
- `canon/WORLD_BIBLE.md`
- `canon/CULTIVATION_SYSTEM.md`
- `canon/FACTIONS_GEOGRAPHY.md`
- `tracking/AUTHOR_TRUTH.md`
- `planning/SERIES_MASTER_OUTLINE.md`
- `planning/VOLUME_BLUEPRINTS.md`
- `planning/TRUTH_REVEAL_LADDER.md`
- `planning/CHARACTER_LONG_ARCS.md`

原则：短期因果决定怎么发生；卷纲决定为什么值得；总纲决定最终方向；期待/兑现决定为什么继续读；Memory Anchor决定什么值得长期记住；Rule Coverage决定交稿前有没有漏规则；External CI证明这些产物真的被执行器检查过。

---

## C. Canon Kernel 定点读取 + Incremental Patch Overlay

根据本章涉及永久ID读取压实Kernel：
- ENTITIES
- FACTS
- KNOWLEDGE
- TIMELINE
- RELATIONSHIPS
- PLOTS
- PROMISES
- INFO_GAPS

然后必须读取 `MANIFEST.md`：
- `CANON_KERNEL_COMPACTED_THROUGH`
- `CANON_KERNEL_PATCH_DIR`
- `CANON_HORIZON`

若 `CANON_HORIZON` 晚于 `CANON_KERNEL_COMPACTED_THROUGH`，必须再读取压实点之后到当前Horizon的所有：

`canon/kernel/patches/CHxxx.jsonl`

这些patch与压实Kernel共同构成当前有效Canon；不得只读旧JSONL而漏掉最新已发布章节。

### Patch优先级

- 已发布正文仍是最高事实源；
- patch是已发布正文的规范化增量，不拥有静默Retcon权；
- 同一主题出现Temporal变化时，以更晚有效记录作为“当前状态”，旧事实保留历史意义；
- UNKNOWN/SUSPECTS不会因为patch存在自动升级；必须读取knowledge状态。

有争议时按source_chapter/Fact ID/patch id回查正文。禁止因为“不确定”默认补全。

Kernel patch协议：`canon/kernel/patches/README.md`。

---

## D. 新概念读取规则

### 新境界
读取 `CULTIVATION_SYSTEM` 对应层；正文只给当前场景所需最小尺度。

### 新势力/地域
读取 `FACTIONS_GEOGRAPHY` 与当前卷Blueprint。

### 推进世界真相
检查 `TRUTH_REVEAL_LADDER`，不得越层。

### 核心人物重大选择
检查 `CHARACTER_LONG_ARCS`。

### 推进能力/身份/资源兑现
检查来源、组织利益、耐久残余与成本，禁止为了“有代价”立即清零。

### 调用旧记忆锚
检查 `MEMORY_ANCHOR_LEDGER` 当前意义、最近回响和下一次回响条件。若没有新增意义，不调用。

---

## E. Context Receipt

起草前创建/刷新 `quality/receipts/CHxxx_CONTEXT_RECEIPT.md`。

至少登记：
- Canon Horizon；
- Kernel compacted-through与已加载patch列表；
- SERIES_V2_8V_2M确认；
- 当前Arc/Volume；
- Fact/Knowledge/FP-P-S；
- 最近正文锚；
- Published Prose Anchor；
- 当前卷细纲；
- 新境界/势力/真相层；
- EXPECTATION/PAYOFF/UPGRADE；
- Memory Anchor System版本；
- 本章可能调用的Anchor IDs / `NO PLANNED ECHO`；
- 当前Arc Memory Gap；
- Rule Coverage版本；
- Failure Memory版本；
- Workflow当前状态；
- 当前候选分支名。

关键源失败：BLOCKED/UNSAFE。

---

## F. Scene Isolation

Rolling Outline不能直接展开成正文。

必须先生成 `quality/scene-cards/CHxxx_SCENE_CARD.md`。Scene Card只保留人物欲望、现场阻力、有限信息、选择、现实收益、代价、净变化，以及第9问的记忆候选。

Scene Card像任务列表：不得进入WRITE。

`NO NEW ANCHOR`是合法答案；“为了本章一定要有一句名台词”不是合法Scene Card目标。

---

## G. 完整写作流程

**LOAD → MACRO ALIGNMENT → CONTEXT RECEIPT → CAUSAL CHECK → REPETITION/PATTERN CHECK → SCENE CARD → PREWRITE → WRITE → MIDWRITE → FREEZE REVISION → POST-DRAFT AUDIT（含Memory Anchor Audit） → PUBLICATION → EXPECTATION/PAYOFF → CONTINUITY PRECOMMIT → FINAL DELIVERY → CANDIDATE BRANCH COMMIT → EXTERNAL CI PASS → USER REVIEW → CANON PROMOTION（含Memory Anchor Ledger Diff + Canon Kernel Patch） → POSTCOMMIT → NEXT CAUSAL HOOK。**

严格同步 `quality/workflow/CHxxx_WORKFLOW.md`。

### MACRO ALIGNMENT 必答

1. 属于哪个Arc？
2. 推进卷级哪个核心问题？
3. 保护/推进哪条人物弧或真相层？
4. 读者在等待什么兑现？
5. 删掉本章会损失什么？
6. 是否重复已经完成的证明/情绪？
7. 本章是否自然承担某个记忆锚的建立/回响？没有也可以，但要明确。

---

## H. 写后审查（强制）

正文完成后不是“顺手看一遍”，而是必须：

1. 冻结 `candidate_revision_id` 与 `candidate_sha256`；
2. 生成 `CHxxx_POST_DRAFT_AUDIT.md`；
3. 对 `RULE_COVERAGE_MATRIX` 逐条取证，包含MEM类Rule IDs；
4. 执行 Memory Anchor Audit，判断新锚候选、旧锚增值、人物辨识度和强造风险；
5. 执行 `FAILURE_MEMORY` ACTIVE回归测试；
6. 后续Gate全部绑定同一revision/SHA；
7. 执行Final Delivery Clean Read；
8. 把最终Candidate及全部审计产物提交当前候选分支；
9. 提交后不再修改，进入External CI。

正文修改后按 `FINAL_DELIVERY_GATE` 失效规则重跑。

---

## I. Candidate 展示硬条件

完整正文只有在**运行时External CI PASS**后才允许展示。

必须同时满足：
- Context Receipt存在；
- Scene Card存在；
- Post-Draft Audit = PASS；
- Rule Coverage = PASS，MEM类Rule IDs无缺项；
- Publication = PASS；
- Expectation/Payoff = PASS；
- Continuity = PASS；
- Failure Regression = PASS；
- Final Delivery = PASS；
- 所有结果绑定同一revision/SHA；
- Candidate与报告已提交 `MANIFEST.md` 指定候选分支；
- GitHub Actions workflow = `Chapter Quality Gate`；
- Actions conclusion = `success`；
- Actions `head_sha` = 当前候选分支HEAD；
- validator tests与strict delivery validation步骤均成功；
- CI后没有新commit。

任一缺失：不得交稿。

`USER_REVIEW`是CI验证后的运行时状态，不需要为它再写一个commit，否则会改变HEAD并使刚通过的CI失效。

---

## J. Canon Promotion / Compaction

用户确认正文后：

1. 正文写入main manuscript；
2. 更新Chapter Ledger / State Diff / Chapter Record / projections；
3. 对尚未压实的Canon事实写 `canon/kernel/patches/CHxxx.jsonl`；
4. 执行Memory Anchor Diff；
5. 更新Manifest Horizon与下一章；
6. 每5章Snapshot或每10章Audit时可把patch压实进主Kernel JSONL，并推进 `CANON_KERNEL_COMPACTED_THROUGH`。

禁止为了省事在每章重写大型Kernel JSONL导致截断/覆盖风险；也禁止创建patch后不把它纳入冷启动。

---

## K. 可执行校验器职责边界

`tools/chapter_gate.py` 可以硬检查：
- 架构版本；
- Candidate存在；
- 2800—4000硬字数；
- 连续一句式叙述段；
- 后台语言泄漏；
- Receipt/Scene/Review报告是否存在；
- Memory Anchor System / Ledger是否存在；
- workflow Gate状态；
- revision/SHA是否一致；
- Rule Coverage是否缺项或存在FAIL/UNKNOWN，包括MEM类Rule IDs。

它**不能100%判断**：
- 人物是否真正立体；
- 因果是否具有文学上的最佳自然度；
- 爽感是否恰到好处；
- 对话是否足够有魅力；
- 一个场面是否真的会被读者多年记住。

这些仍由Post-Draft/Publication/Payoff/Final Clean Read进行判断，但报告缺失、版本不一致或自报流程未完成时，程序会阻断。

---

## L. 冲突优先级

已发布正文事实 > Canon Core / World Bible > 当前有效人物状态（压实Kernel + 未压实patch） > 卷级终点 > 当前Arc > Rolling Outline > 早期具体章号计划。

商业节奏和记忆锚设计都不能覆盖人物利益；旧12卷规划不能覆盖SERIES_V2_8V_2M。
