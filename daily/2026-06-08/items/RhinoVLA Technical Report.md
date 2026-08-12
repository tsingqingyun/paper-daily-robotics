---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.07383v1"
published: "2026-06-05T15:21:41Z"
age_days: 2
score: 37
created: 2026-06-08
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# RhinoVLA Technical Report

> [!summary] 一句话结论（基于摘要）
> Experiments show that RhinoVLA achieves downstream performance comparable to π0.5 at a similar parameter scale, while reaching 11.69 Hz end-to-end inference on Huixi R1, meeting the 10 Hz real-time closedloop control target.

## 关键点

- **问题**：Vision-Language-Action (VLA) models have shown strong potential for robotic manipulation, but real-time deployment on edge hardware remains challenging.
- **创新点 / 方法**：Motivated by this observation, we propose RhinoVLA, a deployment-oriented VLA model co-designed with the Huixi R1 edge SoC.
- **证据**：Experiments show that RhinoVLA achieves downstream performance comparable to π0.5 at a similar parameter scale, while reaching 11.69 Hz end-to-end inference on Huixi R1, meeting the 10 Hz real-time closedloop control target.
- **局限**：Vision-Language-Action (VLA) models have shown strong potential for robotic manipulation, but real-time deployment on edge hardware remains challenging.

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：37
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-08/RhinoVLA Technical Report.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models have shown strong potential for robotic
manipulation, but real-time deployment on edge hardware remains challenging. In this
work, we identify VLM visual and context tokens as a major source of deployment latency:
for GEMM-dominated projection operators, computation grows linearly with the number of
input tokens when model dimensions are fixed. Motivated by this observation, we propose
RhinoVLA, a deployment-oriented VLA model co-designed with the Huixi R1 edge SoC.
RhinoVLA adopts a token-efficient Qwen3-VL backbone and a continuous Action Expert,
reducing the VLM-side token and computation burden while preserving pretrained
multimodal capability. To support cross-robot learning, RhinoVLA further introduces a
unified interface that combines View Registry, 72D physical state-action slot space, and
robotinstance LoRA, allowing heterogeneous robot observations and action schemas to be
aligned under a shared policy. On the deployment side, RhinoVLA is optimized through
hardware-aware compilation, mixed-precision execution, and parallel visual encoding.
Experiments show that RhinoVLA achieves downstream performance comparable to π0.5 at a
similar parameter scale, while reaching 11.69 Hz end-to-end inference on Huixi R1,
meeting the 10 Hz real-time closedloop control target. The project will be open-sourced
at https://github.com/HuixiAI/RhinoVLA.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.07383v1
- Authors: Huixi Intelligence, :, Chen Zhang, Chenyang Zhou, Guanglei Ding, Guanghui He, Haibin Gao, Jiajia Chen, Jianyong Zhang, Lianyi Yu, Ningyi Xu, Ping Xu, Qingchen Li, Yingjun Hu, Yijia Zhang, Yuxi Liu
- Published: 2026-06-05T15:21:41Z
- Age days: 2

</details>
