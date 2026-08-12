---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12978v1"
published: "2026-06-11T07:12:17Z"
age_days: 1
score: 32
created: 2026-06-13
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# Trajectory-Level Redirection Attacks on Vision-Language-Action Models

## 为什么重要

自动筛选分数：32

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[世界模型]], [[视觉语言动作模型 VLA]]

## 摘要

Vision-language-action (VLA) policies bring natural language into closed-loop robot
control, enabling robots to execute manipulation tasks directly from text instructions.
The same interface gives text a recurring role in control because the prompt is reused
at every replanning step, and each prompt-conditioned action changes the future
observations on which the policy acts. Existing VLA attacks study adversarial prompts
that elicit targeted low-level actions or make such actions persist across changing
images. We identify a stronger trajectory-level failure mode: a prompt that still
$\textit{appears}$ to specify the intended task but redirects the final physical
outcome. We mathematically formalize this setting as $\textit{command-preserving
trajectory redirection}$, a prompt-only threat model in which the attacker chooses one
prompt before the episode, all policy and environment components remain fixed, and the
prompt must stay close to the benign instruction while omitting target words and
correction language. To find such prompts, we introduce an on-policy prompt search
method that uses rollouts to discover perturbations whose closed-loop behavior tracks a
target task while satisfying the command-preserving constraints. Experiments in
simulation and on hardware show that near-benign prompt perturbations can redirect VLA
rollouts to attacker-specified targets. These results expose a trajectory-level
vulnerability in VLA instruction grounding: text that appears to preserve the intended
command can still give an adversary control over the robot's final physical outcome.
Project website: https://vla-redirection-attack.github.io/

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12978v1
- Authors: Gokul Puthumanaillam, Vardhan Dongre, Pranay Thangeda, Hooshang Nayyeri, Dilek Hakkani-Tür, Melkior Ornik
- Published: 2026-06-11T07:12:17Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
