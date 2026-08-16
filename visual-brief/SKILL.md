---
name: visual-brief
description: 把模糊的视觉/设计想法梳理成图像生成模型可理解的结构化简报，产出双语提示词并主动去除"AI 味"；适用于插画、海报、UI、图标、Logo、摄影等视觉作品。
whenToUse: 当用户想要生成插画、海报、网页/App 界面、图标、Logo/VI、写实摄影等视觉作品，但想法尚不清晰，或希望让图像生成模型（如 Midjourney、DALL·E/GPT-4o）更准确地理解需求、并避免生成结果"太像 AI"时使用。
---

# 视觉作品想法梳理与图像生成提示词设计（Visual Brief & Prompt Crafting）

本 skill 的目标：当用户要做视觉作品但想法模糊时，把 TA 的想法收敛成一份**图像生成模型能精确理解的结构化简报**，再据此产出**可直接粘贴的双语提示词**，并**主动压低"AI 味"**。所有动作都服务于"让最终成品贴近人想要的、像人做出来的作品"。

配合 `no-slacking`（人机双向不偷懒协议）使用：当需求明显不足时，先按 no-slacking 的校准器做需求体检与验收契约，再进入本 skill 的澄清流程；本 skill 的 Phase 1 即体检通过后的领域化追问。

## 何时使用（触发条件）
- 用户说"帮我做个 logo / 图标 / 海报 / 插画 / 界面 / 封面 / 一张图"，但没给清楚细节，或想法零散。
- 用户有模糊描述（"要高级感 / 简约 / 治愈系 / 赛博朋克"）但无法落地。
- 用户给了参考图或参考风格，但担心生成结果太"AI"。
- 用户已有清晰需求，只想把需求整理成更稳的提示词。

## 核心原则（务必遵守）
1. **先澄清，后生成**：没有拿到足够信息前，不要直接开始堆提示词。用分级提问，先问最决定方向的几个问题。
2. **一次只问一小组问题**：不要一次甩 20 个问题。第一轮最多 5–7 个关键问题；按类别再深挖。用户答不上来的就给默认值，不要卡住流程。
3. **想法→简报→提示词→自检**四段闭环，顺序不可跳。
4. **提示词要"可执行、可验证"**：具体名词、数值、材质、光线，而不是 "beautiful / stunning / high quality" 这类空话。
5. **主动去 AI 味**：每一份交付都包含"负向约束"（避免什么）和"正向风格锚点"（锚定到什么具体风格/媒介/年代）。
6. **双语交付**：说明用中文，最终提示词用英文（Midjourney 与 DALL·E 对英文理解更稳），关键处给中英对照。

## 工作流总览
Phase 1 分级澄清 → Phase 2 判定类别并加载规范 → Phase 3 输出结构化简报 → Phase 4 生成提示词（分模型）→ Phase 5 去 AI 味 → Phase 6 交付自检清单。

---

## Phase 1：分级澄清（Intent Elicitation）

### 1.1 第一轮必问（决定方向，最多 7 问）
在进入具体设计前，先确认这 7 件事（能答多少算多少，答不出的给合理默认并在简报里标注"假设"）：

1. **用途/载体**：这张图用在哪里？（App 图标 / 网页首屏 / 海报 / 社交媒体卡片 / 印刷 / 包装 / 演示文稿…）载体决定尺寸、清晰度与呈现方式。
2. **类别**：属于哪类？（插画 / 平面海报 / 网页 UI / App UI / 图标 / Logo-VI / 写实摄影 / 其他）
3. **主题/主体**：画面里具体有什么？（人物/产品/动物/风景/抽象/字母…）
4. **受众与语境**：给谁看？什么品牌调性或场景？
5. **情绪/氛围**：希望人第一眼感受到什么？（专业可信 / 温暖治愈 / 科技前卫 / 复古怀旧 / 奢华 / 活泼…）
6. **风格方向**：有没有偏好的风格或参考？（可给选项：扁平/极简、插画手绘、写实、3D 渲染、复古/包豪斯、日式/新中式、赛博朋克等；有参考图就让用户描述参考图）
7. **硬性约束**：尺寸/比例、品牌色、必须出现的文字、必须避免的元素。

### 1.2 第二轮按类别深挖
拿到类别后，用 Phase 2 里对应类别的问题清单继续问（见下）。

