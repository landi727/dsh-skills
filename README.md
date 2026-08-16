# dsh-skills

给 DeepSeek Harness（DSH）用的个人技能合集：一条**人机协作 + 视觉产出**的链。

> 技能格式遵循 DSH 的 `SKILL.md` 规范：`<name>/SKILL.md`，YAML frontmatter（`name` / `description` / `whenToUse`），正文为注入给模型的指令。

## 架构总纲（权威定义）

```
no-slacking（入口 + 执行纪律）
  Readiness · Ownership · Risk · Evidence · Stop
      │ 验收标准不足
      ▼
im-satisfied（定标准）
  Success Criteria · Acceptance Contract
      │ 视觉任务
      ▼
visual-brief（模型无关简报）
  Visual Intent · Visual Constraints · Reference Translation · Brief
      │ 根据目标模型
      ▼
model-adapter（模型语法）
  Midjourney · ChatGPT Images · 即梦/豆包 · SD/Flux
```

**触发规则**：no-slacking 是唯一入口（一切任务开工前）；其余按条件接力、按需加载，不要同时全载、不要重复提问。

**每环交付物（交接契约）**：

| 交接 | 传什么 |
|---|---|
| no-slacking → im-satisfied | 指出缺哪一块：目标 / 硬线 / 深度线 / 否决线 |
| im-satisfied → visual-brief | 满意标准卡（含否决线） |
| visual-brief → model-adapter | 13 字段简报（模型无关） |
| model-adapter → 用户 | 最终提示词 + 参数 + 负向语法 |

## 职责一览

- **no-slacking**：入口与执行纪律。Readiness（体检/红黄绿/LIMITED GO/可达性报告）、Ownership（移交三问/反静默简化/指令双义务）、Risk（比例原则/假设透明）、Evidence（证据 vs 判断依据）、Stop（停止条件）。**不负责定标准**。
- **im-satisfied**：Success Criteria（三层推演 + 四块标准卡 ≤300 字）+ Acceptance Contract（否决线点头 + 对卡自检）。证据与比例原则引用 no-slacking。
- **visual-brief**：Visual Intent（分级澄清）、Visual Constraints（六类规范 + 去 AI 味内容知识）、Reference Translation（参考→锚点 + 词汇表）、Brief（13 字段，模型无关）。**不含模型语法**。
- **model-adapter**：简报 → 某模型最终提示词（Midjourney / ChatGPT Images / 即梦·豆包 / SD·Flux 四个 profile），负责负向约束的语法表达。

## 术语表（唯一定义）

- **标准卡四块**：目标 / 硬线 / 深度线 / 否决线。
- **证据 vs 判断依据**：客观可验证任务用当场新鲜证据；创意判断/概念/策略类用判断依据（no-slacking R4）。
- **去 AI 味**：内容知识（AI 味清单、风格锚点）在 visual-brief；语法表达（--no / Avoid: / 负面词）在 model-adapter。
- **LIMITED GO**：红灯下明确上限与风险后继续做的选项。

## 安装

```bash
mkdir -p ~/.dsh/skills
cp -R no-slacking im-satisfied visual-brief model-adapter ~/.dsh/skills/

# 共享目录（Claude / Cursor 等也能读取）：
# cp -R no-slacking im-satisfied visual-brief model-adapter ~/.agents/skills/
```

## 用法示例

- "帮我做个东西，要高级一点" → no-slacking 体检（黄灯：问 1–3 个必答问题）
- "帮我做冥想 App 图标，要安静简约，别太像 AI" → no-slacking → im-satisfied（标准卡）→ visual-brief（简报）→ model-adapter（Midjourney / DALL·E 双版本提示词）

## 同步说明

本仓库是 `~/.dsh/skills` 的发布快照。日常迭代以 `~/.dsh/skills` 为准，改动后同步回仓库：

```bash
for s in no-slacking im-satisfied visual-brief model-adapter; do
  cp ~/.dsh/skills/$s/SKILL.md $s/SKILL.md
done
```

## 灵感来源

- [obra/superpowers](https://github.com/obra/superpowers) —— 尤其 `verification-before-completion`（证据先于断言）。
- [trailofbits/skills](https://github.com/trailofbits/skills) —— 尤其 `ask-questions-if-underspecified`（最小追问集 + 先查再问）。
- [anthropics/skills](https://github.com/anthropics/skills) —— 官方技能仓库格式参考。
