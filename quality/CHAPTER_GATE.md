# CHAPTER GATE V7

> 每章依次通过：
>
> **MACRO ALIGNMENT → PREWRITE → SCENE ISOLATION → WRITE → MIDWRITE → POST-DRAFT AUDIT → PUBLICATION → EXPECTATION/PAYOFF → CONTINUITY → FINAL DELIVERY → USER REVIEW → CANON PROMOTION → POSTCOMMIT。**
>
> 同时服从 `quality/WORKFLOW_STATE_MACHINE.md`。任何缺失步骤一律 FAIL CLOSED。

## 0. 核心变化：写完以后必须重新审稿

过去的风险是“规则都在写前提醒，但写完以后没有逐条验收”。

现在 DRAFTED 后必须先执行 `quality/POST_DRAFT_AUDIT.md`，并用 `quality/RULE_COVERAGE_MATRIX.md` 逐条取证。

**没有 Post-Draft Audit PASS，不得进入 Publication Gate。**

所有Gate最终还必须由 `quality/FINAL_DELIVERY_GATE.md` 验证它们对应的是同一个最终稿 revision。

---

## 1. MACRO ALIGNMENT

写正文前必须回答：
1. 本章属于哪个 Arc？
2. 推进当前卷哪个核心问题？
3. 当前只允许推进到哪一层真相？
4. 是否推进长期人物弧，而非把配角当信息工具？
5. 当前短周期读者具体在等待什么正向兑现？
6. 如果删掉本章，Arc/卷结构与期待曲线损失什么？
7. 是否在重复一个已经完成主证明的世界观结论？
8. 是否为了旧章号/卷长拖延？

若答案显示本章只是“还能写”：退回规划。

## 2. PREWRITE

必须确认：
- Canon Horizon；
- SERIES_V2_8V_2M 架构；
- 上章最后现实动作与自然后果；
- 1—2个核心事件合同；
- 2800—4000容量；
- Timeline / State / Knowledge / Ability；
- 必要FP/P/S；
- 最近5章Narrative Pattern；
- Published Prose Anchor；
- EXPECTATION / PAYOFF / UPGRADE；
- Context Receipt存在；
- workflow状态合法。

任一关键源缺失：BLOCKED。

## 3. SCENE ISOLATION

必须存在 `quality/scene-cards/CHxxx_SCENE_CARD.md`。

Scene Card必须回答：
- 谁想要什么；
- 什么阻止他；
- 他真正知道什么；
- 信息不足处怎样选择；
- 成功实际得到什么；
- 解决什么、付什么；
- 场景结束净变化；
- 新问题怎样从变化长出来；
- 重要配角若无陈缺仍会做什么。

出现后台任务语言、样本逐项展示、纯信息奖励、任务清单感：FAIL。

## 4. WRITE / MIDWRITE

正文目标3200—3600，硬区间2800—4000。

约3000—3300字必须做容量检查：
- 还有2个以上关键节点 → 顺延；
- 开始用对白/摘要赶设定 → 回退；
- 人物为大纲改变行为 → 改大纲；
- 已完成主要选择与后果 → 可以自然收章；
- 为补爽点突然加打脸/资源/能力 → 删除。

完成全文后冻结 `candidate_revision_id`，进入 DRAFTED。

## 5. POST-DRAFT AUDIT（硬门）

必须生成 `quality/reviews/CHxxx_POST_DRAFT_AUDIT.md`。

按 `quality/POST_DRAFT_AUDIT.md` 执行：

### A. Mechanical Lint
- 字数；
- 核心事件数；
- 后25%新节点；
- 一句叙述段最大连续数；
- 短词/空行；
- 后台词扫描；
- 高频AI指纹扫描。

### B. Rule Coverage
读取 `quality/RULE_COVERAGE_MATRIX.md`。

所有本章相关 Rule ID 必须 `PASS / NA`，并有证据；UNKNOWN即BLOCKED。

### C. Falsification
主动寻找：
- 作者便利因果；
- 陈缺越权/降智/全知；
- 配角工具化；
- 对手降智；
- 新人物一次性装配剧情所需技能。

