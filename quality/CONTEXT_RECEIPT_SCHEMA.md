# CONTEXT RECEIPT SCHEMA V3

每章 Candidate 起草前建立 Context Receipt。它记录“这一章实际上依据了什么”，是可追溯构建凭证，不是正文内容。

建议路径：`quality/receipts/CHxxx_CONTEXT_RECEIPT.md`（放在 Candidate 分支；章节晋升后随之进入 main）。

## 固定字段

- `chapter`
- `candidate_branch`
- `canon_horizon`
- `base_commit`
- `context_policy_version`
- `entities_loaded[]`
- `facts_loaded[]`
- `knowledge_loaded[]`
- `timeline_events_loaded[]`
- `plots_loaded[]`
- `promises_loaded[]`
- `info_gaps_loaded[]`
- `recent_chapter_records[]`
- `full_text_sections_loaded[]`：只有确实需要全文时记录
- `planning_sources[]`
- `style_sources[]`
- `warnings[]`
- `degraded_sources[]`

## Block 顺序

1. World / hard constraints
2. Characters / entity state
3. Timeline
4. Plot + Promise + Info Gap
5. Recent continuity
6. Chapter contract
7. Style / quality constraints

## 安全规则

关键 Canon 源读取失败时，不得假装上下文完整；标记 `UNSAFE/BLOCKED`。非关键投影读取失败可降级到 Canon Kernel 定点读取。

Receipt 不要求记录隐藏推理过程，只记录可审计的数据依赖和校验结果。