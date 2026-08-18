---
name: film-review-from-transcript
description: 影评成文 Workflow（v0.3 Researcher+Thinking Partner+Editor）：把口述/聊天/笔记整理成成熟影评——User Core 观点保真 → 研究问题生成 → 主动研究（四类证据+来源层级+真实性分级）→ 论证发展（Clarification/Connection/Deepening/Tension+反例校准）→ 编辑架构 → 写作（Voice Integration）→ Critic 六查附研究台账。可深化作者观点，禁止替换作者观点。
whenToUse: 当用户说"帮我把这些口述/聊天/笔记整理成影评/观后感"、或提供口语化材料希望成文且愿意让 AI 查资料补证据、发展论证时使用。仅服务"已有观点→深化成文"；不用于自动生成用户没有的观点、书评（待验证）、通用文章改写。
---

# Film Review from Transcript（口述稿 → 影评成文 v0.3）

**类型**：Workflow（Writing/Content Production 方向第一个完整工作流）
**定位**：Researcher + Thinking Partner + Editor 三个角色同时存在——主动查证、主动发展论证，最终交付成熟影评。**可以深化作者的观点，不能偷偷换掉作者的观点。**
**Input Contract**：口述稿/聊天记录/观影笔记（≥1 份，不足则红灯流程）+ 可选的成稿要求；作者对"AI 主动研究补证"的许可默认开启（可声明关闭）。
**Output Contract**：成稿 + 台账摘要；完整 User Core / Research Ledger / Argument Architecture / Voice Profile / 台账默认留档备索。
**Boundary**：不自动研究无关资料、不发明用户没有的论题、不写通用文章。体检与提问纪律遵循 no-slacking；"成稿成什么样"说不清时转 im-satisfied。
**Stop Condition**：Critic 六查通过且台账完成即交付；用户改稿单轮只改对应项（no-slacking R5）。
**Reuse Scope**：影评/观后感成文；书评待验证。User Core、Research Question、Argument Development、Provenance 为跨领域候选能力（见 WORKFLOW-RETROSPECTIVE）。

## 核心铁律

1. **User Core 是最高优先级事实**：用户明确表达的核心观点、判断、感受、疑问、立场、价值判断，AI 不得静默反转或替换。可以深化（沿方向推进），不可掉包（换成另一套意思）。
2. **禁止无来源、无依据、无关联地创造新论题**；允许基于 User Core 与 Research Support 做 Developed Interpretation。
3. **同时保留六条红线**：不静默反转用户核心立场；不把疑问偷偷写成确定结论；不把 AI 推测伪装成用户原话；不编造电影事实；不编造导演意图；不为"深刻"制造宏大主题。
4. **成稿必须是一篇完成的文章**：有中心问题、论证层级、思想推进、材料支撑——不是整理干净的观影笔记。
5. **Provenance Control（来源系统）**：所有重要内容内部标记来源——**U**（User Core，用户明确表达）/ **R**（Research Support，查证的外部材料，来源可追溯）/ **D**（Developed Interpretation，沿 U+R 发展出的解释，允许进入正文）/ **X**（New Direction，与主线关联弱的新观点，**只记录到 Possible Extensions，不进入正文**）。覆盖：Central Question、Thesis、一级论点、重要事实、关键解释、结尾判断。

## 流程（九步）

### Step 0 · 材料清点
列全部输入单元；材料不足 → no-slacking 红灯。

### Step 1 · User Core（观点图 + 论断强度）
- 逐条提取用户实际表达（主张/立场强度/原句引用/未解决/未表达），标注论断强度（Observation/Interpretation/Strong Claim/Speculation/Question）。
- 每条标 **U**。User Core 是后续研究与发展不可违反的底座。

### Step 2 · Research Question Generation（研究问题生成）
针对每个重要 U 提问：涉及哪些电影事实？还有哪些场景可能支持或反驳？原作对应内容？电影做了什么改编？创作者是否公开谈过？最大证据缺口是什么？
- 按文章重要性排序；**只研究真正影响文章成立的内容**，禁止"可能有用"式扩张。

