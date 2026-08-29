# CHAPTER WORKFLOW STATE MACHINE V1

> 目的：把“应该执行的规则”变成不可跳步的交稿状态机。避免出现已经写了规则，但实际写章时跳过 LOAD / Scene Card / Gate 仍把失败稿交用户的情况。

## 一、总原则：FAIL CLOSED

任何章节默认处于 `BLOCKED`。

只有前一状态存在可验证产物并通过检查，才允许进入下一状态。

**不能因为作者/模型“记得自己做过”就跳状态。**

如果关键文件读取失败、Receipt 缺失、Scene Card 缺失、任一 Gate 非 PASS，则停在当前状态或退回 `BLOCKED/REWRITE`，不得向用户展示 Candidate 正文。

## 二、状态链

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

## 三、各状态进入条件

### 0. BLOCKED

默认状态。

常见原因：
- 未完成 HOT LOAD；
- 关键 Canon / planning 源无法读取；
- 上一 Candidate 被判 REWRITE；
- 当前 Arc 的阶段收益/因果方向尚未厘清；
- 用户要求重新研究/改方向，旧 Candidate 失效。

### 1. LOADED

必须实际生成：

`quality/receipts/CHxxx_CONTEXT_RECEIPT.md`

Receipt 至少记录：
- Canon Horizon；
- HOT 文件读取结果；
- 最近 1—3 Chapter Records / 上章结尾；
- Published Prose Anchor 实际回读位置；
- 当前 Volume / Arc / Rolling Outline；
- 相关 Canon Kernel IDs；
- 当前人物 State / Knowledge / Ability；
- `quality/EXPECTATION_PAYOFF_GATE.md` 已读取。

缺一关键源，不得进入 LOADED。

### 2. MACRO_ALIGNED

Receipt 或工作流记录中必须回答：
- 本章属于哪个 Arc；
- 推进卷级哪个核心问题；
- 当前真相层允许到哪里；
- 本章推进哪条人物长期弧；
- 当前短周期读者正在等待什么具体兑现；
- 如果删掉本章，Arc/卷损失什么。

若最后一项答案接近“没有”，退回规划层重做。

### 3. SCENE_READY

必须实际存在：

`quality/scene-cards/CHxxx_SCENE_CARD.md`

并通过 Scene Isolation：
- 不直接翻译 Rolling Outline；
- 不含 CH/FP/Canon 等后台任务语言；
- 有人物欲望、现场阻力、有限信息、选择、后果；
- 重要配角即使陈缺不在也有自己的行动；
- 能回答“场景结束人物实际多了什么/少了什么”。

### 4. DRAFTED

正文 Candidate 已写出，但**此状态禁止交用户**。

必须完成：
- 2800—4000 字检查；
- 约 3000—3300 字 MIDWRITE CAPACITY CHECK；
- 1—2 个核心事件限制；
- prose anchor 风格复核。

### 5. PUBLICATION_PASS

必须执行 `quality/PUBLICATION_GATE.md` 并结论为 `PASS`。

若 `REWRITE`：退回 `SCENE_READY` 或 `DRAFTED`，按问题性质重写。

若 `BLOCKED`：退回 `BLOCKED`。

### 6. EXPECTATION_PAYOFF_PASS

必须执行 `quality/EXPECTATION_PAYOFF_GATE.md` 并结论为 `PASS`。

必须能证明：
- 本章/小周期期待清晰；
- 兑现或推进不是纯增加谜题；
- 收益有现实残余；
- 代价没有习惯性把收益归零；
- 主角主动性与奖励类型没有长期重复。

非 PASS 不得交稿。

### 7. CONTINUITY_PASS

执行 Precommit：
- 正文与已发布正文/Canon Kernel/Chapter Ledger 无冲突；
- UNKNOWN/SUSPECTS 未偷升事实；
- 能力来源、进入、代价、受益者一致；
- 伤势、位置、物品、时间、关系连续；
- Candidate Facts/Knowledge/Timeline/Relationship/FP-P-S 已可抽取。

### 8. USER_REVIEW

**只有到达此状态，才允许向用户展示完整 Candidate 正文。**

展示时仍明确：Candidate 尚未进入 Canon。

用户要求重写/否决：状态退回 `BLOCKED` 或相应阶段，旧 Candidate 不得作为事实使用。

### 9. CANON

仅在用户明确确认正文后：
- 固化正文；
- Candidate 状态转 Canon；
- 更新 Kernel / Ledger / Chapter Record / State Projection；
- 更新 Narrative Pattern / Commercial Rhythm / Rolling Outline / Context Card；
- 写 Commit Receipt；
- POSTCOMMIT 校验 Horizon。

## 四、每章工作流文件

每个当前 Candidate 必须有：

`quality/workflow/CHxxx_WORKFLOW.md`

建议字段：

```text
CHAPTER: CHxxx
CANON_HORIZON: CHxxx-1
CURRENT_STATE: BLOCKED|LOADED|...
CONTEXT_RECEIPT: path / MISSING
SCENE_CARD: path / MISSING
PUBLICATION_GATE: PENDING|PASS|REWRITE|BLOCKED
EXPECTATION_PAYOFF_GATE: PENDING|PASS|REWRITE|BLOCKED
CONTINUITY_PRECOMMIT: PENDING|PASS|REWRITE|BLOCKED
USER_DECISION: PENDING|APPROVED|REWRITE
NOTES:
```

## 五、硬禁止

- 没有 Context Receipt 就写正文；
- 没有 Scene Card 就从 Rolling Outline 扩写正文；
- Gate 只是“脑内检查”而没有工作流状态；
- `DRAFTED` 状态直接把正文发用户；
- 用户否决后继续把旧 Candidate 的姓名、事实、道具当 Canon；
- 为赶更新跳过 Gate。

## 六、当前 CH007

上一版 CH007 Candidate 已判 `REWRITE`，未进入 Canon。

因此 CH007 必须从 CH006 Canon Horizon 重新冷启动；旧 Candidate 中新增姓名、编号、南二细节和逃亡执行细节均不具 Canon 权威。
