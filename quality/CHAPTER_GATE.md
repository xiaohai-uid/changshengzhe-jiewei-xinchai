# CHAPTER GATE V4

> 每章依次通过 MACRO ALIGNMENT → PREWRITE → MIDWRITE → PRECOMMIT → CANON PROMOTION → POSTCOMMIT。Candidate 与 Canon 严格分离。

## MACRO ALIGNMENT

写正文前必须先回答：

1. 本章属于哪个 Arc？
2. 本章推进当前卷的哪个核心问题？
3. 本章碰到的世界真相，当前只允许推进到 `TRUTH_REVEAL_LADDER` 哪一层？
4. 本章是否推进一个长期人物弧，而不是让配角只为主角送信息？
5. 如果删掉这一章，当前 Arc/卷会损失什么？如果几乎没有损失，章节合同需要重做。

宏观资料：`planning/SERIES_MASTER_OUTLINE.md` → `planning/VOLUME_BLUEPRINTS.md` → 当前卷 Detail → `planning/ARC_MAP.md`。

宏观规划不得覆盖已发布正文，但章节也不得长期无视卷级功能自由漂移。

## PREWRITE

1. **Canon Horizon**：确认本章从哪个已确认章节/commit 起写，Candidate 没有被误当 Canon。
2. **承接**：上一章最后实际动作/决定最自然导致什么？
3. **合同**：本章最重要的一两件事、必须推进项、绝不能发生项。
4. **容量预算**：正文目标3200—3600字，硬区间2800—4000字；本章任务是否能在该容量内自然完成？若需要后半章连续塞多个节点，写前先拆章。
5. **Entity**：本章关键人物/地点/物件永久 ID 能否解析；身份/别名无串人。
6. **Timeline**：位置、先后、持续时间、伤势恢复是否可成立；未知精确时间不乱补。
7. **角色知识**：KNOWS / SUSPECTS / BELIEVES / UNKNOWN / FALSE-BELIEF 边界无越权。
8. **能力规则**：来源、进入方式、代价、获益方；未知部分保持未知。
9. **新概念尺度**：本章若首次出现境界/势力/术法/制度，是否给读者足够的最小相对尺度，而非只扔术语？
10. **世界观边界**：是否把作者已经锁定的终极答案提前泄漏给读者/角色？
11. **FP/P/S**：相关伏笔、读者承诺、未曝光信息差哪些必须推进、哪些不能揭底。
12. **Narrative Pattern**：不只查具体招式，也查高层破局算法、爽点、代价、章尾是否重复。
13. **Context Receipt**：实际使用的 Canon/记录/规划来源已登记；关键源读取失败则 BLOCKED。

## MIDWRITE CAPACITY CHECK

正文约3000—3300字时强制检查一次：

- 剩余是否还有两个以上关键节点？有则顺延至少一个。
- 是否为了赶大纲开始缩短场景、连续跳时间、用对话快速解释世界观？有则回退。
- 当前核心事件是否已经形成自然后果？若是，允许在2800—4000字内收章，不额外加第二个高潮。
- 若核心事件尚未完成且预计超过4000字，允许跨章，不写成剧情摘要。
- 是否为了达到卷纲节点而强迫人物做不符合当前利益/认知的选择？若是，优先调整节点。

## PRECOMMIT

### 长度与节奏
- 正文是否处于2800—4000字硬区间？
- 常规情况下是否落在3200—3600字附近？偏离时是否有明确叙事理由？
- 后25%是否出现突然加速、连续设定解释、多次反转或多线清仓？若有，FAIL并重构。
- 是否存在为凑2800字而加入的重复心理、无效对话、景物填充？若有，FAIL并重构章节合同。

### 连续性
- Candidate 是否与正式正文、Kernel、Chapter Ledger 冲突？
- 新事实是否有来源章节和证据？
- 变化中的旧事实是否需要关闭有效区间，而非直接覆写？
- 人物状态、位置、伤势、道具、境界和时间是否连续？

### 宏观方向
- 本章实际发生后，仍然服务当前 Arc/Volume 核心问题吗？
- 如果正文自然导致规划改变，是否需要更新 Current Volume Detail / ARC_MAP，而不是假装没偏离？
- 是否为了提前完成后面某卷真相而越过 Reveal Ladder？

### 信息边界
- 作者真相是否提前泄露给读者？
- 读者已知是否被角色越权使用？
- SUSPECTS 是否误写成 KNOWS？
- 新反转是否重新解释旧事实，而不是无铺垫宣布旧事实作废？
- 新境界/新制度首次出现时，读者是否知道它在当前局面的相对高低与意义？

### 剧情质量
- 本章是否集中完成一两件最重要的事？
- 是否有认知/关系/风险/能力至少一项实质变化？
- 配角是否按自身利益行动？
- 是否无代价成功？
- 高层破局模型是否与近/远期章节重复？

### Anti-AI
- 自然段是否回归正常小说节奏，而非短句瀑布？
- 是否删掉动作→感知→身体反应的重复描写？
- 是否用可见证据替代情绪标签和“他终于明白”？
- 是否有万能比喻/空气凝固/深吸一口气等套话堆积？
- 章末是否以动作、对话或现实问题落地，而非总结/哲理/预告？

## CANON PROMOTION

用户确认后，在 Candidate 分支完成：
1. 正文固化。
2. Candidate Facts / Knowledge / Timeline / Relationship / FP-P-S 转 Canon。
3. 更新 Kernel temporal records。
4. 追加 Chapter Ledger + Chapter Record。
5. 重建派生 state/tracking 视图。
6. 更新 Narrative Pattern、Rolling Outline、Context Card。
7. 如果本章改变了卷内真实因果，同步修订 Current Volume Detail / ARC_MAP；不得修改已发生事实迎合旧纲。
8. 写 Commit Receipt 和变更 ID 清单。
9. 全部通过后才合并/推进 `main` Canon Horizon。

失败：不推进 `main`。

## POSTCOMMIT

- 校验 `main` Canon Horizon 与 Manuscript/Kernel/Ledger 一致。
- 每5章 Snapshot + Warm Memory compaction，同时检查是否仍服务当前卷核心问题。
- 每10章 Continuity + Narrative Pattern + Macro Drift Audit。
- Arc 结束生成 Arc Summary，并重算下一 Arc 细纲。
- 卷末生成 Major Canon Version，同时复核下一卷 Blueprint 是否仍成立。
- 若发生 Revision，必须执行 Change Impact Protocol，禁止静默修补。
