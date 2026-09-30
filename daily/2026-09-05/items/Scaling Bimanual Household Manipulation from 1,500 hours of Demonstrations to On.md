---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03591"
published: "Fri, 04 Sep 2026 00:00:00 -0400"
age_days: 0
score: 35
created: 2026-09-05
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Scaling Bimanual Household Manipulation from 1,500 hours of Demonstrations to On-Policy Corrections

> [!summary] 先说人话（基于摘要）
> 该工作发布1,500小时双臂家庭操作示范并训练 XR-2 VLA，同时研究专家数据规模与 DAgger 在线纠错数据两条扩展轴。摘要的核心结论是，两类数据增加都持续提高任务成功率。

## 这篇到底在做什么

- **卡在哪里**：通用双臂策略受制于高质量、大规模人类示范稀缺，家庭任务的多样性又使长尾覆盖尤为困难。仅靠固定离线数据也难以纠正策略实际运行时暴露的错误分布。
- **关键解法**：作者构建高吞吐数据管线收集多样家庭双臂示范，以多阶段训练方案训练 XR-2；随后分别改变专家示范量，并加入人类实时干预形成的 DAgger 纠错数据进行后训练，观察扩展规律。
- **拿什么证明**：发布1,500小时示范数据；摘要称在考察的数据范围内，增加专家示范和 DAgger 纠错数据均带来稳定成功率提升，同时训练效率和数据利用率良好，但未给具体成功率或扩展曲线参数。

## 值不值得读

- **和你的研究有什么关系**：对双臂 VLA 和机器人学习，开放的大规模家庭示范及在线纠错数据可支持可复现的数据扩展研究，也能帮助判断继续采专家数据还是采失败纠正更划算。
- **先别急着信**：摘要未说明任务数量、数据分布、测试泛化边界及具体效率指标；所谓扩展趋势是否跨任务稳定需查全文。
- **判断**：数据资源本身值得重点关注；建模结论应读到扩展曲线和数据划分后再判断，不能仅凭“持续提升”下结论。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-05/Scaling Bimanual Household Manipulation from 1,500 hours of Demonstrations to On.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.03591v1 Announce Type: new Abstract: Learning generalist policies for robust bimanual manipulation is bottlenecked by the scarcity of high quality large scale human demonstration data. In this work, we release 1,500 hours of diverse bimanual manipulation demonstrations covering everyday household tasks, and use this comprehensive corpus to train XR-2, a powerful vision-language-action (VLA) model. Enabled by a purpose built high throughput data pipeline and a carefully designed multi stage training paradigm, XR-2 attains strong manipulation performance in our systematic experiments while retaining favorable training efficiency and high data utilization. We further study two critical scaling axes: varying the amount of expert demonstration data, and post training on DAgger correction data from real time human interventions. In both settings, task success rate improves steadily over the data ranges we probe, exhibiting a clear consistent scaling trend at our current data scale. These results validate both the learning capacity of XR-2 and the promising scaling properties of the released dataset, which we open source to support reproducible research on bimanual robot manipulation learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03591
- Authors: Jiafeng Xu, Qi Li, Yan Shen, Yiyu Ren, Travis Davies, Shaowen He, Ze Wang, Yifan Yang, Ran Cheng, Hao Dong
- Published: Fri, 04 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
