---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.19104v1"
published: "2026-09-16T17:34:43Z"
age_days: 1
score: 39
created: 2026-09-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# rMuscle: Robotic Muscle Memory for Efficient Vision-Language-Action Model Inference

> [!summary] 先说人话（基于摘要）
> rMuscle利用机器人反复执行相似任务时的“计算重复”，缓存视觉输出和内部激活模式，减少VLA推理中的重复计算与权重读取。

## 问题

VLA延迟影响响应速度和运动平滑性。现有推理框架没有充分利用重复作业的相似性，也未区分推理不同阶段的计算与访存瓶颈。

## 创新点或方法

Context Cache复用视觉令牌输出，Action Cache复用神经元激活模式；在线缓存重计算、滑动窗口检索和连续去噪步骤间的掩码共享控制缓存开销。复用依据覆盖跨次执行的内部状态，而不仅是相似图像或动作。

## 证据

在RTX 4090和Jetson Thor上，跨LIBERO、RoboTwin及实体操作任务获得1.29—1.42倍加速；摘要称真实机器人成功率保持不变。

## 局限

方法依赖跨次执行相似性，需核查场景变化时的缓存有效性判断，以及不同任务和硬件的分项收益。

- **判断**：做VLA推理系统值得精读缓存策略；若关注开放环境泛化，先看缓存失效条件与适用范围。

## 研究关联

对VLA部署研究者，尤其是重复工位任务，提供了不必每次重新完成全部计算的系统优化路径。

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-18/rMuscle Robotic Muscle Memory for Efficient Vision-Language-Action Model Inferen.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Factory work is a promising early scenario for embodied AI: assigning repetitive manual jobs to robots has clear economic payoff, and a structured station keeps the jobs tractable for current policies. Vision-Language-Action (VLA) models now dominate as the policy paradigm for these robots. The inference latency of VLA models directly affects robot responsiveness and motion smoothness. However, existing VLA inference frameworks do not fully exploit the characteristics of embodied workloads or account for the distinct bottlenecks across different stages of VLA inference. In this paper, we first characterize embodied workloads and identify substantial task similarity across repeated robot executions. We further find that such similarity extends beyond observations and action trajectories to internal model states. Drawing on these observations, we present rMuscle, a real-time VLA inference framework inspired by human muscle memory. It exploits cross-execution similarity through a dual-phase muscle-memory cache. The Context Cache reuses visual-token outputs to reduce computation, while the Action Cache reuses neuron activation patterns to reduce weight accesses. We keep both the cache memory footprint and access overhead low through online cache recomputation, sliding-window cache retrieval, and mask sharing across consecutive denoising steps. rMuscle achieves 1.29-1.42X speedup on RTX 4090 and Jetson Thor across LIBERO, RoboTwin, and physical manipulation tasks, while maintaining the original success rates on real-world robots.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.19104v1
- Authors: Kaijun Zhou, Zhiyang Li, Le Chen, Jinyu Gu
- Published: 2026-09-16T17:34:43Z
- Age days: 1

</details>
