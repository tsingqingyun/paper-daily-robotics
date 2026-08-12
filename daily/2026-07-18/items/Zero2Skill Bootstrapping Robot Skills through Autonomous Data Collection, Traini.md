---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14047v2"
published: "2026-07-15T17:16:24Z"
age_days: 2
score: 28
created: 2026-07-18
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习"]
---

# Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment

## 为什么重要

自动筛选分数：28

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[机器人学习]]

## 摘要

Autonomous data collection governs the volume and quality of real-world trajectories for
manipulation policy learning. Existing pipelines reduce human effort via self-resetting,
VLM verification, or language-guided correction, yet episode-scoped fixes must be
reissued whenever the same failure recurs, so oversight cost grows with session length
rather than with the number of distinct problems. We present Zero2Skill, a human-robot
symbiotic agentic system in which corrections are retained and reused across rounds. The
collection loop collects, verifies, and resets autonomously, pausing for a remote
operator only when a phase exhausts an explicit retry budget. An LLM parser maps each
natural-language utterance to a structured adjustment stored in Corrective Memory, so
addressed failure modes typically need not be corrected again under the same conditions.
On a real-robot desktop-clearing testbed, Zero2Skill matches teleoperation episode
success while reducing human working time to 16%. Language corrections improve verifier-
human agreement in all four evaluated settings and raise average single-attempt success
from 12.5% to 47.5% (arm-selection: 20.0% to 50.0%). Policies fine-tuned on Zero2Skill
data match teleoperation-trained policy success at a fraction of collection human cost.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14047v2
- Authors: Boyuan Wang, Zhenyuan Zhang, Zhiqin Yang, Peijun Gu, Shuya Wang, Xiaofeng Wang, Xianghui Ze, Yifan Chang, Guosheng Zhao, Jiangnan Shao, Guan Huang, Hengyu Liu, Yonggang Zhang, Wei Xue, Chunyuan Guan, Chenglin Pu, Yike Guo, Xingang Wang, Zheng Zhu
- Published: 2026-07-15T17:16:24Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
