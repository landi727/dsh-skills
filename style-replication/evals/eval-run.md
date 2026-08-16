# style-replication · Eval 运行记录（2026-08-16）

说明：本环境无图像生成模型，**生成与视觉观察步骤无法实跑**，标记为「未验证」；文本层流程步骤已按 Workflow 实跑。不伪造 PASS。

---

## Eval A — 单张参考（文本层实跑）

**输入**
- 参考：1960s 瑞士国际主义风格爵士音乐节海报——黑/红/米白三色、网格化大字排版（类 Helvetica）、斜向强调块、无摄影图。
- 新任务：精品咖啡店开业海报（电子竖版），沿用该视觉语言，主体换为咖啡。

**运行过程（摘要）**

1. Reference Registry：参考角色 = Primary Visual Language（唯一参考）。
2. Human Perception（模拟用户口径）：喜欢"理性、秩序、不啰嗦"；最不能偏离=三色体系与网格排版；不能接受=任何插画风装饰。
3. Visual Facts（关键项）：构图=严格网格、文字占主导；色彩关系=黑主/红强调/米白底、占比约 60/10/30；形状=矩形与斜切块；线条=硬边；材质=纯色平涂无纹理；密度=信息密集但留白有节奏；层级=超大字号 vs 小字对比。
4. Visual DNA：可继承规律 = 网格组织、三色占比关系、硬边几何、字号极端对比、斜向强调；不可机械复制 = 原海报的文字内容与音乐节符号。
5. STYLE SPEC（节选，全文 18 项已按模板填写，总长约 280 字）：
   - 01 Perceptual Goal：理性、克制、可信的专业感。
   - 03 Composition Logic：2–3 列网格，斜向色块做动线。
   - 08 Color World：黑 60% / 米白 30% / 红 10%，红只用于强调。
   - 09 Shape Language：矩形、斜切块；无曲线装饰。
   - 11 Surface/Material：纯色平涂，无纹理无渐变。
   - 13 Typography：粗无衬线，超大标题 vs 小字信息，极端对比。
   - 14 Signature：斜切红色强调块 + 网格大字。
   - 15 Defaults to Reject：霓虹渐变、3D 质感、手绘装饰、居中式"海报模板"。
   - 16 Constants：三色体系、网格、硬边几何、字号对比。
   - 17 Variables：文字内容、版式细节、斜块位置。
   - 18 Source-specific：原海报文字与爵士乐符号不复制。
6. Similarity Dial：70%（同一视觉家族；任务目的是品牌气质延续，不需要完全照搬）。
7. Design Spec：竖版三栏网格；顶部超大"GRAND OPENING"（黑）；中部咖啡杯剪影化硬边图形（黑）；斜切红色块贯穿右上至左下；底部米白区小字信息；留白占比约 30%。
8. Production Input：交 model-adapter → Midjourney + DALL·E 双版本（见 model-adapter 输出示例）。

**检查结果**：Registry 定角色 ✅ / Visual Facts 回答"如何构成" ✅ / STYLE SPEC 可执行 ✅ / Design Spec 生成前定稿 ✅ / 规律迁移而非内容复制 ✅ / Defaults to Reject 已写 ✅ → **PASS（文本层）**；生成层「未验证」。

---

## Eval D — 模糊视觉词（实跑）

**输入**：高级 / 复古 / 艺术感（无参考）。

**运行**：未做任何自动映射。行为：
1. 标记三个词为"待解释信号"；
2. 反例法提问：「什么样子会让你一眼觉得**不**高级？」；
3. 例子法给三个方向选择：A 黑白极简+大量留白 / B 深色木纹+黄铜细节 / C 粗粝印刷质感+手写标牌，请用户选或给参考；
4. 在 STYLE SPEC 未获答复前，全部标为显式假设并记录。

**检查结果**：未套 AI 公式 ✅ / 继续分析并给方向选择 ✅ / 使用了反例法+例子法 ✅ → **PASS（文本层）**。

---

## Eval F — Drift Detection（实跑）