### 1.3 快问快答模式
如果用户明显只想快速要一张图、不想被问太多：按"用途 + 主题 + 风格"三要素直接给一份简报 + 提示词，并在末尾附一句"如需更精准可再补充以下信息…"。不要把快需求拖成问卷。

---

## Phase 2：类别规范库（Category Spec Library）

> 每个类别列出三块：**要澄清的要点**、**该类别规范/生产约束**、**生产流程提示**（它决定模型该"模拟哪个生产阶段的成品"）与**常见坑**。

### 2.1 插画 / 平面海报（Illustration / Poster）

**要澄清**：叙事/主题、风格（手绘/矢量/版画/3D 插画等）、色彩倾向、构图焦点、是否有文字排版需求、成品用途（封面/内页/宣传）。

**规范/约束**：
- 明确"画的媒介"：水彩、钢笔、risograph、丝网印刷、数码厚涂、矢量扁平…这比"插画风"有效得多。
- 构图要有明确焦点与视觉动线（三分法/引导线/留白），避免元素平均分布。
- 若含文字，说明字体气质、字号层级、文字内容（注意：图像模型对长文字易出错，尽量少字）。
- 色彩：给 3–5 色限定色板或明确色相倾向。

**生产流程提示**：专业插画通常经「缩略图草图 → 线稿 → 明度/色稿 → 成稿」。要确认用户要的是**成稿插画**，还是**草图/线稿阶段**的产物（有时用户就要"线稿感"）。海报则要确认是**电子竖版**还是**印刷横版**，印刷需留出血与 CMYK 意识。

**常见坑**：元素堆满无焦点；配色花哨无主色；文字乱码；风格像"多种流行插画平均"。

### 2.2 网页 / App UI（Web / App UI）

**要澄清**：是整页界面还是局部组件？平台（桌面/移动）？产品类型？品牌色/字体？是低保真线框、高保真视觉稿，还是"展示用的营销图"？暗色还是亮色？

**规范/约束**：
- 明确**网格与间距系统**（如 8pt 栅格、栏宽），这是"像真实产品"的关键。
- 明确**组件层级**：导航/标题/正文/按钮/卡片/状态，字号与字重对比要成立。
- **色彩系统**：主色/辅助色/中性色/语义色（成功/警告/错误），对比度满足可读性。
- 明确**风格语言**：毛玻璃/新拟态/极简/企业/游戏化…以及圆角、阴影、描边习惯。

**生产流程提示**：真实 UI 走「线框 → 设计系统 → 组件 → 状态/响应式 → 高保真」。要区分用户要的是**线框图**（灰阶、占位符）、**高保真 mockup**（完整视觉稿，常以设备样机截图呈现），还是**营销展示图**（UI 悬浮、带景深与背景）。这三者对提示词的要求完全不同。

**常见坑**：把 UI 画成"好看的插画"而非可用界面；文字/数字乱码；按钮状态缺失；控件飘忽不对齐。

### 2.3 图标 Icon

**要澄清**：单图标还是一套（set）？风格（线性/面性/双色/3D/毛玻璃）？使用尺寸（16/24/32/48px 或更大）？是否需要与现有图标库风格一致？

**规范/约束**：
- **网格与视觉对齐**：在固定网格（24×24 或 32×32）内做光学对齐，圆角、描边粗细统一（如 2px 描边、2px 圆角）。
- **一致性**：一套图标必须同风格、同描边、同视觉重量；透视与光源统一。
- **可读性**：小尺寸下仍可辨认，避免过多细节。
- 明确是否要**背景底/圆角容器**、**配色**（单色/双色/多色）。

**生产流程提示**：图标按「草图 → 矢量路径（钢笔）→ 网格对齐 → 一致性检查」产出。提示词应强调"flat vector, clean geometric, consistent stroke weight"，并说明是**单图标特写**还是**整套图标矩阵展示**。

**常见坑**：描边粗细不一、透视混乱、细节过多变小看不清、风格不统一。

### 2.4 Logo / 品牌 VI

**要澄清**：品牌名/缩写、行业、品牌气质、是图形标/字标/组合标？要单色版还是全色版？使用场景（名片/App 图标/招牌）？

**规范/约束**：
- **可缩放性**：logo 必须在极小尺寸（如 16px favicon）与极大尺寸都成立，图形要简洁、外轮廓清晰。
- **单色可用性**：必须有黑白单色也成立的能力（去掉颜色后仍能识别）。
- **安全间距与最小尺寸**：四周留白（clear space）。
- 明确**风格**：极简几何 / 字母组合 / 徽章 / 复古 / 负空间巧思 / 渐变。

