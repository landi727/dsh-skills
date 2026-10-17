# 制作与验收证据

把规则、整篇构图和实际检查写入一个项目内的 JSON；按阶段更新，不在交付时补造前置记录。完整构图方案、制作或审查使用此协议；纯规则/方向问答不强制填写。记录只支持追溯，脚本不能判定作品好看、风格忠实或记录真实。

## 三种任务

| task_type | 必需证据 | 返回 0 的含义 |
| --- | --- | --- |
| production | 参考规则、素材前的整体构图、生成素材与参考对照、最终文件、六项验收 | 制作记录齐全且没有记录中的阻断项 |
| review | 适用的参考规则、最终文件、六项验收；无需补造原制作阶段 | 本次审查记录齐全且没有记录中的阻断项 |
| plan | 适用的风格规则、真实可查看的完整构图草稿及理由；不要求成图或生成素材 | 仅完整构图方案的记录齐全，不能称成品通过 |

production 中先保存整篇结构草稿，再生成所需素材，最后检查同一版本的全篇、阅读尺寸和关键局部。海报与长图分别组织构图；共享素材不自动等于共享完整版式。整篇可有不同底色、独立开篇或无框正文，选择须与内容及构图相符。

## 轻量协议

将 `design-evidence.json` 放在项目内。下表中列表项使用所列字段；无需额外报告模板。

| 字段 | 内容 |
| --- | --- |
| task_type | `production`、`review` 或 `plan` |
| has_style_reference | 布尔值：本任务是否要求承接已提供的视觉风格参考；文字规定的画法另写入规则，不等同于已提供参考图 |
| has_drawing_task | 布尔值：是否包含绘画、画法要求或生成图像素材；无参考的原创绘画仍需检查实际素材 |
| needs_graphic_extension | 布尔值：本任务是否包含标题、框体、转场、照片处理等视觉延展 |
| reference_rules | `[{id, source, observation, requirement, critical}]`；source 为参考文件路径或 HTTP(S) 来源；observation 写可见位置与特征，requirement 写本项目如何保留；决定识别度的规则标 `critical: true` |
| composition | `{overview_path, status, evidence}`；制作与完整构图方案均必须指向已保存的整体草稿图；说明重心、字图关系和连续阅读，章节清单不能替代草稿。审查任务可省略此字段 |
| assets | `[{path, generated, prompt_path, reference_sources, rule_ids, status, evidence, comparison_paths}]`；制作任务列需验证的素材。生成素材须保存提示词、引用对应规则并留查看路径；有风格参考时还须引用实际参考并对照。原创无风格参考可令 reference_sources 为空；复用素材的生成字段可为空 |
| outputs | `[{id, type, path}]`；type 为 `poster`、`longform` 或 `other`；制作/审查必须指向最终文件 |
| checks | `[{criterion, status, evidence, view_paths, rule_ids}]`；制作/审查各含下述六项，方案任务无需填写成品验收 |

`status` 统一为 `pass`、`fail`、`not_checked`、`not_applicable`。路径相对 JSON 所在目录解析；实际文件须存在。参考 URL 仅表示来源，不替代已查看的图；脚本不联网验证来源。图片路径可引用局部对照或完整工作板；人须确认它们对应同一最终版本。

三个任务范围布尔值依据用户要求填写，不能为绕过失败改成 false。含风格参考、绘画任务或视觉延展时记录至少一条决定性规则；文字给定的画法同样提取关键规则，可引用保存的 brief。规则 ID 在素材和检查间复用。制作/审查的关键规则必须逐项出现在 `drawing_style` 或 `graphic_extension` 检查中；正文可读性通过不能抵消画风失败。

## 六项检查

| criterion | evidence 写什么 |
| --- | --- |
| content | 对照事实、名称、文案和待补项的结果 |
| drawing_style | 对照决定性规则，写形、线、填色、材质、空间的具体相符或偏离；不可仅凭同色放行 |
| graphic_extension | 检查标题、图片处理、边缘、标记和转场如何承接已选语言，是否只有主题贴图 |
| composition | 检查完整作品的重心、字图关系、密度与章节衔接；长图不能仅逐块判定 |
| reading | 检查实际阅读宽度的字形、层级、断行、图注与必要信息 |
| technical | 检查导出、尺寸、素材/字体加载、溢出与文件可打开 |

每项都写具体证据并覆盖所有最终文件。`pass` 必须有 `view_paths`；四项视觉检查指向实际查看的图片或视觉预览，内容/技术检查也可引用 JSON 或报告。有风格参考的生成素材，其 `comparison_paths` 至少包含素材和参考/对照工作板；原创无风格参考时至少包含素材图并说明对应规则的结果。记录实际差异，不能把“提示词包含规则”当作成图满足规则。

`fail` 或 `not_checked` 阻断合格成品交付。`not_applicable` 必须写具体理由；仅无视觉风格参考且无绘画/画法任务时允许 `drawing_style` 不适用，仅不含视觉延展时允许 `graphic_extension` 不适用。完整平面制作/审查中的 `content`、`composition`、`reading`、`technical` 必须逐项检查，不允许设为不适用。生成素材不能跳过实际图像检查。保留失败证据，修复后更新实际图、相邻区域和判定；不得以改状态代替复查。

运行：`python3 <技能目录>/scripts/check_design_evidence.py <项目目录>/design-evidence.json`。返回 `2` 表示字段、覆盖或文件路径错误；`3` 表示记录包含失败/未检查；`0` 只表示记录检验通过。脚本不读图、不认证看图行为、不测审美；仍须完成真实视觉验收。方案/审查的通过不代替制作稳定性验证。
