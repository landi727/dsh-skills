# 方法依据与项目经验

核查日期：2026-10-06。以下为方法借鉴与适用性判断，不代表这些项目已在本用户的微信长图流程中验证有效。规则用原创表述整理，未复制第三方技能正文、脚本、字体或品牌素材。

## GitHub 取舍

Stars 为核查时 GitHub 显示的仓库级约数，代表关注度，不能证明设计质量，也不能归给一个子技能。

| 来源 | 身份/关注度 | 借鉴 | 调整 |
| --- | --- | --- | --- |
| [Anthropic skills](https://github.com/anthropics/skills) / [canvas-design](https://github.com/anthropics/skills/blob/main/skills/canvas-design/SKILL.md) | 官方示例库，约179.8k Stars | 有主张的视觉方向，形、空间、色彩和层级 | 少文字艺术海报倾向不适配长文；反复强调大师工艺不能代替检查 |
| [Impeccable](https://github.com/pbakaus/impeccable) / [主技能](https://github.com/pbakaus/impeccable/blob/main/plugin/skills/impeccable/SKILL.md) | Paul Bakaus项目，约77.2k Stars | 尊重已有视觉依据，区分优化与重设计，批量检查修复 | 偏前端；其检查轮次上限不作为交付已知缺陷的理由 |
| Impeccable [craft-floor](https://github.com/pbakaus/impeccable/blob/main/plugin/skills/impeccable/reference/craft-floor.md) | 同项目检查参考 | 检查实际结果、真实文案、对比度、间距和覆盖 | 英文行长、网站交互及作者个人禁用项不可照搬 |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) / [design](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/design/SKILL.md) | NextLevelBuilder项目，约133.4k Stars | 规则持久化、公共规则加局部变化、HTML/CSS导出后看PNG | 风格目录不能代替判断，平台尺寸和广告规则需查证，不引入多余UI工程依赖 |
| Anthropic [design-critique](https://github.com/anthropics/knowledge-work-plugins/blob/main/design/skills/design-critique/SKILL.md) | 官方反馈技能 | 第一眼、层级、一致性；具体反馈、优先级和修改 | 补充完整阅读、图形延展及切片连续性 |

上述第三方技能仅作研究材料，未整套安装或执行其命令。

## 文化传播与游戏相关一手案例

| 来源 | 可核实方法 | 本技能迁移建议 |
| --- | --- | --- |
| [COLLINS — Spotify](https://wearecollins.com/case-studies/spotify/) | 用音乐印刷语境的双色处理统一艺人照片，以强对比色对传达能量 | 建立可重复图像处理使异源素材融合，不固定采用双色 |
| [Ben Buysse — Discord](https://benbuysse.com/discord) | 参与者介绍表情化标识、富表现力字体和鲜明色彩，把UI元素纳入传播版式 | 从主题/品牌内部提炼部件，让内容图形版式相互支撑 |
| [Dinamo — Discord](https://abcdinamo.com/custom/discord) | 公开字形定制及营销/产品的字重层级；本次查看了字体层级示例图 | 标题字形与插图协调，信息文字保留功能层级，中文重新选字形 |
| [Pedro Veneziano — Twitch](https://pedroveneziano.com/Twitch/) | 作者记载2023项目，Porto Rocha指导并与Twitch合作；插图共享标识材质和高饱和色体系 | 共享材质/色彩规则，游戏相关内容不默认霓虹科技风 |
| [Riot — User Interface Design](https://www.riotgames.com/en/artedu/user-interface-design) | 官方教学重视受众、及时找到重要信息与一致连贯的体验 | 阅读任务决定层级，主题表达与信息读取协调 |
| [Riot — VALORANT Shaders and Gameplay Clarity](https://www.riotgames.com/en/news/valorant-shaders-and-gameplay-clarity) | 2020-06-30文章说明不同游戏选择不同支柱，本例平衡表现、性能与竞技完整性 | 项目先确定真实任务和取舍；这是跨领域推论，不是Riot微信平面规范 |

这些案例贴近音乐、社群和游戏文化，不能证明所有年轻人喜欢同一画风。旧案例不标为2026最新趋势，当期方向另行核查；未直接查看的视觉细节不冒充已分析。

## 检索到的项目经验

来自既有对话，保留原场景边界，当前用户要求与当前文件优先。

| 对话依据 | 保留要求 | 落点 |
| --- | --- | --- |
| 2026-10-06 确认7月14日《萨尔贡沙海考》整体排版符合要求；要求“像它一样知道怎么排”，插图更精细 | 从真实成功案例继承排版判断，字体/标题/文字方法可借鉴，按新内容重新构图 | 使用 inherit-longform-design 的原SVG、案例测量和内容到构图方法；旧小字与占位线不冒充正式正文，新插图按新布局制作 |
| 2026-09-03 长图：用户否定文章加零散素材，要求完整设计图和连续背景/节奏 | 完整作品是验收对象 | 必须交完整图，素材完成不代表整篇完成 |
| 2026-08-12 正文框：要求随字量自动延展，无须手工拖动 | 容器随内容增长 | 框体分段、流式文字、邻接自动移动 |
| 2026-09-07 模板：认可平面图再转HTML/CSS，文字图片装饰独立 | 视觉基准与实现衔接 | 先验证样板，源文件保留独立文字资产 |
| 2026-09-11 微信：先规划整篇内容/素材，上传文字烘焙进图 | 生产顺序与终态明确 | 先规划，源可编辑，发布可扁平化 |
| 2026-10-03 生成反馈：修到合格再交，禁止私自加轮次不等于不修复 | 区分修复与另起方案 | 处理已知缺陷，服从当前明确数量上限 |
| 本轮：只给插图，期待主动延展平面语言 | 缺框体参考不构成停止理由 | 根据证据自行设计配套元素，说明推导 |

未将单个项目的配色、角色、针织复古或应用UI极简规则固化为所有平面作品的风格。未检索到已认可的“潮流大师名单”，不编造偏好。
