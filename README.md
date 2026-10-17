# dsh-skills

个人技能与工作流的版本化仓库，覆盖研究、写作、视觉制作、项目协作、开发与验收等任务。

当前快照为 **2026-10-17**：同步当前个人安装源的 33 项技能，保留原仓库独有的 6 项，共 39 项。各技能的原有正文、引用、脚本、图标和配套资源随目录保存；对两项存在既有停用记录冲突的长图技能补齐停用入口，并将一项风格库技能中的私有账号文件与目录标识改为按原名称和路径发现，保留原功能规则与权限边界。

## 入口

- [技能版本与启停状态索引](SKILLS-INDEX.md)：先查看每项是否可用、停用或仅为远端保留。
- [机器可读索引](skills-index.json)：内容摘要、状态、来源、文件数与结构校验结果。
- [本次迁移记录](docs/MIGRATION-2026-10-17.md)：合并范围、冲突处理、原始内容哈希与校验限制。
- [既有技能设计标准](docs/SKILL-STANDARD.md) 与 [既有工作流复盘](WORKFLOW-RETROSPECTIVE.md)：原仓库历史资料，保留原样。

每项技能以 `技能名/SKILL.md` 为入口，按需读取其 `references/`、`scripts/`、`assets/`、`agents/` 和已有评估记录。目录清单以状态索引为准。

## 安装与使用

本仓库保存快照，**不自动安装或统一启用全部目录**。先查看索引及该技能主文件，再把选中的完整技能目录复制到目标工具支持的技能位置，保留所有资源；目标工具的安装路径与加载方式以其实际配置为准。

以下 7 项处于停用状态：`analyze-reference-style`、`compose-character-homepage-art`、`design-graphic-systems`、`inherit-longform-design`、`guide-reference-illustration`、`build-modular-longform-templates`、`design-longform-layouts`。不得因同步、安装、引用或新的同类任务而恢复调用；其中 `inherit-longform-design` 永久停用，其余需用户明确重新启用并完成对应配置、验证和保存后才可恢复。

远端独有的 `film-review-from-transcript`、`im-satisfied`、`model-adapter`、`no-slacking`、`style-replication`、`visual-brief` 保留原样。它们不在本次个人安装源中，保留不代表默认安装或重新启用。

## 同步原则

以技能主文件 frontmatter 的 `name` 映射稳定目录名，完整复制该技能的配套文件。同名文件采用当前实际源；远端独有目录及同名目录中的远端独有文件保留。发现启停记录冲突时先核对用户已有决定，记录差异，禁止静默重新启用。

提交前检查 YAML、名称、相对引用、资源与隐私风险，并与源文件逐字节比对。版本索引使用确定性的目录内容 SHA-256，记录快照变化。迁移与结构检查不等同于技能完成了真实任务验证。

当前全部 39 项 YAML 可解析，32 项通过 skill-creator 的严格结构检查；7 项保留历史扩展字段告警。详见迁移记录。已有脚本中的环境依赖与历史成熟度声明随原文件保留，使用前仍需按具体任务核对。

## 来源与许可

保留原仓库 [MIT 许可](LICENSE)。各技能中的已有来源、上游引用与评估记录随文件保存；仓库保留不表示为第三方材料重新授予许可。
