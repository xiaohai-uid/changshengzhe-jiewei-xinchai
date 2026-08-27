# CHAPTER COMMIT PROTOCOL V3

本协议把 `mozhou` 的 Candidate → Canon 生命周期适配为纯 GitHub 小说仓工作流。

## 两个平面

- `main`：Canonical Plane。只包含用户已确认章节及与之匹配的 Canon Kernel。
- `chapter/CHxxx`：Candidate Plane。正文草稿、候选事实、派生视图更新都可修改，直到用户确认。

## Candidate 阶段

1. 从当前 Canon Horizon 编译本章 Context Receipt。
2. 写正文候选。
3. 提取 Candidate Facts / Knowledge / Relationship / Plot / Timeline changes。
4. 所有新事实先留在章节分支，不进入 `main`。
5. PRECOMMIT 校验：实体引用、时间连续性、知识边界、力量规则、P/S 泄露、Narrative Pattern、文风。

## 晋升事务

用户确认后才执行，并尽量作为单一可审计提交/合并边界：

1. 固化正式章节正文。
2. 将 Candidate Facts 转成 canonical temporal records；被改变的旧事实关闭 `valid_to_chapter`，不静默覆盖。
3. 更新 ENTITIES / KNOWLEDGE / TIMELINE / RELATIONSHIPS / PLOTS / PROMISES / INFO_GAPS。
4. 追加 Chapter Ledger 与 Chapter Record。
5. 重建 LIVE / Matrix / Plot 等派生视图。
6. 重算 Rolling Outline、Context Card、Narrative Pattern Ledger。
7. 写 Chapter Commit Receipt（Canon Horizon 前后、变更 ID、警告、校验结果）。
8. 全绿后才把章节分支晋升到 `main`，推进 Canon Horizon。

任何一步失败：不推进 `main`；Candidate 保留以便修复重跑。

## Revision

已经进入 `main` 的章节不得用普通 Candidate 流程静默改写。必须进入 Revision 模式并执行 Change Impact Protocol。