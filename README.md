# dsh-skills —— 个人 AI 生产能力系统

把人的判断、专业方法、执行规则和生产经验，沉淀成 AI 可调用、可组合、可验证的 **Skill 与 Workflow**，让任务从意图持续推进到真实交付。

> 仓库长期覆盖方向：创意/视觉、产品、UI/UX、文案、研究、软件开发、测试、项目控制、资产管理、交付，以及其他真实生产任务。**当前只建成第一个子系统，仓库不限视觉。**

## 仓库总逻辑

```
Human Goal / Judgment
        ↓
Skills + Workflows
        ↓
Controlled Execution
        ↓
Verification
        ↓
Real Deliverable
```

## 架构模型（概念层级，暂不迁移目录）

| 层级 | 定义 | 当前成员 |
|---|---|---|
| CORE / PROTOCOL | 全局执行纪律与协作规则 | no-slacking、im-satisfied |
| CAPABILITY | 可被多个 Workflow 复用的稳定能力 | visual-brief（视觉） |
| WORKFLOW | 组合能力完成完整生产任务 | style-replication、build-closed-illustration-asset-library、build-modular-longform-templates、rebuild-layered-html-template、rebuild-layered-canva-template（视觉） |
| ADAPTER / UTILITY | 模型、工具、外部执行环境适配 | model-adapter |

## 当前子系统：Creative / Visual Production

```
visual-brief（定义任务）
      ↓ Visual Task Brief
      ├─ 视觉决策不足 → art-direct-image → Direction Contract ─┐
      └─ 需要参考复刻 → style-replication → STYLE SPEC + Design Spec ─┤
                                                               ↓
                                                  model-adapter（翻译成模型语言）
      ↓ 最终提示词
generation（真实生成）
      ↓
validation（Visual QA：PASS / PARTIAL / FAIL）
      ↓
targeted revision（定向修正）
```

style-replication 内部目前包含 Reference Analysis / Visual Grammar / Composition-Design / Visual QA，**暂不拆独立 Skill**（升级条件见 docs/SKILL-STANDARD.md）。

另：Writing / Content Production 方向第一个完整 Workflow 已建成（`film-review-from-transcript`：口述/聊天/笔记 → 影评成文，观点与声音保真 + 最小编辑 + 三查台账）。当前为单点，暂不构成子系统。

## Skill Map

| Skill | 类型 | 上游 | 下游 | 职责一句话 |
|---|---|---|---|---|
| no-slacking | Protocol | — | im-satisfied / visual-brief | 入口与执行纪律：Readiness/Ownership/Risk/Evidence/Stop |
| im-satisfied | Protocol | no-slacking | 主线 | 条件分支：满意标准卡 + 验收契约 |
| visual-brief | Visual Capability | no-slacking | style-replication / model-adapter | 定义"这次视觉任务要创作什么"（8 字段 Brief） |
| [art-direct-image](art-direct-image/SKILL.md) | Visual Capability | visual-brief / 直接生图需求 | imagegen / model-adapter | 模糊时补齐少量高影响视觉决定，控制疏密、留白、中性色彩、条件性线条与模型惯性；完整蓝图直通 |
| style-replication | Workflow | visual-brief | model-adapter → generation → QA | 风格复刻全流程：参考→理解→STYLE SPEC→设计→验证→修正 |
| [build-closed-illustration-asset-library](build-closed-illustration-asset-library/SKILL.md) | Workflow（视觉） | 已批准母图 | 用户 / AI排版 / Cursor | 母图分析 → 全量元素拆分与补全 → 编号、令牌、manifest → 封闭资产库；Level 0 Draft，真实生产未验证 |
| [build-modular-longform-templates](build-modular-longform-templates/SKILL.md) | Workflow（视觉） | 原始参考图 + 固定视觉风格 + 模块范围 | 用户 / Cursor（HTML + CSS 文件） | 固定风格 → 模块拆解 → 正文自动增高 → 本地模板文件与组合示例；Level 0 Draft，真实生产未验证 |
| [audit-wechat-article-compatibility](audit-wechat-article-compatibility/SKILL.md) | Capability（发布审查） | 图文策划 / HTML与素材包 / 微信草稿预览 | 策划修改 / 制作验收 / 发布判断 | 审查图片、GIF、SVG、视频、链接和连续长图的微信兼容性，以证据分级、降级方案和双端真机测试形成发布门槛；Level 0 Draft，真实发布验证待完成 |
| [rebuild-layered-html-template](rebuild-layered-html-template/SKILL.md) | Workflow（视觉） | 准确扁平原图 + 目标画布 + 品牌保护区 | 用户 / Cursor（分层 HTML + CSS 文件） | 准确原图 → PSD 式拆层 → 本地 HTML/CSS 重建 → 结构与视觉校验；Level 0 Draft，已完成一次真实生产回测 |
| [rebuild-layered-canva-template](rebuild-layered-canva-template/SKILL.md) | Workflow（视觉） | 准确扁平原图 + 目标可画尺寸 + 品牌保护区 | 用户 / 可画（可编辑 PDF/模板） | 准确原图 → PSD 式拆层 → 可画定向 PDF → 导入与可编辑性校验；Level 0 Draft，真实导入闭环尚待完整验证 |
| model-adapter | Adapter | visual-brief / style-replication | 用户（生成工具） | 把已定创作决定翻译成目标模型可执行语言 |
| film-review-from-transcript | Workflow（写作） | no-slacking →（标准不清时）im-satisfied | 用户（成稿+台账摘要） | 口述/聊天/笔记 → 影评成文：Opinion Map + Voice 保真 + 最小编辑 + 三查台账 |

