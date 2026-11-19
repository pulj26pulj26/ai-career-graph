# AI Career Graph — Nodes

以下是图谱节点的完整定义，包含每个节点的能力信号、证据要求和环节拆解。

```yaml
# graph/nodes.yaml
nodes:
  - id: A1
    line: A                      # A / S
    title: Agent 任务编排与工具调用
    shared: false
    capability_signal: >
      能独立完成一个多步骤 Agent 的编排实现，并在代码与文档中留下
      编排策略选择、工具注册方式、失败后重试/降级的可追溯记录。
    evidence_requirements:        # GitHub 上必须出现的具体工件
      - 可运行的 Agent 仓库，README 写明编排策略（顺序/路由/并行）
      - commit message 中至少一条“为什么选 X 而不是 Y”的编排决策
      - 一次受控失败的运行记录 + 降级行为说明
    stages:                       # 环节拆解：3-5 个
      - name: 场景与工具选型
        knowledge_dependency: 无硬性依赖
        supply_point: null
      - name: 编排逻辑实现
        knowledge_dependency: Python 异步 / API 调用（moderate）
        supply_point: 节点内微型补给：asyncio 基础 + 异常处理模板
      - name: 受控失败与降级
        knowledge_dependency: 错误分类思维（moderate）
        supply_point: 节点内补给：失败模式分类清单
    prerequisites: []             # A1 无前置


  - id: A2
    line: A
    title: Agent 可靠性设计与评估
    shared: true                  # 跨岗位共享节点
    capability_signal: >
      能针对一个可观测的 Agent 设计组件级评估，识别失败模式，
      并记录约束变化（token budget / 工具不可用）下的行为改变。
    evidence_requirements:
      - 组件级指标定义（不只看最终答案对错）
      - 失败样本分类表
      - 至少一条约束变化下的行为对比记录
    stages:
      - name: 选定评估对象
        knowledge_dependency: 需要一个可观测 Agent（strong）
        supply_point: 可调用 A1 产物；或在节点内构造最小靶子
      - name: 组件级指标设计
        knowledge_dependency: 指标设计思维（moderate）
        supply_point: 可复用 S1 的评估指标定义（见迁移 1）
      - name: 约束变化实验
        knowledge_dependency: 受控对比思维（moderate）
        supply_point: 节点内补给：单因子变化记录模板
    prerequisites:
      - node: A1
        strength: strong
        scope: 若跳过 A1，需在“选定评估对象”环节自建最小 Agent

  - id: A3
    line: A
    title: 多 Agent 协作与协议设计
    shared: false
    optional: true                # MVP 可选，不纳入两周验证
    capability_signal: >
      定义两个以上 Agent 的通信契约（消息格式、职责边界、冲突消解），
      并留下协议文档与一次协作成功/失败记录。
    evidence_requirements:
      - 协议文档（消息 schema + 职责边界）
      - 一次双 Agent 协作运行记录
    stages:
      - name: 协议设计
        knowledge_dependency: 消息契约设计（moderate）
        supply_point: 节点内补给：消息 schema 模板
      - name: 消息契约实现          # 新增
        knowledge_dependency: 序列化 / 反序列化与错误处理（moderate）
        supply_point: 节点内补给：JSON Schema 校验模板 + 异常处理骨架
      - name: 协作运行与冲突记录
        knowledge_dependency: A1 编排基础（strong）
        supply_point: 复用 A1 的编排骨架
    prerequisites:
      - node: A1
        strength: strong
        scope: 无编排基础无法构造协作场景
      - node: A2
        strength: moderate
        scope: 只在“冲突消解”环节需要评估视角



  - id: S1
    line: S
    title: RAG 与 LLM 应用评估
    shared: true
    capability_signal: >
      能构建可复现的评估流水线，选择并论证指标，标注失败样本，
      并说明指标选择的理由与局限。
    evidence_requirements:
      - 可复现的评估流水线（检索侧 + 生成侧指标）
      - 失败样本标注
      - 一段“为什么选这个指标而不是另一个”的记录
    stages:
      - name: 评估集与指标选择
        knowledge_dependency: 指标含义理解（moderate）
        supply_point: 节点内补给：Recall@K / NDCG 速查
      - name: 流水线实现
        knowledge_dependency: Python 数据处理（moderate）
        supply_point: 节点内补给：数据清洗与异常处理模板
      - name: 失败分析与指标论证
        knowledge_dependency: 失败归因思维（moderate）
        supply_point: 可复用 A1 的失败记录作为样本来源（见迁移 3）
    prerequisites: []             # 无硬性前置

  - id: S2
    line: S
    title: 实验设计与因果推断
    shared: false
    capability_signal: >
      能设计一个带流量分割和指标选择的实验，跑通统计检验，
      并写出局限性与替代解释。
    evidence_requirements:
      - 实验设计文档（分割方式 + 指标选择理由）
      - 统计检验代码（含置信区间）
      - 局限性与替代解释段落
    stages:
      - name: 实验条件设计
        knowledge_dependency: 因子识别（moderate）
        supply_point: 可参考 A2 的约束变化记录（见迁移 2）
      - name: 统计检验实现
        knowledge_dependency: 基础统计（moderate）
        supply_point: 节点内补给：置信区间计算模板
      - name: 局限性与替代解释
        knowledge_dependency: 批判性写作（light）
        supply_point: null
    prerequisites: []

  - id: S3
    line: S
    title: 面向业务决策的建模与沟通
    shared: false
    capability_signal: >
      能完成从问题定义到模型到决策建议的端到端仓库，
      并明确说明“谁用这个结果、用来做什么决定”。
    evidence_requirements:
      - 端到端建模仓库
      - README 中的决策叙事（使用者 + 决策场景）
    stages:
      - name: 问题定义与建模
        knowledge_dependency: 建模基础（moderate）
        supply_point: null
      - name: 决策阈值与权衡分析      # 新增
        knowledge_dependency: 指标阈值设定与 false positive / false negative 权衡（moderate）
        supply_point: 节点内补给：混淆矩阵与代价敏感阈值选择模板
      - name: 决策叙事撰写
        knowledge_dependency: 因果论证（moderate）
        supply_point: 节点内补给：决策备忘录模板
    prerequisites:
      - node: S2
        strength: moderate
        scope: 只在“决策叙事”环节需要因果思维

























