---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.06830v1"
published: "2026-08-07T05:39:27Z"
age_days: 3
score: 25
created: 2026-08-10
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# When Coordination Becomes a Threat: Communication Attacks in LLM-Controlled Multi-Robot Systems

## 为什么重要

自动筛选分数：25

连接概念：[[智能体 Agent]], [[具身智能评测与基准]]

## 摘要

Large Language Models (LLMs) are increasingly used as high-level planners in embodied
multi-robot systems, enabling robots to interpret natural language instructions and
coordinate executable actions. Yet, this growing reliance on LLM planners also raises
security concerns. Prior work has focused mainly on individual robots, while
communication risks in multi-robot collaboration remain insufficiently understood.
Existing multi-robot studies are further limited to preliminary analysis under the
Decentralized Multi-agent System (DMAS) architecture, so it remains unclear whether
these risks persist across other common communication architectures and how attacker
access settings shape their propagation. To fill this gap, we formulate two
communication attacks corresponding to distinct attacker access settings: the External
Entry Point Attack and the Privileged In-System Attack. We evaluate both attacks across
DMAS, HMAS-1, and HMAS-2 using three LLMs and five embodied multi-robot tasks. Results
show that unsafe information can turn into unsafe actions across all three
architectures: DMAS reaches a 96.7\% entry endorsement rate and a 100\% post endorsement
activation rate, HMAS-1 reaches a 97.8\% unsafe action success rate, and HMAS-2 triggers
88.3\% of task defined unsafe action slots. To mitigate risks from trusted information
flow, we introduce the Claim Provenance and Verification (CPV) Gate, which verifies
communicated claims before downstream reuse and reduces the violation rate from 70.0\%
to 36.6\%.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.06830v1
- Authors: Zhen Huang, Zhihuang Liu, Weijia Shi, Yifan Yang, Weishang Wu, Zhiping Cai
- Published: 2026-08-07T05:39:27Z
- Age days: 3

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
