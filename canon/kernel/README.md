# Canon Kernel V3

本目录是《长生者皆为薪柴》的规范化 Canon 数据层，面向长期连载。

## 权威模型

Canonical Source of Truth 由以下几类文件共同构成：

1. `canon/CANON_CORE.md`：不可轻易改变的世界硬规则。
2. `manuscript/`：已经被用户确认并进入 `main` 的正式正文。
3. `state/CHAPTER_LEDGER.md`：只追加的不可撤销章节事实索引。
4. 本目录的规范化 Canon 数据：实体、事实、人物认知、时间线、关系、剧情线、读者承诺、信息差。

`state/*.md`、`tracking/CONTEXT_CARD.md`、`tracking/TRACKING_STATE.json`、`tracking/AUTHOR_TRUTH.md`、`tracking/READER_KNOWN.md` 均为便于续写的人类可读投影/摘要，不得在与 Canon Kernel 冲突时反向覆盖权威源。

## Canon Horizon

当前 Canon Horizon：`CH007`。

只有已确认章节才能推进 Canon Horizon。正在创作的章节属于 Candidate，不得提前进入 Canon Kernel。

## Candidate → Canon

下一章工作分支为 `chapter/CH008`，属于 Candidate Plane。

候选章节必须完成 Context Receipt / Scene Card / Post-Draft / Publication / Expectation-Payoff / Continuity / Final Delivery，并由GitHub Actions对候选分支精确HEAD严格验证成功；用户确认后，才晋升到 `main`。

## Temporal Rule

Canon 数据尽量使用 `valid_from_chapter` / `valid_to_chapter` 描述有效区间。旧事实被后续正文改变时，关闭旧区间并新增新事实，不静默抹掉历史。

## Entity Rule

长期实体使用永久 ID。名称变化、别名和身份变化不得产生新的实体 ID。一次性无持续价值的物件/路人不强行编号。

当前交易目标在姓名锁定前使用永久占位 ID `TARGET-0001`；后续姓名揭示时只更新 `canonical_name`，不得另建角色实体。

CH007新增 `CHAR-0006` 老周与 `PLACE-0006` 南二，仅锁正文已出现的职责/功能，不外推境界、职衔或更远路线。

## Unknown Rule

UNKNOWN、SUSPECTS、相关性观察不得被升级为客观事实。证据不足时宁可少写 Canon，也不补全答案。

## Revision Rule

任何 Retcon/Revision 必须执行 `quality/CHANGE_IMPACT_PROTOCOL.md`。已经发布的 Chapter Ledger 不偷偷删除；如必须修订，新增修订记录并列出受影响章节/实体/伏笔/信息差。
