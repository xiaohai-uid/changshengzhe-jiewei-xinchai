# CHAPTER GATE V9

> 每章依次通过：
>
> **MACRO ALIGNMENT → PREWRITE → SCENE ISOLATION → NATURALNESS PRECHECK → WRITE → MIDWRITE → POST-DRAFT AUDIT → NARRATIVE NATURALNESS → PUBLICATION → EXPECTATION/PAYOFF → CONTINUITY → FINAL DELIVERY → EXTERNAL CI → USER REVIEW → CANON PROMOTION → POSTCOMMIT。**
>
> 同时服从 `quality/WORKFLOW_STATE_MACHINE.md`。任何缺失步骤一律 FAIL CLOSED。

## 0. 核心变化：正确之外，再拦截“过度工程化”

过去的风险不只是在写完后漏检，也包括：
- 逻辑、连续性、人物都正确，但整章像逐项完成Rolling Outline；
- 段落被切成大量短句独段，靠空行制造节奏；
- 场景已经说明含义，旁白仍替读者总结；
- 转折属于同一提示重复生成时最容易出现的默认答案。

因此新增 `quality/NARRATIVE_NATURALNESS_GATE.md`：
- Scene Card后做一次 Precheck；
- Post-Draft Audit后对冻结候选稿做一次完整 Naturalness Gate；
- 结构问题先修结构，不能靠表面换词处理。

同时继续要求：没有 Post-Draft Audit PASS，不得进入后续Gate；所有Gate必须绑定同一最终稿revision。

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
9. 本章是否自然承担某个记忆锚的建立/回响？没有也可以，但必须明确。

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
- Memory Anchor System / Ledger；
- 当前Arc Memory Gap；
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
- **三个月后最可能记得什么，或明确 `NO NEW ANCHOR`；**
- 重要配角若无陈缺仍会做什么。

出现后台任务语言、样本逐项展示、纯信息奖励、任务清单感、为了记忆点硬造金句：FAIL。

## 4. NATURALNESS PRECHECK

读取 `quality/NARRATIVE_NATURALNESS_GATE.md`，在写正文前回答：
1. 本章最容易形成哪条行政式QUD链？
2. 哪4个Outline节点最容易被逐项翻译？
3. 核心转折的Echo Test结果？
4. 哪条已经存在的本书具体事实让该转折不只是默认答案？
5. 哪一处允许作为普通生活纹理，不承担伏笔/主题任务？
6. 分段纸面对照使用哪一段CH001—CH003 Published Prose Anchor？

明显风险必须先改Scene Card，不得指望全文写完后靠润色补救。

## 5. WRITE / MIDWRITE

正文目标3200—3600，硬区间2800—4000。

约3000—3300字必须做容量检查：
- 还有2个以上关键节点 → 顺延；
- 开始用对白/摘要赶设定 → 回退；
- 人物为大纲改变行为 → 改大纲；
- 已完成主要选择与后果 → 可以自然收章；
- 为补爽点突然加打脸/资源/能力 → 删除；
- 为补记忆点突然加哲理句/怪癖/象征物 → 删除；
- 开始出现连续短句独段/空行节拍 → 先合并段落再继续。

完成全文后冻结 `candidate_revision_id`，进入 DRAFTED。

## 6. POST-DRAFT AUDIT（硬门）

必须生成 `quality/reviews/CHxxx_POST_DRAFT_AUDIT.md`。

按 `quality/POST_DRAFT_AUDIT.md` 执行：

### A. Mechanical Lint
- 字数；
- 核心事件数；
- 后25%新节点；
- 总段数、单句段占比、两句以下段占比、平均段长、最长连续短段；
- 短词/空行；
- 后台词扫描；
- 高频AI指纹扫描。

### B. Rule Coverage
读取 `quality/RULE_COVERAGE_MATRIX.md`。

所有delivery-critical Rule ID必须 `PASS / NA`，并有证据；UNKNOWN即BLOCKED。MEM类与NAT类Rule IDs不可缺失。

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

### I. Memory Anchor Audit
必须回答：
- Scene Card第9问是什么；
- 新Anchor Candidate有/无；
- 旧Anchor是否回响；
- 若回响，意义增加了什么；
- 是否存在强造金句/口头禅/象征物风险；
- 重要人物关键对白/选择是否有自身辨识度；
- Arc收束时MEM-006是否满足。

### J. Regression
执行 `quality/FAILURE_MEMORY.md` 所有ACTIVE项。

