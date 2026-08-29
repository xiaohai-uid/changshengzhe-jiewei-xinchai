# FINAL DELIVERY GATE V1

> 目的：防止“前面的 Gate 都跑过，但正文后来又改了，最后交给用户的版本其实没有被完整检查”。
>
> **这是 USER_REVIEW 之前最后一道硬门。**

## 一、进入条件

必须同时存在并 PASS：

- Context Receipt
- Scene Card
- Post-Draft Audit
- Publication Gate
- Expectation / Payoff Gate
- Continuity Precommit

并且这些结果全部绑定到**同一个 candidate_revision_id**。

任一报告对应旧 revision：`BLOCKED / RECHECK`。

## 二、版本绑定

Final Gate 记录：

```text
chapter:
candidate_revision_id:
post_draft_report:
publication_result:
expectation_payoff_result:
continuity_result:
final_text_changed_after_last_gate: YES/NO
```

### 修改失效规则

- 只改错字/标点：至少重跑 Mechanical Lint + Final Clean Read。
- 改句子、段落、对白：重跑相关 STYLE Rule IDs + Publication + Final。
- 改事件、动机、知识、能力、资源、关系、章尾：Post-Draft Audit、Publication、Expectation/Payoff、Continuity、Final 全部失效并重跑。

禁止“改完以后凭感觉认为不影响”。

## 三、Final Clean Read

这一遍不允许边读边替稿件找理由。

只看：
1. 上一章最后约500字；
2. 当前最终 Candidate 全文。

暂时不看 Rolling Outline 的任务清单。

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

### 10. 章尾

最后300字是否在收束本章后果，而不是突然写一句“策划案金句”？

### 11. 删除测试

尝试删掉：
- 关键反转后的解释段；
- 最后一段总结；
- 陈缺的主题判断句。

如果删掉以后故事更清楚、更有力，则原文应删，不得保留“因为写得好听”。

### 12. 同书测试

把本章随机一段与CH001—CH003/最近高质量正文并排看：是否明显像另一种AI脚本/剧情报告文体？

明显漂移：REWRITE。

## 四、Rule Coverage 完整性

读取 `RULE_COVERAGE_MATRIX.md` 与本章 Post-Draft Report。

要求：
- 本章触发的所有 Rule IDs 已有 PASS/NA；
- `NA` 均有理由；
- 无 `UNKNOWN`；
- 无 orphan hard rule；
- `FAILURE_MEMORY` 中 ACTIVE 回归测试全部通过。

任何缺口：BLOCKED。

## 五、交稿结论

只允许：

- `PASS`：工作流可进入 `USER_REVIEW`；
- `REWRITE`：正文仍有可见规则/小说质量问题；
- `BLOCKED`：审计缺失、版本不一致、规则来源不足。

**没有 Final Delivery PASS，禁止向用户展示完整 Candidate。**

## 六、用户指出漏网错误后的处理

如果用户指出的问题本应被现有规则拦截：

1. 不只修正文；
2. 在 `FAILURE_MEMORY.md` 登记；
3. 找对应 Rule ID；
4. 分析为什么 Gate 没抓住：规则缺失 / 证据不足 / 检查阶段错误 / 修改后未重跑；
5. 更新 Gate 或 Rule Coverage；
6. 从下一章起成为 ACTIVE regression test。

目标是让同一种错误最多由用户指出一次。
