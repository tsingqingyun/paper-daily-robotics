---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12402v1"
published: "2026-06-10T17:58:49Z"
age_days: 1
score: 37
created: 2026-06-12
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# DIRECT: When and Where Should You Allocate Test-Time Compute in Embodied Planners?

## 为什么重要

自动筛选分数：37

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

Vision-Language Models (VLMs) are increasingly deployed as high-level planners for
embodied agents, with an emerging strategy of scaling test-time compute to improve
capability. However, we observe that doing so increases latency, token usage, and FLOPs
while yielding uneven, often diminishing gains in downstream success, limiting where
embodied agents can be deployed. We argue that choosing when and where to spend test-
time compute is central to bringing frontier performance to the real world. We introduce
DIRECT, a routing framework that uses multimodal scene context to allocate compute per
prompt, improving the success--cost Pareto frontier over fixed model selection. Across
three dominant scaling axes, namely chain-of-thought depth, model size, and memory
history, our experiments on VLABench and RoboMME show that test-time compute is not a
uniform lever: different axes yield qualitatively distinct capability gains. We validate
these insights on a physical Franka arm in a DROID setup spanning zero-shot manipulation
and long-horizon chaining, where our router matches or exceeds a stronger model's
success rate at up to 65% lower average latency. Ultimately, our results show that
naively scaling test-time compute is wasteful, and that DIRECT can provide frontier-
level embodied planning in robotic systems at a fraction of the cost. Project page can
be found at jadee-dao.github.io/direct/.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12402v1
- Authors: Jadelynn Dao, Milan Ganai, Yasmina Abukhadra, Ajay Sridhar, Mozhgan Nasr Azadani, Katie Luo, Clark Barrett, Jiajun Wu, Chelsea Finn, Marco Pavone
- Published: 2026-06-10T17:58:49Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
