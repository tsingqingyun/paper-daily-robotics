---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.16074v1"
published: "2026-08-17T04:12:21Z"
age_days: 0
score: 41
created: 2026-08-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# US-VLA: An Ultrasound Vision-Language-Action Model for Embodied Abdomina

> [!summary] 一句话结论（基于摘要）
> Extensive experiments demonstrate that US-VLA achieves competitive performance in ultrasound probe manipulation tasks, indicating its effectiveness and promising generalization within the evaluated abdominal ultrasound setting.

## 关键点

- **问题**：However, existing reinforcement learning and learning-assisted ultrasound scanning methods typically rely on carefully designed reward functions or extensive interaction data, which limits their generalization ability and stability across different devices, patient populations, and complex clinical scenarios.
- **创新点 / 方法**：To address these challenges, we propose an ultrasound vision-language-action model (US-VLA) for automated ultrasound scanning that explicitly encodes clinical semantic goals and generates sequential probe manipulation actions under real-time ultrasound feedback.
- **证据**：Extensive experiments demonstrate that US-VLA achieves competitive performance in ultrasound probe manipulation tasks, indicating its effectiveness and promising generalization within the evaluated abdominal ultrasound setting.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- **筛选分数**：41
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-18/US-VLA An Ultrasound Vision-Language-Action Model for Embodied Abdomina.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Artificial intelligence-assisted ultrasound scanning enhances diagnostic reliability and efficiency by providing real-time guidance for standardized image acquisition and reducing operator dependence. However, existing reinforcement learning and learning-assisted ultrasound scanning methods typically rely on carefully designed reward functions or extensive interaction data, which limits their generalization ability and stability across different devices, patient populations, and complex clinical scenarios. To address these challenges, we propose an ultrasound vision-language-action model (US-VLA) for automated ultrasound scanning that explicitly encodes clinical semantic goals and generates sequential probe manipulation actions under real-time ultrasound feedback. In particular, we first design an ultrasound-aware expert fusion module to jointly integrate ultrasound observations with auxiliary contextual information, enabling semantic ultrasound feedback to effectively guide the scanning process. Then, we construct US-VLA-Data, a real-world dataset covering liver and kidney examinations, which includes five clinically defined standard planes and comprises 320 expert scanning trajectories with approximately 80,000 synchronized timesteps. Extensive experiments demonstrate that US-VLA achieves competitive performance in ultrasound probe manipulation tasks, indicating its effectiveness and promising generalization within the evaluated abdominal ultrasound setting. The source code is available at https://github.com/VMVLab/US-VLA.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.16074v1
- Authors: Cheng Zhang, Xingzheng Wu, Guihao Yan, Xifeng Hu, Zhi Liu, Mei Wu, Qing Cai
- Published: 2026-08-17T04:12:21Z
- Age days: 0

</details>
