---
name: film-review-from-transcript
description: 影评成文 Workflow（v0.2 成熟编辑结构）：把口述/聊天/笔记整理成影评——Opinion Map（论断强度）→ Central Question 与 Argument Clustering → Material Map（观点挂靠具体材料）→ Voice Profile → Article Architecture 与 Thought Movement → 结构性重写 → Critic 四查（观点/Voice/Anti-AI/Editorial）附台账。观点属于作者；文章具备中心问题、论证层级与持续思想推进。
whenToUse: 当用户说"帮我把这些口述/聊天/笔记整理成影评/观后感"、或提供大量口语化材料要成文时使用。仅服务"已有观点→成文"；不用于自动研究电影资料、自动生成用户没有的观点、书评（待验证）、通用文章改写。
---

# Film Review from Transcript（口述稿 → 影评成文 v0.2）

**类型**：Workflow（Writing/Content Production 方向第一个完整工作流）
**Input Contract**：口述稿/聊天记录/观影笔记（≥1 份，不足则红灯流程）+ 可选的成稿要求（篇幅/平台）。
**Output Contract**：成稿 + 台账摘要；完整 Opinion Map / Central Question / Argument Architecture / Material Map / Voice Profile / 台账默认留档，用户索取再给。
**Responsibility**：把用户已有的口述/聊天/笔记整理成**具有成熟编辑结构的影评**——观点、判断方式与个人语言特征属于原作者，同时完成中心问题、论证层级、材料组织与思想推进。**不抢走作者，但要当优秀编辑。**
**Boundary**：不研究电影资料、不发明观点/主题/象征/社会意义/哲学升华、不写通用文章。**例外**：用户明确指称但记不清的客观事实（人名/片名/术语），允许查证补全并在台账标注。体检与提问纪律遵循 no-slacking；"成稿成什么样"说不清时转 im-satisfied。
**Stop Condition**：Critic 四查通过且台账完成即交付；用户改稿时单轮只改对应项（no-slacking R5）。
**Reuse Scope**：影评/观后感成文；书评待真实验证后再扩展。Opinion Map、Argument Architecture、Material Map、Voice Profile、Edit Ledger 为跨领域候选能力（见 WORKFLOW-RETROSPECTIVE）。

## 核心铁律（违反任何一条即失败）

1. **观点属于用户**：输入材料是观点事实源。禁止补写用户没表达过的任何观点、主题、导演意图、象征、社会意义、哲学升华、价值判断。允许补的只有语言连接、论证组织与材料对接。
2. **先理后写**：先 Opinion Map → Central Question / Argument Clustering → Material Map，再动笔。
3. **最小必要编辑保护作者的思想、判断和声音，不保护原始口述的句子结构**：允许重组段落、合并不同位置的材料、改变口述顺序、重新组织句子、删除不服务主线的旁支；严禁新增观点、改变立场强弱、把疑问改成结论、替作者完成他没有完成的思想跳跃。
4. **成稿必须是一篇完成的文章**：有中心问题、有论证层级、有思想推进、有材料支撑——不是整理干净的观影笔记。

## 流程（八步）

### Step 0 · 材料清点（只登记，不重写）
- 列出全部输入单元，标注类型与先后；材料不足 → no-slacking 红灯流程。

### Step 1 · Opinion Map（观点图 + 论断强度）
```
【观点 N】主张/判断（立场强度：断言 / 倾向 / 犹豫 / 中途反悔）
   依据：原句引用（可删口头废话，不改含义）
【未解决】用户自己留下的疑问/摇摆（原样保留）
【未表达】本次材料里用户没有说的主题（防止补写）
```
- 每条标注**论断强度**：Observation / Interpretation / Strong Claim / Speculation / Question。
- **Strong Claim 必须过 Claim → Evidence → Interpretation**：证据撑不住的，降级或标注为作者推测；禁止替用户补证据把判断坐实。