任一硬FAIL：REWRITE。

## 7. NARRATIVE NATURALNESS GATE（硬门）

必须生成Naturalness审查段，逐项执行：
- NAT-001 QUD Sequence；
- NAT-002 Outline Leakage / First-Sentence Test；
- NAT-003 Paragraph Architecture；
- NAT-004 Echo Test；
- NAT-005 Over-Determination；
- NAT-006 Theme Explanation；
- NAT-007 Emotion Mode Mix；
- NAT-008 Texture Variance。

原则：
- 只修真实命中的2—3类，不把全部规则推向反方向极端；
- ACTIVE伏笔仍必须维护，不能用“人类写作会留松线”合理化忘线；
- 若NAT-003分段失败，禁止只把几个短段机械合并，必须重新看局部叙事单位是否切错。

结论：PASS / REWRITE / REPLAN。

## 8. PUBLICATION GATE

Post-Draft + Naturalness PASS 后才读取执行 `quality/PUBLICATION_GATE.md`。

重点复核：
- 小说场景感；
- 段落/句式；
- 提纲扩写；
- 高层破局算法；
- 配角主体性；
- 推理语言；
- 对话；
- 章尾；
- Memory / Distinctiveness：新锚是否自然、旧锚是否增值、人物声音是否趋同。

结论：PASS / REWRITE / BLOCKED。

## 9. EXPECTATION / PAYOFF GATE

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

## 10. CONTINUITY PRECOMMIT

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
- 不因商业化/记忆点设计迫使人物降智。

### Memory Anchor Precommit
- Candidate阶段仅提出Anchor Diff Proposal；
- 不提前修改正式Memory Anchor Ledger；
- 旧Anchor含义与Canon无冲突。

结论：PASS / REWRITE / BLOCKED。

## 11. FINAL DELIVERY GATE（最终硬门）

必须执行 `quality/FINAL_DELIVERY_GATE.md`。

检查：
- Post-Draft / Naturalness / Publication / Payoff / Continuity 是否绑定同一 `candidate_revision_id`；
- 修改后是否重跑受影响Gate；
- Rule Coverage是否完整，含MEM/NAT类Rule IDs；
- Failure Memory回归测试是否全部通过；
- 最终稿是否完成脱离规划文件的Clean Read；
- 最后300字、关键反转后解释、段落风格是否仍合格；
- 最终稿重新独立回答“记住什么”，且没有为此强造内容。

只有 `FINAL_DELIVERY = PASS`，才允许提交候选分支进入外部CI。

## 12. EXTERNAL CI / USER REVIEW

允许展示完整 Candidate 的必要条件：

- POST_DRAFT = PASS
- NARRATIVE_NATURALNESS = PASS
- PUBLICATION = PASS
- EXPECTATION_PAYOFF = PASS
- CONTINUITY = PASS
- FINAL_DELIVERY = PASS
- Rule Coverage无MEM/NAT缺项
- 所有结果 revision/SHA 一致
- 当前候选分支精确HEAD的 `Chapter Quality Gate` = success
- validator tests + strict delivery validation = success
- CI后没有新commit

用户否决后，旧Candidate新增事实立即失去权威。

## 13. CANON PROMOTION

用户明确确认后：
1. 固化正文；
2. Candidate Facts / Knowledge / Timeline / Relationship / FP-P-S 转Canon；
3. 更新Kernel temporal records；
4. 追加Chapter Ledger + Chapter Record；
5. 重建state/tracking投影；
6. 更新Narrative Pattern / Commercial Rhythm / Rolling Outline / Context Card；
7. **执行Memory Anchor Diff：新增/回响/重解释只在此时进入正式Ledger；**
8. 必要时同步修订Detail / ARC_MAP；
9. 写Commit Receipt；
10. POSTCOMMIT校验Horizon。

失败：不推进main。

## 14. POSTCOMMIT

- 每章：State Diff + Narrative Pattern / Commercial Rhythm + Memory Anchor Diff；
- 每5章：Snapshot + Expectation/Payoff回顾 + Failure Pattern回顾 + Memory Anchor Review；
- 每10章：Continuity + Narrative Pattern + Macro Drift + Rule Coverage orphan audit + 人物辨识度回顾；
- Arc结束：Arc Summary + 阶段期待兑现复盘 + Arc Memory Audit；
- 卷末：Major Canon Version + 跨卷Memory Anchor筛选；
- Revision：执行Change Impact Protocol。
