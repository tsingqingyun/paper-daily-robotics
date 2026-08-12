---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2605.13382v1"
published: "2026-05-13T11:37:51Z"
age_days: 0
score: 35
created: 2026-05-14
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# BlockVLA: Accelerating Autoregressive VLA via Block Diffusion Finetuning

> [!summary] 一句话结论（基于摘要）
> Experimental results demonstrate that our BlockVLA achieves a 3.3$\times$ inference acceleration over standard discrete diffusion baselines.

## 关键点

- **问题**：Discrete Diffusion Language Models (dLLMs) provide a promising alternative through parallel token refinement, but their practical deployment in robotics remains limited by repeated denoising function evaluations (NFEs) and the difficulty of directly applying standard KV caching to bidirectional iterative decoding.
- **创新点 / 方法**：To bridge these paradigms, we propose BlockVLA, a framework that adapts pretrained AR backbones into an efficient discrete diffusion policy through a block diffusion paradigm.
- **证据**：Experimental results demonstrate that our BlockVLA achieves a 3.3$\times$ inference acceleration over standard discrete diffusion baselines.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-14/BlockVLA Accelerating Autoregressive VLA via Block Diffusion Finetuning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

While autoregressive (AR) Vision-Language-Action (VLA) models have demonstrated
formidable reasoning capabilities in robotic tasks, their sequential decoding process
often incurs high inference latency and may amplify error accumulation during long-
horizon execution. Discrete Diffusion Language Models (dLLMs) provide a promising
alternative through parallel token refinement, but their practical deployment in
robotics remains limited by repeated denoising function evaluations (NFEs) and the
difficulty of directly applying standard KV caching to bidirectional iterative decoding.
To bridge these paradigms, we propose BlockVLA, a framework that adapts pretrained AR
backbones into an efficient discrete diffusion policy through a block diffusion
paradigm. BlockVLA maintains autoregressive dependencies at the block level while
enabling parallel denoising within each block, thereby combining global causal coherence
with local parallel generation. This design enables prefix KV-cache reuse across
completed blocks, reduces the effective cost of iterative denoising, and provides a
smoother transition from AR pretraining to diffusion-based policy fine-tuning. We
conduct extensive evaluations on the LIBERO and SimplerEnv benchmarks. Experimental
results demonstrate that our BlockVLA achieves a 3.3$\times$ inference acceleration over
standard discrete diffusion baselines. Furthermore, our model exhibits superior training
efficiency, with success rates converging substantially faster than baselines, a gain
that is particularly pronounced in complex, long-horizon tasks, where BlockVLA achieves
significant performance gains in the early stages of training. This work establishes
Block Diffusion as a robust bridge between large-scale pretrained AR models and
efficient, high-frequency real-time robotic control.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.13382v1
- Authors: Ruiheng Wang, Shuanghao Bai, Haoran Zhang, Badong Chen, Xiangyu Xu
- Published: 2026-05-13T11:37:51Z
- Age days: 0

</details>
