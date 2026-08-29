# RULE SYSTEM AUDIT · 2026-08-29

## Scope

本次只优化小说生产/交稿机制，不修改CH001—CH006正文，不改变Canon Horizon，不晋升CH007。

## User-reported root problem

规则已经很多，但过去存在：

1. 写完后没有独立、证据化的自审阶段；
2. Gate可以只凭“脑内检查”宣称完成；
3. 规则散落在PROJECT_RULES / STYLE / GATE中，没有“谁负责验收”总表；
4. 用户纠正过的问题没有自动转成下一章回归测试；
5. Gate通过后若正文继续修改，没有机制让旧PASS失效；
6. 旧高层文档仍可能描述较旧的三重Gate流程。

## Changes made

### A. Rule registry

新增 `quality/RULE_COVERAGE_MATRIX.md`。

所有交稿级硬规则要求：Rule ID / 来源 / 责任Gate / 最低证据 / FAIL动作。

解决“规则存在但无人检查”。

### B. Post-Draft Audit

新增 `quality/POST_DRAFT_AUDIT.md`。

DRAFTED后强制执行：
- Mechanical Lint
- Rule Coverage
- 因果/人物反证
- Knowledge/Power Claim Audit
- Outline Leakage Audit
- Expectation/Payoff资产Diff
- Anti-AI/Redundancy
- Reader Clean Read
- Failure Regression

解决“写完直接认为完成”。

### C. Failure memory

新增 `quality/FAILURE_MEMORY.md`。

将用户已指出的生产错误转为ACTIVE回归测试：
- 跳LOAD
- Outline逐项扩写
- 短句瀑布
- 单章任务过载
- 配角临时装技能
- 主题重复解释
- 章尾翻译Outline
- 重大收益快速清零
- Gate脑内执行
- 审后改稿不重检

### D. Revision binding

所有完整Candidate必须生成 `candidate_revision_id`。

所有写后Gate绑定同一revision；正文修改后按影响范围自动失效。

解决“审A稿，交B稿”。

### E. Final Delivery Gate

新增 `quality/FINAL_DELIVERY_GATE.md`。

在USER_REVIEW前重新检查最终稿本身，而不是信任前面报告。

### F. Workflow migration

已更新：
- `PROJECT_RULES.md`
- `LOAD_ORDER.md`
- `MANIFEST.md`
- `ARCHITECTURE.md`
- `README.md`
- `quality/WORKFLOW_STATE_MACHINE.md`
- `quality/CHAPTER_GATE.md`
- `quality/PUBLICATION_GATE.md`
- `quality/EXPECTATION_PAYOFF_GATE.md`
- `quality/CONTEXT_RECEIPT_SCHEMA.md`
- `quality/CHAPTER_COMMIT_PROTOCOL.md`
- `quality/workflow/CH007_WORKFLOW.md`

统一新链：

LOAD → Receipt → Scene → Draft → Freeze Revision → Post-Draft → Publication → Payoff → Continuity → Final Delivery → User Review → Canon。

## Rule responsibility audit

关键规则族均有责任阶段：

- Workflow/load：Receipt / Workflow
- Canon/Knowledge：Continuity
- Character/causal：Post-Draft falsification
- Power：Claim Audit + Continuity
- Scene/capacity：Midwrite + Post-Draft
- Style/Anti-AI：Mechanical Lint + Post-Draft + Publication
- Payoff/commercial：Expectation/Payoff
- Plot/foreshadowing：Continuity
- Revision/version：Final Delivery
- Historical user corrections：Failure Memory regression

未发现当前交稿级大类完全无人负责。

## Candidate safety

- Canon Horizon保持CH006。
- CH007仍为BLOCKED。
- CH007无candidate_revision_id。
- 旧CH007新增姓名/编号/场景细节仍无Canon权威。
- 新QA机制不会自动晋升任何正文。

## Known limitation

部分小说质量判断无法像编译器一样100%机械化，例如人物是否真正工具化、场景是否“像提纲扩写”。因此本系统不假装全部自动化，而采用：

**机械统计 + 明确反证问题 + 正文证据 + 历史回归测试 + 最终Clean Read。**

关键目标不是宣称“绝不会出错”，而是让明显违反已有规则的问题在交用户前更高概率被系统自己发现，并让同类错误不反复依赖用户纠正。

## Result

**PASS — QA architecture upgraded. Planning/Canon/manuscript unchanged except quality/workflow documentation.**
