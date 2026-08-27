# MEMORY POLICY V3

目标：支持百万至五百万字连载时仍能定点恢复事实，不依赖整书重读。

## 1. HOT MEMORY

每次续写必读：
- `MANIFEST.md`
- `tracking/CONTEXT_CARD.md`
- 当前章合同 / Context Receipt
- 最近 1—3 章的紧凑 Chapter Record 与必要结尾

用途：承接当前动作、场景、短期人物状态。

## 2. WARM MEMORY

当前 Arc（约10—30章）的：
- Arc Map / Arc Summary
- 活跃 FP / P / S
- 相关核心角色状态
- 当前时间线区段

用途：避免短期重复与局部因果漂移。

## 3. COLD MEMORY

当前卷 Snapshot、卷级人物关系与中期承诺。

用途：Arc 切换和跨阶段恢复。

## 4. PERMANENT MEMORY

- `canon/CANON_CORE.md`
- `canon/kernel/ENTITIES.jsonl`
- 仍有效的 Canon Facts / Knowledge / Timeline / Relationships
- 长期 P / S / FP

用途：永久身份、世界硬规则、长期谜题、不可忘事实。

## 5. ARCHIVE

- 完整正文
- 逐章 Record
- 旧 Snapshot / Audit

默认不全量加载。出现争议时按永久 ID、Fact ID、FP/P/S ID、来源章节定点回查。

## Context Budget

Context Card 保持紧凑；逐章 Record 只记影响连续性的变化。不得因为篇幅增长而把全部历史 Diff 或全文塞进每次续写上下文。

## Compaction

- 每章：更新 Hot 状态与 Chapter Record。
- 每5章：生成 Snapshot，并压缩/刷新 Warm 状态。
- 每10章：Continuity Audit + Narrative Pattern Audit。
- 每个 Arc 收束：生成 Arc Summary，旧 Hot 转 Archive。
- 每卷：Major Canon Version + 卷级审计。

Compaction 只能改变检索/摘要形式，不能删除 Canon 历史。