---
name: style-replication
description: 视觉风格复刻完整 Workflow：用户给参考说"做出这种风格/延续这个系列/更像一点/怎么不像了"时使用——Reference Registry → 人的感知（Perception Notes）→ 视觉事实拆解 → 抽取 Visual DNA（含受保护签名元素）→ STYLE SPEC（18 项）→ Similarity Dial 分档 → Composition/Design Spec → Element Selection → model-adapter 转译 → Visual QA（PASS/PARTIAL/FAIL + 自测三问）→ Targeted Revision（V2 锚定）。输入 Visual Task Brief 与参考集，输出生产输入与验证结果。
whenToUse: 当任务需要学习和复刻一种视觉语言、基于参考生成新内容、延续既有视觉体系、更换主体后保持视觉一致、控制参考继承程度（"像一点/更接近/别太像"）、或分析生成结果为何偏离参考并定向修正时使用。上游是 visual-brief；生成执行经 model-adapter。
---

# Style Replication（风格复刻 Workflow）

**类型**：Workflow（参考 → 理解 → 视觉语法 → 新画面设计 → 生产 → 验证 → 定向修正）
**Reuse Scope**：视觉领域专属；跨领域骨架复用见 WORKFLOW-RETROSPECTIVE。
**Boundary**：不定义"要创作什么"（visual-brief）；不翻译模型语法（model-adapter）。证据纪律遵循 no-slacking R4（QA 结论=判断依据）；停止条件遵循 no-slacking R5。
**Stop Condition**：QA 连续两轮 FAIL → 停下如实报告；其余遵循 no-slacking R5。

## 入口 · 参考意图消歧

开工前先确认用户对参考的意图，它直接决定 dial 与受保护清单：

- **复刻**（尽量像）→ dial 70–85%，但仍不复制受保护签名元素。
- **延续**（同体系新内容）→ dial 50–70%。
- **借鉴灵感**（inspired, not copying）→ 无论 dial 数值，原创性优先（见 Similarity Dial 越权规则）。

## 输入契约

1. **Visual Task Brief**（visual-brief 产出）。
2. **Reference Set**（参考图/参考描述；无参考时走"无参考模式"）。
3. **Human Feedback / Judgment**（人的感知，见 Stage 2）。

## 输出契约

STYLE SPEC + **Perception Notes** + Composition/Design Spec + Production Input（交 model-adapter）+ Validation Result + Revision Instruction。

## Stage 1 · Reference Registry（参考登记）

- 给每份参考定角色（仅限以下）：Primary Visual Language / Composition / Color / Typography / Material / Element System / Content / Current Version / Other。
- **禁止默认把所有参考平均混合。** 多参考冲突时：① 判断冲突 → ② 按任务目的定主次 → ③ 写入 Registry。
- 参考图只用于本任务分析，**不写入任何可复用资产**，除非用户拥有且明确授权。

## Stage 2 · Human Perception（人的感知）

优先读取：第一感受、最喜欢什么、最希望继承什么、最不能偏离什么、用户认为风格成立的原因、对失败结果的评价、过去已形成的视觉判断。

- AI 可以：帮语言化、组织、追问真正阻塞的问题、检查感受与视觉事实是否一致。
- **必须产出 Perception Notes**（把以上判断落成一份笔记）；后续 QA 对照的是这份笔记，不是临时回忆。
- **禁止自动映射**：高级→黑白极简、复古→黄色、艺术感→颗粒、未来感→紫色霓虹等模型惯性映射一律禁止。模糊词是待解释信号，用反例法/例子法让用户选方向，或标为显式假设。

## Stage 3 · Visual Facts（视觉事实拆解）

逐项检查（重点看**关系/比例/位置/分布/重复/对比/层级/节奏**）：

Composition / Space-Depth / Scale-Proportion / Density-Rhythm / Visual Hierarchy / Color Relationships / Shape Language / Line-Edge / Surface-Material / Lighting / Typography / Element Selection / Repetition / Negative Space。

优先回答：**画面具体是如何被构成出来的？**

## Stage 4 · Extract Visual DNA（含受保护签名元素）

抽出"**替换具体内容后仍然成立的视觉规律**"：构图组织、空间关系、比例系统、颜色关系、形状关系、视觉密度、节奏、元素选择惯性、表面材质、主体出现方式、字体尺度与位置、视觉层级、情绪温度、重复机制。

严格区分：**规律（可继承）vs 具体内容（不可机械复制）**。

同时列出**受保护签名元素（不复制）**：
- 精确人物、姿势、手势、服装、编排；
- 精确物件、剪影、花木、图案排布；
- 精确前景-背景布局与负空间形状；
- 源品牌名、slogan、logo、专有标记、特色字标字形；
- 可逐像素辨认的构图。

原则：参考有著名特征时，抽象其原理而非重复特征；**品牌名/slogan/标记在任何档位都永不复制**。

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

说明：01 Perceptual Goal 是 Brief 的 Creative Intent 在**视觉语言层面**的转译，不重复抄 Brief；18 Source-specific 与 Stage 4 的受保护清单合并理解。

