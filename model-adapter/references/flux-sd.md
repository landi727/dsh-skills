# Stable Diffusion / Flux（本地 ComfyUI / A1111，2026-08-16 撰写）

- 正向：标签式短语，逗号分隔，可用权重 `(word:1.2)`。
- 负面提示词：独立输入框，把 AI 味清单写成通用负面词串。
- 采样：steps / CFG 给保守默认（SD 系 CFG 4–7）；Flux 用低 CFG（1–3）与对应采样器，注意习惯差异。
- 参考图/线稿约束时建议 ControlNet / LoRA 方案，而不是硬写进文字。

示例：
正向：`coffee shop poster, swiss international typographic style, grid layout, oversized black headline, off-white background, red diagonal block, flat colors, hard-edge geometric shapes, negative space`
负面：`worst quality, low quality, neon, gradient, 3d render, glossy, texture, decoration, centered template`
