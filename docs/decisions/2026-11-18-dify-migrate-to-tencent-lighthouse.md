# ADR-003: Dify 控制面迁移至腾讯云 Lighthouse

**状态**: Accepted
**日期**: 2026-11-18

## 背景
cloud.dify.ai 在当前网络环境下无法打开；ClawCloud Run 已于
2026-05-11 停止服务。ADR-001 的 Dify 云版路径不再可行。

## 决策
控制面迁移至腾讯云 Lighthouse 预装 Dify 镜像（dify 1.10.1-fix.1，
2核4G，60GB SSD）。数据面（AutoDL Ollama）保持不变，延续
ADR-001 的控制面/数据面分离架构。

## 否决的方案
- AutoDL 源码部署 Dify：控制面与数据面重新耦合，需手动装
  PostgreSQL/Redis/Weaviate，运维成本天级，不符合 3-4 周证据
  生产目标。
- Sealos 一键部署：可行但配置步骤多于腾讯云镜像。

## 后果
控制面小时级可用。需在 Dify 中配置 Ollama provider 指向
AutoDL 公网地址。
