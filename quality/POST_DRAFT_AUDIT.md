# POST-DRAFT AUDIT V2

> 目的：正文写完以后，不立刻进入 Publication Gate，而是先把 Candidate 当成“可能有错的稿件”进行一次证据化审查。
>
> 本协议专门解决：规则很多，但作者写完后只凭记忆/感觉说“应该没问题”，最后由用户人工指出违规。
>
> V2新增Memory Anchor Audit：不仅检查“有没有写坏”，还检查人物、场面、关系和物件是否留下可识别记忆，以及已有锚点是否被低价值复读。

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

如果修改改变事件、人物选择、知识、收益、能力、关系、记忆锚候选或章尾，则 Publication / Expectation-Payoff / Continuity 必须全部重跑。

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
context_receipt:
word_count:
paragraph_count:
mechanical_lint: PASS/REWRITE
rule_coverage: PASS/REWRITE/BLOCKED
adversarial_review: PASS/REWRITE
memory_anchor_audit: PASS/REWRITE
reader_clean_read: PASS/REWRITE
result: PASS/REWRITE/BLOCKED
```

Post-Draft Audit PASS 只允许进入后续 Publication Gate，不等于可以交用户。

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

## A2. 段落扫描

记录：
- 总段落数；
- 一句式叙述段数量；
- 最大连续一句式叙述段数；
- 是否存在连续短词独段；
- 是否存在大量空行制造节奏。

最大连续无必要一句式叙述段 ≥3：直接 REWRITE。

对应：`STYLE-001/002`。

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

所有delivery-critical Rule ID都必须填，不只填“本章感觉相关”的规则：

| Rule ID | Status | Evidence | Note |
|---|---|---|---|
| ... | PASS / FAIL / NA | 段落号/来源/计数 | ... |

## 规则

- `PASS`：有证据。
- `NA`：本章确实不触发，并写理由。
- `FAIL`：立即进入 REWRITE。
- `UNKNOWN`：视为 BLOCKED，不能猜。

禁止把十几条规则合成一句“人物/连续性都正常”。

---

# 五、PASS C · Causal / Character Falsification

这一遍不是问“写得合理吗”，而是假设它不合理，主动找反例。

逐项尝试推翻：

### C1. 因果

- 如果删掉作者安排，只看上章最后动作，本章开场还自然吗？
- 本章最大转折是谁的选择造成的？
- 有没有一个事件只因为“Outline需要它发生”才发生？
- 是否存在一个更自然但被作者忽略的直接后果？

找到作者便利：REWRITE。

### C2. 陈缺

逐个列出本章陈缺的关键决定：
- 当时知道什么？
- 不知道什么？
- 为什么现在行动？
- 风险意识是否符合17岁药铺学徒＋当前经历？
- 是否为了爽点、对白或推进突然变得大胆/全知？

对应：`CHAR-001/002`, `SCENE-004`。

### C3. 配角

对每个重要配角回答：

> 如果陈缺今天没有进入这个场景，他原本会做什么？

然后检查正文里是否真的存在这条独立行动痕迹。

答不出来或正文无痕：REWRITE。

对应：`CHAR-003`。

### C4. 对手

若陈缺获利或对手吃亏：
- 对手的决定是否符合其利益？
- 是否靠突然失察、无意义嘲讽、集体降智给陈缺送机会？

对应：`ALG-002`。

---

# 六、PASS D · Knowledge / Power Claim Audit

把正文里所有“新断言”列出来，而不是只审重大设定。

至少分四类：

1. 陈缺新知道/相信/怀疑的事；
2. 配角新表现出的知识；
3. 新能力/旧能力的新用途；
4. 新世界机制/制度事实。

每条写：

`claim → speaker/POV → evidence/source → KNOWS/SUSPECTS/BELIEVES/UNKNOWN → safe?`

任何无来源 KNOWS：REWRITE。

力量使用额外回答：
- 从哪里来？
- 怎么进入？
- 为什么此刻还能用？
- 代价是什么？
- 谁最终获益？

对应：`KNOW-001/002`, `POWER-001/002/003`。

---

# 七、PASS E · Outline Leakage Audit

将 Rolling Outline / Scene Card 与正文并排比较：

1. 列出 Outline 的主要节点顺序；
2. 列出正文真正发生的事件顺序；
3. 检查是否存在连续4项以上“一一对应、顺序相同、没有人物因果改变”的情况；
4. 检查章尾是否几乎只是把 Outline 的章尾问题换成小说句子；
5. 检查新人物是否一次性获得“刚好完成本章任务”的全部技能/经历/信息。

明显逐项扩写：REWRITE，退回 Scene Card，不做句子级润色。

对应：`SCENE-002`, `STYLE-005`, `END-001`。

---

# 八、PASS F · Expectation / Payoff Evidence

不先看“爽不爽”，先做资产 Diff。

## 开场资产

记录陈缺本章开始时：
- Ability
- Resource
- Status
- Freedom
- Leverage
- Impact
- Information

## 章末资产

同样记录七项。

然后明确：

`NET DELTA = + / 0 / -`

允许失败章为负，但必须符合明确 Arc 设计；如果连续高压后仍为负，必须触发商业节奏重算。

额外回答：
- 当前期待是什么？
- 本章兑现了什么？
- 哪个收益在章末仍存在？
- 新问题如何从这个收益长出来？

对应：`PAY-001~005`。

---

# 九、PASS G · Anti-AI / Redundancy Audit

从正文中主动找以下三类问题：

### G1. 读者已经看懂，叙述又解释一次

至少检查：
- 关键反转后3段；
- 关键人物选择后2段；
- 章尾最后300字。

发现主题复述/结论复述：优先删除。

### G2. 一个动作写三次

检查：
- 动作发生；
- 身体感知；
- 叙述再解释意义。

三层若表达同一件事，保留最有效的一到两层。

### G3. 研究报告腔

陈缺谨慎是否被写成连续逻辑限定句？

能换成“暂不行动/保留退路/不下注”的，优先行为化。

对应：`STYLE-004/005/006`。

---

# 十、PASS H · Reader Clean Read

这一遍临时不看 Outline、Canon、Scene Card，只以“普通读者”身份读：

- 上一章最后约500字；
- 当前章全文。

必须能回答：

1. 陈缺这一章具体想要什么？
2. 中途发生了什么让事情变难？
3. 他做了哪个真正的选择？
4. 章末现实发生了什么变化？
5. 这一章最值得继续读下去的东西是 ACTION / PAYOFF / GROWTH / RELATIONSHIP / MYSTERY 哪一个？
6. 有没有哪一段明显像作者在完成任务、解释设定、做总结？
7. 如果删掉最后一句，章尾是否仍然有因果推动力？如果没有，说明钩子可能是硬写出来的。

第1/3/4无法明确回答：REWRITE。

---

# 十一、PASS I · Memory Anchor Audit

读取：
- `quality/MEMORY_ANCHOR_SYSTEM.md`
- `tracking/MEMORY_ANCHOR_LEDGER.md`
- 当前Scene Card第9问

必须记录：

```text
scene_memory_answer:
new_anchor_candidate: YES/NO
anchor_type: SCENE/LINE/BEHAVIOR/OBJECT/RELATIONSHIP/THEME/NA
existing_anchor_echoed: ID/NO
meaning_added_or_changed:
forced_memorability_risk: PASS/REWRITE
anchor_diff_proposal: NONE / proposed change after Canon Promotion
```

### I1. 新锚不是硬要求

`new_anchor_candidate = NO` 完全允许。

如果本章主要功能是承接、兑现、过渡、恢复、移动、准备，只要场景成立，不因“没有名场面”判FAIL。

对应：`MEM-001`。

### I2. 新锚必须自然

若有新Anchor Candidate，必须能指出正文中的具体画面/动作/台词/物件/关系变化，并回答：

- 去掉作者解释后还成立吗？
- 是否与人物当下利益有关？
- 是否具有本书/本人物辨识度？

仅因为“句子很漂亮”不得登记。

对应：`MEM-002/003`。

### I3. 旧锚回响必须增值

若出现Ledger已有锚：

必须写出本次比上次多了什么：
- 新情绪；
- 新关系；
- 新信息；
- 新权力关系；
- 新含义。

如果只是原句/物件机械提醒，没有增值：REWRITE或删除回响。

对应：`MEM-004`。

### I4. 人物辨识度

对本章最重要的1—2名角色，选一个关键对白或选择，问：

> 隐去姓名后，它是否符合这个人物独有的关注点、利益与回避方式？

不要求“百分百猜中”，但若所有角色都说成同一种作者式聪明话，应重写。

对应：`MEM-005`。

### I5. Arc收束额外审计

若本章是Arc收束章，必须读取Ledger的Arc Memory Audit，确认：

1. 可复述场面锚；
2. 主要人物强性格瞬间；
3. 可继续回响锚；
4. 一句话阶段变化。

不足：`REPLAN/REWRITE`，不得靠最后一页临时塞名场面。

对应：`MEM-006`。

---

# 十二、PASS J · Regression Tests

读取 `quality/FAILURE_MEMORY.md`。

所有 `ACTIVE` 历史失败模式必须逐项执行回归测试。

用户曾经指出过的问题，不能因为“这章看起来不错”就跳过。

---

# 十三、审查结论

只能是：

- `PASS`：可以进入 Publication Gate；
- `REWRITE`：退回 DRAFTED / SCENE_READY，按问题层级重写；
- `BLOCKED`：事实/规则来源不足，退回 LOAD/规划。

## 强制重写层级

- 句式/段落问题 → 可以局部改稿；
- 知识越权/连续性问题 → 修改相关场景并重跑 Continuity；
- 提纲扩写/人物工具化/因果错误 → 退回 Scene Card 重构；
- 当前正向期待不存在 → 退回 Rolling Outline / Arc 规划，不在正文里硬补爽点；
- 记忆锚强造/无增值复读 → 删除或重写相关场景；
- Arc整体缺乏任何可复述残余 → 回Arc结构层重算，禁止只补金句。
