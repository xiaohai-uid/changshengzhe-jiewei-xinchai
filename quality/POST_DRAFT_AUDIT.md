# POST-DRAFT AUDIT V3

> 目的：正文写完以后，不立刻进入 Publication Gate，而是先把 Candidate 当成“可能有错的稿件”进行一次证据化审查。
>
> 本协议专门解决：规则很多，但作者写完后只凭记忆/感觉说“应该没问题”，最后由用户人工指出违规。
>
> V3新增 Narrative Naturalness 接口与 Paragraph Architecture 强制指标。分段属于叙事结构，不再只用“短句多不多”粗略判断。

## 一、核心原则

### 1. 写完 ≠ 可审

Candidate 完成后先冻结一个版本，生成：

- `candidate_revision_id`
- Candidate 字数
- Candidate 段落数
- 若正文已落仓，记录 blob SHA；若尚未落仓，用本次工作流内部 revision id 绑定。

所有后续 PASS 都必须绑定这个 revision。

### 2. 修改即失效

正文任何实质修改后：

- 新建 revision id；
- 修改涉及的 Gate 自动失效；
- 至少重新跑 Mechanical Lint + 被修改部分对应 Rule IDs + Final Delivery Gate。

如果修改改变事件、人物选择、知识、收益、能力、关系、记忆锚候选或章尾，则 Publication / Expectation-Payoff / Continuity / Narrative Naturalness 必须全部重跑。

### 3. 不允许“已检查”式结论

每个关键 PASS 必须给证据。可用：段落号、原句、计数、来源事实、前后状态 Diff、最近章节比较、Memory Anchor Ledger对照。

---

# 二、审查产物

每章必须生成：

`quality/reviews/CHxxx_POST_DRAFT_AUDIT.md`

至少包含：

```text
chapter:
candidate_revision_id:
canon_horizon:
scene_card:
word_count:
paragraph_count:
mechanical_lint: PASS/REWRITE
rule_coverage: PASS/REWRITE/BLOCKED
adversarial_review: PASS/REWRITE
memory_anchor_audit: PASS/REWRITE
narrative_naturalness: PASS/REWRITE/REPLAN
reader_clean_read: PASS/REWRITE
result: PASS/REWRITE/BLOCKED
```

Post-Draft Audit PASS 只允许进入后续 Narrative Naturalness / Publication Gate，不等于可以交用户。

---

# 三、PASS A · Mechanical Lint

这一遍只查可机械/半机械确认的问题，不做文学判断。

## A1. 长度与容量

记录：
- 正文字符数；
- 是否在 2800—4000；
- 若偏离3200—3600，原因；
- 核心事件数量；
- 最后25%出现的新概念/新反转数量。

对应：`CAP-001/002/003`, `SCENE-001`。

## A2. Paragraph Architecture / 段落扫描

必须记录：
- 总段落数；
- 单句叙述段数量与占比；
- 两句以下叙述段数量与占比；
- 最大连续无必要单句叙述段数；
- 平均段落字符数；
- 最短/最长正文段；
- 段长离散度（仅作分布预警）；
- 连续短词独段；
- 是否存在大量空行制造节奏。

必须额外做两个功能检查：

1. **单句段理由表**：每个单句叙述段写明为什么必须独立；答不出则合并。
2. **Anchor对照**：随机抽当前正文中段400—600字，与CH001—CH003 Published Prose Anchor并排，看当前纸面是否显著更薄、更碎。

硬性：
- 最大连续无必要一句式叙述段 ≥3：REWRITE；
- 连续两轮以上“短动作独段→解释独段→结论独段”：REWRITE；
- 去掉空行后明显更像正常小说：REWRITE。

对应：`STYLE-001/002`, `NAT-003`, `FM-003`, `FM-013`。

## A3. 后台泄漏扫描

明确搜索：
- `CH0`
- `Canon / CANON`
- `Ledger`
- `State Diff`
- `Snapshot`
- `上一章 / 第X章 / 本章 / 前文`
- 其他只存在于后台的标签

必须记录 `0 hit` 或命中位置。

对应：`STYLE-003`。

## A4. 高频 AI 指纹扫描

搜索并计数：
- 陈缺心里一沉
- 他忽然明白
- 原来如此
- 真正的问题是
- 深吸一口气
- 微微一怔 / 心头一颤 / 意味深长
- 空气仿佛凝固 / 时间仿佛静止
- 这不能证明 / 这只能证明 / 至少说明 / 这不代表
- 不是……而是……
- 他没有……只是……

不是全部零命中才合格；必须检查是否形成机械复用。

对应：`STYLE-004/006`。

---

# 四、PASS B · Rule Coverage Audit

打开 `quality/RULE_COVERAGE_MATRIX.md`。

所有delivery-critical Rule ID都必须填，不只填“本章感觉相关”的规则。NAT类Rule IDs必须覆盖。

| Rule ID | Status | Evidence | Note |
|---|---|---|---|
| ... | PASS / FAIL / NA | 段落号/来源/计数 | ... |

