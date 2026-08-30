# CH010 WORKFLOW

CHAPTER: CH010
CANON_HORIZON: CH009
SERIES_ARCHITECTURE: SERIES_V2_8V_2M
CANDIDATE_BRANCH: chapter/CH010
CANDIDATE_PATH: candidate/CH010.md
CURRENT_VOLUME_TARGET: ~70-75 chapters
CURRENT_ARC_TARGET: ~CH001-CH011/12
CURRENT_STATE: FINAL_DELIVERY_PASS
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
EXTERNAL_CI: PENDING_EXACT_HEAD
USER_DECISION: APPROVED

## State History

- BLOCKED → LOADED → MACRO_ALIGNED → SCENE_READY.
- DRAFTED-R1: invalidated before downstream PASS because explanatory-summary risks were found.
- DRAFTED-R2: body revised to remove explanatory summaries; all content gates passed and exact-head CI succeeded.
- USER_REVIEW: user explicitly approved CH010 body.
- DRAFTED-R3-TITLE: user also criticized chapter-title quality. Only the title changed from `少了一个人以后` to `这笔账得有人认`; body remained byte-for-byte identical below the title line.
- R3 invalidated R2 SHA bindings and reran/rebound Post-Draft, Publication, Expectation/Payoff, Continuity and Final Delivery to the new exact candidate SHA.

## Prewrite gates

LOAD: PASS
MACRO_ALIGNMENT: PASS
CONTEXT_RECEIPT: PASS
SCENE_CARD: PASS
MEMORY_Q9: PASS
REPETITION_CHECK: PASS

## Frozen R3 metrics

- Mechanical body count: 3220.
- Core events: 2.
- Paragraphs: 111.
- Max consecutive one-sentence narrative paragraphs: 2.
- Backend-language scan: 0 hit.
- Listed AI-fingerprint scan: 0 hit.
- Body difference from R2: NONE.
- Title: `这笔账得有人认`.

## Delivery contract

- TARGET remains unreturned, not confirmed escaped.
- Han Ya learns through an on-page messenger/handoff channel.
- Chen reports only facts he observed and accepts accountability exposure.
- Lao Zhou acts for production/accountability.
- Han's direct action serves his own threatened interest; no mentor/hero framing.
- Zhao half-day work and Chen three-day recheck remain valid.
- Exact-head external CI must succeed before canon promotion.
