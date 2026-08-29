# CH007 WORKFLOW

CHAPTER: CH007
CANON_HORIZON: CH006
SERIES_ARCHITECTURE: SERIES_V2_8V_2M
CANDIDATE_BRANCH: chapter/CH007-v2
CANDIDATE_PATH: candidate/CH007.md
CURRENT_VOLUME_TARGET: ~70-75 chapters
CURRENT_ARC_TARGET: ~CH001-CH011/12
CURRENT_STATE: BLOCKED
CANDIDATE_REVISION_ID: NONE
CONTEXT_RECEIPT: MISSING_FOR_REWRITE
SCENE_CARD: MISSING_FOR_REWRITE
POST_DRAFT_AUDIT: PENDING
RULE_COVERAGE: PENDING
FAILURE_REGRESSION: PENDING
PUBLICATION_GATE: PENDING
EXPECTATION_PAYOFF_GATE: PENDING
CONTINUITY_PRECOMMIT: PENDING
FINAL_DELIVERY_GATE: PENDING
EXTERNAL_CI: PENDING
USER_DECISION: REWRITE_PREVIOUS_CANDIDATE

## Required Rule Set

- `quality/RULE_COVERAGE_MATRIX.md`
- `quality/POST_DRAFT_AUDIT.md`
- `quality/PUBLICATION_GATE.md`
- `quality/EXPECTATION_PAYOFF_GATE.md`
- `quality/FINAL_DELIVERY_GATE.md`
- `quality/FAILURE_MEMORY.md`
- `quality/WORKFLOW_STATE_MACHINE.md`
- `tools/chapter_gate.py`
- `.github/workflows/chapter-quality.yml`

## Notes

- 前一版CH007 Candidate已REWRITE，未进入Canon。
- 旧 `chapter/CH007` 是此前失败Candidate时代的历史分支，不再作为当前候选工作面。
- 当前工作分支固定为 `chapter/CH007-v2`，从最新main重新建立。
- 旧Candidate新增姓名、编号、南二具体器物/流程、运输细节均不具Canon权威。
- 系列规划为8卷/约200万字；旧12卷规模不得驱动本章。
- 第一卷目标约70—75章；七日考核Arc约CH011/12收束，但真实因果优先。
- 重新执行HOT LOAD、Context Receipt、Macro Alignment、Scene Card前，不得进入DRAFTED。
- 新CH007基于CH006已发布结尾重新起写。
- 完成正文后必须先冻结revision，生成Post-Draft Audit，并逐项执行Failure Memory回归测试。
- Post-Draft / Publication / Expectation-Payoff / Continuity / Final Delivery全部PASS且revision/SHA一致后，把Candidate及报告提交到候选分支。
- **提交后必须读取GitHub Actions真实运行结果；只有 `Chapter Quality Gate` 对候选分支当前精确HEAD返回 `success`，运行时才允许进入USER_REVIEW并向用户展示正文。**
- CI通过后若候选分支HEAD再次变化，旧CI自动失效，必须重新验证。
