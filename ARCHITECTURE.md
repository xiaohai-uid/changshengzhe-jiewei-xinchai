# 《长生者皆为薪柴》仓库架构 v3

本仓库采用“已发布正文 Canon + Canon Kernel + 状态投影 + 规划层 + 质量门禁”的混合模式。

当前系列规划：**约200万字 / 8卷 / 约580—620章**。规划可以调整未来，但不能覆盖已发生正文。

## 一、事实权威层级

发生冲突时按以下顺序裁决：

1. 用户当前明确决定
2. `main` 分支已发布正文 + `canon/CANON_CORE.md`
3. World Bible / Cultivation System 等硬世界规则
4. `canon/kernel/` + `state/CHAPTER_LEDGER.md`
5. Snapshot / State Diff / tracking投影
6. `planning/` 中当前有效规划
7. 旧卷纲与早期设想

## 二、规划层级

当前规划结构：

**Series Master → Volume Blueprints → Current Volume Detail → Arc Map → Rolling Outline → Scene Card**

其中：

- `SERIES_MASTER_OUTLINE.md`：8卷/200万字总方向、终局命题；
- `VOLUME_BLUEPRINTS.md`：八卷核心问题与Arc顺序；
- `planning/volumes/V01_DETAIL.md`：当前第一卷细纲；
- `ARC_MAP.md`：当前卷各Arc容量与功能；
- `ROLLING_OUTLINE.md`：只约束下一章及后约3章的因果方向；
- Scene Card：把后台规划翻译成人物世界内部场景。

规划不允许直接生成正文。

## 三、为什么保留 tracking/

长期连载时，多个Markdown容易出现“各自都对、彼此不一致”。因此：

- `tracking/TRACKING_STATE.json`：结构化当前状态投影；
- `tracking/CONTEXT_CARD.md`：冷启动热状态；
- `tracking/AUTHOR_TRUTH.md`：作者层确定事实；
- `tracking/READER_KNOWN.md`：读者当前可确认/合理推断；
- `tracking/chapter-records/`：每章连续性变化。

## 四、章节 FAIL-CLOSED 工作流

每章不得靠“记得做过”判断流程，而必须有可追踪状态。

### 1. LOAD / MACRO ALIGNMENT

读取HOT源，确认Canon Horizon、当前Arc、当前正向期待、卷级功能和人物长期弧。

### 2. CONTEXT RECEIPT

实际登记读取来源。关键源缺失则BLOCKED。

### 3. SCENE CARD

Rolling Outline必须先被翻译为世界内部的欲望、阻力、有限信息、选择、收益与代价。

### 4. WRITE / MIDWRITE

单章常规3200—3600字；约3000—3300字时检查容量，剩余重要节点过多则顺延。

### 5. 三重硬门

- `PUBLICATION_GATE`：小说质感、段落、人物主体性、非提纲扩写；
- `EXPECTATION_PAYOFF_GATE`：期待→兑现→升级、收益耐久、主动权与奖励多样性；
- `CONTINUITY PRECOMMIT`：Canon、Knowledge、能力、时间线、关系、伏笔一致。

三者全部PASS才可进入USER_REVIEW。

### 6. USER REVIEW / CANON PROMOTION

用户确认后才更新正文、Kernel、Ledger、Tracking、Rolling Outline。被否定Candidate不得污染Canon。

## 五、200万字压缩机制

旧12卷/350—500万规划已废弃。

当前采用八卷版本，核心压缩方式：

1. 合并相邻理念卷，而不是删除核心真相；
2. 一个结论只做一次主证明；
3. 后续重复出现时写行动后果，不再重复调查；
4. 地图变化必须带来新规则/利益结构；
5. 旧伏笔优先于新增谜题；
6. 第一卷目标约70—75章，其余卷约65—90章；
7. 预计超过约210万字前必须做Macro Drift Audit。

## 六、上下文预算

冷启动不要求重读全书。优先：

1. `PROJECT_RULES.md`
2. `MANIFEST.md`
3. `tracking/CONTEXT_CARD.md`
4. 当前 `ARC_MAP.md`
5. `ROLLING_OUTLINE.md`
6. 当前卷Detail相关部分
7. 最近1—3个Chapter Record / 必要正文结尾
8. Style Guide / Scene Card / Gate文件
9. 本章涉及的Kernel ID

## 七、分支规则

- `main`：正式Canon。
- `chapter/CHxxx`：下一章工作分支（如使用）。
- 用户认可章节后才进入正式Canon Horizon。
- 被否定草稿、Scene Card失败稿、Gate失败稿均不得反向写入Canon。

## 八、研究层

`quality/research/` 保存番茄官方、榜单样本、知乎作者经验等商业阅读研究。

研究只影响质量与未来规划，不拥有事实权威。禁止把榜单相关性、单作者经验或短篇公式直接升级成世界规则/机械写作公式。

核心架构目标：**写得久而不吃书，写得紧而不疲劳，商业节奏增强但不牺牲人物和因果。**
