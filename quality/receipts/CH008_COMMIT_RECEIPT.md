# CH008 COMMIT RECEIPT

chapter: CH008
published_title: 《好药不能当废料》
user_status: 用户明确表示“已经发布”
canon_promotion: PASS
canon_horizon_after: CH008
next_chapter: CH009
series_architecture: SERIES_V2_8V_2M

## Canon manuscript

- `manuscript/volume-01-baigushan/CH008-好药不能当废料.md`
- 内容来自已通过CH008候选交稿流程、用户实际发布的最终稿。
- 未对正文做事后润色/Retcon。

## Canon/state products updated

- `state/diffs/CH008_STATE_DIFF.md`
- `tracking/chapter-records/CH008.md`
- `state/LIVE_STATE.md`
- `state/KNOWLEDGE_MATRIX.md`
- `state/RELATIONSHIP_STATE.md`
- `state/PLOT_LEDGER.md`
- `state/CHAPTER_LEDGER.md` append-only新增CH008
- `tracking/CONTEXT_CARD.md`
- `planning/ROLLING_OUTLINE.md`
- `planning/ARC_MAP.md`
- `quality/NARRATIVE_PATTERN_LEDGER.md`

## Canon Kernel incremental update

为避免每章晋升时重写多个大型JSONL造成截断/覆盖风险，本次引入：

- `canon/kernel/patches/README.md`
- `canon/kernel/patches/CH008.jsonl`

Manifest记录：

- `CANON_KERNEL_COMPACTED_THROUGH: CH007`
- `CANON_KERNEL_PATCH_DIR: canon/kernel/patches/`

`LOAD_ORDER V10` 已明确要求：若Horizon晚于compacted-through，冷启动必须加载所有未压实patch。

因此当前有效Kernel = 压实Kernel through CH007 + CH008 patch。

## CH008 locked facts

1. 韩鸦通过正常青绳核对/移交流程进入南二，亲耳得知陈缺次日继续工作与二验照旧。
2. 韩鸦最初要求陈缺故意把仍可用青藤扔进废篓增加西门开启；陈缺拒绝，以保住南二信用与双方可用价值为理由。
3. 韩鸦仍握剔虫把柄，但收窄次日具体任务为：照常挑药，只观察TARGET西门行动；不主动制造废料/接触；二验叫走则去。
4. 韩鸦给陈缺普通外敷伤膏；它只缓解表层筋肉紧张，不治经脉。章末仍剩大半包。
5. 陈缺章末留宿南廊；次日早饭后先去南二，二验等叫。
6. 真木属灵气仍几乎耗尽；右手仍抬不到肩高。
7. TARGET姓名、背景、完整路线/同伙与韩鸦杀人动机仍UNKNOWN。
8. 赵石CH008未出场，精确位置仍UNKNOWN。

## Memory Anchor migration

本次同时启用正式Memory Anchor生产系统：

- `quality/MEMORY_ANCHOR_SYSTEM.md`
- `tracking/MEMORY_ANCHOR_LEDGER.md`
- Rule Coverage新增 `MEM-001~006`
- Scene Card新增第9问
- Post-Draft / Publication / Final / Load Order / State Machine均已接入
- validator识别MEM Rule IDs并要求Memory控制文件存在

CH008正式Memory Diff：

- `MA-006`: PLANTED → ECHOED。CH007“救药越干净、门开越少”的成本冲突在CH008扩展到韩鸦也要求牺牲好药换开门次数；没有机械复读原句。
- `MA-008`: 新增PLANTED。陈缺在韩鸦威胁下以“因为师兄没去”指出威胁尚未执行，并用南二位置对双方的现实价值争到第一次有限执行边界。保护的是关系逻辑/人物声音，不允许未来复读成口头禅。

## Continuity protection for CH009

- CH009必须从CH008章末的次日安排自然开始。
- 不得无因清零南二工作入口。
- 不得恢复真木属灵气作解法。
- 不得连续第三章用“认药证明有用”作为主解。
- 不得复制CH008“韩鸦威胁→陈缺算账→韩鸦让步”谈判结构。
- 第一Arc仍缺陈缺真正的强行动场面，但Memory System明确禁止为了补缺口硬造名场面。

result: PASS
