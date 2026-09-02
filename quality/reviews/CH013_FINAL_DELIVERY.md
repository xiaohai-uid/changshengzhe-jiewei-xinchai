# CH013 FINAL DELIVERY

CANDIDATE_REVISION_ID: CH013-R2-LEAF-NOT-YELLOW
CANDIDATE_SHA256: ea4994a2571015d4808cc27e6f4fdff97cca37747b4f9a4251a86e7052f3f79c
RESULT: PASS

POST_DRAFT_REPORT: quality/reviews/CH013_POST_DRAFT_AUDIT.md
NATURALNESS_REPORT: quality/reviews/CH013_NATURALNESS.md
RULE_COVERAGE_REPORT: quality/reviews/CH013_RULE_COVERAGE.md
PUBLICATION_REPORT: quality/reviews/CH013_PUBLICATION_GATE.md
EXPECTATION_PAYOFF_REPORT: quality/reviews/CH013_EXPECTATION_PAYOFF_GATE.md
CONTINUITY_REPORT: quality/reviews/CH013_CONTINUITY_PRECOMMIT.md

## Final clean read

Read from published CH012 ending into frozen CH013 R2 without using Rolling Outline as prose guidance.

### On-page chapter spine

Chen Que starts his first full workday in the herb-garden outer shed. The bed is counted and weak seedlings cannot be casually declared waste, so the easiest version of using herb-garden material for secret cultivation is blocked by ordinary production logic. During legitimate contact with living seedlings, Chen risks three tiny interceptions from different plants, then at night circulates the accumulated qi only through the already-established three turns.

### Concrete want / obstacle / choice

Want: keep the herb-garden trial while making the live-herb access produce real cultivation value.

Obstacle: useful qi is strongest in living rooted plants, but those plants are counted under his responsibility; dead/uprooted material is much weaker; his right arm remains injured and his abnormal white-cord status is checked daily.

Choice: rather than take a full strand from one plant or wait passively for free dead material, he takes only tiny leading portions from three separate rooted seedlings during ordinary work, stopping when bodily costs rise.

### Material ending change

- True wood qi: near-empty → a small real reserve sufficient for one controlled three-turn circulation.
- Right arm: still injured and unable to rise above shoulder level, but at approximately the same work height it can remain stable for several breaths longer after circulation.
- Plant cost: at least the first touched seedling shows a more drooping leaf tip by evening; immediate yellowing does not occur that day, long-term damage unknown.
- Institutional status: herb-garden trial survives the day; white cord/black mark, daily wrist check and three-day recheck remain.

### Continue-reading driver

GROWTH + BODY TEMPERING PRECURSOR. External qi still fades, while the injured arm appears to retain a small functional effect after the qi has circulated. The next causal problem is how to turn temporary external qi into lasting bodily carrying capacity without inventing a new manual verse or destroying accountable plants.

## Paragraph / anti-AI final check

- body characters: 2823; inside hard 2800–4000 range and intentionally not padded;
- body paragraphs: 36;
- average paragraph length: ~78 characters;
- unnecessary one-sentence narrative paragraphs: 0;
- max consecutive one-sentence narrative run: 0;
- no short-word waterfall;
- no backend labels after R1 corrections;
- no administrative side-line settlement;
- no late theme explanation;
- no `轮截/活偿/真正炼身` author lecture;
- final sentence preserves uncertainty about the plant rather than announces the next plot.

## Title final review — 《叶子不能黄》

PASS.

The title is a concrete operational constraint, not an event summary. It works on two levels without explanation: the herb-garden worker cannot visibly damage assigned plants, and Chen's old full-strand cultivation method would destroy the resource interface he just earned. It does not reveal a formal breakthrough and does not repeat the recent title structures.

## Memory final read

Scene Card remains `NO NEW ANCHOR`.

No new slogan, object or mannerism is proposed. MA-005 appears only as routine wrist inspection. MA-009/010/011 remain cooling. ARC-V01-02 is ongoing, so MEM-006 is NA with reason recorded in Rule Coverage.

## Revision integrity

- R1 was invalidated before post-draft PASS due to backend `CH004` leakage, premature `许管事` naming, an incorrect Zhao/`灵胎` association, over-specific transplant timing, weak same-day right-arm baseline, and paragraph fragmentation.
- R2 fixes those issues and is frozen as `CH013-R2-LEAF-NOT-YELLOW`.
- Every post-draft report binds the same SHA256: `ea4994a2571015d4808cc27e6f4fdff97cca37747b4f9a4251a86e7052f3f79c`.
- No body or title modifications occurred after R2 post-draft audits began.

## External CI requirement

This internal PASS permits PR/external validation only.

Required before user delivery:
- workflow=`Chapter Quality Gate`;
- branch=`candidate/ch013-herb-garden-r1`;
- conclusion=`success`;
- run.head_sha equals current candidate branch HEAD;
- no subsequent candidate commit after the successful run.

FINAL DELIVERY RESULT: PASS — proceed to exact-head external CI.