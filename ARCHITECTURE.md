# 《长生者皆为薪柴》仓库架构 V4

本仓库采用“已发布正文 Canon + Canon Kernel + 状态投影 + 规划层 + 证据化质量门禁”的长篇生产模式。

当前系列：**约200万字 / 8卷 / 约580—620章**。规划可以调整未来，但不能覆盖已发生正文。

架构目标：用户主要负责判断“好不好看、喜不喜欢、方向是否满意”；连续性、规则执行与交稿QA由生产系统承担。

## 一、事实权威层级

发生冲突时：

1. 用户当前明确决定
2. `main` 已发布正文 + `canon/CANON_CORE.md`
3. World Bible / Cultivation System 等硬世界规则
4. `canon/kernel/` + `state/CHAPTER_LEDGER.md`
5. Snapshot / State Diff / tracking投影
6. 当前有效planning
7. 旧卷纲与历史草稿

## 二、规划层级

**Series Master → Volume Blueprints → Current Volume Detail → Arc Map → Rolling Outline → Scene Card**

规划不能直接生成正文。Rolling Outline只规定因果方向与阶段期待，必须先经过Scene Card。

## 三、Tracking层

- `TRACKING_STATE.json`：结构化当前状态投影；
- `CONTEXT_CARD.md`：冷启动热状态；
- `AUTHOR_TRUTH.md`：作者层确定事实；
- `READER_KNOWN.md`：读者当前可确认/合理推断；
- `chapter-records/`：章节连续性变化。

## 四、质量层：从“有规则”升级为“可验证规则”

核心文件：

- `quality/RULE_COVERAGE_MATRIX.md`：交稿级硬规则总登记；
- `quality/POST_DRAFT_AUDIT.md`：写完后的证据化自审；
- `quality/PUBLICATION_GATE.md`：小说质感/场景结构；
- `quality/EXPECTATION_PAYOFF_GATE.md`：期待→兑现→升级；
- `quality/FINAL_DELIVERY_GATE.md`：最终交付版本复检；
- `quality/FAILURE_MEMORY.md`：历史漏检错误回归测试；
- `quality/WORKFLOW_STATE_MACHINE.md`：不可跳步状态机。

### Rule Coverage原则

每条交稿级硬规则必须有：
- Rule ID；
- 来源；
- 责任Gate；
- 最低证据；
- FAIL动作。

新增规则没有进入Rule Coverage Matrix，视为配置不完整。

## 五、章节Evidence-Based工作流

完整链：

**LOAD**
→ **Context Receipt**
→ **Macro Alignment**
→ **Scene Card**
→ **Write / Midwrite**
→ **Freeze Candidate Revision**
→ **Post-Draft Audit**
→ **Publication Gate**
→ **Expectation/Payoff Gate**
→ **Continuity Precommit**
→ **Final Delivery Gate**
→ **User Review**
→ **Canon Promotion**
→ **Postcommit**

### 写后审查是独立阶段

完整正文产生后不能直接进入“交稿”。必须先冻结 `candidate_revision_id`，生成Post-Draft报告，并逐条执行Rule Coverage和Failure Regression。

Post-Draft包括：
- Mechanical Lint；
- Causal/Character Falsification；
- Knowledge/Power Claim Audit；
- Outline Leakage Audit；
- 资产Diff；
- Anti-AI/Redundancy；
- Reader Clean Read；
- 历史失败回归测试。

### Revision Binding

所有写后PASS必须绑定同一个candidate revision。

正文修改后，旧PASS按影响范围自动失效。禁止“审A稿、改成B稿、直接交B稿”。

### Final Delivery

Final Delivery再次只读最终稿，验证：
- 所有Gate revision一致；
- Rule IDs无遗漏；
- ACTIVE Failure Memory全部通过；
- 没有Gate后未审修改；
- 最终稿仍像同一本小说。

只有Final Delivery PASS才能进入User Review。

## 六、Failure Memory机制

用户指出过的生产问题永久转成回归测试，例如：
- 跳过完整LOAD；
- Outline逐项扩写；
- 短句瀑布；
- 一章任务过载；
- 配角为剧情临时装技能；
- 场景已经表达后再总结主题；
- 章尾翻译大纲钩子；
- 重大成长迅速清零；
- Gate只在脑内执行；
- Gate通过后改正文不重检。

目标：**同一种生产错误尽量只让用户指出一次。**

## 七、200万字压缩机制

旧12卷/350—500万规划已废弃。

压缩方式：
1. 合并相邻理念卷，不删核心真相；
2. 一个结论只做一次主证明；
3. 后续写行动后果，不重复调查；
4. 地图变化必须带来新规则/利益结构；
5. 旧伏笔优先于新增谜题；
6. 第一卷约70—75章，其余卷约65—90章；
7. 预计超过约210万字前做Macro Drift Audit。

## 八、Candidate与Canon

- Candidate可反复修改；
- 用户确认前不推进Canon Horizon；
- 用户否决后Candidate新增事实不进入规划权威；
- 用户确认后才执行Commit Protocol；
- 已发布正文Revision必须执行Change Impact Protocol。

## 九、审计节奏

- 每章：Post-Draft Audit + State Diff + Narrative/Commercial Rhythm；
- 每5章：Snapshot + Expectation/Payoff + Failure Pattern review；
- 每10章：Continuity + Narrative Pattern + Macro Drift + Rule Coverage orphan audit；
- Arc结束：阶段兑现复盘；
- 卷末：Major Canon Version。

核心架构目标：**写得紧而不疲劳，写得久而不吃书，交稿前尽量由系统自己发现错误，而不是把QA转嫁给用户。**