**生产流程提示**：logo 走「手绘概念 → 矢量化 → 网格/黄金比例对齐 → 单色与反白测试 → 应用规范」。提示词应强调"minimal vector mark, flat, scalable, solid silhouette, works in single color, no gradients unless specified, no photo textures"，并说明是要**单个标志**还是**带应用的 VI 展板**。

**常见坑**：细节过多缩成糊；文字乱码；依赖渐变色在单色下失效；像"照片"而非"矢量标志"。

### 2.5 写实摄影（Photography）

**要澄清**：主体（人物/产品/风景/食物）、用途（广告/社媒/编辑）、风格（自然光棚拍、街拍、胶片、商业精修）。

**规范/约束**：用"拍摄语言"而非形容词——
- 镜头焦距（24/35/50/85/135mm）、光圈（f/1.4–f/16，决定景深）、快门/动态模糊。
- 光线方向与性质：侧光/逆光/柔光箱/自然窗光/黄金时刻/阴天散射。
- 胶片或调色：Portra 400 / Kodak Gold / 数码中性 / 特定白平衡。
- 机位与视角：平视/俯拍/仰拍/过肩。

**生产流程提示**：真实摄影有「布光 → 构图 → 拍摄 → 后期调色」。提示词应明确"这一张是抓拍还是摆拍、直出还是精修"，并主动加入真实感锚点（颗粒、景深、环境光、不完美的细节）。

**常见坑**：塑料感皮肤、滥用浅景深、光线廉价（HDR 感）、构图居中无张力。

### 2.6 其他/混合
不限于上述类别时，先判定最接近的类别套用其规范，再补充特殊约束。混合需求（如"海报里的 UI 展示"）分层描述：先定主体类别，再把次要元素作为"画面中的物件"描述清楚。

---

## Phase 3：结构化简报（Brief Template）

拿到信息后，固定用下面字段输出简报（缺失项标注"假设：…"）：

1. **一句话目标**：这张图要达成什么。
2. **类别 + 规格**：类别；尺寸/比例；用途载体。
3. **主体/主题**：画面里具体是什么，谁在做什么。
4. **风格与锚点**：风格方向 + 具体媒介/年代/艺术家锚点（见 Phase 5）。
5. **构图**：焦点在哪、视角、留白、元素主次。
6. **色彩**：主色/辅色/中性色，色板倾向或具体色值。
7. **光照**：方向、性质、氛围。
8. **材质/纹理**：表面质感、颗粒、手作感等。
9. **情绪**：第一眼感受 + 语气（活泼/克制/庄重…）。
10. **必含元素**：不能少的。
11. **禁含元素**：不能出现的（含 AI 味负向清单，见 Phase 5）。
12. **技术规格**：分辨率/清晰度需求、是否需文字、是否需留白或出血。
13. **参考锚点**：用户给的关键词/参考图描述，固定下来避免漂移。

---

## Phase 4：生成提示词（分模型）

> 提示词一律以英文为主（更稳），附中文对照。下面是分模型写法。

### 4.1 Midjourney
句式：`[主体/场景] [具体动作/状态] [风格锚点] [构图/视角/焦距] [光线] [色彩] [材质/媒介] [细节] [参数]`
- 参数：`--ar 16:9`（比例）、`--v 6` 或 `--v 7`（版本）、`--s <0-1000>`（风格化，越低越贴文字描述）、`--iw <0-2>`（有参考图时图重权重）、`--no <要避免的>`（负面词）。
- 风格锚点写具体：`risograph poster, 1970s Polish poster style` 而不是 `vintage`。
- 少用空话：删除 `masterpiece, ultra detailed, 8k, cinematic` 等（除非确有意义）。

示例：
```
A minimalist geometric app icon for a mindfulness app, a calm circular lotus mark, flat vector, solid dark-teal silhouette on warm off-white background, centered, generous negative space, 2px consistent stroke, crisp edges, no gradients, no text, no photorealism --ar 1:1 --v 6 --style raw --no glow, 3d render, gradient, busy detail
```

