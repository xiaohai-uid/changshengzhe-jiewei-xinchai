# CONTEXT RECEIPT SCHEMA V4

每章 Candidate 起草前建立 Context Receipt。它记录“这一章实际上依据了什么”，是可追溯构建凭证，不是正文内容。

建议路径：`quality/receipts/CHxxx_CONTEXT_RECEIPT.md`。

## 固定字段

- `chapter`
- `candidate_branch`
- `canon_horizon`
- `base_commit`
- `series_architecture`
- `context_policy_version`
- `entities_loaded[]`
- `facts_loaded[]`
- `knowledge_loaded[]`
- `timeline_events_loaded[]`
- `plots_loaded[]`
- `promises_loaded[]`
- `info_gaps_loaded[]`
- `recent_chapter_records[]`
- `full_text_sections_loaded[]`
- `planning_sources[]`
- `style_sources[]`
- `quality_sources[]`
- `rule_coverage_version`
- `post_draft_audit_version`
- `final_delivery_gate_version`
- `failure_memory_version`
- `workflow_state_machine_version`
- `expectation`
- `payoff_role`
- `upgrade_direction`
- `warnings[]`
- `degraded_sources[]`

## Block 顺序

1. World / hard constraints
2. Characters / entity state
3. Timeline
4. Plot + Promise + Info Gap
5. Recent continuity
6. Current Volume / Arc / Chapter contract
7. Expectation / Payoff / Upgrade
8. Style / quality constraints
9. Audit-rule versions and workflow state

## HOT质量源完整性

每章至少确认已加载：

- `quality/CHAPTER_GATE.md`
- `quality/WORKFLOW_STATE_MACHINE.md`
- `quality/RULE_COVERAGE_MATRIX.md`
- `quality/POST_DRAFT_AUDIT.md`
- `quality/PUBLICATION_GATE.md`
- `quality/EXPECTATION_PAYOFF_GATE.md`
- `quality/FINAL_DELIVERY_GATE.md`
- `quality/FAILURE_MEMORY.md`

缺失任一交稿硬门源：Receipt 标 `UNSAFE/BLOCKED`，不得进入 LOADED。

## 安全规则

关键 Canon 源读取失败时，不得假装上下文完整；标记 `UNSAFE/BLOCKED`。非关键投影读取失败可降级到 Canon Kernel 定点读取。

Receipt 不要求记录隐藏推理过程，只记录可审计的数据依赖、版本和校验结果。
