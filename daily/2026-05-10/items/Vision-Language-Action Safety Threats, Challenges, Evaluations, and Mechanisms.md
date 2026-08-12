---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - VLA and Robot Foundation Models"
url: "https://arxiv.org/abs/2604.23775v1"
published: "2026-04-26T15:58:19Z"
score: 33
created: 2026-05-10
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms

## 为什么重要

自动筛选分数：33

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-Language-Action (VLA) models are emerging as a unified substrate for embodied
intelligence. This shift raises a new class of safety challenges, stemming from the
embodied nature of VLA systems, including irreversible physical consequences, a
multimodal attack surface across vision, language, and state, real-time latency
constraints on defense, error propagation over long-horizon trajectories, and
vulnerabilities in the data supply chain. Yet the literature remains fragmented across
robotic learning, adversarial machine learning, AI alignment, and autonomous systems
safety. This survey provides a unified and up-to-date overview of safety in Vision-
Language-Action models. We organize the field along two parallel timing axes, attack
timing (training-time vs. inference-time and defense timing (training-time vs.
inference-time, linking each class of threat to the stage at which it can be mitigated.
We first define the scope of VLA safety, distinguishing it from text-only LLM safety and
classical robotic safety, and review the foundations of VLA models, including
architectures, training paradigms, and inference mechanisms. We then examine the
literature through four lenses: Attacks, Defenses, Evaluation, and Deployment. We survey
training-time threats such as data poisoning and backdoors, as well as inference-time
attacks including adversarial patches, cross-modal perturbations, semantic jailbreaks,
and freezing attacks. We review training-time and runtime defenses, analyze existing
benchmarks and metrics, and discuss safety challenges across six deployment domains.
Finally, we highlight key open problems, including certified robustness for embodied
trajectories, physically realizable defenses, safety-aware training, unified runtime
safety architectures, and standardized evaluation.

## 来源

- Source: arXiv Daily - VLA and Robot Foundation Models
- URL: https://arxiv.org/abs/2604.23775v1
- Authors: Qi Li, Bo Yin, Weiqi Huang, Ruhao Liu, Bojun Zou, Runpeng Yu, Jingwen Ye, Weihao Yu, Xinchao Wang
- Published: 2026-04-26T15:58:19Z

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
