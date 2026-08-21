---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: false
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.18701v1"
published: "2026-08-19T08:58:47Z"
age_days: 1
score: 27
created: 2026-08-21
concepts: ["多模态基础模型", "机器人学习", "具身智能评测与基准"]
---

# SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformable-Object Manipulation

> [!summary] 一句话结论（基于摘要）
> Building upon this dataset, we establish a closed-loop benchmark that uses fixed object-specific calibration to define the Deformation-aware Success Rate (DSR), which counts a rollout as successful only when it completes the task and keeps peak normalized def…

## 关键点

- **问题**：A primary bottleneck is the absence of visuo-tactile datasets that pair policy-visible contact observations with independent physical ground truth over complete tasks.
- **创新点 / 方法**：We introduce SoftVTBench, a visuo-tactile dataset for physical-interaction-aware deformable-object manipulation.
- **证据**：Building upon this dataset, we establish a closed-loop benchmark that uses fixed object-specific calibration to define the Deformation-aware Success Rate (DSR), which counts a rollout as successful only when it completes the task and keeps peak normalized deformation within tolerance.
- **局限**：These results show that making touch available does not by itself ensure effective multimodal fusion.

## 研究关联

- **概念**：[[多模态基础模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；摘要已提供证据与局限，仍建议按需核对全文
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-21/SoftVTBench A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformab.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Physical interaction quality is central to deformable-object manipulation, yet most benchmarks evaluate task success alone. A policy may complete the task while allowing slip or causing excessive compression. A primary bottleneck is the absence of visuo-tactile datasets that pair policy-visible contact observations with independent physical ground truth over complete tasks. We introduce SoftVTBench, a visuo-tactile dataset for physical-interaction-aware deformable-object manipulation. It contains 4,000 expert demonstrations and more than 50 assets, including volumetric deformable objects and visually matched rigid twins. At 20 Hz, each episode synchronizes multi-view RGB, dual-finger tactile RGB and marker motion, proprioception, language, and binary and continuous gripper actions, alongside evaluator-only finite-element (FEM) states. Building upon this dataset, we establish a closed-loop benchmark that uses fixed object-specific calibration to define the Deformation-aware Success Rate (DSR), which counts a rollout as successful only when it completes the task and keeps peak normalized deformation within tolerance. Across Diffusion Policy, $π_{0.5}$, and FastWAM, all 12 in-distribution configurations contain successful rollouts that violate the deformation tolerance, accounting for 0.7--24% of each configuration's successes. Under distribution shift, visuo-tactile variants achieve higher task success in all six policy--suite comparisons and higher DSR in five, whereas their in-distribution benefits are mixed. These results show that making touch available does not by itself ensure effective multimodal fusion. SoftVTBench therefore provides a common visuo-tactile resource for studying not only whether a policy succeeds, but how it physically interacts with deformable objects and when touch improves that interaction.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.18701v1
- Authors: Bowen Jing, Mingxin Wang, Ruiyang Hao, Chenchen Ge, Hanwen Shen, Junjie He, Yang Cui, Yiming Hou, Weitao Zhou, Jiawei Wang, Minglei Li, Dandan Zhang, Ding Zhao, Houde Liu, Xiaofan Li, Si Liu, Ping Luo, Haibao Yu
- Published: 2026-08-19T08:58:47Z
- Age days: 1

</details>