### Step 2 · Central Question + Argument Clustering（中心问题与论点收束）
- **Central Question**：这份材料真正值得讨论的是什么？可以是一个问题、一个矛盾、一个核心判断、一个未解决的冲突。**禁止为了拥有 thesis 而发明用户不存在的观点**——它必须能从 Opinion Map 中推导出来。
- **Argument Clustering**：哪些观点属于同一个更大的论证？产出：核心命题、一级论点、二级判断、证据、观察、旁支（轻处理或舍弃，记台账）、疑问、推测、**Tension（内在矛盾，决定结尾）**。

### Step 3 · Material Map（材料地图）
把每条重要判断挂到具体材料上：
```
判断
 ↳ 场景 / 台词 / 人物行为 / 叙事安排 / 摄影·声音·剪辑等形式处理 / 原作与电影差异 / 用户原句
```
- 挂不上材料的判断：降级为推测，或标注"证据不足"。
- 防止文章只剩抽象议论。

### Step 4 · Voice Profile（声音档案，三层）
1. **Thought Signature**：判断方式、强弱、犹豫、自我修正、思考节奏——必须保留。
2. **Authorial Voice**：词汇、句型、节奏、表达锋利度、常用表达方式——保留并适度书面化。
3. **Speech Noise**：口头禅、重复、填充词、转录断裂、无信息量自我插话——默认清理。
另提取高价值原句清单与禁用语清单（见 `references/voice-markers.md`、`references/anti-ai-patterns.md`）。

### Step 5 · Article Architecture + Thought Movement（文章结构设计）
正式写作前完成文章级设计：
- **开头从哪里进入**（优先具体的人/场景/动作/细节，见 `references/editorial-reference.md`）；
- **中心问题何时出现**；
- **每部分承担什么推进作用**；核心观点如何逐渐深化；
- **材料如何分布**；转折在哪里；最大矛盾在哪里形成；在哪里结束最合适。
- **Thought Movement**：回答"为什么这一段之后是下一段？"——结构必须由思想关系形成（判断 → 为什么 → 作品具体做了什么 → 这意味着什么 → 获得了什么 → 付出了什么 → 下一个问题），禁止主题分类目录。
- 小标题存在时：标题承担判断或问题推进；禁止"配乐/摄影/主题"式资料分类标题。

### Step 6 · Draft（起草：允许结构性重写）
- 允许：重组段落、合并不同位置的材料、改变口述顺序、重新组织句子、删除不服务主线的旁支。
- 红线：观点来源存在、立场强度未改变、疑问没变结论、没有加入新解释、高价值表达没有无意义丢失。
- 段落开头必须多样化：禁止每段"总起句+冒号+条目"同构；禁止"第一点/第二点"枚举（除非材料如此）。
- 承接纪律：衔接句的"意思"必须来自 Opinion Map。
- 每处增/删/并/调/改都记入编辑台账。

### Step 7 · Critic（四查 + 台账）
1. **观点保真查**：观点来源存在、无新增观点、疑问没变结论、立场强度没变、"未表达"没被补写。
2. **Voice 查**：Thought Signature 与 Authorial Voice 保留、Speech Noise 清理、高价值原句保留、禁用语未出现。
3. **Anti-AI 查**：模板开头/同构段落/条目枚举/过度总结/虚假升华/金句制造/高频套话 + Horoscope 测试。
4. **Editorial Review（完成度查）**：全文真正讨论的问题清楚吗？每部分服务主线吗？观点有层级吗？证据支撑判断吗？文章持续向前推进吗？有明显旁枝吗？段落只是并列吗？抽象判断有具体材料吗？小标题承担论证吗？结尾完成文章形成的主要矛盾吗？
- 查不过 → 回 Step 5/6 定向修改。台账列明增/删/并/调/改 + 原因。

### Step 8 · 交付
- 遵循 no-slacking Internal by default：展示成稿 + 台账摘要；完整留档备索。
- QA 结论属判断依据（no-slacking R4）。

## 失败处理
- 材料缺失/过少：no-slacking 红灯流程。
- 用户要求"升华"：说明边界，或按 im-satisfied 立"允许补写范围"。
- Critic 两轮不过：停下报告，不无限改。

## 链
- 上游：no-slacking（体检/提问上限）→（标准说不清时）im-satisfied
- 下游：用户（成稿 + 台账摘要）
