---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.23885v1"
published: "2026-09-20T21:42:12Z"
age_days: 2
score: 38
created: 2026-09-23
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# HumynexSurg-1: A Curated Expert Liposuction Dataset

> [!summary] 先说人话（基于摘要）
> HumynexSurg-1提供一小批专家吸脂操作记录，把口述决策与视觉、压力和手部力信息同步保存。价值主要在于怎样采集视觉难以直接解释的接触操作，而非已经实现自主手术。

## 问题

摘要指出手术在机器人示范语料中覆盖不足，力信息尤其稀缺；吸脂器械在皮下工作，专家依赖触觉与判断，单靠外部视频难以完整描述操作。

## 创新点或方法

记录一位专家在猪腹部组织上的操作，组织同步多模态信号与专用语言标签；当前器械运动以侧视视频中的工具—手轨迹表示，力通道作为状态输入，并用GR00T N1.7进行微调验证。

## 证据

数据含14段、42,738帧、35.6分钟和356条口述，95%可映射到标签体系。每次微调少于一小时；摘要称增加会话降低未见会话误差，但未提供误差数值。

## 局限

测量的6自由度手柄姿态、经验证的力通道、超声及触诊属于后续采集计划，不能算作当前版本能力；数据仅来自一位专家的猪组织操作。

- **判断**：优先读数据说明与质量报告，模型结果只宜作为数据接入训练流程的初步验证。

## 研究关联

对机器人学习有明确的数据设计参考价值，尤其是专家决策语言与接触状态的同步；作为大规模基础模型训练或广泛能力评测的数据依据仍有限。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/HumynexSurg-1 A Curated Expert Liposuction Dataset.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robot foundation models learn manipulation from large demonstration corpora, but surgery is missing from those corpora: across the 780-hour Open-H surgical collection, one dataset carries synchronized force and none covers an aesthetic procedure. Liposuction is the hard case, because the instrument works under the skin and the surgeon operates by feel and by judgment. Humynex Robotics builds curated expert datasets for this kind of procedure. HumynexSurg-1 is the first release: a master liposuction surgeon performing on porcine abdominal tissue while narrating every decision, recorded with synchronized suction pressure, six-axis hand force/torque, top-down RGB-D video, side video and a lavalier microphone -- 14 episodes, 42,738 frames, 35.6 minutes, 356 utterances of which 95% compile into a liposuction-specific label schema. The capture follows a patent-pending sensing plan organized around the quantities a policy needs, so a channel captured today by a model can be upgraded to a sensor tomorrow without changing the data format. This release captures the instrument motion as a tool-hand track in the side video and provides the force channel as state; the funded capture adds a measured 6-DoF handle pose, a validated force channel, ultrasound imaging of the fat layer, and palpation sensing. As a proof of concept, NVIDIA Isaac GR00T N1.7 fine-tunes on the dataset with no custom code in under an hour per run and learns the recorded sessions; scaling probes on the same episodes show where further gains come from: every new session lowers the error on an unseen session. The dataset, its label schema, its quality-assurance reports and its evaluation protocol are the product; the next capture, many short sessions across fat regions with the sensors named here, is what the probes point to.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.23885v1
- Authors: Rhea Huang, David L. Matlock, Laurence Reich
- Published: 2026-09-20T21:42:12Z
- Age days: 2

</details>
