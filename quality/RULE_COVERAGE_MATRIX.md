# RULE COVERAGE MATRIX V4

> 目的：解决“规则存在，但没有任何 Gate 真正检查”的问题。
>
> 本文件是交稿级规则总登记。凡影响 Candidate 是否可交用户的硬规则，都必须在这里拥有：**Rule ID → 来源 → 检查阶段 → 可验证证据 → 失败动作**。
>
> 新增/修改交稿级规则时，如果没有同步更新本矩阵，则该规则变更视为不完整。

## 一、证据原则

PASS 不能只写“已检查”。必须至少留下以下一种证据：

- `TEXT`：引用 Candidate 中相关句/段或段落编号；
- `COUNT`：字数、段落、一句段连续数、关键词命中数等机械统计；
- `SOURCE`：对应 Canon / State / Knowledge / Planning 来源路径与事实 ID；
- `DIFF`：场景前后人物状态/资源/关系的明确变化；
- `COMPARE`：与最近章节、Rolling Outline、Scene Card、Memory Anchor Ledger 的结构比较；
- `NONE-HIT`：对明确可扫描的违禁项执行搜索后 0 命中；
- `CI`：GitHub Actions workflow run id + branch + exact head_sha + conclusion。

任何硬规则若只能靠“作者感觉”判断，必须在 Post-Draft Audit 中增加一个可观察问题，不能直接 PASS。

`WF-006` 属于外部执行规则：Post-Draft 阶段可以标 `NA`，理由必须明确写“External CI only after final candidate commit”；它最终由运行时 Actions 结果负责，不能因Post-Draft的NA而免除。

## 二、工作流与事实权威

| Rule ID | 硬规则 | 主要来源 | 检查阶段 | 最低证据 | FAIL |
|---|---|---|---|---|---|
| WF-001 | HOT LOAD / Context Receipt 未完成不得写正文 | PROJECT_RULES / LOAD_ORDER | PREWRITE | Receipt 路径 + loaded sources | BLOCKED |
| WF-002 | Scene Card 未完成不得从 Outline 进入正文 | SCENE_CARD / CHAPTER_GATE | PREWRITE | Scene Card 路径 | BLOCKED |
| WF-003 | 所有 Gate 必须按状态机顺序执行 | WORKFLOW_STATE_MACHINE | ALL | workflow state history | BLOCKED |
| WF-004 | Gate PASS 必须绑定同一 Candidate Revision 与正文SHA | POST_DRAFT / FINAL_DELIVERY | POSTWRITE | revision_id + candidate_sha256 | RECHECK |
| WF-005 | 任意正文或最终标题修改使受影响的下游 PASS 失效 | FINAL_DELIVERY / CHAPTER_TITLE_STANDARD | POSTWRITE | revision change log / SHA change | RECHECK |
| WF-006 | 完整Candidate只有在当前候选分支精确HEAD的 `Chapter Quality Gate` 外部CI成功后才能交用户 | MANIFEST / WORKFLOW / FINAL_DELIVERY | EXTERNAL CI | Actions run id + branch + head_sha=current HEAD + conclusion=success | BLOCKED |
| CAN-001 | 已发布正文事实高于未来规划 | MANIFEST / PROJECT_RULES | CONTINUITY | source chapter / fact | REWRITE |
| CAN-002 | 已发布事实不得静默 Retcon | CHANGE_IMPACT_PROTOCOL | CONTINUITY | no-conflict / revision receipt | BLOCKED |
| KNOW-001 | 角色不得使用不该知道的信息 | KNOWLEDGE MATRIX | CONTINUITY | claim → knowledge source | REWRITE |
| KNOW-002 | UNKNOWN/SUSPECTS/BELIEVES 不得偷升为事实 | PROJECT_RULES | CONTINUITY | claim classification | REWRITE |

## 三、人物、因果与力量

