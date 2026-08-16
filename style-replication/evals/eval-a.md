# Eval A — 单张参考

**目标**：验证 Reference Analysis → STYLE SPEC → 新构图设计 → 视觉语言迁移的完整链路。

**输入**：1 张明确参考 + 1 个不同内容的新任务。

**检查点**：
- [ ] Reference Registry 是否给参考定了明确角色？
- [ ] Visual Facts 是否回答了"画面如何被构成"，而非罗列形容词？
- [ ] STYLE SPEC 是否简练、可执行（非艺术评论）？
- [ ] Design Spec 是否在生成前决定了画什么、放在哪、怎样组织？
- [ ] 迁移到新内容后，视觉规律（而非具体内容）是否稳定保留？
- [ ] Defaults to Reject 是否写入了模型最可能滑向的默认结果？

**通过判定**：6 项全达成 = PASS；「规律迁移」与「Defaults to Reject」为核心项，任一未达成即 FAIL。