（每个 Skill 的 Trigger/Input/Output/Failure/Validation 等 10 项结构见各自 SKILL.md，标准见 docs/SKILL-STANDARD.md。）

## 目录结构

```
dsh-skills/
├── no-slacking/SKILL.md          （入口与执行纪律）
├── im-satisfied/SKILL.md         （条件分支：满意标准卡）
├── visual-brief/
│   ├── SKILL.md                  （瘦身后的主流程）
│   └── references/               （category-norms / ai-tells / vocabulary）
├── style-replication/
│   ├── SKILL.md                  （完整 Workflow）
│   ├── references/               （element-selection）
│   └── evals/                    （eval-a…f + eval-run 运行记录）
├── art-direct-image/
│   ├── SKILL.md                  （模糊生图的轻量视觉导演）
│   ├── agents/openai.yaml        （Skill 显示与隐式调用信息）
│   ├── assets/icon.svg           （Skill 图标）
│   └── references/               （摄影、插画平面、产品物件与生成后验收）
├── build-closed-illustration-asset-library/
│   ├── SKILL.md                  （封闭插图资产库 Workflow）
│   ├── agents/openai.yaml        （Skill 显示与调用信息）
│   ├── references/               （视觉分析、拆分补全与交付契约）
│   ├── scripts/                  （资产库结构与来源校验）
│   └── evals/                    （行为测试场景与运行状态）
├── build-modular-longform-templates/
│   ├── SKILL.md                  （模块化长图文模板 Workflow）
│   ├── agents/openai.yaml        （Skill 显示与调用信息）
│   ├── assets/icon.svg           （Skill 图标）
│   └── references/html-delivery.md（HTML 文件、延展与验收规则）
├── audit-wechat-article-compatibility/
│   ├── SKILL.md                  （微信公众号交互与兼容性审查 Capability）
│   ├── agents/openai.yaml        （Skill 显示与调用信息）
│   └── references/               （证据分级、功能基线、发布测试与报告模板）
├── rebuild-layered-canva-template/
│   ├── SKILL.md                  （扁平原图转可画分层 PDF/模板 Workflow）
│   ├── agents/openai.yaml        （Skill 显示与调用信息）
│   ├── assets/icon.svg           （Skill 图标）
│   └── references/               （图层模型、PDF 与可画 QA）
├── rebuild-layered-html-template/
│   ├── SKILL.md                  （扁平原图转 PSD 式分层 HTML/CSS Workflow）
│   ├── agents/openai.yaml        （Skill 显示与调用信息）
│   ├── references/               （图层模型、素材策略与视觉 QA）
│   ├── scripts/                  （本地资源与文件结构检查）
│   └── evals/                    （真实生产回测记录）
├── model-adapter/
│   ├── SKILL.md                  （转译原则与边界）
│   └── references/               （midjourney / chatgpt-images / jimeng / flux-sd / generic）
├── film-review-from-transcript/
│   ├── SKILL.md                  （Writing 方向第一个 Workflow）
│   ├── references/               （anti-ai-patterns / voice-markers / shape-catalog）
│   └── evals/                    （eval-a…h + eval-run 运行记录）
├── docs/SKILL-STANDARD.md        （全仓库 Skill 设计标准）
└── WORKFLOW-RETROSPECTIVE.md     （本轮样板复盘）
```

