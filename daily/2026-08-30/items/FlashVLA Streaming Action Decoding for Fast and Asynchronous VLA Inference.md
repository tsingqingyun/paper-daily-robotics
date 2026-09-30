---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.27384v1"
published: "2026-08-27T17:19:29Z"
age_days: 2
score: 36
created: 2026-08-30
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# FlashVLA: Streaming Action Decoding for Fast and Asynchronous VLA Inference

> [!summary] 先说人话（基于摘要）
> FlashVLA让流匹配 VLA 边生成边执行：维护处于不同噪声级的动作块缓冲区，用分块因果注意力每步产出一个可执行动作块。

## 这篇到底在做什么

- **卡在哪里**：流匹配 VLA 解码需要多轮迭代，推理慢；异步执行虽减少等待，却容易造成动作不连续。已有方法往往只能改善吞吐或异步稳定性中的一项。
- **关键解法**：输入 VLM 上下文和多噪声级动作块，持续输出执行块。流式缓冲区配合 chunk-wise causal attention 逐步去噪，分块自回归关系隐式约束动作连续性；不同于完整解码一段动作后再执行，也不需要额外未来状态条件。
- **拿什么证明**：摘要称模拟和真实实验中显著提速并维持较强任务表现；单 GPU 可达到至少 30Hz，真实部署支持平滑异步推理。其余成功率和延迟数字未给出。

## 值不值得读

- **和你的研究有什么关系**：对 VLA 落地者，这是直接针对控制频率和执行空转的系统机制，可能比继续缩小视觉语言骨干更能改善真实机器人闭环体验。
- **先别急着信**：需全文核查 30Hz 所对应的 GPU、动作块长度、模型规模及端到端延迟，并确认异步连续性是否会牺牲快速纠错。
- **判断**：做实时流匹配 VLA 的研究者应精读；其他读者至少看清流式缓冲与因果分块设计。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-30/FlashVLA Streaming Action Decoding for Fast and Asynchronous VLA Inference.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models are increasingly promising for robotic manipulation, yet their real-world deployment remains bottlenecked by high inference latency and unstable asynchronous execution. This challenge is particularly pronounced in flow-matching-based VLA models, where action decoding requires multiple iterative steps conditioned on the VLM context. While efficient inference methods improve control frequency and asynchronous methods reduce execution idle time, existing approaches often fail to jointly achieve low-latency inference and accurate, temporally consistent asynchronous execution. We introduce \textbf{FlashVLA}, a streaming action decoding framework that addresses both challenges in a unified formulation. FlashVLA maintains a streaming action buffer with multiple chunks at different noise levels and decodes them using chunk-wise causal attention. This design allows FlashVLA to produce one executable action chunk per inference step. Moreover, its chunk-wise autoregressive formulation implicitly preserves action continuity, enabling smooth asynchronous execution without extra future-state conditioning. Across extensive simulated and real-world experiments, FlashVLA substantially improves inference speed while maintaining strong task performance. It can achieve $\geq$30\,Hz control frequency on a single GPU with smooth asynchronous inference in real-world deployment.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.27384v1
- Authors: Zekai Li, Jiaming Tang, Zhijian Liu
- Published: 2026-08-27T17:19:29Z
- Age days: 2

</details>