| Rule ID | 硬规则 | 主要来源 | 检查阶段 | 最低证据 | FAIL |
|---|---|---|---|---|---|
| CHAR-001 | 陈缺谨慎、观察、风险意识，不因挑衅降智 | PROJECT_RULES | POST_DRAFT | 本章关键选择 + 动机证据 | REWRITE |
| CHAR-002 | 陈缺允许错判，不得无证据知道答案 | PROJECT_RULES / STYLE | POST_DRAFT | 推理链证据来源 | REWRITE |
| CHAR-003 | 重要配角有主角不在场时仍会推进的目标 | PROJECT_RULES / SCENE_CARD | POST_DRAFT | 配角独立行动说明 + 正文证据 | REWRITE |
| CAUSAL-001 | 上章真实后果优先于旧章纲 | PROJECT_RULES | PREWRITE/POST | 上章末动作 → 本章起点 | REWRITE |
| CAUSAL-002 | 关键转折必须由人物选择/现实压力造成，不靠作者便利 | STYLE / CHAPTER_GATE | POST_DRAFT | 因果链 | REWRITE |
| POWER-001 | 新力量回答来源、进入方式、代价、最终受益者 | PROJECT_RULES | CONTINUITY | 四项来源映射 | BLOCKED/REWRITE |
| POWER-002 | 升级后必须出现具体可见能力差异 | PROJECT_RULES | PAYOFF | before/after 能力证据 | REWRITE |
| POWER-003 | 不得靠临时爆种抹平大境界差 | CULTIVATION_SYSTEM | CONTINUITY | 境界/条件/代价 | REWRITE |

## 四、场景与结构

| Rule ID | 硬规则 | 主要来源 | 检查阶段 | 最低证据 | FAIL |
|---|---|---|---|---|---|
| SCENE-001 | 一章优先 1—2 个核心事件 | PROJECT_RULES | LINT/POST_DRAFT | 核心事件列表 | REWRITE |
| SCENE-002 | 不得把 Rolling Outline 逐项扩写成正文 | PUBLICATION_GATE | POST_DRAFT | Outline vs Draft 顺序比较 | REWRITE |
| SCENE-003 | 制度/测试场景重点样本通常不超过 1—2 个 | SCENE_CARD / STYLE | POST_DRAFT | 样本计数 | REWRITE |
| SCENE-004 | 人物在信息不足处作选择，而非看完答案精准通关 | SCENE_CARD | POST_DRAFT | 选择时已知/未知清单 | REWRITE |
| CAP-001 | 正文 2800—4000，常规 3200—3600 | PROJECT_RULES | LINT | 字数统计 | REWRITE |
| CAP-002 | 约3000—3300字仍有2个以上关键节点则顺延 | PROJECT_RULES | MIDWRITE | capacity check record | REWRITE |
| CAP-003 | 后25%不得清仓式塞设定/多反转 | STYLE | POST_DRAFT | 后25%事件/新概念列表 | REWRITE |

## 五、文风、标题与 Anti-AI

| Rule ID | 硬规则 | 主要来源 | 检查阶段 | 最低证据 | FAIL |
|---|---|---|---|---|---|
| STYLE-001 | 常规自然段优先2—5句；连续3个无必要一句叙述段 FAIL | STYLE / PUBLICATION | LINT | 最大连续一句叙述段数 | REWRITE |
| STYLE-002 | 禁止短词瀑布/大量空行制造假节奏 | STYLE | LINT/POST | 命中位置 | REWRITE |
| STYLE-003 | 禁止 CHxxx/Canon/上一章等后台语言泄漏 | STYLE | LINT | 违禁词扫描 0 hit | REWRITE |
| STYLE-004 | 谨慎主要通过行为，限制“这不能证明/至少说明”等报告腔 | STYLE | LINT/POST | 高频短语计数 + 语境检查 | REWRITE |
| STYLE-005 | 删除场景已表达后再次总结主题/解释的句子 | STYLE | POST_DRAFT | 重复解释位置 | REWRITE |
| STYLE-006 | 高频万能情绪句/句式不能机械复用 | STYLE | LINT/POST | 命中计数 + 最近章节比较 | REWRITE |
| STYLE-007 | 对话不能变成设定问答机 | STYLE | POST_DRAFT | 信息是否可由行动替代 | REWRITE |
| STYLE-008 | **最终章节名不得只是事件摘要/流程标签；至少承载冲突、反常识、具体意象、双关回收或人物选择之一，并检查最近5章标题结构重复；标题改动视为版本改动** | CHAPTER_TITLE_STANDARD / STYLE / PUBLICATION | PUBLICATION + FINAL | 标题5问 + recent-5 compare + candidate SHA binding | REWRITE / RECHECK |
| END-001 | 章尾来自本章现实后果，不靠金句/神秘台词/作者预告硬切 | STYLE / PUBLICATION | POST_DRAFT | 最后300字审查 | REWRITE |

