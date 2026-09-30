---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.29078v1"
published: "2026-08-29T06:10:20Z"
age_days: 3
score: 36
created: 2026-09-01
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# DREAM: Deployment-Time Demonstration Generation via Real-to-Sim for Scalable Policy Adaptation

> [!summary] 先说人话（基于摘要）
> DREAM 从部署现场的空间扫描和语言指令自动生成 VLA 微调数据：重建场景、把指令转成符号目标与成功条件，再用任务—运动规划生成并验证轨迹。

## 问题

预训练 VLA 到新工作区仍常需该环境的动作标注示范，而每个空间、物体布局或任务都重新遥操作，成本很高。

## 创新点或方法

输入捕获的工作区和语言指令，输出经随机物体配置扩增、成功条件验证并渲染的图像—动作样本，用于微调已有 VLA。它用大语言模型生成符号目标和判据，用任务—运动规划求可行轨迹；区别于人工示范，是在部署时由真实场景的仿真副本自动采数。

## 证据

摘要只说明进行了真实机器人语言条件操作实验，并比较自动数据微调与直接部署的成功率、以及和人工遥操作的采集成本；没有报告可核查的结果数字或明确比较结论。


## 局限

摘要没有证明其确实提升成功率或降低成本；最需核查场景重建误差、自动成功判据和规划轨迹如何影响真实执行。

- **判断**：概念值得读，但在缺少摘要结果的情况下只建议先读实验部分；是否成立完全取决于真实机器人收益与成本核算。

## 研究关联

对 VLA 和机器人学习团队，它瞄准的是最现实的部署适配成本，并把规划器、仿真和基础模型组合成自动数据工厂。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-01/DREAM Deployment-Time Demonstration Generation via Real-to-Sim for Scalable Poli.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models have made strong progress in language-conditioned robot manipulation, but improving their performance in a new workspace still often requires action-labeled data from that environment. Collecting such data by human teleoperation is costly, especially when each workspace, object arrangement, or task may require new demonstrations. We present DREAM, a framework that generates fine-tuning data for a pretrained VLA from a captured workspace and a language instruction, without requiring a task-specific human demonstration. DREAM reconstructs the workspace, automatically translates the instruction into symbolic task goals and success criteria using a large language model, and uses task-and-motion planning to generate feasible robot trajectories. The planned trajectories are augmented across randomized object configurations, verified by the generated success criteria, and rendered into image-action examples for VLA fine-tuning. Through real-robot experiments on language-conditioned manipulation tasks, we study whether DREAM can serve as a scalable data-collection system for the deployment workspace by examining whether fine-tuning on its automatically generated data improves success over direct deployment and how its data-collection cost compares with human teleoperation when adapting a VLA to a new workspace.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.29078v1
- Authors: Makoto Sato, Tatsuya Matsushima, Yutaka Matsuo, Yusuke Iwasawa
- Published: 2026-08-29T06:10:20Z
- Age days: 3

</details>
