# CHAPTER WORKFLOW STATE MACHINE V4

> 目的：把“规则很多”升级为“每一步都有产物、证据、版本绑定，并由外部执行器验证”。
>
> 总原则：**FAIL CLOSED + EVIDENCE REQUIRED + REVISION BOUND + EXTERNAL CI VERIFIED。**

## 一、当前系列架构硬校验

HOT LOAD时必须从 `MANIFEST.md` 确认：

- `PLANNING_ARCHITECTURE = SERIES_V2_8V_2M`
- 目标总量约200万字
- 当前卷/Arc/Canon Horizon与Context Card一致

加载到旧“12卷 / 350万—500万 / 第一卷110—130章”并试图驱动当前正文，视为 `DEPRECATED CONFLICT`，保持BLOCKED。

## 二、状态链

`BLOCKED`
→ `LOADED`
→ `MACRO_ALIGNED`
→ `SCENE_READY`
→ `DRAFTED`
→ `POST_DRAFT_PASS`
→ `PUBLICATION_PASS`
→ `EXPECTATION_PAYOFF_PASS`
→ `CONTINUITY_PASS`
→ `FINAL_DELIVERY_PASS`
→ `EXTERNAL_CI_PASS`（运行时状态）
→ `USER_REVIEW`（运行时状态）
→ `CANON`

任何状态不能跳跃。

`EXTERNAL_CI_PASS`不能由Markdown自报。它只能来自GitHub Actions真实结果：候选分支当前HEAD对应的 `Chapter Quality Gate` conclusion=`success`。

## 三、版本原则

每次形成完整Candidate，必须生成 `candidate_revision_id` 与 `candidate_sha256`。

所有写后审查都必须绑定同一revision和SHA。

正文发生修改：
- 错字/标点：至少重跑Mechanical Lint + Final Delivery，并产生新SHA；
- 句段/对白：相关Style checks + Publication + Final失效；
- 事件/动机/知识/能力/资源/关系/章尾：Post-Draft、Publication、Expectation/Payoff、Continuity、Final全部失效。

任何候选分支新commit都会改变HEAD；旧的External CI success因此自动失效。

禁止“审的是A稿，交的是B稿”。

## 四、各状态进入条件

### 0. BLOCKED

默认状态。以下任一存在即保持BLOCKED：
- HOT LOAD不完整；
- 关键Canon/planning源失败；
- 规划架构冲突；
- Context Receipt缺失；
- 用户改方向导致旧Candidate失效；
- 当前正向期待或场景因果尚未设计清楚。

### 1. LOADED

必须存在 `quality/receipts/CHxxx_CONTEXT_RECEIPT.md`。

Receipt至少记录：Canon Horizon、系列架构、HOT来源、最近正文、Published Prose Anchor、当前卷/Arc/Outline、相关Canon IDs、人物状态/知识/能力、Expectation/Payoff方向、质量规则版本。

### 2. MACRO_ALIGNED

必须回答：
1. 属于哪个Arc；
2. 推进卷级哪个核心问题；
3. 真相允许到哪层；
4. 推进哪条人物弧；
5. 读者正在等什么具体兑现；
6. 删掉本章会损失什么；
7. 是否重复已经完成主证明的结论；
8. 是否为了旧章号/卷长继续拖。

存在明显问题：退回规划。

### 3. SCENE_READY

必须存在 `quality/scene-cards/CHxxx_SCENE_CARD.md`。

必须通过：人物欲望、现实阻力、有限信息、信息不足处选择、现实收益、双向代价、场景净变化、配角独立行动。

Scene Card仍像任务清单：FAIL。

### 4. DRAFTED

完整Candidate已写出并冻结revision id/SHA。

此状态**绝对禁止交用户**。

必须已完成：
- 2800—4000字初检；
- Midwrite Capacity Check；
- 1—2核心事件限制；
- prose anchor初步复核。

### 5. POST_DRAFT_PASS

必须生成 `quality/reviews/CHxxx_POST_DRAFT_AUDIT.md`。

按 `quality/POST_DRAFT_AUDIT.md` 完成：Mechanical Lint、Rule Coverage、因果/人物反证、Knowledge/Power Claim Audit、Outline Leakage Audit、Expectation/Payoff资产Diff预审、Anti-AI/Redundancy、Reader Clean Read、Failure Memory Regression。

报告必须PASS且revision/SHA完全匹配。

### 6. PUBLICATION_PASS

执行 `quality/PUBLICATION_GATE.md`。小说质感、场景结构、段落、对话、章尾、胜利算法全部PASS。

