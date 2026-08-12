---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.18953v1"
published: "2026-06-17T11:36:54Z"
age_days: 1
score: 42
created: 2026-06-19
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "Sim2Real", "具身智能评测与基准"]
---

# Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement

> [!summary] 一句话结论（基于摘要）
> Across five manipulation tasks on a real Franka Research 3 (FR3) robot, our method improves the success rate from 42% to 76% zero-shot, and the improved rollouts can be further reused to retrain the base VLA for self-improvement without additional teleoperati…

## 关键点

- **问题**：Vision-Language-Action (VLA) models can generalize across diverse manipulation tasks, but their imitation-learning-based policies remain brittle in precise physical interactions due to compounding execution errors; Can a reinforcement learning policy trained purely in simulation improve the robustness of real-world VL…
- **创新点 / 方法**：We propose an object- centric residual RL framework that refines VLA actions using object poses, enabling a compact observation space that transfers consistently between simulation and reality.
- **证据**：Across five manipulation tasks on a real Franka Research 3 (FR3) robot, our method improves the success rate from 42% to 76% zero-shot, and the improved rollouts can be further reused to retrain the base VLA for self-improvement without additional teleoperation.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：42
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models can generalize across diverse manipulation tasks,
but their imitation-learning-based policies remain brittle in precise physical
interactions due to compounding execution errors; Can a reinforcement learning policy
trained purely in simulation improve the robustness of real-world VLAs zero-shot?
Residual RL, which learns a corrective policy on top of a frozen VLA, offers a natural
framework, but existing approaches face a fundamental sim-to-real dilemma: privileged-
state methods require lossy distillation for deployment; image-based methods suffer from
the visual domain gap; and real-world RL is costly and unsafe. We propose an object-
centric residual RL framework that refines VLA actions using object poses, enabling a
compact observation space that transfers consistently between simulation and reality. To
align the two domains, we additionally replay the same teleoperation demonstrations in
simulation to train a sim counterpart of the real-world VLA. The residual RL policy is
trained only in simulation with pose noise injection and dropout, and transfers zero-
shot to the real robot. Across five manipulation tasks on a real Franka Research 3 (FR3)
robot, our method improves the success rate from 42% to 76% zero-shot, and the improved
rollouts can be further reused to retrain the base VLA for self-improvement without
additional teleoperation. Project page: https://www.microsoft.com/en-
us/research/articles/object-centric-residual-rl/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.18953v1
- Authors: Kinam Kim, Namiko Saito, Heecheol Kim, Katsushi Ikeuchi, Jaegul Choo, Yasuyuki Matsushita
- Published: 2026-06-17T11:36:54Z
- Age days: 1

</details>
