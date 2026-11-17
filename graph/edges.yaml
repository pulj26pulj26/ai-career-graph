# graph/edges.yaml
edges:
  - id: M1
    from: S1
    to: A2
    artifact: 评估指标定义 + 失败样本分类表
    consumed_at: A2 / 组件级指标设计
    strength: strong
    note: 跨节点迁移证据，需在 A2 文档中简短论证指标在新语境下的适用性

  - id: M2
    from: A2
    to: S2
    artifact: 约束变化下的行为记录 + 失败模式分类
    consumed_at: S2 / 实验条件设计
    strength: moderate
    note: 作为需要被实验控制的协变量候选

  - id: M3
    from: A1
    to: S1
    artifact: 工具调用 trace
    consumed_at: S1 / 失败分析与指标论证
    strength: moderate
    note: 作为评估样本来源，避免凭空构造靶子

  - id: M4
    from: S3
    to: A3
    artifact: 决策叙事
    consumed_at: A3 / 协议设计
    strength: weak
    note: 不构成能力信号迁移，只丰富业务约束上下文
