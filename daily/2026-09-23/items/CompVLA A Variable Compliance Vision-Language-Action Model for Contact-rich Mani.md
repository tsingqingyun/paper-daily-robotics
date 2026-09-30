---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.23614v1"
published: "2026-09-20T13:03:53Z"
age_days: 2
score: 35
created: 2026-09-23
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# CompVLA: A Variable Compliance Vision-Language-Action Model for Contact-rich Manipulation

> [!summary] 先说人话（基于摘要）
> CompVLA让机器人同时决定怎么移动，以及接触时该有多硬或多柔顺。它用独立的Compliance Expert预测随时间变化的刚度和虚拟位移，再交给阻抗控制执行。

## 问题

接触操作要求机器人适当顺应外力，纯运动学动作命令无法直接表达这种调节，导致现有VLA在真实接触任务上表现下降。

## 创新点或方法

从RGB和语言联合预测运动与刚度矩阵；专门的柔顺性模块输出动态刚度及虚拟位移曲线，通过几何阻抗控制转换为接触行为。

## 证据

摘要报告在多种接触任务上平均成功率高于普通VLA与已有柔顺性VLA，并称消融支持各组件作用；摘要未给出可核查的结果数字。

## 局限

需核查刚度监督来源、矩阵约束及接触稳定性验证；摘要没有任务规模和量化差距。

- **判断**：做阻抗控制与VLA融合可重点读方法，性能优势需等待全文数字支撑。

## 研究关联

对接触型VLA，提供了把柔顺性作为策略输出直接学习的方案，有助于研究视觉和任务语义如何影响物理交互。

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/CompVLA A Variable Compliance Vision-Language-Action Model for Contact-rich Mani.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Contact-rich manipulation, requiring robots to regulate not only motion but also how they yield to external forces, has emerged as the next frontier for Vision-Language-Action (VLA) models. However, existing VLAs output purely kinematic commands, degrading performance on real-world contact-rich tasks. In this paper, we introduce CompVLA, a unified VLA framework that jointly predicts motion and stiffness matrix from RGB and language inputs. Our approach augments the conventional architecture with a dedicated Compliance Expert, which outputs time-varying stiffness and virtual displacement profiles executed via geometric impedance control. We demonstrate that CompVLA achieves the highest average success rate across diverse contact-rich tasks, outperforming both vanilla and compliance-aware VLA baselines, with ablations confirming each component is essential.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.23614v1
- Authors: Jongmin Kim, Junsu Ha, Che-Sang Park, Minchang Song, Hyeokju Jeong, Himchan Hwang, Jianlong Fu, Frank C. Park
- Published: 2026-09-20T13:03:53Z
- Age days: 2

</details>
