# Candidate Plane

本目录只用于 `chapter/CHxxx` 候选分支，不代表 Canon。

## 固定路径

当前完整候选正文必须保存为：

`candidate/CHxxx.md`

例如：`candidate/CH007.md`。

对应必须存在：

- `quality/receipts/CHxxx_CONTEXT_RECEIPT.md`
- `quality/scene-cards/CHxxx_SCENE_CARD.md`
- `quality/reviews/CHxxx_POST_DRAFT_AUDIT.md`
- `quality/reviews/CHxxx_PUBLICATION_GATE.md`
- `quality/reviews/CHxxx_EXPECTATION_PAYOFF_GATE.md`
- `quality/reviews/CHxxx_CONTINUITY_PRECOMMIT.md`
- `quality/reviews/CHxxx_FINAL_DELIVERY.md`
- `quality/workflow/CHxxx_WORKFLOW.md`

## Version binding

完整 Candidate 冻结后计算 SHA-256。

Post-Draft / Publication / Expectation-Payoff / Continuity / Final Delivery 报告都必须包含：

```text
candidate_revision_id: CHxxx-Rnn
candidate_sha256: <64 hex>
result: PASS|REWRITE|BLOCKED
```

任何正文改动都会改变 SHA-256。最终校验器发现报告 SHA 与正文不一致时直接失败。

## Delivery contract

`chapter/CHxxx` 分支上的 GitHub Actions `Chapter Quality Gate` 必须通过后，才允许把完整 Candidate 交给用户审阅。

自动校验覆盖：

- 当前8卷/200万架构；
- Candidate 是否存在；
- 2800—4000硬字数；
- 连续一句式叙述段；
- 后台语言泄漏；
- Context Receipt / Scene Card 是否存在；
- 工作流各 Gate 是否 PASS；
- 所有报告是否绑定同一 revision 与 Candidate SHA；
- Rule Coverage Matrix 的 Rule IDs 是否全部在 Post-Draft Audit 中 PASS/NA；
- FAIL/UNKNOWN 是否存在。

人物是否工具化、因果是否自然、爽感是否成立等文学判断仍需审稿报告人工/模型判断；但报告缺失、结果非PASS、版本不一致时，程序会阻断。

用户确认前，本目录任何内容都不得写入正式 Canon。
