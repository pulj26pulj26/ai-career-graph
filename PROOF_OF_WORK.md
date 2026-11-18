# Proof of Work — AI 岗位图谱 MVP

本档案中的能力声称均对应仓库中可追溯的 commit 或 ADR。

## 技能矩阵

| 能力维度 | 证据工件 | 位置 |
|---|---|---|
| 图谱设计与校验 | 6 节点 YAML + 校验脚本 | graph/ + scripts/validate.py |
| 部署架构决策 | ADR-001 / ADR-003 | docs/decisions/ |
| 模型量化判断与排错 | ADR-002 / ADR-004 | docs/decisions/ |
| Agent 编排 | 待 A1 产出 | A1-agent-orchestration/ |
| RAG 评估 | 待 S1 产出 | S1-rag-evaluation/ |

## 关键决策时间线

- 2026-11-18：图谱 MVP 定义完成（6 节点、4 迁移边、A2/S1 共享）。
- 2026-11-18：识别 AutoDL 不支持 docker-in-docker，Dify 云版 +
  AutoDL Ollama 拆分（ADR-001）。
- 2026-11-18：Q2_K→Q4_K_M 切换，hf.co 重定向失败，转 hf-mirror
  + ollama create（ADR-002）。
- 2026-11-18：Dify 云版不可用，控制面迁移至腾讯云 Lighthouse
  （ADR-003）。
- 2026-11-18：Ollama 服务器重建，模型拉取路径修正（ADR-004）。

## 方法论

- 决策记录：否决了重要替代方案的决定写 ADR。
- Commit 规范：三段式（what / why / how）。
- 证据边界：技能矩阵每行必须指向可验证工件。
