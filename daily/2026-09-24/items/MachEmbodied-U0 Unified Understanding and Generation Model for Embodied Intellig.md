---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.25627v1"
published: "2026-09-22T03:36:36Z"
age_days: 1
score: 43
created: 2026-09-24
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# MachEmbodied-U0: Unified Understanding and Generation Model for Embodied Intelligence

> [!summary] 先说人话（基于摘要）
> MachEmbodied-U0（ME-U0）尝试让机器人同时理解下一步要做什么、在哪里操作、场景将怎样变化，并据此生成动作。它用 Mixture-of-Transformers 连接理解与生成专家，把语义定位和视觉动力学一起纳入控制。

## 问题

通用操作需要任务语义、交互位置、场景变化和精细动作协同。摘要指出，VLA 通常缺少显式动力学建模，而世界动作模型虽然预测视觉变化，却未必显式提供操作所需的语义与空间结构。

## 创新点或方法

子任务预测和可供性定位引导基于 flow matching 的视觉动力学与动作联合生成；未来视觉监督包括 RGB、深度、表面法线和光流。MRPE 用于对齐视觉动力学与更细粒度的控制时间尺度。

## 证据

预训练使用约 4,200 小时机器人与第一视角示范。RoboDojo 平均分为 17.66，LIBERO 和 LIBERO-Plus 平均成功率分别为 99.0% 和 82.5%；另报告真实操作验证及无对应下游监督的子任务、可供性和视觉动力学零样本能力。

## 局限

摘要无法拆分多种视觉监督、模型结构和预训练规模各自带来的收益，也未给出真实操作的量化结果。

- **判断**：值得深入阅读架构与训练目标，尤其关注理解和动力学能力如何实际改善控制，而不只看 LIBERO 分数。

## 研究关联

对世界模型与 VLA 研究者，它提供了将任务理解、几何运动预测和动作学习放进同一模型的具体架构，并展示这些中间能力可以单独迁移。

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：43
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/MachEmbodied-U0 Unified Understanding and Generation Model for Embodied Intellig.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

General-purpose robot control requires models to understand task intent, identify where to interact, capture how the scene evolves, and generate precise actions. Vision-language-action models provide strong semantic priors but typically do not explicitly model scene dynamics, while world-action models couple visual prediction with control without necessarily exposing the task-relevant semantic and spatial structure needed for fine-grained manipulation. We present MachEmbodied-U0 (ME-U0), a unified embodied foundation model connecting understanding and generation experts through a Mixture-of-Transformers architecture. Subtask prediction and affordance grounding guide joint visual-dynamics and action generation via flow matching. Visual dynamics encompass future RGB, depth, surface normals, and optical flow, providing complementary supervision for appearance, geometry, and motion. Multi-rate Rotary Position Encoding (MRPE) aligns visual dynamics with fine-grained control. We pretrain ME-U0 on approximately 4,200 hours of curated demonstrations from robotic datasets and egocentric datasets. Using only the supervision natively available in each downstream benchmark, ME-U0 achieves an average score of 17.66 on the RoboDojo simulation benchmark and average success rates of 99.0\% and 82.5\% on LIBERO and LIBERO-Plus, respectively. We additionally validate ME-U0 on real-world robotic manipulation tasks, demonstrating its effectiveness beyond simulation. Without corresponding downstream supervision, ME-U0 further demonstrates zero-shot subtask prediction, affordance grounding, and visual dynamics on simulated and real-world observations. Overall, ME-U0 combines competitive downstream control performance with transferable task-grounding and visual-dynamics capabilities across simulation and the real world.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.25627v1
- Authors: Haoran Wen, Wenfu Wang, Kunsong Shi, Jingke Wang, Wancheng Feng, Yiren Zhang, Yueran Zhao, Xuancheng Zhang, Nanfei Ye, Xingru Chen, Zhaohong Sun, Chengmin Yang, Zikang Yu, Penghao Bi, Jia Shi, Yu Liu, Kun Zhan, Yan Xie
- Published: 2026-09-22T03:36:36Z
- Age days: 1

</details>
