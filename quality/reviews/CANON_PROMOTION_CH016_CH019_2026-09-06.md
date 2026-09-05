# CANON PROMOTION RECEIPT · CH016—CH019

Date: 2026-09-06
Repository: `xiaohai-uid/changshengzhe-jiewei-xinchai`
Canonical branch: `main`
Canon Horizon before: CH015
Canon Horizon after: CH019
Next chapter: CH020

## User authorization

本次晋升依据用户在连续完成并确认CH016—CH019后明确指令：**“今天的工作结束了，都提交了。”**

该指令按项目长期约定视为：结束当日创作，并将当日已确认正文与对应状态持久化到项目GitHub源。

## Chapter authority

### CH016《我就给你单开一行》
- Source: existing `chapter/ch016` candidate text.
- Promotion basis: subsequent chapters均在用户知情下以该章为前置继续，最终用户要求当日全部提交。
- Canon status: `canonical-published`.
- Canon manuscript: `manuscript/volume-01-baigushan/CH016-我就给你单开一行.md`.

### CH017《现在不值这块地》
- Source: user supplied a complete rewritten chapter and explicitly instructed **“以这个为正文”**.
- Authority: `USER_FINAL_OVERRIDE`.
- Earlier assistant CH017 draft is invalid and must not be treated as canon.
- Canon manuscript: `manuscript/volume-01-baigushan/CH017-现在不值这块地.md`.

### CH018《这车，我不碰》
- Source: user supplied a complete rewritten chapter and explicitly instructed **“以这个作为第十八章的正文”**.
- Title: assistant recommendation《这车，我不碰》 subsequently explicitly accepted by user.
- Authority: `USER_FINAL_OVERRIDE`.
- Earlier assistant CH018 draft is invalid and must not be treated as canon.
- Canon manuscript: `manuscript/volume-01-baigushan/CH018-这车，我不碰.md`.

### CH019《干得快，就再多干一畦》
- Source: assistant delivered chapter; user then explicitly ended the work session and required all current work submitted.
- Canon status: `canonical-user-confirmed`.
- Canon manuscript: `manuscript/volume-01-baigushan/CH019-干得快，就再多干一畦.md`.

## Canon artifacts written

For each CH016—CH019:
- Canon manuscript under `manuscript/volume-01-baigushan/`.
- State Diff under `state/diffs/CHxxx_STATE_DIFF.md`.
- Append-only Chapter Ledger record under `state/ledger-appends/CHxxx.md`.
- Canon Kernel patch under `canon/kernel/patches/CHxxx.jsonl`.

Derived state refreshed through CH019:
- `state/LIVE_STATE.md`
- `state/KNOWLEDGE_MATRIX.md`
- `state/RELATIONSHIP_STATE.md`
- `state/PLOT_LEDGER.md`
- `tracking/CONTEXT_CARD.md`
- `tracking/TRACKING_STATE.json`
- `planning/ROLLING_OUTLINE.md`
- `MANIFEST.md`

## Key canonical changes promoted

- CH016: formal food ration begins materially supporting sustained labor; right-arm endurance improves while public elevation stays about half an inch above shoulder; Chen Que deliberately skips one cultivation night to manage the seven-day recovery record; new seedling-sorting permission acquired.
- CH017: seven pale-green-tag marginal seedlings become Chen Que's accountable loss responsibility; one healthy, strong-wood-qi but weak-bitter Qingxu seedling is judged by Xu as **“现在不值这块地”** and retained in the back shed for later re-screening; only the limited mismatch between wood qi/liveliness and current plot value is confirmed.
- CH018: seven tagged seedlings resolve to two dead/five alive; Chen Que's first formal seedling-loss entry is recorded; Zhao Shi's wet-dregs/bitter-fishy trigger is reproduced; Zhao Shi trades heavier dry-dregs labor for permission to avoid the trigger cart and is conditionally retained in the dregs shed.
- CH019: Chen Que receives back-shed recovering-seedling work; the same strong-wood-qi seedling remains vigorous and weak-bitter; one ultra-small extraction plus strict three turns after ordinary waist/thigh fatigue produces next-morning recovery clearly better than ordinary-rest control; evidence for generalized flesh-bearing strengthens but no formal Body Tempering breakthrough occurs; improved work efficiency immediately produces additional workload.

## Protected unknowns after promotion

The following remain UNKNOWN / unconfirmed:
- Complete Body Tempering method and exact qi-to-flesh mechanism.
- Whether Chen Que has formally entered 炼身; current canon says **no formal confirmation**.
- Full relation between Qingxu medicinal value/maturity and perceptible wood qi.
- Long-term plant/medicinal effect of Chen Que's ultra-small extraction from the back-shed seedling.
- Contents of Zhao Shi's trigger wet-dregs barrels, whether they are the same material as CH015 black pottery jars, Zhao Shi's exact bloodworm state, and full pharmacy treatment mechanism.
- TARGET-0001 final fate/location/companions.
- Final meaning of “天地亦食修士”.

## Snapshot / Audit boundary

- Existing Snapshot remains `canon/snapshots/STATE_SNAPSHOT_V2.4.md`, effective through CH015.
- CH016—CH019 are carried by patches/diffs/ledger appends.
- After CH020 canonical promotion, MUST generate next 5-chapter snapshot (`STATE_SNAPSHOT_V2.5`) and run the next 10-chapter continuity audit (`CONTINUITY_AUDIT_CH020`).

## Workflow note

CH017 and CH018 are direct user-final text, so project rules prohibit gates from silently rewriting them; they are recorded as `USER_FINAL_OVERRIDE`.

CH016 and CH019 were promoted under explicit user confirmation at end of session. This receipt records the exact authority boundary and prevents older candidate/draft text from superseding main Canon.

## Result

`CANON_PROMOTION: COMPLETE`
`CANON_HORIZON: CH019`
`NEXT: CH020`
