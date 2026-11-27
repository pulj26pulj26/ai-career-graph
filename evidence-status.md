# Evidence Status

Version: 0.1
Created: 2026-11-27
Project: AI Career Graph Reliability Lab

## 状态定义

- VERIFIED：已有可复现代码、日志或实验结果。
- IMPLEMENTED：功能已实现，但还缺少完整验证。
- IN_PROGRESS：正在开发，尚不能作为最终成果。
- PLANNED：只有方案或计划。
- KNOWN_GAP：明确没有亲手完成过，不得包装成已有经验。

## 当前能力清单

| 能力 | 状态 | 证据位置 | 简历使用规则 |
|---|---|---|---|
| Dify＋Ollama云边RAG | VERIFIED | docs/evidence/2026-11-27-baseline/ | 验证通过后可写“独立完成技术验证” |
| 混合检索区分度0.01→0.06 | VERIFIED | docs/s1-retrieval-tuning-log.md | 必须保留实验范围，不扩大为产品性能提升 |
| 现有4篇ADR | VERIFIED | docs/adr/ 或现有ADR目录 | 可写“输出4篇ADR” |
| 分层记忆 | PLANNED | 尚无 | 不写进简历 |
| 记忆净增益与消融 | PLANNED | 尚无 | 不写进简历 |
| FastAPI模型服务化 | PLANNED | 尚无 | 不写进简历 |
| 并发压测与成本评估 | PLANNED | 尚无 | 不写进简历 |
| 监控告警与故障注入 | PLANNED | 尚无 | 不写进简历 |
| 发布与回滚 | PLANNED | 尚无 | 不写进简历 |
| 大型高并发生产系统运维 | KNOWN_GAP | 无 | 明确没有亲手做过，不得写成已有经验 |

## 规则

1. 方案不等于完成，Demo不等于生产级。
2. 没有原始证据的能力，不进入简历。
3. 负向结果和失败样本必须保留。
4. 每次状态升级必须附带证据路径和提交哈希。
