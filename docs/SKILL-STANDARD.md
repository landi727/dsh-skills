# SKILL-STANDARD（全仓库通用 Skill 设计标准）

适用于本仓库所有 Skill，不限视觉领域。新 Skill 立项、修改、评审都先对照本标准。

## Skill 类型

每个 Skill 必须明确标注类型：

| 类型 | 定义 |
|---|---|
| Protocol | 全局执行纪律（跨任务生效的规则） |
| Capability | 可被多个 Workflow 复用的稳定专业能力 |
| Workflow | 把多个能力组合成完整生产任务的流程 |
| Adapter | 工具、模型、外部执行环境适配 |

## 必备结构（10 项）

一个成熟 Skill 至少回答：

1. **Trigger**：什么时候使用、什么时候不用。
2. **Responsibility**：负责什么。
3. **Boundary**：不负责什么。
4. **Input Contract**：必须拿到什么输入，缺了怎么办。
5. **Workflow**：具体怎么执行。
6. **Output Contract**：必须交付什么。
7. **Failure Handling**：失败、缺资料、能力不足怎么处理。
8. **Validation**：怎么证明完成。
9. **Stop Condition**：什么时候停止。
10. **Reuse Scope**：全仓库 / 领域 / 某 Workflow 专属。

**落地要求**：主 SKILL.md 必须**显式**声明至少 6 项——类型、Responsibility、Boundary、Input Contract、Output Contract、Failure Handling；Trigger 以 frontmatter 的 whenToUse 承担；Validation、Stop Condition、Reuse Scope 可显式或**引用全局规则**（如 no-slacking R4/R5），但引用必须写明出处，不能靠模型自己猜。

## Progressive Disclosure 规则（仓库统一）

```
SKILL.md      模型真正执行的核心流程（短、程序化、可执行）
references/   专业知识、方法资料、扩展规则（按任务读取）
scripts/      可确定性执行的自动操作
assets/       示例、模板、视觉资产
evals/        测试案例与评价标准
```

- 主 SKILL.md 优先保证执行清晰；长知识一律下沉 references/。
- references/ **不会自动加载**：SKILL.md 必须写明"何时、读哪个文件"，否则知识会变成死档。
- **跨 skill 引用规范**：相对路径只对**本 skill 自己的**资源目录有效。引用其他 skill 的文件必须写"读取 \<skill 名\> 技能的 references/\<文件\>"（例如"读取 visual-brief 技能的 references/ai-tells.md"），不得写会被本 skill 目录解析的相对路径。

## 内部步骤升级成独立 Skill 的条件

全部满足才拆：

- 被至少 2 个 Workflow 稳定复用；
- 有独立触发条件；
- 有独立输入/输出；
- 有独立失败模式；
- 有独立验证方法；
- 脱离原 Workflow 后仍有使用价值。

优先顺序：**先真实生产 → 发现稳定方法 → 再抽象成 Skill**。禁止先建能力树再找用途。

## 设计原则

- 成熟机制直接继承（如 evidence-before-claims、最小追问集），禁止为体现原创重新发明。
- 未判断适用性不照搬外部内容。
- 冲突时决策顺序：仓库长期目标 → 当前 Workflow 目标 → 实际生产有效性。
- 禁止机械拼接多个 Skill；禁止因"未来可能有用"提前开发未验证 Skill。
- **Production First**：现有能力足以推进真实任务时，禁止为了优化 Skill 而暂停生产；Skill 迭代放在真实生产间隙或事后。**运行时执行版：no-slacking R5。**
- **Internal by default**：Brief / SPEC / Perception Notes / QA 明细等中间结构默认内部生成、落盘并供后续环节读取，不逐份向用户展示。只向用户展示：阻塞性问题（BLOCK）、影响方向或成本的重大决策、正式交付物（最终提示词、QA 结论、修正指令）、用户主动要求的内容。**运行时执行版：no-slacking R2。**
- **Eval 准入（成熟度门槛）**：
  - Level 0 Draft：结构齐、未跑 eval；
  - Level 1 Text-validated：文本层 eval 全例 PASS（含失败模式），真实执行未验证；
  - Level 2 Production-validated：至少一次真实生产全流程跑通 + 一次定向修正闭环，结果记入 evals；
  - 只有 Level 2 可标注"成熟 Skill"。
  - **诚实标注**：文本层与真实执行必须分开记录；未验证部分必须显式标注"未验证"，禁止虚报（style-replication 的 eval-run 为范本）。

## 格式红线

- frontmatter 的 description / whenToUse 值内**禁止 ASCII 冒号+空格（`: `）**（会让 YAML 解析失败、skill 被 DSH 静默跳过），统一用全角「：」。
- 名称 kebab-case；name 与目录名一致。
- 发布前跑一遍 README「发布前检查」的两条命令。
