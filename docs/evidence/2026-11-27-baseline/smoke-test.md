# Baseline Smoke Test

Date: 2026-11-27
Purpose: 冻结 Reliability Lab 开发前的可运行RAG基线。

## Runtime

- Control plane: 腾讯云 Lighthouse / Dify
- Data plane: AutoDL / Ollama
- LLM: Qwen2.5-7B-Instruct（记录实际量化版本）
- Embedding: bge-m3

## Verification

| Test | Expected | Actual | Pass? | Evidence |
|---|---|---|---|---|
| 普通语义问题 | 正常召回并回答 | 待填写 | 待填写 | 待填写 |
| 硬标识符问题 | 目标标识符可区分 | 待填写 | 待填写 | 待填写 |
| 无答案问题 | 不编造答案 | 待填写 | 待填写 | 待填写 |

## Current Known Issues

- 待填写；没有则写“无”。

## Conclusion

- [ ] 当前版本可以运行。
- [ ] 当前配置与依赖已保存。
- [ ] 当前实验结果已保存。
- [ ] 该版本可以作为后续记忆与可靠性实验的基线。
