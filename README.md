# 《长生者皆为薪柴》

本仓库是长篇小说《长生者皆为薪柴》的唯一事实与生产规划库（Source of Truth）。

**从正文开始读**　[第一章《入门先死三成》](manuscript/volume-01-baigushan/CH001-入门先死三成.md) → [第二章《最安全的人往往死得最快》](manuscript/volume-01-baigushan/CH002-最安全的人往往死得最快.md) → [第一卷目录](manuscript/volume-01-baigushan/)

下方是作者工作区，规划、人物状态和设定包含后续剧情。

## 当前系列目标

- 目标总量：约200万中文字
- 规划安全区间：约190万—210万字
- 结构：8卷
- 预计章节：约580—620章
- 常规单章：3200—3600字
- 核心体验：玄幻成长 + 生存博弈 + 规则破解 + 世界真相逐层揭露

旧“350万—500万 / 12卷”规划已经废弃。

## 仓库用途

- 保存已经确认的正式正文；
- 维护CANON / State / Knowledge / Relationship / Plot / Chapter Ledger；
- 保存Series Master、Volume Blueprints、当前卷细纲、Arc Map、Rolling Outline；
- 保存Scene Card、Context Receipt与章节工作流；
- 通过Rule Coverage、Post-Draft Audit、Failure Memory与Final Delivery减少用户人工QA；
- 通过Git历史追踪Canon与规划变化。

## 当前进度

[生产清单](MANIFEST.md) 的 `CANON_HORIZON` 记录已确认章节，`CURRENT_SNAPSHOT` 和 `LATEST_STATE_DIFF` 指向对应的状态记录。读者可直接按[第一卷正文](manuscript/volume-01-baigushan/)的章号顺序阅读。

## 第一卷容量

- 七日考核：约CH001—11/12
- 药圃与真炼身：约CH012—26
- 坏掉的虫种：约CH027—39
- 内山的药：约CH040—52
- 交药期：约CH053—64
- 离山：约CH065—75

章号只是容量提醒，真实因果优先。

## 交稿级质量机制

完整Candidate写完后必须冻结revision，然后依次通过：

1. `POST_DRAFT_AUDIT`：机械扫描、规则取证、因果/人物反证、Knowledge/Power审查、Outline泄漏、Anti-AI、Reader Clean Read；
2. `PUBLICATION_GATE`：小说质感与场景结构；
3. `EXPECTATION_PAYOFF_GATE`：期待→兑现→升级；
4. `CONTINUITY_PRECOMMIT`：Canon/Knowledge/能力/时间线/关系/伏笔；
5. `FINAL_DELIVERY_GATE`：确认最终交付版本就是被完整审查的版本。

同时必须：
- `RULE_COVERAGE_MATRIX`中相关硬规则逐条PASS/NA并有证据；
- `FAILURE_MEMORY`所有ACTIVE历史失败模式完成回归测试；
- 所有Gate绑定同一 `candidate_revision_id`；
- Gate通过后正文如有修改，按影响范围重跑。

只有workflow进入 `USER_REVIEW`，才允许把完整Candidate交给用户。

用户确认后才进行Canon Promotion。

## 写作入口

写作前必须按 `LOAD_ORDER.md` 读取；当前有效路径和权威顺序以 `MANIFEST.md` 为准。