## 六、爽感、成长与商业节奏

| Rule ID | 硬规则 | 主要来源 | 检查阶段 | 最低证据 | FAIL |
|---|---|---|---|---|---|
| PAY-001 | 当前短周期必须有正向期待，不长期只剩“不死/不暴露” | EXPECTATION_PAYOFF | PAYOFF | expectation statement + prior source | BLOCKED/REWRITE |
| PAY-002 | 信息不能长期成为唯一主奖励 | EXPECTATION_PAYOFF | PAYOFF | 最近3—5次奖励类型 | REWRITE |
| PAY-003 | 重大获得不能习惯性立即归零 | EXPECTATION_PAYOFF | PAYOFF | durability diff | REWRITE |
| PAY-004 | 成本存在，但付完成本后应留下可累积资产 | PROJECT_RULES | PAYOFF | before/after asset diff | REWRITE |
| PAY-005 | 主角主动权应逐步净增长 | NARRATIVE_PATTERN | PAYOFF | agency delta | REWRITE |
| ALG-001 | 最近高层破局算法不得机械重复 | NARRATIVE_PATTERN / STYLE | POST_DRAFT | 最近5章 compare | REWRITE |
| ALG-002 | 对手吃亏必须来自合理利益选择，不靠集体降智 | PROJECT_RULES | POST_DRAFT | opponent goal/choice consequence | REWRITE |

## 七、记忆锚、人物辨识度与回响

| Rule ID | 硬规则 | 主要来源 | 检查阶段 | 最低证据 | FAIL |
|---|---|---|---|---|---|
| MEM-001 | Scene Card必须回答“三个月后最可能记住什么”，允许NO NEW ANCHOR但必须明确 | MEMORY_ANCHOR_SYSTEM / SCENE_CARD | PREWRITE/POST_DRAFT | Scene Card第9问 + Post-Draft记录 | BLOCKED/REWRITE |
| MEM-002 | 新记忆锚必须来自具体场面、人物选择、关系、物件或世界冲突，不能只因句子漂亮 | MEMORY_ANCHOR_SYSTEM | POST_DRAFT | Candidate具体位置 + 为什么值得记 | REWRITE |
| MEM-003 | 禁止为了名场面硬造哲理金句、固定口头禅、象征物或破坏人物逻辑 | MEMORY_ANCHOR_SYSTEM / PUBLICATION | POST_DRAFT/PUBLICATION | forced_memorability_risk + 语境证据 | REWRITE |
| MEM-004 | 已有记忆锚回响必须增加新情绪/关系/信息/权力或含义，不得无增值复读 | MEMORY_ANCHOR_LEDGER | POST_DRAFT | Anchor ID + previous meaning + new meaning | REWRITE |
| MEM-005 | 重要人物关键对白/选择应逐渐形成可识别关注点与利益逻辑，避免所有角色共用作者式聪明声音 | MEMORY_ANCHOR_SYSTEM / STYLE | POST_DRAFT/PUBLICATION | 隐名测试 + 人物动机证据 | REWRITE |
| MEM-006 | Arc收束时必须自然留下：可复述场面、主要人物强性格瞬间、可继续回响锚、一句话阶段变化 | MEMORY_ANCHOR_SYSTEM / MEMORY_ANCHOR_LEDGER | ARC AUDIT | Arc Memory Audit四项证据 | REPLAN/REWRITE |

