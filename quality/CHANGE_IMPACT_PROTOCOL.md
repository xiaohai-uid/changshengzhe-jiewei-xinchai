# CHANGE IMPACT PROTOCOL V3

用于 Retcon、设定修订、正文回炉和重大 Canon 更改。

## 原则

每个章节/摘要/规划都应能追溯它依赖过哪些 Entity / Fact / FP / P / S / Timeline ID。改变 Canon 后，不允许只修眼前文件然后假设后文自动安全。

## 流程

1. 列出 changed IDs，以及旧值 → 新值。
2. 根据来源章节、Context Receipt、Chapter Record 和引用关系查找依赖者。
3. 分类：
   - `MUST_REVIEW`：直接依赖被修改事实，可能产生矛盾。
   - `RECOMMENDED_REVIEW`：间接依赖、主题/关系/伏笔意义可能改变。
   - `UNAFFECTED`：无依赖证据。
4. 检查三轨：客观事实 / 读者已知 / 角色认知。
5. 检查后续人物状态、时间线、道具、能力、关系、P/S/FP。
6. 输出 Revision Receipt；在影响清单处理完前，不开始依赖该修订的新章节。

## 禁止

- 静默删除已发布 Chapter Ledger 事实。
- 为配合新设定偷偷重写角色旧认知。
- 只更新一个 Markdown 视图而不更新 Canon Kernel。
- 把“没找到引用”当成“肯定没影响”；证据不足时标 `RECOMMENDED_REVIEW`。