规则：
- `PASS`：有证据。
- `NA`：本章确实不触发，并写理由。
- `FAIL`：立即进入 REWRITE。
- `UNKNOWN`：视为 BLOCKED，不能猜。

---

# 五、PASS C · Causal / Character Falsification

这一遍不是问“写得合理吗”，而是假设它不合理，主动找反例。

### C1. 因果
- 如果删掉作者安排，只看上章最后动作，本章开场还自然吗？
- 本章最大转折是谁的选择造成的？
- 有没有一个事件只因为“Outline需要它发生”才发生？
- 是否存在一个更自然但被作者忽略的直接后果？

找到作者便利：REWRITE。

### C2. 陈缺
逐个列出本章陈缺的关键决定：当时知道什么、不知道什么、为什么行动、风险是否符合17岁药铺学徒＋当前经历、是否突然大胆/全知。

### C3. 配角
对每个重要配角回答：如果陈缺今天没有进入这个场景，他原本会做什么？正文是否存在这条独立行动痕迹？

### C4. 对手
若陈缺获利或对手吃亏：对手决定是否符合其利益，是否靠突然失察、嘲讽或降智送机会。

---

# 六、PASS D · Knowledge / Power Claim Audit

把正文里所有“新断言”列出来，至少分：
1. 陈缺新知道/相信/怀疑；
2. 配角新表现出的知识；
3. 新能力/旧能力新用途；
4. 新世界机制/制度事实。

每条写：
`claim → speaker/POV → evidence/source → KNOWS/SUSPECTS/BELIEVES/UNKNOWN → safe?`

任何无来源 KNOWS：REWRITE。

---

# 七、PASS E · Outline Leakage / QUD

将 Rolling Outline / Scene Card 与正文并排：
1. 列Outline主要节点；
2. 列正文事件；
3. 连续4项以上一一对应、顺序相同、没有人物因果改变：REWRITE；
4. 抽正文每段首句，若几乎能直接还原Outline：REWRITE；
5. 给主要段落/场景写隐含问题，若形成行政式QUD链：REWRITE；
6. 检查章尾是否只是把Outline章尾问题换成小说句子；
7. 新人物是否一次性获得刚好完成本章任务的全部技能/经历/信息。

对应：`SCENE-002`, `STYLE-005`, `END-001`, `NAT-001/002`。

---

# 八、PASS F · Expectation / Payoff Evidence

记录开场与章末 Ability / Resource / Status / Freedom / Leverage / Impact / Information，并明确NET DELTA。

额外回答：
- 当前期待是什么？
- 本章兑现了什么？
- 哪个收益在章末仍存在？
- 新问题如何从这个收益长出来？

---

# 九、PASS G · Anti-AI / Redundancy Audit

### G1. 读者已经看懂，叙述又解释一次
重点检查：关键反转后3段、关键人物选择后2段、章尾最后300字。发现主题复述/结论复述：优先删除。

### G2. 一个动作写三次
动作发生→身体感知→叙述再解释意义，若三层表达同一件事，保留最有效的一到两层。

### G3. 研究报告腔
陈缺谨慎是否被写成连续逻辑限定句？能行为化的优先行为化。

### G4. Emotion mode
抽查强情绪是否长期只写心跳、发冷、绷紧、呼吸、出汗等身体反应；若是，改为行为、简单命名或回避。

对应：`STYLE-004/005/006`, `NAT-006/007`。

---

# 十、PASS H · Reader Clean Read

临时不看Outline、Canon、Scene Card，只读上一章最后约500字+当前章全文，回答：
1. 陈缺这一章具体想要什么？
2. 中途什么让事情变难？
3. 他做了哪个真正的选择？
4. 章末现实发生什么变化？
5. 最值得继续读的是 ACTION / PAYOFF / GROWTH / RELATIONSHIP / MYSTERY 哪一个？
6. 哪段像作者在完成任务/解释设定/做总结？
7. 删掉最后一句，章尾是否仍有因果推动力？

第1/3/4无法明确回答：REWRITE。

---

# 十一、PASS I · Memory Anchor Audit

读取Memory Anchor System/Ledger与Scene Card第9问，记录新锚有无、旧锚是否增值、是否强造金句/象征物。新锚不是硬要求。

---

# 十二、PASS J · Narrative Naturalness

完整执行 `quality/NARRATIVE_NATURALNESS_GATE.md`：
- NAT-001 QUD Sequence；
- NAT-002 Outline Leakage / First-Sentence Test；
- NAT-003 Paragraph Architecture；
- NAT-004 Echo Test；
- NAT-005 Over-Determination；
- NAT-006 Theme Explanation；
- NAT-007 Emotion Mode Mix；
- NAT-008 Texture Variance。

只修真实命中的2—3类，禁止为了“去AI”把全部指标推到反方向极端。

---

# 十三、PASS K · Failure Memory Regression

执行 `quality/FAILURE_MEMORY.md` 所有ACTIVE项。任一硬FAIL：REWRITE/BLOCKED。