**输入**（模拟偏移结果）：生成海报变成了紫橙渐变背景、发光 3D 咖啡杯、居中大字带霓虹光晕。

**诊断**：
1. 最大偏差：色彩体系整体偏移（黑/红/米白 → 紫橙渐变）+ 材质偏移（平涂 → 3D 发光）。
2. 定位变量：08 Color World、11 Surface/Material、15 Defaults to Reject 被违反。
3. 优先级：Color World > Surface/Material > 其余。
4. 修正指令：只改两个变量——负向约束追加「no gradients, no neon, no 3d gloss, flat colors only」+ 重申三色占比；保留已成立的网格与斜块构图，不重写整条提示词。

**检查结果**：找到最大偏差 ✅ / 定位到具体变量 ✅ / 排出优先级 ✅ / 只修关键变量 ✅ / 未推翻重来 ✅ → **PASS（文本层）**；真实图像观察「未验证」。

---

## Eval B / C / E — 状态

案例已建立（见 eval-b/c/e.md），需要真实参考图集与生成模型才能运行，当前标记为「待运行」。文本层预判：Eval B 的风险点在"偶然内容 vs 稳定规律"的区分；Eval E 的风险点在 Signature 在换主体后是否仍可辨认。

## 第二轮修复后补记（2026-08-16 同日）

本轮修复为增量（Dial 分档定义、受保护签名元素、V2 锚定、自测三问、Perception Notes、无参考模式、原创性措辞），不改变 Eval A/D/F 已通过项；A/D/F 文本层结论维持 PASS，B/C/E 仍待真实参考集与生成模型。新增机制（自测三问、受保护清单）需在下一次真实生产中首测。

## 第三轮补跑：Eval B / C / E（文本层实跑）

### Eval B — 同风格多参考（PASS，文本层）
**输入**：三份同风格参考（瑞士风格爵士海报 / 建筑展海报 / 葡萄酒标，均为描述文本）。
**运行**：Registry 三份均定角色 = Primary Visual Language；Visual Facts 取交集：网格组织、黑/红/米白三色关系、硬边几何、字号极端对比、斜切强调块；Visual DNA 提取：Constants = 网格 + 三色占比 + 硬边 + 字号对比 + 斜块；Source-specific = 各张的具体内容（乐器、建筑图、酒名）。
**结论**：找到稳定共同规律 ✅、区分偶然内容与稳定规则 ✅、未平均混合 ✅ → PASS（文本层）；真实图像层未验证。

### Eval C — 多参考不同职责（PASS，文本层）
**输入**：Image 1 = Visual Language（瑞士海报）；Image 2 = Composition（对角构图杂志内页）；Image 3 = Color（陶土/藏青/奶油摄影色卡）。
**运行**：Registry 按职责登记；冲突识别——Image 2 的对角构图与 Image 1 的网格冲突；按任务目的（海报）定主次：构图以 Image 1 为主、只借 Image 2 的对角动线；Color 以 Image 3 的色板关系为准；冲突与主次已写入 Registry。STYLE SPEC 中可看出每份参考的贡献来源（03 来自 Image 1+2 融合、08 来自 Image 3）。
**结论**：各司其职 ✅、冲突定主次并记录 ✅、贡献可溯源 ✅ → PASS（文本层）。

### Eval E — Content Transfer（PASS，文本层）
**输入**：Eval A 的 STYLE SPEC + 新主体（新茶品牌招牌海报，换掉咖啡内容）。
**运行**：Constants 全部保持（三色体系/网格/硬边/字号对比/斜块机制）；Variables 按需变化（文字内容、斜块位置、杯型图形换茶壶剪影）；Signature（斜切红块 + 网格大字）在新设计中仍可辨认，且出现在 Design Spec 的指定位置。
**结论**：Constants 稳定 ✅、Variables 按需 ✅、Signature 可辨认 ✅、无"为换而换"元素 ✅ → PASS（文本层）；真实图像层未验证。

**三例遗留**：B/C/E 的真实图像观察与生成仍待有生成模型的环境；此为唯一未验证环节。

