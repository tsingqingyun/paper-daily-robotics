---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2602.05765"
published: "Mon, 07 Sep 2026 00:00:00 -0400"
age_days: 0
score: 33
created: 2026-09-08
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# RL-VLA$^3$: A Flexible and Asynchronous Reinforcement Learning Framework for VLA Training

> [!summary] 先说人话（基于摘要）
> RL-VLA³ 让仿真、模型推理和训练异步推进，减少彼此等待。它解决的是 VLA 强化学习流水线效率问题。

## 问题

同步框架把完整轨迹当作不可拆分单元，并交替采样与优化；物理仿真的高延迟和耗时波动使这种组织方式产生等待。

## 创新点或方法

通过动态批处理调度和灵活环境分片，在仿真、推理、训练组件之间实现细粒度异步交互，替代严格同步的完整 rollout 流程。

## 证据

跨多种仿真后端、VLA 架构和 RL 算法测试，吞吐比同步基线最高提高 85.2%，样本效率保持一致；扩展性验证覆盖 8—256 张 GPU。


## 局限

需核查异步数据滞后如何处理，以及不同配置下的实际增益；最高吞吐收益不代表所有部署规模。

- **判断**：大规模训练团队值得精读系统与扩展实验，小规模实验者可先核查最低配置收益。

## 研究关联

对大规模 VLA 后训练和具身 Agent 基础设施有直接价值，能提高已有学习算法的资源利用效率。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-08/RL-VLA$ 3$ A Flexible and Asynchronous Reinforcement Learning Framework for VLA.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2602.05765v3 Announce Type: replace Abstract: Reinforcement learning (RL) has emerged as a critical paradigm for post-training Vision-Language-Action (VLA) models, enabling embodied agents to adapt and improve through environmental interaction. However, existing RL frameworks for VLAs inherit synchronous design principles from traditional LLM training, treating entire rollouts as indivisible units and alternating strictly between data collection and policy optimization. This fundamentally mismatches the unique characteristics of VLA training, as physical simulators introduce highly variable, resource-intensive latencies. To address this, we introduce RL-VLA$^3$, a fully asynchronous distributed RL framework that enables fine-grained asynchronous interaction between simulation, inference, and training components through dynamic batching schedulers and flexible environment sharding strategies. Extensive experiments across diverse simulation backends, VLA architectures, and RL algorithms demonstrate that RL-VLA$^3$ achieves throughput improvements of up to 85.2\% over synchronous baselines while maintaining identical sample efficiency, with scalability validated from 8 to 256 GPUs. To our knowledge, RL-VLA$^3$ is the first fully asynchronous RL training framework tailored specifically for the system-level challenges of VLA training.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2602.05765
- Authors: Haoran Sun, Yongjian Guo, Zhong Guan, Shuai Di, Xiaodong Bai, Jing Long, Tianyun Zhao, Mingxi Luo, Hongke Zhao, Likang Wu, Xiaotie Deng, Xu Chu, Xi Xiao, Sheng Wen, Yicheng Gong, Junwu Xiong
- Published: Mon, 07 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
