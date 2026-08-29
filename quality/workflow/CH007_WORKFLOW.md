# CH007 WORKFLOW

CHAPTER: CH007
CANON_HORIZON: CH006
SERIES_ARCHITECTURE: SERIES_V2_8V_2M
CANDIDATE_BRANCH: chapter/CH007-v2
CANDIDATE_PATH: candidate/CH007.md
CURRENT_VOLUME_TARGET: ~70-75 chapters
CURRENT_ARC_TARGET: ~CH001-CH011/12
CURRENT_STATE: DRAFTED
CANDIDATE_REVISION_ID: CH007-R1-7457D669
CANDIDATE_SHA256: 7457d66918b3e007c9849b3603d6e88901465201dcece6c25a8a1b9beaa23d33
CONTEXT_RECEIPT: quality/receipts/CH007_CONTEXT_RECEIPT.md
SCENE_CARD: quality/scene-cards/CH007_SCENE_CARD.md
POST_DRAFT_AUDIT: PENDING
RULE_COVERAGE: PENDING
FAILURE_REGRESSION: PENDING
PUBLICATION_GATE: PENDING
EXPECTATION_PAYOFF_GATE: PENDING
CONTINUITY_PRECOMMIT: PENDING
FINAL_DELIVERY_GATE: PENDING
EXTERNAL_CI: PENDING
USER_DECISION: PENDING_REWRITE_REVIEW

## State History

- BLOCKED: previous Candidate rejected; no rewrite artifacts.
- LOADED: HOT LOAD, Published Prose Anchors and targeted Canon Kernel recorded in Context Receipt.
- MACRO_ALIGNED: current Arc, volume function, truth ceiling and expectation/payoff direction checked.
- SCENE_READY: Scene Card passed character desire, obstacle, limited information, choice, durable payoff, cost and supporting-character independent-action checks.
- DRAFTED: complete Candidate frozen as CH007-R1-7457D669 / SHA256 7457d66918b3e007c9849b3603d6e88901465201dcece6c25a8a1b9beaa23d33.

## Draft Capacity Record

- Mechanical body count by validator-equivalent counting: 3262.
- Normal target 3200-3600 satisfied; hard 2800-4000 satisfied.
- Core events: 2.
  1. 陈缺在南二真实药材处理压力中主动暴露药铺能力，救回受潮发热药材并争取可用位置。
  2. TARGET-0001利用废药出门流程试探侧门，与陈缺的分拣目标发生有限碰撞。
- Midwrite Capacity Check at 3000-3300 equivalent: main choice and consequence already formed; no two-plus unresolved mandatory nodes were forced into the ending. No additional subplot added.
- Residual true qi did not recover or become solution.

## Required Rule Set

- quality/RULE_COVERAGE_MATRIX.md
- quality/POST_DRAFT_AUDIT.md
- quality/PUBLICATION_GATE.md
- quality/EXPECTATION_PAYOFF_GATE.md
- quality/FINAL_DELIVERY_GATE.md
- quality/FAILURE_MEMORY.md
- quality/WORKFLOW_STATE_MACHINE.md
- tools/chapter_gate.py
- .github/workflows/chapter-quality.yml

## Delivery Lock

- Candidate cannot be shown to user from DRAFTED state.
- All downstream reports must bind exactly to CH007-R1-7457D669 and the stored SHA256.
- Any Candidate edit invalidates this freeze and requires a new revision/SHA plus affected gate reruns.