### Step 3 · Active Research（主动研究）
按 `references/research-sources.md` 执行：四类证据（Film/Adaptation/Creator/Context）+ 来源优先级 + 真实性四档（Confirmed Fact / Reported Information / Interpretation / Speculation）+ 查不到标 Unverified。
- 结果进 **Research Ledger**（每条：R 编号、内容、来源、档位、用途）。
- 发现反例必须保留（见 Step 4 校准）。

### Step 4 · Argument Development（论证发展）
把 U / R / D 放在一起思考（规则见 `references/argument-development.md`）：每个一级论点回答 U（作者原本说什么）/ R（哪些材料支持或挑战）/ D（材料让观点更完整了吗）。
- 四类发展：**Clarification / Connection / Deepening / Tension**。
- **允许挑战作者**：作者观点 → 支持材料 → 反例/矛盾 → 重新校准判断强度。校准建立在事实与原方向上。
- X（新方向）：记录到 Possible Extensions，不进入正文；重大 X 标出供用户选择。

### Step 5 · Editorial Architecture（编辑架构）
- Central Question（主导主线，允许多个独立观察受主线控制）+ Argument Clustering + Material Map——现在以 **U + R + D** 为完整材料源。
- Thought Movement：回答"为什么这段之后是下一段"。
- 开头四种同等级入口（强判断/具体场景/核心矛盾/真正的问题，由材料决定）；小标题承担判断推进。
- 遵循 `references/editorial-reference.md`（《人物》×看理想机制）。

### Step 6 · Writing（写作 + Voice Integration）
- 允许结构性重写；红线：不反转 U、不改立场强弱、不把疑问写成结论、关键表达可追溯。
- Voice 三层（Thought Signature/Authorial Voice/Speech Noise）沿用；**AI 发展的 D 内容也必须进入作者现有 Voice**——删除来源标签后通读，能明显感到"哪几段是 AI 后补的"就重写。
- 段落开头多样化；承接纪律；每处增/删/并/调/改入台账并标 U/R/D/X。

### Step 7 · Critic（六查 + 台账）
1. **观点保真查**：U 是否全部保留、方向未反转、疑问没变结论；正文无 X、无无来源新论题。
2. **Voice 查**：Thought Signature/Authorial Voice 保留、Speech Noise 清理、原句保留、禁用语未出现。
3. **Voice Integration 查**：去掉来源标签通读全文——能明显分辨哪段是 AI 后补的吗？能，就重写。
4. **Anti-AI 查**：模板开头/同构段落/条目枚举/虚假升华/金句制造/高频套话 + Horoscope 测试。
5. **Sophisticated AI Tell 查**：每段都完整闭环？观点之间过度丝滑？同一隐喻贯穿全文过于工整？每个矛盾都有答案？所有句子都"有意义"？作者原本的不确定性消失了？
6. **Editorial Review + Over-editing Check + Restraint Pass**：中心问题/每段服务主线/层级/证据/推进/旁枝/并列段/材料支撑/小标题/结尾矛盾；重复核心隐喻、每段扣题句、人为首尾呼应、连续金句、把犹豫整理成过度完整逻辑——"删掉一两句聪明话是否更自然"；**思想可以发展得深，文字不要为了显得聪明而变复杂**。
- 查不过 → 回 Step 5/6 定向修改。

### Step 8 · 交付
- 展示成稿 + 台账摘要 + Research Ledger 摘要（研究用了哪些来源）；完整留档备索（含 Possible Extensions）。
- QA 结论属判断依据（no-slacking R4）。

## 失败处理
- 材料缺失：no-slacking 红灯。
- 研究受限（如访谈未获取）：按 Unverified 标注，禁止编造。
- 用户拒绝 AI 补证：退化为纯编辑模式（R/D 停用，只 U）。
- Critic 两轮不过：停下报告。

## 链
- 上游：no-slacking（体检/提问上限）→（标准说不清时）im-satisfied
- 下游：用户（成稿 + 台账摘要）
