---
name: style-replication
description: 视觉风格复刻完整 Workflow：Reference Registry → 人的感知 → 视觉事实拆解 → 抽取 Visual DNA → STYLE SPEC（18 项）→ Similarity Dial → Composition/Design Spec → Element Selection → model-adapter 转译 → Visual QA（PASS/PARTIAL/FAIL）→ Targeted Revision。输入 Visual Task Brief 与参考集，输出生产输入与验证结果。
whenToUse: 当任务需要学习和复刻一种视觉语言、基于参考生成新内容、延续既有视觉体系、更换主体后保持视觉一致、控制参考继承程度、或分析生成结果为何偏离参考并定向修正时使用。上游是 visual-brief；生成执行经 model-adapter。
---

# Style Replication（风格复刻 Workflow）

**类型**：Workflow（完整生产流程：参考 → 理解 → 视觉语法 → 新画面设计 → 生产 → 验证 → 定向修正）
**Boundary**：不定义"要创作什么"（visual-brief）；不翻译模型语法（model-adapter）。证据纪律遵循 no-slacking R4（QA 结论=判断依据）；停止条件遵循 no-slacking R5。

## 输入契约

1. **Visual Task Brief**（visual-brief 产出；参考缺失时先做 Stage 1 并标注）。
2. **Reference Set**（参考图/参考描述，尽量带角色说明）。
3. **Human Feedback / Judgment**（人的感知是正式输入，见 Stage 2）。

## 输出契约

STYLE SPEC + Composition/Design Spec + Production Input（交 model-adapter）+ Validation Result + Revision Instruction。

## Stage 1 · Reference Registry（参考登记）

- 给每份参考定角色（只允许以下角色）：Primary Visual Language / Composition / Color / Typography / Material / Element System / Content / Current Version / Other。
- **禁止默认把所有参考平均混合。**
- 多参考冲突时：① 判断冲突 → ② 按任务目的定主次 → ③ 写入 Registry。

## Stage 2 · Human Perception（人的感知）

优先读取：第一感受、最喜欢什么、最希望继承什么、最不能偏离什么、用户认为风格成立的原因、对失败结果的评价、过去已形成的视觉判断。

- AI 可以：帮语言化、组织、追问真正阻塞的问题、检查感受与视觉事实是否一致。
- **禁止自动映射**：高级→黑白极简、复古→黄色、艺术感→颗粒、未来感→紫色霓虹等模型惯性映射一律禁止。模糊词是待解释信号，用反例法/例子法让用户选方向，或标为显式假设。

## Stage 3 · Visual Facts（视觉事实拆解）

逐项检查（重点看**关系/比例/位置/分布/重复/对比/层级/节奏**）：

Composition / Space-Depth / Scale-Proportion / Density-Rhythm / Visual Hierarchy / Color Relationships / Shape Language / Line-Edge / Surface-Material / Lighting / Typography / Element Selection / Repetition / Negative Space。

优先回答：**画面具体是如何被构成出来的？**

## Stage 4 · Extract Visual DNA

抽出"**替换具体内容后仍然成立的视觉规律**"：构图组织、空间关系、比例系统、颜色关系、形状关系、视觉密度、节奏、元素选择惯性、表面材质、主体出现方式、字体尺度与位置、视觉层级、情绪温度、重复机制。

严格区分：**规律（可继承）vs 具体内容（不可机械复制）**。

## STYLE SPEC（核心中间交付物，18 项）

```
STYLE SPEC
01. Perceptual Goal      人的整体感受目标
02. Domain / Context     作品所属内容世界与使用语境
03. Composition Logic    构图规律
04. Spatial Logic        空间、层次和深度规律
05. Scale & Proportion   大小、比例、视觉重量
06. Density & Rhythm     疏密、重复与节奏
07. Visual Hierarchy     焦点、主次与视觉路径
08. Color World          颜色关系、占比、重复、对比
09. Shape Language       形状体系
10. Line / Edge Language 线条、轮廓和边缘处理
11. Surface / Material   填色、纹理、材质和表面
12. Element Selection    什么类型的元素属于这个视觉世界
13. Typography           适用时记录字体与排版逻辑
14. Signature            最具识别性的视觉机制
15. Defaults to Reject   模型最容易滑向、必须主动拒绝的默认结果
16. Constants            新作品中保持稳定的规则
17. Variables            允许改变的部分
18. Source-specific      属于参考本身、不应机械复制的具体特征
```

要求：简练、可执行、能约束后续设计、能用于最终 Validation；**禁止写成长篇艺术评论**；不适用项标 N/A。

## Similarity Dial（参考继承程度）

30% 只保留抽象规律 / 50% 明显视觉亲缘 / 70% 同一视觉家族 / 85% 高度继承视觉语言。

- 它是**创作控制参数**，不是可测量的真实相似度；禁止声称可量化。
- 用户没给时按任务目的选择，并把选择与理由记录进 STYLE SPEC。

## Design Before Generation（生成前必须完成设计）

至少确定：主体、元素、元素关系、位置、比例、空间层次、构图、视觉焦点、节奏、留白、颜色分布。

输出 **COMPOSITION / DESIGN SPEC**；复杂任务且工具允许时可加 thumbnail / wireframe / grayscale sketch / layout draft。

核心要求：**最终生成前已经知道画什么、放在哪里、怎样组织**；生成模型只执行已形成的主要设计决定。

## Element Selection（元素选择）

新元素必须来自：任务内容 + Domain/Context + STYLE SPEC + 参考自身的元素选择规律。生成前问：**为什么这个元素属于当前作品？**

主动识别并拒绝：AI 默认装饰、无意义漂浮物、模板化构图物件、套路场景、与概念无关的"丰富画面"、与视觉世界无关的惯性元素。

领域差异见 `references/element-selection.md`（按需读取）。

## Production（生产）

把 STYLE SPEC + Design Spec + Target Model 交给 model-adapter 转译；本 skill 不写模型语法。

## Validation（Visual QA）

生成后同时对照 5 个来源：Reference / Human Perception / STYLE SPEC / Composition-Design Spec / Final Output。

至少检查：Perceptual Goal、Composition、Space、Scale、Density/Rhythm、Hierarchy、Color、Shape、Line、Material、Element System、Typography、Signature、Defaults to Reject。

输出 **PASS / PARTIAL / FAIL**；失败项必须指出：**什么偏了、偏在哪、属于哪个变量、对整体影响多大**。

禁止用"看起来挺像/基本差不多/效果还可以/比较统一"作为主要 QA 依据。QA 结论属于判断依据（no-slacking R4），须给出具体对比，不许"感觉不错"。

## Targeted Revision（定向修正）

1. 找最大偏差 → 2. 定位对应变量 → 3. 每轮只修 1–2 个关键变量 → 4. 保留已成立部分 → 5. 重新执行 → 6. 再次 Validation。

禁止：全部推翻重来、每轮重写完整 Prompt、无目的抽卡、修改已通过的变量、无理由更换 Style Direction、因"可能更好"无限迭代。

## 失败处理

- 参考缺失/模糊：Stage 1 标注，Stage 2 用最小追问补齐。
- 参考严重冲突且无法定主次：回 visual-brief 补 References 字段。
- QA 连续两轮 FAIL：停下，如实报告"最大偏差 + 变量 + 已修尝试"，不继续抽卡。

## 链

- 上游：visual-brief（任务简报）→（标准不足时）im-satisfied
- 下游：model-adapter（转译）→ 用户生成 → 本 skill Validation → Targeted Revision
