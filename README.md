# dsh-skills

给 DeepSeek Harness（DSH）用的个人技能合集，目前包含两个相互衔接的 skill。

> 技能格式遵循 DSH 的 `SKILL.md` 规范：`<name>/SKILL.md`，YAML frontmatter（`name` / `description` / `whenToUse`），正文为注入给模型的指令。

## 技能列表

### `no-slacking` · 《咱都别偷懒》
人机双向不偷懒协议，通用所有任务。

- **人，你别偷懒**：需求不清、素材不足、说不清"怎样算满意"时，不假装能做——追问或拒绝，并给出「可达性报告」。
- **AI，也别偷懒**：不把能自己做的活推给人、不静默简化、不无证据报完成（证据先于断言）。
- **心有猛虎，细嗅蔷薇**：敢拍板、能推进，同时按比例原则防止过度分析与过度验证（明文禁止安心式重复验证，如反复比对哈希）。

### `visual-brief` · 视觉作品想法梳理
视觉/设计类任务的领域落地层，面向 Midjourney 与 DALL·E/GPT-4o。

- 把模糊想法收敛成**图像生成模型可理解的结构化简报**（13 字段）。
- 覆盖插画/海报、网页/App UI、图标、Logo/VI、写实摄影六类，各含规范 + 生产流程 + 常见坑。
- 产出**双语提示词**（分模型）+ **去 AI 味**（负向约束 + 正向风格锚点）+ 自检清单。

### 两者关系

```
no-slacking（底层通用协议）→ 需求体检 + 验收契约
        └─ 视觉类任务 ─→ visual-brief（领域落地）→ 想法→简报→提示词→去AI味→自检
```

## 安装

把需要的技能目录复制到 DSH 的技能根目录之一：

```bash
# 方案 A：DSH 用户级（推荐，仅 DSH 可用）
mkdir -p ~/.dsh/skills
cp -R no-slacking visual-brief ~/.dsh/skills/

# 方案 B：共享 agent 目录（Claude / Cursor 等也能读取）
mkdir -p ~/.agents/skills
cp -R no-slacking visual-brief ~/.agents/skills/
```

DSH 会在下一次目录快照时自动发现；无需重启。

## 用法

直接对 DSH 说出需求即可触发，例如：

- "帮我做个冥想 App 的图标，要安静简约，别太像 AI" → 触发 `no-slacking`（体检）+ `visual-brief`（澄清→简报→提示词）。
- "帮我做个东西，要高级一点" → 触发 `no-slacking` 的需求体检，先问 1–3 个必答问题而不是假装开工。

## 灵感来源

- [obra/superpowers](https://github.com/obra/superpowers) —— 尤其 `verification-before-completion`（证据先于断言）。
- [trailofbits/skills](https://github.com/trailofbits/skills) —— 尤其 `ask-questions-if-underspecified`（最小追问集 + 先查再问）。
- [anthropics/skills](https://github.com/anthropics/skills) —— 官方技能仓库格式参考。

## 同步说明

本仓库是 `~/.dsh/skills` 的发布快照。日常迭代以 `~/.dsh/skills` 为准，改动后可用以下命令同步回仓库：

```bash
cp ~/.dsh/skills/no-slacking/SKILL.md no-slacking/SKILL.md
cp ~/.dsh/skills/visual-brief/SKILL.md visual-brief/SKILL.md
```
