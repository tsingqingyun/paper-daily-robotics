---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.10915v1"
published: "2026-09-10T00:00:32Z"
age_days: 2
score: 38
created: 2026-09-12
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# IMLE-VLA: Fast Single-Step Action Generation for Vision-Language-Action Policies

> [!summary] 先说人话（基于摘要）
> IMLE-VLA把多轮迭代生成动作改成一步生成，减少机器人等待推理的停顿。它用条件隐式最大似然估计保留多种可行动作，避免简单回归头的模式坍缩。

## 问题

扩散或flow-matching动作头需要反复采样，例如π0.5使用10步Euler积分，形成推理瓶颈并拖慢执行。直接改成普通回归又可能损失动作分布的多样性。

## 创新点或方法

保留视觉语言骨干，以cIMLE训练的单步条件生成器替换迭代动作头，输出连续动作；核心差异是用训练目标维持多模态覆盖，执行时不再多步采样。

## 证据

应用于π0.5后推理频率由15 Hz升至55 Hz，动作吞吐量最高提高11倍；LIBERO的40项任务平均成功率98.0%，LIBERO-plus保持原模型鲁棒性。Franka四项真实任务均优于π0.5，jerk降低2.2—3.0倍，每回合累计VLA推理时间降低3.9—6.6倍。


## 局限

需核查频率、吞吐量、累计推理时间与任务完成时间各自的测量口径，不能把这些倍率互换。

- **判断**：值得精读并考虑复现动作头替换，速度收益同时有基准和实机证据支撑。

## 研究关联

直接关联VLA延迟、动作平滑性和任务表现，适合需要实时闭环操作的研究者。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-12/IMLE-VLA Fast Single-Step Action Generation for Vision-Language-Action Policies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) policies leverage pretrained vision-language backbones to achieve strong cross-task generalization. A leading design couples this backbone with a dedicated continuous action head trained via diffusion or flow matching. However, such heads rely on iterative multi-step sampling, for example 10 Euler steps in $π_{0.5}$. This creates an inference bottleneck that produces stop-and-go movement in the robot and slower task completion. We introduce IMLE-VLA, which replaces the iterative action head with a single-step conditional generator trained via conditional Implicit Maximum Likelihood Estimation (cIMLE). The cIMLE objective promotes multimodal action coverage, avoiding the mode collapse of naive regression heads while eliminating multi-step sampling entirely. When IMLE-VLA is applied to $π_{0.5}$, it increases inference frequency 3.67x (55 Hz vs. 15 Hz), enabling up to 11x higher action throughput. On the 40-task LIBERO benchmark, IMLE-VLA achieves the highest average success rate (98.0%) among all baselines while leading in inference frequency. Under the test-time perturbations of LIBERO-plus, IMLE-VLA retains $π_{0.5}$'s robustness while other baselines degrade sharply, confirming that the cIMLE head preserves generalization. Real-world experiments on a Franka Emika Panda across four tasks demonstrate smoother motion (2.2x to 3.0x lower jerk) and faster task completion, with IMLE-VLA outperforming $π_{0.5}$ on every task and reducing average VLA inference time per episode by 3.9x to 6.6x. Videos and code are available at https://kianhk6.github.io/IMLE-VLA/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.10915v1
- Authors: Kian Hosseinkhani, Qinhe Peng, George Shramko, Mehran Aghabozorgi, Jianing Qian, Tristan Engst, Alireza Moazeni, Dinesh Jayaraman, Ke Li
- Published: 2026-09-10T00:00:32Z
- Age days: 2

</details>
