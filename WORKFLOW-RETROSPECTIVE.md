# WORKFLOW-RETROSPECTIVE（style-replication 样板复盘，2026-08-16）

只回答四件事。用于帮助未来扩展整个 AI Production System，不代表现在要拆分或新建任何 Skill。

## 1. 哪些机制只属于视觉领域？

- Visual Facts 拆解清单（构图/空间/色彩关系/形状语言……）——视觉专属观察框架。
- STYLE SPEC 的 18 项字段——按视觉维度组织的规格语言。
- Element Selection 的领域差异（插画/影视概念/平面/UI）——视觉元素语汇。
- Reference Registry 的"角色"词汇（Visual Language/Composition/Color……）——视觉参考的职责划分。

## 2. 哪些机制具有跨领域价值？

| 机制 | 跨领域形态 |
|---|---|
| Reference Registry（先定角色，禁止平均混合） | 任何"参考输入"型任务：文案参考、代码库风格参考、研究资料 |
| 规律 vs 具体内容（可继承/不可机械复制） | 代码风格、写作风格、产品决策模式的迁移 |
| STYLE SPEC 的 Constants / Variables 二分 | 任何"延续既有体系"的任务的稳定项/可变项清单 |
| Similarity Dial（继承程度是沟通参数，不冒充测量） | 任何"多像原参考"的控制需求 |
| Design Before Generation（生成前定稿） | 写作大纲、代码设计文档、方案设计先行 |
| Visual QA 五源对照 + PASS/PARTIAL/FAIL + 偏差定位 | 任何交付物的验收 QA：对照目标/规范/事实，指出偏了什么、哪个变量、影响多大 |
| Targeted Revision（只修 1–2 个关键变量） | 一切迭代：改稿、改代码、改方案 |
| Defaults to Reject（模型最易滑向的默认） | 每个领域都可维护自己的"AI 惯性清单" |

## 3. 哪些内部步骤已经稳定到可能升级为 Capability？

（仅列候选，均未达到拆分条件——未被 2 个 Workflow 复用）

- **Visual QA**：五源对照 + 分级结论 + 偏差定位。最接近独立 Capability，等待第二个视觉 Workflow 出现后再评估。
- **Visual Grammar（Visual Facts + Visual DNA）**：观察框架稳定，但触发与输入输出仍与风格复刻强绑定。
- **Reference Registry**：逻辑简单，暂时不值得独立。

## 4. 哪些执行控制机制未来可用于开发/产品/文案/项目控制/交付？

- **验证前不声称完成**（QA 结论=判断依据 + 证据/依据分级）——已由 no-slacking R4 全局化，直接复用。
- **生成前设计定稿**——对应"先写设计文档再写代码"、"先列大纲再写正文"。
- **最大偏差优先、定向修正、停止条件**——对应改稿/改代码/改方案的收敛纪律。
- **模糊词不自动映射、强制反例法/例子法**——对应产品需求里的"要高级"、"要丝滑"等空洞词的处理。
- **Progressive Disclosure（主流程短、知识下沉 references/）**——所有领域 Skill 的结构规则（已在 SKILL-STANDARD 固化）。

**结论**：本轮没有发现应立即拆分的 Capability；执行控制机制大多已被 no-slacking 全局化。下一阶段扩展时优先复用 no-slacking 与 SKILL-STANDARD，而不是复制本 Workflow。

## 附：Visual QA 拆分评估（遗留问题处置记录）

按 SKILL-STANDARD 的升级条件逐条对照 Visual QA：

| 条件 | 现状 | 是否满足 |
|---|---|---|
| 被 ≥2 个 Workflow 稳定复用 | 仅 style-replication 使用 | ❌ |
| 有独立触发条件 | 只在 Workflow 尾部触发 | ❌ |
| 有独立输入/输出 | 输入与 STYLE SPEC 强绑定 | ⚠️ |
| 有独立失败模式 | 依赖本 Workflow 的偏差定位语境 | ⚠️ |
| 有独立验证方法 | 尚未经真实生成跑通 | ❌ |
| 脱离原 Workflow 仍有价值 | 有（但未证实） | ⚠️ |

**决定：不拆。** 重新评估的触发条件：① 第二个视觉 Workflow 出现；② Visual QA 被复用 ≥2 次；③ 有真实生产验证记录。三个条件同时满足后再启动拆分评估。

## 附2：film-review-from-transcript 调研取舍与 Capability 候选（2026-08-16）

### 采用的外部机制

| 机制 | 来源 | 落地为 |
|---|---|---|
| 声音分析维度（词汇指纹/句式节奏/强度词）+ 高价值原句 + 禁用语清单 | [claude-voice-analyzer](https://github.com/aplaceforallmystuff/claude-voice-analyzer) | Voice Profile（任务级，从本次口述稿提取） |
| Horoscope 测试 + 分级模式库 + 改动前后报告 | [antislop](https://github.com/aplaceforallmystuff/signal-starter-kit) | Anti-AI 查 + 编辑台账；模式库改写为中文影评语境 |
| Reader Testing（新鲜读者捉盲点） | [doc-coauthoring](https://github.com/anthropics/skills) | Critic 三查（观点保真/Voice/Anti-AI） |

### 未采用的（及原因）

- antislop 的英文词表（delve/tapestry…）→ 本地化为中文影评高频词，否则无用。
- voice-analyzer 的"3–5 篇范文 → 项目级 VOICE.md"→ 本任务是单次口述稿成文，Voice Profile 为任务级；项目级 VOICE.md 记入候选。
- doc-coauthoring 的三阶段交互式共建（上下文访谈 + 迭代 + 读者测试）→ 我们是一次性材料 → 成稿场景，访谈部分已由 no-slacking/im-satisfied 承担，不复制。
- glmv-doc-based-writing：API 调用壳，无机制可采；writing-shape（mattpocock 主线未找到）与 article-writing（通用无显著机制）未采用。

### 跨领域 Capability 候选（不立即拆）

1. **Opinion Map**：观点事实源提取（主张+原句+立场强度+未表达）——可复用于书评/产品反馈/访谈整理。
2. **Voice Profile**：任务级声音档案，未来可升级为项目级 VOICE.md 型 Capability（多任务共享同一作者声音）。
3. **Edit Ledger**：任何"AI 改写"任务的审计台账（增/删/并/调/改逐项 + 原因）。
4. **Anti-AI 模式库**：跨文体的 AI 痕迹分级清单（当前影评语境版）。
