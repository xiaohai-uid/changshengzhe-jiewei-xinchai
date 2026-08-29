# FINAL DELIVERY GATE V3

> 目的：防止“前面的 Gate 都跑过，但正文后来又改了，最后交给用户的版本其实没有被完整检查”。
>
> 本Gate通过后，**仍不能立即交用户**。最终还必须把完整Candidate与报告提交到候选分支，由GitHub Actions对该精确HEAD执行外部校验并成功。

## 一、进入条件

必须同时存在并 PASS：

- Context Receipt
- Scene Card（含Memory第9问）
- Post-Draft Audit（含Memory Anchor Audit）
- Publication Gate
- Expectation / Payoff Gate
- Continuity Precommit

并且这些结果全部绑定到**同一个 candidate_revision_id + candidate_sha256**。

任一报告对应旧revision/旧SHA：`BLOCKED / RECHECK`。

## 二、版本绑定

Final Gate记录：

```text
chapter:
candidate_revision_id:
candidate_sha256:
post_draft_report:
publication_result:
expectation_payoff_result:
continuity_result:
final_text_changed_after_last_gate: YES/NO
result: PASS|REWRITE|BLOCKED
```

### 修改失效规则

- 只改错字/标点：至少重跑 Mechanical Lint + Final Clean Read，并产生新SHA。
- 改句子、段落、对白：重跑相关 STYLE/MEM Rule IDs + Publication + Final。
- 改事件、动机、知识、能力、资源、关系、记忆锚候选/回响、章尾：Post-Draft Audit、Publication、Expectation/Payoff、Continuity、Final全部失效并重跑。

禁止“改完以后凭感觉认为不影响”。

## 三、Final Clean Read

这一遍不允许边读边替稿件找理由。

只看：
1. 上一章最后约500字；
2. 当前最终Candidate全文。

暂时不看Rolling Outline任务清单。

必须逐项确认：

### 1. 开场连续性
第一场景是否是上章实际动作自然造成的？

### 2. 主角欲望
普通读者能否在前25%篇幅内理解陈缺这一章在争什么？

### 3. 选择
本章是否至少存在一次真正会改变后果的选择，而不是只观察/被安排？

### 4. 人物独立性
重要配角是否看起来在过自己的今天，而不是等陈缺来触发功能？

### 5. 知识边界
有没有一句话读起来像角色“突然知道作者后台”？

### 6. 因果
有没有关键节点只能用“作者需要下一幕发生”解释？

### 7. 小说感
有没有测试报告、剧情摘要、任务清单、设定问答、短句瀑布感？

### 8. 情绪与兑现
章末相比章初，陈缺或局势究竟改变了什么？是否留下现实残余？

### 9. 成本
收益有代价吗？代价是否又把收益彻底清零？

### 10. 记忆与辨识度
不看Scene Card答案，读完整章后重新问：

> 三个月后，普通读者最可能记得这一章什么？

允许答案是“没有新的强锚，本章主要完成X”。

若有记忆点，继续问：
- 它是否来自场面/人物/关系，而非作者刻意写金句？
- 若是旧Anchor回响，是否真的增值？
- 人物关键对白/选择是否符合其独有关注点？

### 11. 章尾
最后300字是否在收束本章后果，而不是突然写一句“策划案金句”？

### 12. 删除测试
尝试删掉关键反转后的解释段、最后总结、陈缺主题判断句；若删后更清楚、更有力，则原文应删。

### 13. 同书测试
把本章随机一段与CH001—CH003/最近高质量正文并排看：是否明显像另一种AI脚本/剧情报告文体？明显漂移：REWRITE。

## 四、Rule Coverage完整性

读取 `RULE_COVERAGE_MATRIX.md` 与本章Post-Draft Report。

要求：
- 所有delivery-critical Rule IDs已有PASS/NA，包括MEM-001~006；
- NA均有理由；
- 无UNKNOWN；
- 无orphan hard rule；
- `FAILURE_MEMORY` ACTIVE回归测试全部通过；
- `MEMORY_ANCHOR_SYSTEM.md` 与 `tracking/MEMORY_ANCHOR_LEDGER.md` 已加载；
- Candidate阶段只提出Anchor Diff，不提前改正式Ledger。

任何缺口：BLOCKED。

## 五、Final Gate结论

只允许：

- `PASS`：允许把最终Candidate与全部报告提交到当前候选分支，进入**外部CI验证**；
- `REWRITE`：正文仍有可见规则/小说质量问题；
- `BLOCKED`：审计缺失、版本不一致、规则来源不足。

**Final Delivery PASS ≠ USER_REVIEW。**

## 六、External CI Delivery Check（Final之后强制）

候选分支提交完成后，不再修改Candidate或报告，等待/读取实际GitHub Actions：`Chapter Quality Gate`。

交稿前必须验证：

1. workflow run对应当前候选分支；
2. `conclusion = success`；
3. run的`head_sha`与候选分支当前HEAD完全一致；
4. 自动测试步骤成功；
5. strict delivery validation步骤成功；
6. CI成功后没有任何新commit改变候选分支HEAD。

任一条件不成立：**禁止展示完整Candidate。**

这个External CI不能由工作流Markdown自报PASS；必须读取GitHub Actions真实结果。

## 七、为什么USER_REVIEW不在CI后再提交一次状态文件

如果CI成功后为了把 `CURRENT_STATE` 改成 `USER_REVIEW` 再提交一次，候选分支HEAD会变化，刚刚验证的CI就不再对应最终HEAD。

因此：
- 仓库最终可审状态停在 `FINAL_DELIVERY_PASS`；
- 外部CI success对该HEAD成立后；
- 作者系统在运行时进入 `USER_REVIEW` 并把正文交用户；
- 交稿前不再修改该分支。

## 八、用户指出漏网错误后的处理

如果用户指出的问题本应被现有规则拦截：

1. 不只修正文；
2. 在 `FAILURE_MEMORY.md` 登记；
3. 找对应Rule ID；
4. 分析为什么Gate/Validator/CI没抓住；
5. 更新Gate、Rule Coverage、自动测试或校验器；
6. 从下一章起成为ACTIVE regression test。

若用户指出“人物/场面不够有记忆度”，先判断是：
- 单章本来无需新锚；
- Arc整体确实缺记忆残余；
- 已有锚没有被保护/增值；
- 人物声音趋同。

禁止第一反应就是往正文补一句金句。

目标：同一种生产错误尽量只让用户指出一次。
