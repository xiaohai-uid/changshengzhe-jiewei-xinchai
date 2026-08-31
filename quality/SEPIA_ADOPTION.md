# SEPIA ADOPTION NOTE V1

Source reviewed: Nanako0129/sepia (MIT), especially:
- `skills/sepia/SKILL.md`
- `references/narrative-pass.md`
- `references/discourse-pass.md`
- `references/rubric.md`
- `references/style-pass.md`
- `references/model-fingerprints.md`

## Adopted

1. **Architecture before style**：先修叙事结构，再修段落/话语流，最后才修词句。
2. **QUD Sequence**：检查段落/场景是否形成行政式问答链。
3. **Outline First-Sentence Test**：段首句若能完整复原Outline，视为过度工程化风险。
4. **Echo Test**：核心转折是否属于同一前提重复生成时的默认答案；若是，必须由本书既有具体事实支撑。
5. **Theme Explanation Cut**：场景/象征已成立后，不让旁白再解释意义。
6. **Emotion Mode Mix**：不长期只用心跳、发冷、绷紧、呼吸等身体反应表现情绪。
7. **Calibration / Select, don't accumulate**：每章只处理真正命中的自然度问题，不把所有反AI指标推到相反极端。
8. **Leave slack**：允许普通句子、生活纹理、非伏笔性细节存在；但ACTIVE Plot Ledger不受此条影响，不能遗忘。
9. **Paragraph architecture**：结合Sepia discourse-flow思想与本项目用户纠错，分段作为独立结构层审查，而非单纯句式问题。

## Not mechanically adopted

1. 现实世界作品/品牌/地点引用：本书为封闭玄幻世界，除非世界设定自然允许，不引入。
2. 直接读者称呼/第四墙：不作为本书去AI手段。
3. 为了人类分布强行非线性叙事：第一卷高压连续考核以因果清晰优先。
4. “留下未回收细节”不得覆盖Plot Ledger；只有从未被定义为伏笔的生活纹理可以无后续。
5. 任何统计型“人类/AI倾向”只作审稿先验，不作作者身份判断，也不作为单章硬数值目标。

## Project integration

- New hard gate: `quality/NARRATIVE_NATURALNESS_GATE.md`
- Workflow updated: `quality/CHAPTER_GATE.md` V9
- Post-draft updated: `quality/POST_DRAFT_AUDIT.md` V3
- Failure Memory added:
  - FM-013 分段失真
  - FM-014 叙事过度整齐

This note is quality-system documentation, not story Canon.
