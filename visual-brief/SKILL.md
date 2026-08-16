---
name: visual-brief
description: 视觉子系统入口：用户想做图（插画/海报/UI/图标/Logo/摄影等）但没说清"要创作什么"时，必须先产出 8 字段 Visual Task Brief（Goal / Deliverable / Content / Audience 与 Context / Creative Intent / References / Constraints / Acceptance）。只定义任务，不做设计、不复刻风格、不写模型语法（分别由 style-replication、model-adapter 负责）。
whenToUse: 当用户提出视觉类任务（插画、海报、UI、图标、Logo、摄影等）需要先定义"要创作什么"再推进时使用。深度风格分析与复刻转入 style-replication；提示词翻译转入 model-adapter。
---

# Visual Brief（视觉任务定义）

**类型**：Visual Capability
**Reuse Scope**：视觉领域（定义任务的能力；未来其他领域出现"任务定义"需求时按 SKILL-STANDARD 评估通用化）
**Responsibility**：只回答一个问题——**这次视觉任务到底要创作什么？**
**Boundary**：不做视觉设计、不做风格复刻、不做视觉 QA、不写模型语法。
**Stop Condition**：8 字段齐（或缺失项已标"假设/不适用"）即完成；追问遵循 no-slacking 全局上限。

## 流程

1. 体检已在 no-slacking 做过；本 skill 只梳理视觉专属维度（能用上下文推断的不问）。
2. 澄清 7 个维度：用途/载体、类别、主体、受众与语境、情绪感受、风格方向、硬性约束。
   维度与字段映射：用途/载体+类别→Deliverable；主体→Content；受众与语境→Audience & Context；情绪感受→Creative Intent；风格方向→References/Creative Intent；硬性约束→Constraints；任务目标→Goal。
3. **提问纪律**：遵循 no-slacking 全局上限——整条链累计最多 1–3 个阻塞问题，其余用上下文/参考/显式假设补齐（标注"假设"）。快问快答：用户只想快速要图时，按"用途+主题+风格"三要素直接出简报。
4. 需要领域规范（UI/Logo/摄影/插画/平面的生产约束）→ 读 `references/category-norms.md`；需要去 AI 味清单 → 读 `references/ai-tells.md`；需要中英术语 → 读 `references/vocabulary.md`。**按需读，不全读。**

## 输出：Visual Task Brief（8 字段）

1. **Goal**：最终希望作品解决什么任务。
2. **Deliverable**：作品类型、载体、比例、尺寸、数量。
3. **Content**：必须表达、出现、保留什么。
4. **Audience & Context**：谁看、在哪里看、什么使用语境。
5. **Creative Intent**：希望产生什么感受、判断和体验。
6. **References**：有哪些参考；每份参考分别承担什么职责（只做职责登记；风格层的拆解在 style-replication 的 Reference Registry，不在这里做）。
7. **Constraints**：品牌、内容、技术、生产、时间等约束。
8. **Acceptance**：已有验收标准；缺失时沿用与 im-satisfied 的关系（标准不足 → im-satisfied 出标准卡）。

填写纪律：无意义的字段标"不适用"，禁止编造填充；缺失项标"假设"；**不含任何模型参数**。

## 失败处理

- 类别不明确：判定最接近类别，按该类别规范追问（读 category-norms.md）。
- 参考缺失：Brief 标注"参考缺失"，转 style-replication 时先做 Reference Registry。
- 资料不足：按 no-slacking 红灯流程（可达性报告 / LIMITED GO）。

## 收尾自检

- [ ] 8 字段齐？"不适用/假设"已标注？
- [ ] 每份参考的职责写清了吗？
- [ ] 没有混入风格设计决定（style-replication 的事）和模型参数（model-adapter 的事）？

## 链

- 上游：no-slacking（体检）→（标准不足时）im-satisfied
- 下游：风格复刻/延续视觉体系 → style-replication；直接生成 → model-adapter
