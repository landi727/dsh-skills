---
name: model-adapter
description: 图像生成模型适配器：接收 visual-brief 的模型无关简报，按目标模型（Midjourney / ChatGPT Images / 即梦·豆包 / SD·Flux）输出该模型的最终提示词与参数，并把去 AI 味的负向约束翻译成该模型的语法（--no / Avoid: / 负面提示词）。
whenToUse: 当已有（或刚产出）一份 visual-brief 简报、需要转成某个具体图像模型的提示词时使用。没有简报时先走 visual-brief。
---

# 图像模型适配器（Model Adapter）

输入：`visual-brief` 的简报（模型无关）+ 目标模型。
输出：该模型的最终提示词（可直接粘贴）+ 参数 + 负向约束语法。

原则：
- 简报是唯一事实来源：只做"翻译"，不改意图、不增删简报要素。
- 去 AI 味分工：内容知识（AI 味清单/风格锚点）来自 visual-brief；本 skill 负责用**该模型的语法**表达负向约束。
- 一个模型一个 profile；模型未列时按最接近的 profile 处理并向用户说明依据。

## Profile 1 · Midjourney

- 句式：`[主体/场景] [动作状态] [风格锚点] [构图/视角/焦距] [光线] [色彩] [材质媒介] [细节] [参数]`
- 参数：`--ar`（比例）、`--v`（版本）、`--s`（风格化，越低越贴文字；去 AI 味常用 `--s 100 --style raw`）、`--iw`（参考图权重，有参考图时提高，让参考压过模型惯性）、`--no`（负面词）
- 负向约束：简报"禁含元素 + AI 味清单"合并进 `--no`（逗号分隔短语）
- 删空话：masterpiece / ultra detailed / 8k / cinematic
- 迭代：保留 seed 只改一处

示例（冥想 App 图标简报 → Midjourney）：
```
A minimalist app icon for a meditation app, a single calm lotus mark, flat vector, consistent 2px dark-teal stroke, centered on warm off-white background, generous negative space, crisp edges, solid silhouette, no gradients, no 3D, no text --ar 1:1 --v 6 --style raw --no glow, glossy, gradient, photorealism, clutter
```

## Profile 2 · ChatGPT Images（DALL·E / GPT-4o）

- 无 `--no`：负向约束并入正文，用 `Avoid: ...` 或 `Do not include ...` 成句。
- 成段自然语言，顺序：主体 → 环境 → 风格 → 构图 → 光线 → 色彩 → 材质 → 排除项。
- 明确画幅与干净度；可要求胶片颗粒等真实感锚点。
- 长文字易错：简报含长文字时提醒拆分排版或改用 SVG/排版工具。

示例：
```
A flat vector app icon for a meditation app: a single calm lotus symbol drawn with a consistent 2px dark-teal outline, centered on a warm off-white square with generous negative space. Minimalist geometric style, crisp edges, solid silhouette, scalable. Flat colors only, no gradients. Avoid: 3D glossy render, glow effects, gradients, photorealism, decorative clutter, any text.
```

## Profile 3 · 即梦 / 豆包（国产在线模型）

- 中文为主，英文风格锚点词可保留（如 risograph、Swiss Style）。
- 负向词：多数支持独立"负面提示词"输入或"避免"句式；不确定时正文加"不要出现……"。
- 国产模型美学惯性常见"国风/糖水/磨皮"，去 AI 味锚点要更具体（点名媒介/年代/颗粒/手作痕）。
- 比例/清晰度/风格化程度按平台控件逐项给建议。

示例：
```
极简几何的冥想 App 图标：一朵莲花符号，2px 深青绿描边，居中于暖米白背景，大量留白，扁平矢量，边缘干净，轮廓完整，可缩放。纯色，无渐变。不要出现：3D 光泽、发光、渐变、写实、多余装饰、任何文字。
```

## Profile 4 · Stable Diffusion / Flux（本地 ComfyUI / A1111）

- 正向：标签式短语，逗号分隔，可用权重 `(word:1.2)`。
- 负面提示词：独立输入框，把 AI 味清单写成通用负面词串（worst quality, plastic skin, oversaturated, ...）。
- 采样：steps / CFG 给保守默认（SD 系 CFG 4–7）；Flux 用低 CFG（1–3）与对应采样器，注意习惯差异。
- 参考图/线稿约束时建议 ControlNet / LoRA 方案，而不是硬写进文字。

示例：
正向：`meditation app icon, lotus mark, flat vector, 2px dark teal outline, centered, warm off-white background, negative space, minimal, crisp edges, solid silhouette, no gradients`
负面：`worst quality, low quality, 3d render, glossy, glow, gradient, photorealism, text, clutter`

## 链

- 上游：`visual-brief` 简报；下游：用户把提示词粘贴到对应工具。
