---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.15009v1"
published: "2026-08-15T03:39:40Z"
age_days: 2
score: 38
created: 2026-08-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# ForceU-VLA: A Force-Aware Vision-Language-Action Model for Embodied Ultrasound Scanning

> [!summary] 一句话结论（基于摘要）
> Extensive experimental results demonstrate that ForceU-VLA significantly improves contact stability and probe pressure regulation in embodied ultrasound scanning, thereby effectively enhancing task execution quality and overall system reliability.

## 关键点

- **问题**：However, existing methods suffer from loosely coupled modeling between force and ultrasound modalities and lack awareness of scanning stages, which limits their ability to capture dynamic probe-tissue interactions.
- **创新点 / 方法**：To address these issues, we propose ForceU-VLA, a force-aware Vision-Language-Action model for autonomous embodied ultrasound scanning, which leverages force signals and ultrasound image feedback throughout the scanning process to enable accurate and high-quality ultrasound acquisition.
- **证据**：Extensive experimental results demonstrate that ForceU-VLA significantly improves contact stability and probe pressure regulation in embodied ultrasound scanning, thereby effectively enhancing task execution quality and overall system reliability.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-18/ForceU-VLA A Force-Aware Vision-Language-Action Model for Embodied Ultrasound Sc.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied intelligent ultrasound scanning enables the automation and standardization of the ultrasound examination process by integrating perception, decision-making, and execution capabilities. However, existing methods suffer from loosely coupled modeling between force and ultrasound modalities and lack awareness of scanning stages, which limits their ability to capture dynamic probe-tissue interactions. To address these issues, we propose ForceU-VLA, a force-aware Vision-Language-Action model for autonomous embodied ultrasound scanning, which leverages force signals and ultrasound image feedback throughout the scanning process to enable accurate and high-quality ultrasound acquisition. Firstly, we propose a Force-Ultrasound Synergistic Fusion Module (FUSFM) that synergistically fuses ultrasound visual and force-feedback information to provide stable, reliable guidance for probe motion. Secondly, a Stage-Adaptive Modulation Mechanism (SAMM) is proposed to accommodate the task requirements across different scanning stages by adaptively modulating multimodal features to enhance their representation quality. Additionally, we introduce ForceU-VLA-Data, a real-world, force-aware embodied ultrasound dataset that integrates visual, force, and action signals, including data from two organs across five representative clinical scanning views, and comprising 450 expert-collected trajectories with approximately 100,000 synchronized multimodal frames. Extensive experimental results demonstrate that ForceU-VLA significantly improves contact stability and probe pressure regulation in embodied ultrasound scanning, thereby effectively enhancing task execution quality and overall system reliability. The source code is available at https://github.com/VMVLab/ForceU-VLA.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.15009v1
- Authors: Xingzheng Wu, Cheng Zhang, Guihao Yan, Xifeng Hu, Zhi Liu, Qing Cai
- Published: 2026-08-15T03:39:40Z
- Age days: 2

</details>