### D. Claim Audit
逐项检查新知识、新能力、新世界事实的来源和状态。

### E. Outline Leakage
Rolling Outline / Scene Card 与正文并排比较；逐项扩写则退回Scene Card。

### F. Asset Diff
记录章初/章末 Ability / Resource / Status / Freedom / Leverage / Impact / Information。

### G. Anti-AI / Redundancy
删掉读者已经看懂后的解释、重复动作、报告腔。

### H. Reader Clean Read
只看上章结尾+本章，确认人物欲望、选择、变化、继续阅读动力。

### I. Regression
执行 `quality/FAILURE_MEMORY.md` 所有ACTIVE项。

任一硬FAIL：REWRITE。

## 6. PUBLICATION GATE

Post-Draft PASS 后才读取执行 `quality/PUBLICATION_GATE.md`。

重点复核：
- 小说场景感；
- 段落/句式；
- 提纲扩写；
- 高层破局算法；
- 配角主体性；
- 推理语言；
- 对话；
- 章尾。

结论：PASS / REWRITE / BLOCKED。

## 7. EXPECTATION / PAYOFF GATE

必须执行 `quality/EXPECTATION_PAYOFF_GATE.md`。

至少证明：
- 当前正向期待明确；
- 本章推进/兑现而非只加谜题；
- 获得有现实残余；
- 代价未机械归零；
- 奖励类型不长期重复；
- 陈缺主动权在合理周期内增长；
- 新冲突从获得自然升级。

结论：PASS / REWRITE / BLOCKED。

## 8. CONTINUITY PRECOMMIT

### 连续性
- Candidate与正式正文/Kernel/Ledger无冲突；
- Temporal fact正确关闭/新增；
- UNKNOWN/SUSPECTS未偷升；
- 位置、伤势、物品、时间连续；
- 能力来源/进入/代价/受益者一致；
- Active Plot处理合理。

### 人物与小说
- 陈缺关键决定符合人格与证据；
- 配角按自身利益行动；
- 本章状态变化真实；
- 不因商业化迫使人物降智。

结论：PASS / REWRITE / BLOCKED。

## 9. FINAL DELIVERY GATE（最终硬门）

必须执行 `quality/FINAL_DELIVERY_GATE.md`。

检查：
- Post-Draft / Publication / Payoff / Continuity 是否绑定同一 `candidate_revision_id`；
- 修改后是否重跑受影响Gate；
- Rule Coverage是否完整；
- Failure Memory回归测试是否全部通过；
- 最终稿是否完成脱离规划文件的Clean Read；
- 最后300字、关键反转后解释、段落风格是否仍合格。

只有 `FINAL_DELIVERY = PASS`，workflow才可进入 `USER_REVIEW`。

## 10. USER REVIEW

允许展示完整 Candidate 的必要条件：

- POST_DRAFT = PASS
- PUBLICATION = PASS
- EXPECTATION_PAYOFF = PASS
- CONTINUITY = PASS
- FINAL_DELIVERY = PASS
- 所有结果 revision 一致

用户否决后，旧Candidate新增事实立即失去权威。

## 11. CANON PROMOTION

用户明确确认后：
1. 固化正文；
2. Candidate Facts / Knowledge / Timeline / Relationship / FP-P-S 转Canon；
3. 更新Kernel temporal records；
4. 追加Chapter Ledger + Chapter Record；
5. 重建state/tracking投影；
6. 更新Narrative Pattern / Commercial Rhythm / Rolling Outline / Context Card；
7. 必要时同步修订Detail / ARC_MAP；
8. 写Commit Receipt；
9. POSTCOMMIT校验Horizon。

失败：不推进main。

## 12. POSTCOMMIT

- 每章：State Diff + Narrative Pattern / Commercial Rhythm；
- 每5章：Snapshot + Expectation/Payoff回顾 + Failure Pattern回顾；
- 每10章：Continuity + Narrative Pattern + Macro Drift + Rule Coverage orphan audit；
- Arc结束：Arc Summary + 阶段期待兑现复盘；
- 卷末：Major Canon Version；
- Revision：执行Change Impact Protocol。
