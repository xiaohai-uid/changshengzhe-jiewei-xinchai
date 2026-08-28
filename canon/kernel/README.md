# Canon Kernel V3

本目录是《长生者皆为薪柴》的规范化 Canon 数据层，面向百万至五百万字长期连载。

## 权威模型

Canonical Source of Truth 由以下几类文件共同构成，而不是某一个巨大状态文件：

1. `canon/CANON_CORE.md`：不可轻易改变的世界硬规则。
2. `manuscript/`：已经被用户确认并进入 `main` 的正式正文。
3. `state/CHAPTER_LEDGER.md`：只追加的不可撤销章节事实索引。
4. 本目录的规范化 Canon 数据：实体、事实、人物认知、时间线、关系、剧情线、读者承诺、信息差。

`state/*.md`、`tracking/CONTEXT_CARD.md`、`tracking/TRACKING_STATE.json`、`tracking/AUTHOR_TRUTH.md`、`tracking/READER_KNOWN.md` 均为便于续写的人类可读投影/摘要，不得在与 Canon Kernel 冲突时反向覆盖权威源。

## Canon Horizon

当前 Canon Horizon：`CH006`。

只有已确认章节才能推进 Canon Horizon。正在创作的章节属于 Candidate，不得提前写入 `main` 的 Canon Kernel。

## Candidate → Canon

下一章工作分支建议为 `chapter/CH007`，属于 Candidate Plane。

候选章节通过 Scene Card / Publication Gate / PRECOMMIT 后，在该分支内完成候选事实提取和所有派生更新；只有全部校验通过且用户确认，才把这一整组变化晋升/合并到 `main`。失败时 Candidate 可以重写，但 `main` 不受污染。

## Temporal Rule

Canon 数据尽量使用 `valid_from_chapter` / `valid_to_chapter` 描述有效区间。旧事实被后续正文改变时，关闭旧区间并新增新事实，不静默抹掉历史。

## Entity Rule

长期实体使用永久 ID。名称变化、别名和身份变化不得产生新的实体 ID。一次性无持续价值的物件/路人不强行编号。

当前交易目标在姓名锁定前使用永久占位 ID `TARGET-0001`；后续姓名揭示时只更新 `canonical_name`，不得另建一个角色实体造成串人。

## Unknown Rule

UNKNOWN、SUSPECTS、相关性观察不得被升级为客观事实。证据不足时宁可少写 Canon，也不补全答案。

## Revision Rule

任何 Retcon/Revision 必须执行 `quality/CHANGE_IMPACT_PROTOCOL.md`。已经发布的 Chapter Ledger 不偷偷删除；如必须修订，新增修订记录并列出受影响章节/实体/伏笔/信息差。
