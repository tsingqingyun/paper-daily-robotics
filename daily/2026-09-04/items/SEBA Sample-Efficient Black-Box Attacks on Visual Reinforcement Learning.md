---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2511.09681"
published: "Thu, 03 Sep 2026 00:00:00 -0400"
age_days: 0
score: 38
created: 2026-09-04
concepts: ["智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# SEBA: Sample-Efficient Black-Box Attacks on Visual Reinforcement Learning

> [!summary] 先说人话（基于摘要）
> SEBA面向图像输入、连续控制的视觉强化学习黑盒攻击，用影子Q模型估计攻击后的累计回报、GAN生成近乎不可见扰动，并用世界模型减少真实环境查询。

## 这篇到底在做什么

- **卡在哪里**：现有黑盒攻击主要针对向量观测或离散动作RL，在图像连续控制中会遭遇大动作空间和高查询成本，因而攻击效果和样本效率不足。
- **关键解法**：输入是智能体视觉观测，输出是对图像的对抗扰动；影子Q模型评估扰动下的长期回报，生成器据此优化攻击，世界模型模拟动力学以替代部分环境交互。两阶段迭代在学习影子模型与改进生成器之间交替。
- **拿什么证明**：MuJoCo和Atari实验显示，SEBA能显著降低累计回报、保持视觉保真度，并较既有黑盒和白盒方法大幅减少环境交互。摘要未给出可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：对机器人学习和具身评测研究者，它给出视觉策略安全性与查询受限攻击的测试工具；对世界模型研究者，则展示了模型不仅能规划，也能作为降低真实系统试探成本的攻击代理。
- **先别急着信**：摘要未量化攻击幅度、查询节省或视觉不可察觉性，也没有说明仿真攻击与真实机器人风险之间的对应程度。
- **判断**：做视觉策略鲁棒性或红队评测者值得精读；若关注一般世界模型，应重点读查询替代机制，不能从摘要判断现实攻击能力。

## 研究关联

- **概念**：[[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-04/SEBA Sample-Efficient Black-Box Attacks on Visual Reinforcement Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2511.09681v3 Announce Type: replace-cross Abstract: Visual reinforcement learning has achieved remarkable progress in visual control and robotics, but its vulnerability to adversarial perturbations remains underexplored. Most existing black-box attacks focus on vector-based or discrete-action RL, and their effectiveness on image-based continuous control is limited by the large action space and excessive environment queries. We propose SEBA, a sample-efficient framework for black-box adversarial attacks on visual RL agents. SEBA integrates a shadow Q model that estimates cumulative rewards under adversarial conditions, a generative adversarial network that produces visually imperceptible perturbations, and a world model that simulates environment dynamics to reduce real-world queries. Through a two-stage iterative training procedure that alternates between learning the shadow model and refining the generator, SEBA achieves strong attack performance while maintaining efficiency. Experiments on MuJoCo and Atari benchmarks show that SEBA significantly reduces cumulative rewards, preserves visual fidelity, and greatly decreases environment interactions compared to prior black-box and white-box methods. The code is available at https://github.com/tairanhuang/seba online.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2511.09681
- Authors: Tairan Huang, Yulin Jin, Junxu Liu, Qingqing Ye, Haibo Hu
- Published: Thu, 03 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
