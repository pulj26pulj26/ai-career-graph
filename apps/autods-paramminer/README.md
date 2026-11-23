# AutoDS-ParamMiner: 汽车音响芯片 Datasheet 参数抽取流水线

## 在线体验与复现

- **[打开 AutoDS-ParamMiner 在线应用](http://111.230.145.223/workflow/Iyo0UvCF8ckFGPTT)**
- [查看 Dify DSL 工作流文件](workflow.yml)

### 在 Dify 中复现

1. 下载本目录的 `workflow.yml`。
2. 在 Dify 工作室中选择“导入 DSL 文件”。
3. 重新配置模型供应商及必要的访问凭据。
4. 发布应用，并上传汽车芯片 Datasheet，输入part_number 运行。

> 在线应用用于演示参数抽取流程，请勿上传包含商业秘密或敏感信息的文档。

## 1. 业务背景与痛点
汽车电子领域的芯片 Datasheet（数据手册）通常长达数十页，充满复杂的双栏排版与表格。传统人工提取关键参数（如输出电压、THD+N、封装等）耗时且易错。

## 2. 系统架构
本工作流基于 Dify 搭建，实现了端到端的参数抽取与质量校验。
（这里放上你提供的那张 Dify 画布全景截图）

**核心处理链路**：
1. **文本抽取与清洗 (Code①)**：剔除 PDF 中的虚线噪声，基于正则匹配提取特定章节（Features, Electrical Specifications 等），避免超长上下文干扰。
2. **LLM 结构化抽取**：采用 Qwen2.5 (Few-shot)，强制输出 JSON。
3. **质量校验与防护 (Code②)**：对 LLM 返回的 JSON 进行强类型转换（如字符串转 float）、区间校验、空值填补，并输出 `status` (success/warn/failed)。
4. **可视化渲染**：将长 JSON 转化为 Markdown 表格，便于业务人员肉眼验收。

## 3. 架构决策与踩坑记录 (核心亮点)
- **为什么用双层代码节点？** 直接在 Prompt 里让 LLM 输出纯净 JSON 极其不稳定。Code① 负责"喂干净的上下文"，Code② 负责"兜底和校验"，实现了逻辑解耦。
- **如何解决大模型幻觉？** 在 Code② 中加入了 16 个 Required 字段的校验，如果缺失超过 12 个，自动降级为 `warn` 并触发人工复核（Human-in-the-loop）。
