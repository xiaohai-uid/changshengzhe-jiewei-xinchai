# 《长生者皆为薪柴》仓库架构 v2

本仓库采用“正文 Canon + 单一结构化追踪权威 + 人类可读派生视图”的混合模式。

## 一、事实权威层级

发生冲突时按以下顺序裁决：

1. `main` 分支已发布正文
2. `state/CHAPTER_LEDGER.md` 中已追加的不可撤销事实
3. `tracking/TRACKING_STATE.json` 当前结构化状态
4. `state/`、`tracking/*.md` 等人类可读视图
5. `planning/` 中的滚动计划
6. 旧卷纲与早期设想

规划永远不能覆盖已发生正文。

## 二、为什么增加 tracking/

原有 LIVE / KNOWLEDGE / RELATIONSHIP / PLOT / CHAPTER 六套状态继续保留，但它们是便于阅读的视图。长期连载时，多个 Markdown 文件容易出现“各自都对、彼此不一致”的问题，因此新增：

- `tracking/TRACKING_STATE.json`：唯一结构化当前状态。
- `tracking/CONTEXT_CARD.md`：冷启动状态卡，写下一章优先读取。
- `tracking/AUTHOR_TRUTH.md`：作者层确定事实；不得把 UNKNOWN 填成答案。
- `tracking/READER_KNOWN.md`：读者截至当前正文能确认/合理推断的信息。
- `tracking/chapter-records/`：每章只记录影响未来连续性的紧凑变化。

## 三、章节事务

每章使用三阶段门禁：

### PREWRITE
加载状态卡、当前合同/滚动纲、最近章节、相关角色与伏笔；做因果检查、重复破局检查、信息差检查。

### PRECOMMIT
正文完成后检查：事实冲突、角色越权知情、力量来源/进入/代价/获益者、同类爽点重复、AI式分段/总结式章尾、伏笔处理。

### POSTCOMMIT
提取事实 → 更新 Tracking State → 更新派生状态 → 追加 Chapter Ledger → 重算 Rolling Outline → 每5章 Snapshot / 每10章 Audit。

## 四、上下文预算

长篇不允许每次从第一章重读。

冷启动优先：

1. `PROJECT_RULES.md`
2. `MANIFEST.md`
3. `tracking/CONTEXT_CARD.md`
4. `planning/ROLLING_OUTLINE.md`
5. 最近 3 章正文或其关键结尾
6. 仅定点读取本章涉及的角色/伏笔/规则文件

遇到旧细节争议时，再回查对应正文或 Chapter Ledger。

## 五、分支规则

- `main`：正式 Canon。
- `chapter/CHxxx`：下一章工作分支。
- 用户认可章节后才进入 `main`。
- 被否定草稿不得污染正式 State。

## 六、吸收来源

架构思想来自本账号 `storyrepo` 已整理的长篇生产协议，并参考其中标注的 webnovel-writer、oh-story、AI_NovelGenerator、chinese-novelist 等实现。这里只吸收适合本书的协议层，不机械复制无法在当前网页版工作流中执行的整套引擎。