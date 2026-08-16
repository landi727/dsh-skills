---
name: model-adapter
description: Adapter：把已确定的创作决定翻译成目标模型可执行的语言——Visual Task Brief、STYLE SPEC、Composition/Design Spec → 最终提示词、参数、负向约束、必要技术适配。禁止重新决定概念、创意方向、构图、色彩世界、元素体系、视觉层级与 Signature。
whenToUse: 当已有 visual-brief 简报或 style-replication 的 STYLE SPEC/Design Spec，需要转成某个具体图像模型的提示词时使用。没有上游决定时先走 visual-brief 或 style-replication。
---

# Model Adapter（模型适配器）

**类型**：Adapter
**Reuse Scope**：视觉生成工具链；跨领域的"适配器"模式可参照本结构
**Responsibility**：把已确定的创作决定翻译成目标模型可执行的语言。
**Boundary**：不决定 Concept / Creative Direction / Composition / Color World / Element System / Visual Hierarchy / Signature。
**Stop Condition**：输出契约四件套齐（提示词/参数/负向约束/适配披露）即完成。

## 输入契约

1. Visual Task Brief（来自 visual-brief）
2. STYLE SPEC（存在时，来自 style-replication）
3. Composition/Design Spec（存在时）
4. Target Model（用户指定，或向用户确认）

缺 STYLE SPEC/Design Spec 时：只翻译 Brief；**不得自行补设计决定**，缺失部分标"由模型自由发挥"并披露。

## 转译原则

- 保持语义不变；允许为模型能力做**必要技术适配**（如长文字→拆分/换工具）；影响创作结果的适配必须披露。
- 去 AI 味分工：内容知识见 **visual-brief 技能的 `references/ai-tells.md`**（以 visual-brief 的资源目录解析，本 skill 不复制）；本 skill 负责用目标模型语法表达负向约束。
- 未知模型 → 读 `references/generic-natural-language.md`，不猜专属语法。

## 模型知识（Progressive Disclosure）

模型语法、版本、参数不放在主文件，按目标模型读取：

- `references/midjourney.md`
- `references/chatgpt-images.md`
- `references/jimeng.md`
- `references/flux-sd.md`
- `references/generic-natural-language.md`（未知模型默认）

版本时效：references 中参数为撰写日默认（2026-08-16）；目标模型刚发布新版本时先查官方文档再定参数。

## 输出契约

最终模型输入（提示词）+ 参数 + 负向约束 + 必要技术适配说明（含披露项）。

## 失败处理

- 目标模型未知：用 generic-natural-language.md，并说明依据。
- 上游决定缺失：只翻译已有部分，缺失项披露，不代做决定。
- 模型能力与设计决定冲突：做最小技术适配并披露，或如实报告冲突让用户裁决。

## 链

- 上游：visual-brief（简报）→ style-replication（STYLE SPEC / Design Spec）
- 下游：用户把输出粘贴到目标模型生成。