### 4.2 DALL·E / GPT-4o / 在线模型
- 用自然语言成段描述，按"主体 → 环境 → 风格 → 构图 → 光线 → 色彩 → 材质 → 排除项"顺序。
- 没有 `--no`，把"避免"写进正文：`Avoid: oversaturated colors, plastic skin, ...` 或 `The image should NOT include ...`。
- 明确尺寸/画幅倾向与整体干净度。
- 若模型支持，可要求"真实胶片颗粒、轻微不完美"。

示例：
```
A flat vector app icon for a mindfulness app: a single calm lotus mark drawn with a consistent 2px dark-teal stroke, centered on a warm off-white background with generous negative space. Minimalist geometric style, crisp edges, solid silhouette, scalable. Flat colors only, no gradients. Avoid: 3D glossy render, glow effects, photorealism, extra decorative clutter, any text.
```

### 4.3 通用英文句式骨架（填空用）
`[Subject] in [style anchor], [composition/viewpoint], [lighting], [color palette], [medium/texture], [mood]. Avoid: [negative list].`

---

## Phase 5：去 AI 味（De-AI-fication）★ 核心

AI 生成图常带一批"内在喜好"，它们会压过你的提示词。去 AI 味 = **负向约束（明确禁止）+ 正向锚点（锚定真实风格/媒介）**，双管齐下。

### 5.1 AI 常见"油腻/塑料感"清单（AI Tells）
对照检查，逐条决定是否要禁：

**材质/色彩**
- 塑料感 / 过度光滑的 3D 渲染质感（glossy plastic / Octane-render look）
- 皮肤过度磨皮、蜡像感、无毛孔纹理
- 过度饱和、糖果色、青橙对比 / 紫橙渐变（teal-orange / neon purple gradient）
- 廉价 HDR、滥用体积光/耶稣光、霓虹光晕

**构图**
- 主体悬浮、死板居中、完美对称
- 滥用浅景深、奶油虚化 bokeh
- 元素平均分布、无焦点、无意图的堆细节

**内容**
- 空泛形容词堆砌（masterpiece / ultra-detailed / 8k / cinematic / beautiful）
- 空洞眼神、千篇一律的"完美微笑脸"
- 文字/手部/对称结构崩坏
- "概念图"质感而非"成品"质感

**风格**
- 无来源的"流行风格平均"、默认 Midjourney 味
- 无年代/媒介/艺术家锚点，画面显得凭空生成

### 5.2 正向去 AI 味手段（Style Anchors）
1. **锚定具体媒介/年代/流派/艺术家**：`risograph print, 1970s Polish poster`、`flat vector, Swiss/International Style`、`gouache, children's book`、`35mm film, Kodak Portra 400`。用真实存在的锚点替代泛泛的风格词。
2. **用拍摄语言描述光线与镜头**：`50mm lens, f/2.8, natural window light from the left, slight film grain`。
3. **主动要求"不完美"**：`film grain, paper texture, hand-drawn imperfections, scanned print, slight halation`。真实感来自不完美。
4. **构图刻意打破居中对称**：`rule of thirds, off-center subject, asymmetric balance, subject cropped at the edge`。
5. **限制色板**：明确 `limited palette, 3–5 colors` 或给具体色值/色名。
6. **留白**：`generous negative space` 常能立刻去掉"AI 堆满"的感觉。

### 5.3 分模型落地
- **Midjourney**：把负面词塞进 `--no`，正向锚点写进正文，`--s` 调低（如 `--s 100`）+ `--style raw` 可减少过度风格化；`--iw` 提高让参考图压过模型惯性。
- **DALL·E / GPT-4o**：没有负面提示词，把"避免清单"用 `Avoid: ...` 或 `Do not include ...` 写进正文；正向锚点同样写进正文。

### 5.4 多轮迭代
先出图 → 用 Phase 6 清单自检 → 标出残留的 AI 味 → 只改对应项重生成（Midjourney 可保留 seed 微调）。不要把"更高质量"当作修改方向，要定向修改具体问题。

---

## Phase 6：自检清单（Self-check）

交付前，对着成品/预期逐条核对：

**需求合规**
- [ ] 主体/主题对了？没有多画/漏画关键元素？
- [ ] 风格、色彩、情绪与简报一致？
- [ ] 尺寸/比例正确？
- [ ] 必含元素都在？禁含元素没出现？
- [ ] 文字（若有）正确且无乱码？

