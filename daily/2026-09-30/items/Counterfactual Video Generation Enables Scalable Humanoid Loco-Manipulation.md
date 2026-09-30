---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.38172v1"
published: "2026-09-29T17:59:45Z"
age_days: 0
score: 38
created: 2026-09-30
concepts: ["Sim2Real", "具身智能评测与基准"]
---

# Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation

> [!summary] 先说人话（基于摘要）
> PRISM 用少量真人视频生成大量交互变体，再把这些不完美的视频转成物理合理的训练轨迹。最终人形机器人仅凭机载深度观察，就能对新物体实例执行拿起、搬运和放下。

## 问题

从视频学习人形机器人的移动操作，需要同时看清全身运动和人与物体接触，但这类高质量、多样视频难采集。有限示例难以支撑对不同物体和初始条件的泛化。

## 创新点或方法

通过视频到视频生成，将少量示例扩展成数百段反事实交互视频；以接触为锚点重建人和物体运动，并重定向为物理合理轨迹。利用类别内变化训练单一策略，再直接部署到真实机器人。

## 证据

摘要报告生成数百段视频，并在无真实世界微调条件下完成实机部署。机器人使用机载深度观察，对箱子、桶、收纳容器和球的新实例、尺寸及初始配置执行拿取、搬运和放下；未给出成功率。

## 局限

摘要支持的是类别内未见物体泛化；需核查生成视频中的交互错误如何被识别和修正，以及各类别的实际成功率。

- **判断**：值得精读接触锚定与物理轨迹生成部分，这是从视频多样性走向可执行技能的关键环节。

## 研究关联

对 Sim2Real 和人形机器人学习，价值在于连接生成式数据扩增、接触重建和真实控制，使少量视频有机会覆盖更多交互条件。

- **概念**：[[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Teaching humanoids loco-manipulation skills, such as carrying diverse objects, via visual imitation is a promising path toward generalist robots. However, collecting diverse, high-quality interaction videos, such as clips that clearly show a person's full body and unoccluded interactions with objects, poses a practical barrier to scaling this approach. We propose PRISM, a real-to-sim-to-real framework that overcomes this limitation by amplifying a handful of real videos into a large, diverse training set. PRISM first generates hundreds of diverse "counterfactual" human-object interaction videos via video-to-video (V2V) generation from a few exemplar real videos. Our contact-anchored real-to-sim pipeline then reconstructs both human and object motions, retargeting this imperfect video data into physically plausible trajectories. The intra-class variability across these counterfactual videos lets us train a single policy that generalizes to unseen objects within each category. We demonstrate the full pipeline by deploying this policy on a real robot without any real-world fine-tuning. Using only onboard depth observations, our humanoid picks up, carries, and drops objects, including boxes, barrels, bins, and balls, across novel instances, sizes, and initial configurations.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.38172v1
- Authors: Zihan Wang, Zhen Wu, Pieter Abbeel, Rocky Duan, Jitendra Malik, Carmelo Sferrazza, C. Karen Liu, Guanya Shi, Angjoo Kanazawa
- Published: 2026-09-29T17:59:45Z
- Age days: 0

</details>
