# LOAD ORDER V5

每次用户说“继续 / 写下一章”时，采用分层冷启动。目标不是重读全书，而是同时保证：上一章因果、当前 Arc、当前卷终点、全书真相方向与正式小说文风都被加载。

## A. 每章必读 HOT

1. `PROJECT_RULES.md`
2. `MANIFEST.md`
3. `tracking/CONTEXT_CARD.md`
4. `planning/ARC_MAP.md` 当前 Arc
5. `planning/ROLLING_OUTLINE.md` 当前章
6. 当前卷细纲中与本 Arc 相关部分：当前为 `planning/volumes/V01_DETAIL.md`
7. 最近 1—3 个 `tracking/chapter-records/`；必要时回读上章结尾全文
8. `style/STYLE_GUIDE.md`
9. `quality/SCENE_CARD_TEMPLATE.md`
10. `quality/CHAPTER_GATE.md`
11. `quality/PUBLICATION_GATE.md`

## A2. Published Prose Anchor（每章强制）

每次起草正文前，必须回读至少 2 段已经发布并被确认质量稳定的正式正文，优先从当前卷最近章节与 CH001—CH003 中选择。

用途不是复制句子，而是重新校准：
- 自然段长度；
- 动作、观察、心理如何合段；
- 对话密度；
- 推理如何藏进行为；
- 章节世界内部语言，而不是后台管理语言。

若 Candidate 出现明显短句瀑布、提纲扩写、研究报告腔，优先回到已发布正文重新校准，而不是仅靠抽象 Style Guide 修补。

## B. 书级方向 WARM/PERMANENT

以下不要求每章全量塞入上下文，但在冷启动、Arc切换、每5章Snapshot、每10章Audit、出现新世界观/境界/势力时必须定点读取：

- `canon/CANON_CORE.md`
- `canon/WORLD_BIBLE.md`
- `canon/CULTIVATION_SYSTEM.md`
- `canon/FACTIONS_GEOGRAPHY.md`
- `tracking/AUTHOR_TRUTH.md`
- `planning/SERIES_MASTER_OUTLINE.md`
- `planning/VOLUME_BLUEPRINTS.md`
- `planning/TRUTH_REVEAL_LADDER.md`
- `planning/CHARACTER_LONG_ARCS.md`

原则：**短期因果决定本章怎么发生；卷纲决定本章为什么值得发生；总纲决定这件事最终把整本书推向哪里。**

## C. 定点读取 Canon Kernel

根据本章合同中的永久 ID，只读取相关：
- `canon/kernel/ENTITIES.jsonl`
- `FACTS.jsonl`
- `KNOWLEDGE.jsonl`
- `TIMELINE.jsonl`
- `RELATIONSHIPS.jsonl`
- `PLOTS.jsonl`
- `PROMISES.jsonl`
- `INFO_GAPS.jsonl`

遇到旧事实争议，再按 `source_chapter` / Fact ID / Entity ID / FP-P-S ID 回查 Chapter Record 或正式正文。禁止因为“不确定”就默认补全。

## D. 新概念读取规则

### 首次出现新境界
必须读取 `canon/CULTIVATION_SYSTEM.md` 对应境界；正文只给当前场景所需的最小尺度，不一次百科讲完。

### 首次出现新势力/新地域
必须读取 `canon/FACTIONS_GEOGRAPHY.md` 与当前卷 Blueprint，确认该势力为何存在、资源来源、受益者和成本承担者。

### 推进世界真相
必须检查 `planning/TRUTH_REVEAL_LADDER.md`：本卷允许推进到哪一层，哪些答案仍应保持 UNKNOWN。

### 核心人物做重大选择
必须检查 `planning/CHARACTER_LONG_ARCS.md`，防止人物为了赶大纲突然性格漂移。

## E. Context Receipt

起草 Candidate 前创建/刷新 `quality/receipts/CHxxx_CONTEXT_RECEIPT.md`，记录实际读取依赖。

至少登记：
- Canon Horizon；
- 当前 Arc / Volume；
- 相关 Fact / Knowledge / FP-P-S；
- 最近正文锚；
- Published Prose Anchor 实际读取章节；
- 本章若涉及的新境界/势力/真相层；
- 是否读取当前卷细纲。

关键 Canon 或规划源读取失败时，本章标 `BLOCKED/UNSAFE`，不能假装已完成连续性检查。

## F. Scene Isolation

Rolling Outline 不能直接展开成正文。

写正文前必须先按 `quality/SCENE_CARD_TEMPLATE.md` 把本章翻译成角色世界内部场景。Scene Card 必须脱离 CH/FP/Canon/Knowledge 等后台标签，只保留人物欲望、现场阻力、有限信息、选择与后果。

如果 Scene Card 仍像“任务列表”，不得进入 WRITE。

## G. 写作流程

LOAD → MACRO ALIGNMENT → CONTEXT RECEIPT → CAUSAL CHECK → REPETITION/PATTERN CHECK → SCENE CARD → PREWRITE GATE → WRITE → MIDWRITE CAPACITY CHECK → PUBLICATION GATE → PRECOMMIT → EXTRACT CANDIDATE → 用户确认 → CANON PROMOTION → POSTCOMMIT → NEXT CAUSAL HOOK。

### MACRO ALIGNMENT 必答

写章前内部必须能回答：
1. 这章属于哪个 Arc？
2. 它推进当前卷哪个核心问题？
3. 它推进/保护了哪条长期人物弧或真相层？
4. 如果删掉这章，卷级结构损失什么？若答案是“几乎没有”，则本章合同需要重做。

## H. 冲突优先级

已发布正文事实 > Canon Core / World Bible > 当前有效人物状态 > 卷级终点 > 当前 Arc > Rolling Outline > 早期具体章号计划。

如果卷纲和已发生正文冲突，修订卷纲；如果短期剧情连续偏离卷级功能，必须在 Arc Audit 中显式重算，而不是悄悄变成想到哪写到哪。
