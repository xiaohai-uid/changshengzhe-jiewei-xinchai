# CHAPTER COMMIT PROTOCOL V4

本协议管理 Candidate → Canon 生命周期。

## 两个平面

- `main`：Canonical Plane，只包含用户已确认章节及匹配Canon。
- `chapter/CHxxx`：Candidate Plane，允许反复重写，直到用户确认。

## Candidate 阶段

1. 从当前Canon Horizon编译Context Receipt。
2. 生成并通过Scene Card。
3. 写正文Candidate。
4. 冻结 `candidate_revision_id`。
5. 生成 `CHxxx_POST_DRAFT_AUDIT.md`，完成Rule Coverage、Failure Regression、Mechanical Lint、因果/人物/知识/Anti-AI审查。
6. 通过Publication Gate。
7. 通过Expectation/Payoff Gate。
8. 执行Continuity Precommit。
9. 执行Final Delivery Gate，确认所有PASS绑定同一revision。
10. 只有workflow进入 `USER_REVIEW`，才允许展示完整Candidate。
11. 所有新Facts / Knowledge / Relationship / Plot / Timeline changes仍只属于Candidate，不进入main。

## Revision Binding

正文一旦修改：
- 更新revision id；
- 按 `FINAL_DELIVERY_GATE.md` 失效规则重跑受影响审查；
- 禁止沿用旧revision的PASS。

## 用户确认后的晋升事务

用户明确确认后才执行，并尽量作为单一可审计边界：

1. 固化正式章节正文。
2. 将Candidate Facts转为canonical temporal records；旧事实需要变化时关闭 `valid_to_chapter`，不静默覆盖。
3. 更新ENTITIES / KNOWLEDGE / TIMELINE / RELATIONSHIPS / PLOTS / PROMISES / INFO_GAPS。
4. 追加Chapter Ledger与Chapter Record。
5. 重建LIVE / Matrix / Plot等派生视图。
6. 更新Narrative Pattern / Commercial Rhythm / Rolling Outline / Context Card。
7. 写Chapter Commit Receipt，记录：Canon Horizon前后、Candidate revision、变更IDs、Gate结果、警告。
8. 全绿后才推进main Canon Horizon。

任何一步失败：不推进main；Candidate保留以修复重跑。

## 用户否决

用户要求重写/否决时：
- 当前Candidate revision失效；
- 其中新增姓名、编号、道具、机制、关系等不得进入Canon/未来规划事实层；
- 根据问题回到BLOCKED / SCENE_READY / DRAFTED；
- 重新执行需要的审查链。

## Revision 已发布正文

已经进入main的章节不得用普通Candidate流程静默改写。必须进入Revision模式并执行Change Impact Protocol。
