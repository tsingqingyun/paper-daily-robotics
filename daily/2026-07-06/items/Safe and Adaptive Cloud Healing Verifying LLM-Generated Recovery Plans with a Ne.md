---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.01595v1"
published: "2026-07-02T01:45:30Z"
age_days: 4
score: 24
created: 2026-07-06
concepts: ["智能体 Agent", "世界模型", "机器人学习"]
---

# Safe and Adaptive Cloud Healing: Verifying LLM-Generated Recovery Plans with a Neural-Symbolic World Model

## 为什么重要

自动筛选分数：24

连接概念：[[智能体 Agent]], [[世界模型]], [[机器人学习]]

## 摘要

As the scale and complexity of cloud-based AI systems continue to escalate, ensuring
service reliability through rapid fault detection and adaptive recovery has become a
critical challenge. While existing approaches integrate Large Language Models (LLMs) for
semantic understanding and Deep Reinforcement Learning (DRL) for policy optimization,
they often rely on sequential, loosely coupled architectures that underutilize the
generative and reasoning capabilities of LLMs. In this paper, we propose a paradigm
shift with PASE, a Planning-Aware Semantic self-healing engine, a novel fault self-
healing framework that reconceptualizes recovery as a neuro-symbolic program synthesis
task. PASE employs an LLM as a core Plan Synthesis Engine to generate structured
recovery plans from a library of semantic primitives. A Neural-Symbolic World Model
verifies plan feasibility through simulation, while a Meta-Prompt Optimizer, trained via
DRL, learns to generate optimal prompts that guide the LLM's planning process. This
tight reason-plan-verify-adapt loop enables dynamic, context-aware recovery strategy
generation beyond predefined action spaces. Experiments on a real-world cloud fault
injection dataset demonstrate that PASE significantly outperforms state-of-the-art
methods, reducing average system recovery time by over 40% and improving fault detection
accuracy in unknown fault scenarios. Our framework advances autonomous system management
by unifying LLM-based reasoning with model-assisted verification and meta-learned
guidance.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.01595v1
- Authors: Junyan Tan, Haoran Lin, Siyuan Guo, Yichen Fang, Xinyue Luo, Tianyu Shen, Zeyu Qiao
- Published: 2026-07-02T01:45:30Z
- Age days: 4

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
