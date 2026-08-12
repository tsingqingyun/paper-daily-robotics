---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.12659v1"
published: "2026-07-14T11:38:36Z"
age_days: 2
score: 36
created: 2026-07-17
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference

> [!summary] 一句话结论（基于摘要）
> Extensive experiments demonstrate that Jetson-PI achieves 8.66x and 5.41x improvements in control frequency compared with naive PyTorch and vla.cpp on NVIDIA Jetson Orin, while outperforming VLASH by 14.8\% in average success rate on the LIBERO benchmark.

## 关键点

- **问题**：However, deploying VLA models on low-power onboard devices, such as the Jetson Orin, remains challenging due to their high computational complexity, which leads to substantial inference latency and low control frequency.
- **创新点 / 方法**：In this paper, we propose Jetson-PI, a method for efficient VLA deployment on onboard devices via Foresight-Aligned Asynchronous Correction.
- **证据**：Extensive experiments demonstrate that Jetson-PI achieves 8.66x and 5.41x improvements in control frequency compared with naive PyTorch and vla.cpp on NVIDIA Jetson Orin, while outperforming VLASH by 14.8\% in average success rate on the LIBERO benchmark.
- **局限**：However, deploying VLA models on low-power onboard devices, such as the Jetson Orin, remains challenging due to their high computational complexity, which leads to substantial inference latency and low control frequency.

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-17/Jetson-PI Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchro.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have achieved impressive performance on diverse
embodied tasks. However, deploying VLA models on low-power onboard devices, such as the
Jetson Orin, remains challenging due to their high computational complexity, which leads
to substantial inference latency and low control frequency. Asynchronous inference can
partially mask this latency by parallelizing action execution and subsequent inference,
but it introduces two critical issues: perception-execution misalignment and long
reaction time. In this paper, we propose Jetson-PI, a method for efficient VLA
deployment on onboard devices via Foresight-Aligned Asynchronous Correction. To address
misalignment, we train a lightweight future correction module that predicts future
environment representation conditioned on committed actions, enabling the action expert
to directly predict actions from the future time step. To reduce reaction time, we
introduce confidence-based scheduling optimization that adaptively balances VLM and
action expert invocations, complemented by system-level accelerations including CUDA
graph reuse, GPU-resident intermediate buffering, and flow unrolling. Extensive
experiments demonstrate that Jetson-PI achieves 8.66x and 5.41x improvements in control
frequency compared with naive PyTorch and vla.cpp on NVIDIA Jetson Orin, while
outperforming VLASH by 14.8\% in average success rate on the LIBERO benchmark. The code
of our asynchronous algorithm is available on https://github.com/PKU-SEC-Lab/Jetson-PI,
and our efficient llama.cpp-based inference engine is available on
https://github.com/PKU-SEC-Lab/Jetson-PI-Edge.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.12659v1
- Authors: Zebin Yang, Qi Wang, Yunhe Wang, Xiurui Guo, Bo Yu, Shaoshan Liu, Jiafeng Xu, Hao Dong, Meng Li
- Published: 2026-07-14T11:38:36Z
- Age days: 2

</details>
