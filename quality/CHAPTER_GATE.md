# CHAPTER GATE V5

> 每章依次通过：MACRO ALIGNMENT → PREWRITE → SCENE ISOLATION → WRITE → MIDWRITE → PUBLICATION GATE → PRECOMMIT → CANON PROMOTION → POSTCOMMIT。Candidate 与 Canon 严格分离。

## MACRO ALIGNMENT

写正文前必须回答：
1. 本章属于哪个 Arc？
2. 推进当前卷哪个核心问题？
3. 当前只允许推进到哪一层真相？
4. 是否推进长期人物弧，而非把配角当信息工具？
5. 如果删掉本章，Arc/卷损失什么？若几乎没有，重做章节合同。

## PREWRITE

1. **Canon Horizon**：确认从哪一章正式 Canon 起写。
2. **上一章因果**：最后实际发生的动作最自然导致什么？
3. **合同**：只保留 1—2 个核心事件。
4. **容量**：目标 3200—3600 字，硬区间 2800—4000 字。
5. **Timeline / State / Knowledge / Ability**：位置、身体、物品、能力、已知/未知无越权。
6. **FP/P/S**：只推进本场真正需要的项。
7. **Pattern**：检查最近五章高层胜利算法，不只看道具是否重复。
8. **Published Prose Anchor**：实际回读至少两段已发布高质量正文，校准段落和叙述质感。
9. **Context Receipt**：登记实际读取来源；关键源缺失则 BLOCKED。

## SCENE ISOLATION（硬门）

正文不得从 Rolling Outline 直接展开。

必须先按 `quality/SCENE_CARD_TEMPLATE.md` 生成角色世界内部 Scene Card，回答：
- 谁现在想要什么？
- 现场阻力是什么？
- 他真正知道什么？
- 哪个信息不足处必须做选择？
- 选择解决什么，又新增什么代价？
- 场景结束后现实发生什么变化？

Scene Card 若仍出现 CHxxx、FP-xxx、Canon、KNOWS、必须推进、章尾目标等后台标签，FAIL。

如果场景结构仍是“样本A/B/C逐项展示→主角看懂答案→精准通关”，FAIL，除非该结构此前长期未用且本章有实质误判/代价。

## MIDWRITE CAPACITY CHECK

正文约 3000—3300 字检查：
- 是否还有两个以上关键节点？有则顺延。
- 是否开始用对话/摘要赶设定？有则回退。
- 是否强迫人物为大纲改变行为？有则改大纲。
- 本章主要选择是否已经产生后果？产生后可以自然收章，不额外加第二个高潮。

## PUBLICATION GATE（先于 PRECOMMIT）

必须读取并逐项执行 `quality/PUBLICATION_GATE.md`。

以下任一出现即 REWRITE，不得交稿：
- 后台语言泄漏（第三章/上一章/CHxxx/Canon 等）；
- 连续三个以上无必要的一句式叙述段；
- 大量短词独段制造假节奏；
- 提纲逐项扩写；
- 最近五章高层破局算法重复；
- 陈缺判断正确且几乎无代价；
- 重要配角若主角不在场就“无事可做”；
- 同类“这不能证明/至少说明”解释腔反复出现；
- 章尾靠神秘人突然抛一句信息硬切，而非本章因果后果。

Publication Gate 结论只允许 PASS / REWRITE / BLOCKED。

## PRECOMMIT

### 连续性
- Candidate 是否与正式正文、Kernel、Chapter Ledger 冲突？
- 状态变化是否关闭旧 temporal fact 并新增新 fact，而非覆盖历史？
- UNKNOWN/SUSPECTS 是否误升为事实？
- 能力来源、进入方式、代价和受益者是否一致？

### 小说质量
- 正文是否 2800—4000 字，常规约 3200—3600？
- 是否集中完成 1—2 个核心事件？
- 是否有认知/关系/风险/能力/身份至少一项实质变化？
- 成功是否带来新的成本、暴露面或债？
- 配角是否按自身利益行动？
- 常规段落是否自然承载动作/观察/心理，而非短句瀑布？
- 是否像同一本已发布小说，而不是管理系统生成的剧情报告？

### Reader Experience
- 本章读者最想知道的主问题是什么？
- 问题是否发生变化而不是只多一条症状？
- 是否有情绪变化？
- 是否兑现至少一点？
- 章尾是否自然推出下一步？

## CANON PROMOTION

用户确认后：
1. 正文固化。
2. Candidate Facts / Knowledge / Timeline / Relationship / FP-P-S 转 Canon。
3. 更新 Kernel temporal records。
4. 追加 Chapter Ledger + Chapter Record。
5. 重建 state/tracking 投影。
6. 更新 Narrative Pattern、Rolling Outline、Context Card。
7. 正文自然改变卷内因果时同步修订 Detail / ARC_MAP，不改过去迎合旧纲。
8. 写 Commit Receipt。
9. 全部通过才推进 `main` Canon Horizon。

失败：不推进 `main`。

## POSTCOMMIT

- 校验 Canon Horizon 与 Manuscript/Kernel/Ledger 一致。
- 每5章 Snapshot + Warm Memory compaction + Publication Pattern 回顾。
- 每10章 Continuity + Narrative Pattern + Macro Drift Audit。
- Arc 结束生成 Arc Summary 并重算下一 Arc。
- 卷末生成 Major Canon Version。
- Revision 必须执行 Change Impact Protocol，禁止静默修补。