### 7. EXPECTATION_PAYOFF_PASS

执行 `quality/EXPECTATION_PAYOFF_GATE.md`。必须证明期待/兑现/升级成立，收益有耐久残余，商业节奏没有重新掉回纯高压/纯谜题。

### 8. CONTINUITY_PASS

执行Precommit：Canon/正文无冲突；Knowledge无越权；状态/时间/物品/伤势连续；能力来源/进入/代价/受益者一致；Candidate变化可抽取。

### 9. FINAL_DELIVERY_PASS

执行 `quality/FINAL_DELIVERY_GATE.md`。

必须确认：
- Post-Draft / Publication / Payoff / Continuity全部对应同一revision/SHA；
- Rule Coverage所有相关Rule ID PASS/NA；
- Failure Memory ACTIVE项全部通过；
- 最终稿完成Clean Read；
- Gate后没有未审修改。

随后将Candidate、Receipt、Scene Card、所有Review报告和workflow状态一起提交到当前候选分支。提交后不再改稿。

### 10. EXTERNAL_CI_PASS（运行时）

作者系统必须读取GitHub Actions真实结果并验证：
- workflow=`Chapter Quality Gate`；
- branch=当前候选分支；
- conclusion=`success`；
- run.head_sha=候选分支当前HEAD；
- validator tests成功；
- strict delivery validation成功。

这一步不通过，禁止进入USER_REVIEW。

为了不改变已经通过CI的HEAD，`EXTERNAL_CI_PASS`不要求再写回一个新commit。

### 11. USER_REVIEW（运行时）

**只有EXTERNAL_CI_PASS成立，才允许向用户展示完整Candidate。**

用户否决/要求重写：旧Candidate失效，新增事实无权进入规划/Canon；按问题退回相应状态，重大重写直接回BLOCKED/SCENE_READY。任何重写都产生新revision/SHA并重新走CI。

### 12. CANON

只有用户明确确认后：
- 固化正文；
- Candidate Facts/Knowledge/Timeline/Relationship/Plots转Canon；
- 更新Kernel/Ledger/Chapter Record/State Projection；
- 更新Narrative Pattern/Commercial Rhythm/Rolling Outline/Context Card；
- 写Commit Receipt；
- POSTCOMMIT校验Canon Horizon。

## 五、每章工作流文件

`quality/workflow/CHxxx_WORKFLOW.md`至少记录：

```text
CHAPTER:
CANON_HORIZON:
SERIES_ARCHITECTURE: SERIES_V2_8V_2M
CANDIDATE_BRANCH:
CANDIDATE_PATH:
CURRENT_STATE:
CANDIDATE_REVISION_ID:
CONTEXT_RECEIPT:
SCENE_CARD:
POST_DRAFT_AUDIT: PENDING|PASS|REWRITE|BLOCKED
PUBLICATION_GATE: PENDING|PASS|REWRITE|BLOCKED
EXPECTATION_PAYOFF_GATE: PENDING|PASS|REWRITE|BLOCKED
CONTINUITY_PRECOMMIT: PENDING|PASS|REWRITE|BLOCKED
FINAL_DELIVERY_GATE: PENDING|PASS|REWRITE|BLOCKED
RULE_COVERAGE: PENDING|PASS|BLOCKED
FAILURE_REGRESSION: PENDING|PASS|BLOCKED
EXTERNAL_CI: PENDING
USER_DECISION:
```

`EXTERNAL_CI`字段只表示尚待外部验证，不能靠手工改成PASS取得交稿权。交稿权来自实际Actions API结果。

## 六、硬禁止

- 没有Receipt写正文；
- 没有Scene Card写正文；
- Gate只在脑内执行；
- DRAFTED直接交用户；
- Post-Draft Audit缺失仍继续；
- Rule Coverage只写“全部正常”而无证据；
- Gate通过后修改正文却不重跑；
- Final Delivery PASS后不提交候选分支/不跑CI就交稿；
- 用旧CI结果对应新HEAD；
- 用户否决后继续沿用旧Candidate新事实；
- 为赶更新跳步；
- 使用废弃12卷规划驱动当前章节；
- 为命中旧卷长继续已经完成的Arc。

## 七、当前CH007

上一版CH007已REWRITE且非Canon；旧 `chapter/CH007` 为历史候选分支。

新CH007使用 `chapter/CH007-v2`，从CH006 Canon Horizon重新冷启动，并执行V4状态链。旧Candidate姓名、编号、南二布局、运输细节均无权威。
