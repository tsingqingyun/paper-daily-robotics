---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14270v1"
published: "2026-06-12T08:51:51Z"
age_days: 3
score: 23
created: 2026-06-16
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Robust Fall Recovery for Armless Bipedal-Wheeled Robots Via Force-Guided Learning

> [!summary] 一句话结论（基于摘要）
> To address this, we introduce FTSR (Force-guided Teacher-student framework with Stage-wise Rewards).

## 关键点

- **问题**：Without arms or other legs to provide supportive assistance, a bipedal-wheeled robot must rely solely on the actuation of its legs, making recovery particularly difficult.
- **创新点 / 方法**：To address this, we introduce FTSR (Force-guided Teacher-student framework with Stage-wise Rewards).
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：23
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-16/Robust Fall Recovery for Armless Bipedal-Wheeled Robots Via Force-Guided Learnin.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Fall recovery is critical for autonomous legged locomotion. Existing methods have
demonstrated that some legged robots, such as humanoids and quadrupeds, are capable of
fall recovery from diverse postures by utilizing arms or coordinating multi-legs to
generate support forces. Without arms or other legs to provide supportive assistance, a
bipedal-wheeled robot must rely solely on the actuation of its legs, making recovery
particularly difficult. To address this, we introduce FTSR (Force-guided Teacher-student
framework with Stage-wise Rewards). The force-guided method constructs an external
auxiliary force during simulation training that correlates directly with the robot's
real-time height, explicitly formulating this force as an optimizable constraint.
Through constrained reinforcement learning, the policy is guided toward reducing force
dependency gradually and increasing the body height, developing internal recovery
strategies despite having no arms for support. Height-progressive stage-Wise rewards
progressively structure posture stabilization during recovery and transition to
sustained locomotion, integrated with teacher-student architecture distilling privileged
knowledge of force effects and recovery dynamics. After simulation training, the policy
is deployed on a physical armless bipedal-wheeled robot and extensively evaluated.
Experiments confirm robust and reliable fall recovery under diverse challenging
conditions, demonstrating strong environmental adaptability and motion robustness, while
maintaining full post-recovery motion capability. The framework also generalizes
effectively to a high-DOF humanoid, confirming its practical generalizability. The
project page is available at https://2350575870.github.io/force-guided.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14270v1
- Authors: Haidong Hou, Zhangguo Yu, Tao Han, Hengbo Qi, Khaleel Ghazal, Yu Zhang, Yidong Du, Xuechao Chen, Fei Meng
- Published: 2026-06-12T08:51:51Z
- Age days: 3

</details>
