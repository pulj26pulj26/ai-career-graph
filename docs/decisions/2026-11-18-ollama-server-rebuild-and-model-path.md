# ADR-004: Ollama 推理服务器重建与模型拉取路径修正

**状态**: Accepted
**日期**: 2026-11-18

## 背景
原 Ollama 服务器到期不可续租。新 AutoDL 实例需重建推理后端。
此前 Q4_K_M 拉取因 DNS64/NAT64 与 Ollama 重定向地址校验冲突
失败（redirect target not allowed）。

## 决策
新实例沿用 OLLAMA_HOST=0.0.0.0:6006、
OLLAMA_MODELS=/root/autodl-tmp/models。模型拉取优先
hf-mirror.com + 手动 GGUF + ollama create，完全绕开 registry
重定向校验。

## 排错记录
- hf: command not found → pip install huggingface_hub。
- cd: gguf 目录不存在 → mkdir -p。
- ollama create 报错 → 查看 ollama.log 定位为 GGUF 缺失/路径错。
- 最终用 wget 从 hf-mirror.com 下载 bartowski 仓库标准
  Q4_K_M 文件后导入成功。

## 风险
此前 ChartQA 微调版模型身份未确认，本轮优先拉标准
Qwen/Qwen2.5-7B-Instruct-GGUF。