说明：`MEM-001~005` 每章必须在Post-Draft Rule Coverage中出现；没有新锚时可以PASS/NA，但必须有明确证据和理由。`MEM-006` 非Arc收束章可标NA，理由写明“Arc ongoing”。

## 八、伏笔、反转与长篇压缩

| Rule ID | 硬规则 | 主要来源 | 检查阶段 | 最低证据 | FAIL |
|---|---|---|---|---|---|
| PLOT-001 | ACTIVE伏笔不得无故消失；推进/延迟必须有状态 | PROJECT_RULES | CONTINUITY | FP status diff | REWRITE |
| PLOT-002 | 重要谜底必须有前置证据 | PROJECT_RULES | CONTINUITY | evidence source | REWRITE |
| REV-001 | 反转重新解释旧事实，不无铺垫否定旧事实 | PROJECT_RULES | POST_DRAFT | old fact + new meaning | REWRITE |
| LEN-001 | 一个世界观结论主证明完成后，不换地图重复证明 | PROJECT_RULES 2M | MACRO/POST | prior proof + new function | REPLAN |
| LEN-002 | 不新增只负责讲观点的NPC/重复副本凑长度 | PROJECT_RULES 2M | MACRO/POST | character independent function | REPLAN |

## 九、交稿前最终规则

| Rule ID | 硬规则 | 主要来源 | 检查阶段 | 最低证据 | FAIL |
|---|---|---|---|---|---|
| FINAL-001 | Post-Draft Audit 必须存在且与最终稿 revision/SHA 一致 | POST_DRAFT_AUDIT | FINAL | report path + revision + SHA | BLOCKED |
| FINAL-002 | 所有 delivery-critical Rule ID 都必须 PASS/NA 且 NA 有理由 | 本矩阵 | FINAL | coverage table | BLOCKED |
| FINAL-003 | 最终稿必须脱离规划文件做一次 Clean Read | FINAL_DELIVERY_GATE | FINAL | clean-read result | REWRITE |
| FINAL-004 | 最终稿正文或标题修改后必须重跑受影响检查 | FINAL_DELIVERY_GATE / CHAPTER_TITLE_STANDARD | FINAL | revision history / SHA change | RECHECK |
| FINAL-005 | 只有 Final Delivery PASS + WF-006 外部CI成功，运行时才可进入 USER_REVIEW | WORKFLOW / FINAL_DELIVERY | FINAL+EXTERNAL | Final report + exact-head CI success | BLOCKED |

## 十、维护规则

1. `PROJECT_RULES / STYLE_GUIDE / Gate / MEMORY_ANCHOR_SYSTEM / CHAPTER_TITLE_STANDARD / Executable Validator` 新增硬规则时，必须同步本矩阵。
2. 每条硬规则只允许一个“最终责任 Gate/执行阶段”，其他Gate可以预检，避免所有文档都模糊负责。
3. 用户指出一个本应被规则拦截却漏出的错误时：
   - 登记到 `quality/FAILURE_MEMORY.md`；
   - 找出对应 Rule ID；
   - 若无 Rule ID，新增；
   - 为其设计可验证证据；
   - 若可机械化，优先增加到 `tools/chapter_gate.py` 与自动测试；
   - 从下一章开始作为回归测试。
4. 每5章Snapshot同时执行Memory Anchor Review，清理一次性细节、检查过度使用与人物记忆缺口。
5. 每10章Audit检查一次本矩阵是否存在“规则已新增但无人负责”的orphan rule。
6. 每Arc收束执行MEM-006，不允许靠最后一章硬塞名场面补齐。
7. External CI规则不能由Post-Draft报告自我证明；必须读取GitHub Actions真实结果。
8. `STYLE-008`属于人工语义Gate，不能仅靠机械关键词判定好标题；机械化只负责辅助检测重复结构/版本绑定，最终由Publication Title Review负责。
