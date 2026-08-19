---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.17962v1"
published: "2026-08-18T16:16:23Z"
age_days: 0
score: 36
created: 2026-08-19
concepts: ["多模态基础模型", "机器人学习", "具身智能评测与基准"]
---

# PRISM: Precision and contact-rich Real-world Industrial Skill dataset with Multimodal sensing

> [!summary] 一句话结论（基于摘要）
> However, most existing datasets emphasize short-horizon, low-contact tasks such as pick-and-place, and therefore do not capture the precision control, force/torque or tactile regulation, and multimodal feedback required for industrial assembly.

## 关键点

- **问题**：However, most existing datasets emphasize short-horizon, low-contact tasks such as pick-and-place, and therefore do not capture the precision control, force/torque or tactile regulation, and multimodal feedback required for industrial assembly.
- **创新点 / 方法**：To address this gap, we introduce PRISM, a large-scale multimodal dataset for contact-rich industrial operations.
- **证据**：However, most existing datasets emphasize short-horizon, low-contact tasks such as pick-and-place, and therefore do not capture the precision control, force/torque or tactile regulation, and multimodal feedback required for industrial assembly.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-19/PRISM Precision and contact-rich Real-world Industrial Skill dataset with Multim.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent progress in robotic learning has been fueled by large-scale datasets collected in everyday environments. However, most existing datasets emphasize short-horizon, low-contact tasks such as pick-and-place, and therefore do not capture the precision control, force/torque or tactile regulation, and multimodal feedback required for industrial assembly. To address this gap, we introduce PRISM, a large-scale multimodal dataset for contact-rich industrial operations. The dataset spans more than 25 manipulation tasks (e.g., electronic components plug/unplug, conveyor-based sorting) and covers diverse mechanical constraints. PRISM includes more than 5,000 trajectories totaling 45 hours of teleoperated demonstrations, recorded using synchronized multi-view RGB-D, force/torque, tactile, and robot-state measurements. In contrast to datasets collected in household or laboratory settings, PRISM provides a realistic benchmark for multimodal perception and control under high-precision industrial constraints, and serves as a foundation for contact-rich, generalizable manipulation in real-world manufacturing environments. The dataset is open-sourced at: https://tengbo-yu.github.io/PRISM/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.17962v1
- Authors: Tengbo Yu, Jiahao Wu, Hanning Wang, Rui Chen, Chuanhou Liu, Chuang Sun, Hangxin Liu
- Published: 2026-08-18T16:16:23Z
- Age days: 0

</details>