**AI 味残留**
- [ ] 有没有塑料感/光滑 3D 感/廉价 HDR？
- [ ] 色彩是否过饱和/糖果色/紫橙渐变？
- [ ] 构图是否死板居中/平均堆细节？
- [ ] 是否滥用浅景深虚化？
- [ ] 人物是否"蜡像脸/空洞眼神"？
- [ ] 是否像"无来源的流行风格平均"？
- [ ] 是否需要加入颗粒/纹理/不完美以增强真实感？

---

## 交付格式（最终输出给用户）

按固定顺序输出，方便用户直接拿去用：

1. **结构化简报**（Phase 3 模板，中文，标注假设项）
2. **最终提示词**（英文主 + 中文对照；按目标模型给出 Midjourney 版 / DALL·E 版）
3. **去 AI 味说明**（本作用了哪些负向约束与风格锚点，为什么）
4. **自检清单**（Phase 6，让用户拿到图后对照）
5. **一句话下一步建议**（如需迭代/换风格/给参考图）

---

## 词汇表（Prompt Vocabulary，中英对照）

| 中文 | English（提示词用） |
|---|---|
| 扁平矢量 | flat vector |
| 极简几何 | minimalist geometric |
| 一致描边 | consistent stroke weight |
| 负空间/留白 | negative space / whitespace |
| 可缩放 | scalable / solid silhouette |
| 丝网印刷 | silkscreen / screenprint |
| 孔版印刷 | risograph / riso print |
| 瑞士国际主义风格 | Swiss / International Typographic Style |
| 包豪斯 | Bauhaus |
| 水粉/儿童绘本 | gouache / children's book |
| 胶片颗粒 | film grain |
| 浅景深/奶油虚化 | shallow depth of field / bokeh |
| 侧光/逆光/柔光 | side light / backlight / soft light |
| 黄金时刻 | golden hour |
| 三分法构图 | rule of thirds |
| 不对称平衡 | asymmetric balance |
| 出血/裁切 | bleed / cropped at edge |
| 单色/反白 | single color / reversed (white on dark) |
| 低多边形 | low-poly |
| 新拟态/毛玻璃 | neumorphism / glassmorphism |
| 8pt 栅格 | 8pt grid |

---

## 示例（Worked Examples）

### 示例 A：一个冥想 App 的图标（Icon）
**简报**：一句话目标=做一个安静、可信的冥想 App 图标；类别=图标；风格=扁平矢量/极简几何；构图=居中莲花负空间；色彩=深青绿 + 暖米白；必含=莲花；禁含=渐变、3D、文字、复杂装饰；情绪=平静、克制。
**Midjourney**：
```
A minimalist app icon for a meditation app, a single calm lotus mark, flat vector, consistent 2px dark-teal stroke, centered on warm off-white background, generous negative space, crisp edges, solid silhouette, no gradients, no 3D, no text --ar 1:1 --v 6 --style raw --no glow, glossy, gradient, photorealism, clutter
```
**DALL·E**：
```
A flat vector app icon for a meditation app: a single calm lotus symbol drawn with a consistent 2px dark-teal outline, centered on a warm off-white square with generous negative space. Minimalist geometric style, crisp edges, solid silhouette, scalable. Flat colors only. Avoid: 3D glossy render, glow effects, gradients, photorealism, decorative clutter, any text.
```

### 示例 B：一张"治愈系"插画海报（Illustration）
**简报**：目标=一张放松的社媒插画；风格=水彩+手绘、留白、暖色；构图=女孩侧坐窗边，焦点在人物，三分法；色彩=暖米/鼠尾草绿/陶土橙，低饱和；光线=清晨柔和窗光；材质=纸纹+手绘不完美；情绪=安静治愈。
**Midjourney**：
```
A quiet illustration of a young woman sitting by a window, morning soft window light from the left, watercolor and gouache on textured paper, warm cream sage-green terracotta limited palette, rule of thirds, off-center subject, generous negative space, hand-drawn imperfections, visible paper grain --ar 4:5 --v 6 --style raw --no plastic skin, glossy, oversaturated, neon, centered symmetric composition, excessive bokeh
```
**DALL·E**：
```
A quiet illustration of a young woman sitting sideways by a large window. Soft morning light comes from the left. Painted in watercolor and gouache on textured paper, with a warm limited palette of cream, sage green, and terracotta, low saturation. Off-center composition using the rule of thirds, generous negative space, visible paper grain and slight hand-drawn imperfections. The mood is calm and healing. Avoid: plastic skin, glossy finish, oversaturated neon colors, dead-centered symmetric composition, excessive bokeh.
```
