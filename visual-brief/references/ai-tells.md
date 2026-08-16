# AI Tells（去 AI 味：内容知识）

visual-brief 与 style-replication 按需读取。这里是**内容知识**；如何用某模型语法表达负向约束，见 model-adapter/references/。

## AI 味清单（逐条决定要不要禁）

- **材质/色彩**：塑料感/光滑 3D 渲染、磨皮蜡像皮肤、过饱和糖果色、青橙/紫橙渐变、廉价 HDR、体积光/霓虹光晕。
- **构图**：主体悬浮居中、完美对称、滥用浅景深 bokeh、元素平均堆细节。
- **内容**：空泛形容词堆砌（masterpiece/8k/cinematic）、空洞眼神完美微笑脸、文字手部崩坏、"概念图"而非"成品"。
- **风格**：无来源的"流行风格平均"、默认模型味。

## 正向锚点（去 AI 味六法）

1. 锚定具体媒介/年代/流派（risograph print, 1970s Polish poster / Swiss Style / gouache children's book / 35mm Kodak Portra 400）。
2. 用拍摄语言（50mm, f/2.8, 左侧窗光, slight film grain）。
3. 主动要"不完美"（film grain, paper texture, hand-drawn imperfections, scanned print）。
4. 构图打破居中（rule of thirds, off-center, asymmetric, cropped at edge）。
5. 限色板（limited palette, 3–5 colors 或具体色值）。
6. 留白（generous negative space）。

## 模糊情绪词（待解释信号，禁止自动映射）

"高级、复古、艺术感、治愈系、赛博朋克、未来感"这类词**不许**直接套用现成视觉公式（高级→黑白极简、复古→黄色、艺术感→颗粒、未来感→紫色霓虹都是模型惯性映射）。正确做法：用反例法/例子法让用户选方向（"更像 A 还是更像 B"），或标为显式假设。