## 安装

```bash
mkdir -p ~/.dsh/skills
cp -R no-slacking im-satisfied visual-brief art-direct-image style-replication model-adapter film-review-from-transcript build-closed-illustration-asset-library build-modular-longform-templates audit-wechat-article-compatibility rebuild-layered-html-template rebuild-layered-canva-template ~/.dsh/skills/

# 共享目录（Claude / Cursor 等也能读取）：
# cp -R no-slacking im-satisfied visual-brief art-direct-image style-replication model-adapter film-review-from-transcript build-closed-illustration-asset-library build-modular-longform-templates audit-wechat-article-compatibility rebuild-layered-html-template rebuild-layered-canva-template ~/.agents/skills/
```

（用 `cp -R` 以包含各 skill 的 `references/`。）

## 同步说明

本仓库是 `~/.dsh/skills` 的发布快照。日常迭代以 `~/.dsh/skills` 为准：

```bash
for s in no-slacking im-satisfied visual-brief art-direct-image style-replication model-adapter film-review-from-transcript build-closed-illustration-asset-library build-modular-longform-templates audit-wechat-article-compatibility rebuild-layered-html-template rebuild-layered-canva-template; do
  mkdir -p $s && cp -R ~/.dsh/skills/$s/ $s/
done
```

## 发布前检查

改完 frontmatter 后跑一次检查，防止 skill 因格式错误被 DSH 静默跳过：

```bash
# 1) 快速检查：frontmatter 同一行不得出现第二个 ASCII ": "（"Avoid: /" 这类写法会让 YAML 解析失败）
awk 'BEGIN{fm=0} /^---$/ {fm=!fm; next} fm && gsub(/: /, ": ") > 1 {print FILENAME ":" FNR ": " $0}' */SKILL.md

# 2) 完整检查：用与 DSH 同源的 yaml 库解析（先 npm i yaml，或指向本机已有路径）
node -e "
const fs = require('fs');
const yaml = require('yaml');
for (const n of ['no-slacking','im-satisfied','visual-brief','art-direct-image','style-replication','model-adapter','film-review-from-transcript','build-closed-illustration-asset-library','build-modular-longform-templates','audit-wechat-article-compatibility','rebuild-layered-html-template','rebuild-layered-canva-template']) {
  const s = fs.readFileSync(n + '/SKILL.md', 'utf8');
  const m = s.match(/^---\n([\s\S]*?)\n---/);
  try { yaml.parse(m[1]); console.log(n, 'OK'); }
  catch (e) { console.log(n, 'FAIL:', e.message); }
}
"
# 3) 双向一致性：生效版（~/.dsh/skills）与仓库副本必须逐字节一致
for s in no-slacking im-satisfied visual-brief art-direct-image style-replication model-adapter film-review-from-transcript build-closed-illustration-asset-library build-modular-longform-templates audit-wechat-article-compatibility; do
  diff -q ~/.dsh/skills/$s/SKILL.md $s/SKILL.md || echo "$s 不一致"
done
```

## 灵感来源

- [obra/superpowers](https://github.com/obra/superpowers) —— evidence-before-claims。
- [trailofbits/skills](https://github.com/trailofbits/skills) —— 最小追问集 + 先查再问。
- MengTo Skills —— Reference Registry / Visual DNA / Reusable Visual Grammar / Signature / Similarity Dial / Constants & Variables（style-replication 的主基线）。
- Anthropic frontend-design 与 Joshua frontend-design-principles —— 生成前明确创作方向、distinctive visual choices、Defaults to Reject。
- OpenAI Product Design Skills —— Router 与 focused workflow 分离、Design 与 QA 分离。
- [anthropics/skills](https://github.com/anthropics/skills) 与 Anthropic Skill Creator —— Progressive Disclosure、SKILL.md 短流程 + references/ + evals。
