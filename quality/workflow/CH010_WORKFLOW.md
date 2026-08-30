# CH010 WORKFLOW

CHAPTER: CH010
START_CANON_HORIZON: CH009
FINAL_CANON_HORIZON: CH010
SERIES_ARCHITECTURE: SERIES_V2_8V_2M
CANDIDATE_BRANCH: chapter/CH010
FINAL_MANUSCRIPT: manuscript/volume-01-baigushan/CH010-这笔账得有人认.md
CURRENT_VOLUME_TARGET: ~70-75 chapters
CURRENT_ARC_TARGET: ~CH001-CH011/12
CURRENT_STATE: CANON
CANDIDATE_REVISION_ID: CH010-R3-TITLE-7BCD91EF
CANDIDATE_SHA256: 7bcd91eff5282269d6972f08bce568d4b2d3a243804baecb1974b598b2d7de31
CONTEXT_RECEIPT: quality/receipts/CH010_CONTEXT_RECEIPT.md
SCENE_CARD: quality/scene-cards/CH010_SCENE_CARD.md
POST_DRAFT_AUDIT: PASS
RULE_COVERAGE: PASS
FAILURE_REGRESSION: PASS
PUBLICATION_GATE: PASS
EXPECTATION_PAYOFF_GATE: PASS
CONTINUITY_PRECOMMIT: PASS
FINAL_DELIVERY_GATE: PASS
EXTERNAL_CI: PASS
EXTERNAL_CI_RUN_ID: 33289158711
EXTERNAL_CI_HEAD: 34ca5dc94bc43847151e26ab2905490e035db187
USER_DECISION: APPROVED
CANON_PROMOTION: PASS

## State History

- BLOCKED → LOADED → MACRO_ALIGNED → SCENE_READY.
- DRAFTED-R1: invalidated before downstream PASS because explanatory-summary risks were found.
- DRAFTED-R2: body revised to remove explanatory summaries; content gates and exact-head CI passed.
- USER_REVIEW: user explicitly approved CH010 body.
- TITLE_REVIEW: user指出章节名质量弱。旧标题《少了一个人以后》判为事件摘要型弱标题。
- DRAFTED-R3-TITLE: body unchanged; title revised to《这笔账得有人认》. Because title is part of Candidate bytes, R2 Gate bindings were invalidated and all downstream reports rebound to R3.
- EXTERNAL_CI_R3: GitHub Actions `Chapter Quality Gate` run `33289158711` on exact head `34ca5dc94bc43847151e26ab2905490e035db187` completed successfully; validator regression and strict-delivery validation both succeeded.
- USER_DECISION: user said“我已经确认了”。
- CANON_PROMOTION: approved Candidate promoted to `main`, manuscript written under final title, CH010 kernel patch / State Diff / Chapter Record / Commit Receipt / Snapshot V2.3 / Continuity Audit created, projections advanced, Manifest moved to CH011.

## Frozen R3 metrics

- Mechanical body count: 3220.
- Core events: 2.
- Paragraphs: 111.
- Max consecutive one-sentence narrative paragraphs: 2.
- Backend-language scan: 0 hit.
- Listed AI-fingerprint scan: 0 hit.
- Body difference from R2: NONE.
- Final title: `这笔账得有人认`.

## Canon protection

- TARGET remains unreturned at chapter end, not confirmed escaped/captured/dead.
- Han Ya learns through an on-page messenger/handoff channel.
- Chen reports only facts he observed and accepts accountability exposure.
- Lao Zhou acts for production/accountability.
- Han's direct action serves his own threatened interest; no mentor/hero framing.
- Zhao half-day work and Chen three-day recheck remain valid.
- No true-qi recovery.

## Post-promotion artifacts

- `manuscript/volume-01-baigushan/CH010-这笔账得有人认.md`
- `canon/kernel/patches/CH010.jsonl`
- `state/diffs/CH010_STATE_DIFF.md`
- `tracking/chapter-records/CH010.md`
- `quality/receipts/CH010_COMMIT_RECEIPT.md`
- `canon/snapshots/STATE_SNAPSHOT_V2.3.md`
- `quality/reviews/CONTINUITY_AUDIT_CH010.md`
- `quality/CHAPTER_TITLE_STANDARD.md`

CH010 is closed. Future work starts from CH011 and must not reopen this Candidate unless the user explicitly requests a published-text revision.
