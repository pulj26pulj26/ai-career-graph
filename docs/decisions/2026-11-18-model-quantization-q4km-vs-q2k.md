# ADR-002: 模型量化选择 Q4_K_M 而非 Q2_K

**状态**: Accepted
**日期**: 2026-11-18

## 背景
A1/S1 节点需要稳定的结构化输出与工具调用参数生成。7B 模型在
Q2_K（2-bit）下 JSON 易不闭合、工具调用参数格式错乱。

## 决策
使用 Qwen2.5-7B-Instruct 的 Q4_K_M（约 4.7GB），2080Ti 级显存
可稳定加载，工具调用稳定性显著优于 Q2_K。

## 排错记录
- 镜像站无标签回退到 Q2_K（3.0GB）。
- 显式 :Q4_K_M 标签生成 0B 空模型。
- ModelScope 指定文件 404。
- hf.co 直连报 redirect target not allowed（DNS64/NAT64 与
  Ollama 重定向校验冲突）。
- 最终路径：hf-mirror.com 下载 GGUF + ollama create 导入。

## 否决的方案
- Q2_K：精度不足。Q5_K_M/Q6_K：显存与加载时间超限。
