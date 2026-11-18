# ADR-001: Dify 云端 + AutoDL Ollama 推理架构

**状态**: Superseded by ADR-003
**日期**: 2026-11-18

## 背景
无本地 GPU/电脑，开发在 AutoDL。AutoDL 不支持 docker-in-docker，
Dify 无法在实例内部署。裸金属整机包月成本不现实。

## 决策
Dify 云版（cloud.dify.ai）承担编排，AutoDL 仅跑 Ollama 推理，
监听 0.0.0.0:6006，模型存 /root/autodl-tmp/models。

## 否决的方案
- AutoDL 内嵌 Docker 部署 Dify：平台限制。
- 裸金属：成本不现实。
- 纯 Python 替代 Dify：丢失可视化编排证据。

## 后果
控制面/数据面分离，接近企业实际部署。Dify 云版有额度限制。
