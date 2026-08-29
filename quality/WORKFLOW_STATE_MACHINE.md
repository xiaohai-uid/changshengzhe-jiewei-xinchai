# CHAPTER WORKFLOW STATE MACHINE V2

> 目的：把“应该执行的规则”变成不可跳步的交稿状态机。避免已经写了规则，但实际写章时跳过 LOAD / Scene Card / Gate 仍把失败稿交用户。

## 一、总原则：FAIL CLOSED

任何章节默认处于 `BLOCKED`。

只有前一状态存在可验证产物并通过检查，才允许进入下一状态。

**不能因为作者/模型“记得自己做过”就跳状态。**

如果关键文件读取失败、Receipt缺失、Scene Card缺失、任一Gate非PASS，则停在当前状态或退回 `BLOCKED/REWRITE`，不得向用户展示Candidate正文。

## 二、当前系列架构硬校验

HOT LOAD时必须从 `MANIFEST.md` 确认：

- `PLANNING_ARCHITECTURE = SERIES_V2_8V_2M`
- 目标总量约200万字
- 当前卷/Arc/Canon Horizon与Context Card一致

如果任何加载到的旧规划仍以“12卷 / 350万—500万 / 第一卷110—130章”为当前有效结构，必须视为**DEPRECATED CONFLICT**：

1. 不得进入 `LOADED`；
2. 先以Manifest → Series Master → Volume Blueprints → Current Volume Detail的权威顺序解析；
3. 旧规划只能作为历史资料，不得驱动正文。

## 三、状态链

`BLOCKED`
→ `LOADED`
→ `MACRO_ALIGNED`
→ `SCENE_READY`
→ `DRAFTED`
→ `PUBLICATION_PASS`
→ `EXPECTATION_PAYOFF_PASS`
→ `CONTINUITY_PASS`
→ `USER_REVIEW`
→ `CANON`

## 四、各状态进入条件

### 0. BLOCKED

默认状态。

常见原因：
- 未完成HOT LOAD；
- 关键Canon / planning源无法读取；
- 规划架构版本冲突；
- 上一Candidate被判REWRITE；
- 当前Arc阶段收益/因果方向尚未厘清；
- 用户要求重新研究/改方向，旧Candidate失效。

### 1. LOADED

必须实际生成：

`quality/receipts/CHxxx_CONTEXT_RECEIPT.md`

Receipt至少记录：
- Canon Horizon；
- `SERIES_V2_8V_2M`架构确认；
- HOT文件读取结果；
- 最近1—3 Chapter Records / 上章结尾；
- Published Prose Anchor实际回读位置；
- 当前Volume / Arc / Rolling Outline；
- 当前卷容量锚与本Arc在八卷规划中的功能；
- 相关Canon Kernel IDs；
- 当前人物State / Knowledge / Ability；
- `quality/EXPECTATION_PAYOFF_GATE.md`已读取。

缺一关键源，不得进入LOADED。

### 2. MACRO_ALIGNED

Receipt或工作流记录中必须回答：
- 本章属于哪个Arc；
- 推进卷级哪个核心问题；
- 当前真相层允许到哪里；
- 本章推进哪条人物长期弧；
- 当前短周期读者正在等待什么具体兑现；
- 如果删掉本章，Arc/卷损失什么；
- 本章是否在重复一个已经完成主证明的世界观结论；
- 当前Arc是否出现“为了旧章号/旧卷长继续拖”的风险。

若最后两项存在明显风险，退回规划层重做。

### 3. SCENE_READY

必须实际存在：

`quality/scene-cards/CHxxx_SCENE_CARD.md`

并通过Scene Isolation：
- 不直接翻译Rolling Outline；
- 不含CH/FP/Canon等后台任务语言；
- 有人物欲望、现场阻力、有限信息、选择、后果；
- 重要配角即使陈缺不在也有自己的行动；
- 能回答“场景结束人物实际多了什么/少了什么”。

### 4. DRAFTED

正文Candidate已写出，但**此状态禁止交用户**。

必须完成：
- 2800—4000字检查；
- 约3000—3300字MIDWRITE CAPACITY CHECK；
- 1—2个核心事件限制；
- prose anchor风格复核。

### 5. PUBLICATION_PASS

必须执行 `quality/PUBLICATION_GATE.md` 并结论为 `PASS`。

若 `REWRITE`：退回 `SCENE_READY` 或 `DRAFTED`。

若 `BLOCKED`：退回 `BLOCKED`。

### 6. EXPECTATION_PAYOFF_PASS

必须执行 `quality/EXPECTATION_PAYOFF_GATE.md` 并结论为 `PASS`。

必须能证明：
- 本章/小周期期待清晰；
- 兑现或推进不是纯增加谜题；
- 收益有现实残余；
- 代价没有习惯性把收益归零；
- 主角主动性与奖励类型没有长期重复。

非PASS不得交稿。

### 7. CONTINUITY_PASS

执行Precommit：
- 正文与已发布正文/Canon Kernel/Chapter Ledger无冲突；
- UNKNOWN/SUSPECTS未偷升事实；
- 能力来源、进入、代价、受益者一致；
- 伤势、位置、物品、时间、关系连续；
- Candidate Facts/Knowledge/Timeline/Relationship/FP-P-S已可抽取。

### 8. USER_REVIEW

**只有到达此状态，才允许向用户展示完整Candidate正文。**

展示时仍明确：Candidate尚未进入Canon。

用户要求重写/否决：状态退回 `BLOCKED` 或相应阶段，旧Candidate不得作为事实使用。

### 9. CANON

仅在用户明确确认正文后：
- 固化正文；
- Candidate状态转Canon；
- 更新Kernel / Ledger / Chapter Record / State Projection；
- 更新Narrative Pattern / Commercial Rhythm / Rolling Outline / Context Card；
- 写Commit Receipt；
- POSTCOMMIT校验Horizon。

## 五、每章工作流文件

每个当前Candidate必须有：

`quality/workflow/CHxxx_WORKFLOW.md`

建议字段：

```text
CHAPTER: CHxxx
CANON_HORIZON: CHxxx-1
SERIES_ARCHITECTURE: SERIES_V2_8V_2M
CURRENT_STATE: BLOCKED|LOADED|...
CONTEXT_RECEIPT: path / MISSING
SCENE_CARD: path / MISSING
PUBLICATION_GATE: PENDING|PASS|REWRITE|BLOCKED
EXPECTATION_PAYOFF_GATE: PENDING|PASS|REWRITE|BLOCKED
CONTINUITY_PRECOMMIT: PENDING|PASS|REWRITE|BLOCKED
USER_DECISION: PENDING|APPROVED|REWRITE
NOTES:
```

## 六、硬禁止

- 没有Context Receipt就写正文；
- 没有Scene Card就从Rolling Outline扩写正文；
- Gate只是“脑内检查”而没有工作流状态；
- `DRAFTED`状态直接把正文发用户；
- 用户否决后继续把旧Candidate的姓名、事实、道具当Canon；
- 为赶更新跳过Gate；
- 使用已经废弃的12卷/350—500万旧规划驱动当前章节；
- 为命中旧卷长或总字数而继续已经完成的Arc。

## 七、当前 CH007

上一版CH007 Candidate已判 `REWRITE`，未进入Canon。

因此CH007必须从CH006 Canon Horizon重新冷启动；旧Candidate中新增姓名、编号、南二细节和逃亡执行细节均不具Canon权威。

当前系列宏观基线：八卷/约200万字；第一卷约70—75章；当前七日考核Arc计划约CH011/12收束，但真实因果优先。
