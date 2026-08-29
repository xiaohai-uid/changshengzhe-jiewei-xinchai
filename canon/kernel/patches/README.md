# CANON KERNEL PATCHES

## 目的

`canon/kernel/*.jsonl` 是周期性压实后的规范化 Canon Kernel。

为了避免每章晋升时重写多个大型 JSONL 文件，新的 Canon 事实先以**逐章增量补丁**写入本目录；冷启动时，补丁与压实Kernel共同构成当前有效Canon。

## 权威规则

- `MANIFEST.md` 记录 `CANON_KERNEL_COMPACTED_THROUGH`。
- 若 `CANON_HORIZON` 晚于该章节，则必须读取从压实点之后到当前Horizon的所有 `patches/CHxxx.jsonl`。
- patch中的事实拥有与对应已发布正文相同的Canon权威；若与已发布正文冲突，以正文为准。
- patch不能覆盖旧事实做静默Retcon；需要关闭旧Temporal fact时必须显式写 `closes` / `supersedes` 关系。
- 每5章Snapshot或每10章Continuity Audit时可执行Kernel Compaction：把patch合并进对应 FACTS/KNOWLEDGE/TIMELINE/RELATIONSHIPS/PLOTS/INFO_GAPS，再更新 `CANON_KERNEL_COMPACTED_THROUGH`。

## Patch记录格式

每行一个JSON对象，至少包含：

```json
{"kind":"fact|knowledge|relationship|timeline|plot|info_gap","id":"...","source_chapter":8,"status":"canonical","payload":{}}
```

可选字段：

- `closes`: 被本记录关闭的旧Fact/状态描述；
- `supersedes`: 显式替代的旧记录；
- `certainty`: confirmed / observed / inferred / reported；
- `note`: 作者层最小说明。

## 冷启动规则

每章LOAD Canon Kernel时：

1. 读取需要的压实Kernel文件；
2. 读取 `MANIFEST.CANON_KERNEL_COMPACTED_THROUGH`；
3. 若当前Horizon更晚，读取所有尚未压实的逐章patch；
4. 相同主题以更晚的Temporal record为当前状态，但历史事实不删除；
5. UNKNOWN/SUSPECTS仍服从Knowledge状态，不因patch存在自动升级。

本目录是为了**增量写入和防止大文件误覆盖**，不是第二套平行Canon。