## Similarity Dial（参考继承程度，分档定义）

- **30% 远灵感**：只保留抽象原则（情绪、密度、对比）。
- **50% 可辨认影响**：同媒介与情绪基调；改色板、构图、主体、字体系统。
- **70% 相邻品牌家族**：共享构图逻辑、纹理、色板关系、人物存在方式与字标尺度；换主体、动作、排布、字形。"别太不像参考"时默认此档。
- **85% 近邻**：保留大部分高层语法，但至少改四个签名元素；不得重建一个可辨认的商业身份。
- **越权规则**：用户表达"inspired 不是 copying"时，即使 70–85% 也保原创。
- 数值是**创作控制参数**，不是可测量的相似度，禁止声称可量化；选择与理由记录进 STYLE SPEC。

## Design Before Generation（生成前必须完成设计）

至少确定：主体、元素、元素关系、位置、比例、空间层次、构图、视觉焦点、节奏、留白、颜色分布。

输出 **COMPOSITION / DESIGN SPEC**；复杂任务且工具允许时可加 thumbnail / wireframe / grayscale sketch / layout draft。

核心要求：**最终生成前已经知道画什么、放在哪里、怎样组织**；生成模型只执行已形成的主要设计决定。

纪律：
- 用户已定方向（Brief 写死的要求）**严格跟随**；Defaults to Reject 只作用于未约束的自由轴。
- **一次只冒一个**可辩护的视觉风险，其余保持克制（Chanel：出门前摘一件配饰）。
- **唯一性自检**：如果一个同类模型拿到相似任务很可能产出近似方案，本方案即失败——回到内容世界找独特性（Sameness is failure）。

## Element Selection（元素选择）

新元素必须来自：任务内容 + Domain/Context + STYLE SPEC + 参考自身的元素选择规律。生成前问：**为什么这个元素属于当前作品？**

主动识别并拒绝：AI 默认装饰、无意义漂浮物、模板化构图物件、套路场景、与概念无关的"丰富画面"、与视觉世界无关的惯性元素。

领域差异见 `references/element-selection.md`（按需读取）。

## Production（生产）

把 STYLE SPEC + Design Spec + Target Model 交给 model-adapter 转译；本 skill 不写模型语法。

## Validation（Visual QA）

生成后同时对照 5 个来源：Reference / **Perception Notes** / STYLE SPEC / Composition-Design Spec / Final Output。

至少检查：Perceptual Goal、Composition、Space、Scale、Density/Rhythm、Hierarchy、Color、Shape、Line、Material、Element System、Typography、Signature、Defaults to Reject。

输出 **PASS / PARTIAL / FAIL**；失败项必须指出：**什么偏了、偏在哪、属于哪个变量、对整体影响多大**。

禁止用"看起来挺像/基本差不多/效果还可以/比较统一"作为主要 QA 依据。QA 结论属于判断依据（no-slacking R4），须给出具体对比，不许"感觉不错"。

**自测三问（交付给用户前）**：
1. **Swap test**：把本方案换成同类默认方案，会有人注意到差别吗？注意不到的地方=默认了。
2. **Squint test**：眯眼看，层级、焦点、节奏还在吗？
3. **Signature test**：能指出 signature 具体出现在画面哪里吗？"整体感觉"不算。

**原创性措辞**：区分"共同视觉语法"（不算问题）与"特征性复制"（记入失败项）；用"重叠/原创性风险"措辞，不做抄袭/侵权的法务断言。

## Targeted Revision（定向修正 + V2 锚定）

1. 找最大偏差 → 2. 定位对应变量 → 3. 每轮只修 1–2 个关键变量 → 4. 保留已成立部分 → 5. 重新执行 → 6. 再次 Validation。

禁止：全部推翻重来、每轮重写完整 Prompt、无目的抽卡、修改已通过的变量、无理由更换 Style Direction、因"可能更好"无限迭代。

**V2 锚定**（用户要"更接近参考"时）：参考作为 Image 1、当前版作为 Image 2；保留当前命名与语义；只改 dial 与视觉语法；重申受保护排除项；另存版本（v2），默认不覆盖 v1。

## 无参考模式

用户只有模糊词、没有参考时：跳过 Stage 1/3/4；从任务的内容世界直接定方向（**Domain-first**：这个主题的世界里有什么材料、物象、行话？）；STYLE SPEC 的 Domain/Context、Color World、Signature 从内容世界推导；模糊词按 Stage 2 处理。

## 失败处理

- 参考缺失/模糊：Stage 1 标注，Stage 2 用最小追问补齐。
- 参考严重冲突且无法定主次：回 visual-brief 补 References 字段。
- QA 连续两轮 FAIL：停下，如实报告"最大偏差 + 变量 + 已修尝试"，不继续抽卡。

## 链

- 上游：visual-brief（任务简报）→（标准不足时）im-satisfied
- 下游：model-adapter（转译）→ 用户生成 → 本 skill Validation → Targeted Revision
