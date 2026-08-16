# Midjourney（2026-08-16 撰写，参数为当日默认；新版本先查官方文档）

- 句式：`[主体/场景] [动作状态] [风格锚点] [构图/视角/焦距] [光线] [色彩] [材质媒介] [细节] [参数]`
- 参数：`--ar`（比例）、`--v`（版本）、`--s`（风格化，越低越贴文字；去 AI 味常用 `--s 100 --style raw`）、`--iw`（参考图权重，有参考图时提高让参考压过模型惯性）、`--no`（负面词）。
- 负向约束：把"禁含元素 + AI 味清单"合并进 `--no`（逗号分隔短语）。
- 删空话：masterpiece / ultra detailed / 8k / cinematic。
- 迭代：保留 seed 只改一处。

示例（瑞士风格咖啡海报）：
```
coffee shop opening poster, Swiss International Typographic Style, strict grid layout, oversized black Helvetica headline, off-white background, one red diagonal accent block, flat colors, hard-edge geometric shapes, no photography --ar 3:4 --v 6 --style raw --no neon, gradient, 3d render, glossy, texture, decoration
```
