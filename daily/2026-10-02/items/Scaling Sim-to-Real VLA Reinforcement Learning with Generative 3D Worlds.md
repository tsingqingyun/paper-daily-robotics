---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2603.18532"
published: "Thu, 01 Oct 2026 00:00:00 -0400"
age_days: 0
score: 37
created: 2026-10-02
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "Sim2Real"]
---

# Scaling Sim-to-Real VLA Reinforcement Learning with Generative 3D Worlds

> [!summary] 这篇论文到底做了什么（基于摘要）
> 《Scaling Sim-to-Real VLA Reinforcement Learning with Generative 3D Worlds》用生成式三维世界模型和语言场景设计器，批量建造可交互场景来训练 VLA。它把扩大训练覆盖面的工作转向场景生成，再结合域随机化将仿真训练所得迁移到真机。

## 问题

任务是用强化学习改进预训练 VLA，同时保留跨场景能力。真机训练能避开仿真与现实的差异，却难以低成本更换大量物体和背景，容易把广泛预训练的模型练成场景专用策略；仿真可扩展，但人工建场景也昂贵。

### 用一个例子理解

理解用例（非论文实验）：输入“在不同厨房台面上把杯子放到托盘”的场景描述；生成器产出不同物体和背景的交互环境，策略在其中试错并接受随机化训练；最后输入真实台面画面，输出放杯动作。

## 创新点或方法

本文将人工逐个设计场景改为用三维生成模型配合语言驱动的设计器，构造一百个含不同物体和背景的可交互场景。从模仿学习策略出发，在这些场景中并行进行强化学习微调，并结合域随机化支持迁移。训练阶段利用生成环境反复交互；真机推理阶段执行训练后的策略，摘要没有说需要在线生成三维世界。奖励、强化学习算法和随机化参数未说明。

### 方法如何工作

1. 用语言驱动设计器组织场景需求，为批量生成提供任务相关条件。
2. 生成多样的三维交互场景，让策略能实际试动作并获得反馈。
3. 从模仿策略出发并行强化学习，使策略在多种场景中调整行为。
4. 结合域随机化进行训练并在真机测试，检查仿真所得能力能否迁移；随机化细节摘要只说明到此。

### 必要术语

- Sim-to-Real：将仿真训练所得能力迁移到真实机器人；本文用真机成功率检验。
- 域随机化：训练时改变环境属性，减少对单一条件的依赖；本文用它辅助迁移，具体属性未说明。
- 零样本泛化：无需在新测试条件下继续训练就完成任务；本文用它衡量增加场景多样性的作用。

## 证据

摘要报告，相对预训练模仿基线，仿真成功率从9.7%升至最高79.8%，完成任务速度达到1.25倍；真机成功率从21.7%升至75%，速度达到1.13倍。场景多样性消融显示，增加多样性改善零样本泛化。摘要未给具体任务、真机测试次数、未见场景划分或误差范围；这些数字支持所测条件下的迁移收益，不能直接外推到任意操作任务。

## 局限

整体提升同时包含强化学习、生成场景和域随机化的作用，不能全部归因于生成模型。多样性消融更贴近这一归因问题，但需核查是否控制训练样本数与计算量。所谓数据近乎无限描述的是生成潜力，不保证接触物理正确，也不保证每个新场景都提供有效变化。

- **判断**：值得细读场景生成和多样性消融，尤其核查交互物理与未见场景测试；这决定它能否成为可复用的训练方法。

## 研究关联

值得借鉴的是在强化学习前先扩展可交互环境的分布。对已有较广知识的策略，训练只覆盖一个场景，可能限制微调后的适用范围；生成场景提供了一种降低扩展成本的办法。

### 下一步读哪里

核查生成物体如何获得碰撞、质量和摩擦等交互属性，失败场景如何筛除；再查看多样性消融是否固定总交互量，以及真机物体和背景是否与训练分布充分区分。速度收益还需确认只统计成功任务还是全部尝试。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 Sim2Real
- **筛选分数**：37
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-02/Scaling Sim-to-Real VLA Reinforcement Learning with Generative 3D Worlds.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2603.18532v4 Announce Type: replace Abstract: The strong performance of large vision-language models (VLMs) trained with reinforcement learning (RL) has motivated similar approaches for fine-tuning vision-language-action (VLA) models in robotics. Many recent works fine-tune VLAs directly in the real world to avoid addressing the sim-to-real gap. While real-world RL circumvents sim-to-real issues, it inherently limits the generality of the resulting VLA, as scaling scene and object diversity in the physical world is prohibitively difficult. This leads to the paradoxical outcome of transforming a broadly pretrained model into an overfitted, scene-specific policy. Training in simulation can instead provide access to diverse scenes, but designing those scenes is also costly. In this work, we show that VLAs can be RL fine-tuned across broad scene and object distributions and with reduced labor by leveraging 3D world generative models. Using these models together with a language-driven scene designer, we generate 100 diverse interactive scenes containing unique objects and backgrounds, enabling scalable and highly parallel policy learning. Starting from a pretrained imitation baseline, our approach increases simulation success from 9.7% up to 79.8% while achieving a 1.25$\times$ speedup in task completion time. We further demonstrate successful sim-to-real transfer enabled by the quality of the generated scenes together with domain randomization, improving real-world success from 21.7% to 75% and achieving a 1.13$\times$ speedup. Finally, we further highlight the benefits of leveraging the effectively unlimited data from 3D world generative models through an ablation study showing that increasing scene diversity directly improves zero-shot generalization.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2603.18532
- Authors: Andrew Choi, Xinjie Wang, Zhizhong Su, Wei Xu
- Published: Thu, 01 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
