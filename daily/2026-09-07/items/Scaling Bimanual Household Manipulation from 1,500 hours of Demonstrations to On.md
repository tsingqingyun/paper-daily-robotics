---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03591v1"
published: "2026-09-03T09:37:09Z"
age_days: 3
score: 35
created: 2026-09-07
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Scaling Bimanual Household Manipulation from 1,500 hours of Demonstrations to On-Policy Corrections

> [!summary] 先说人话（基于摘要）
> 作者发布1,500小时双臂家庭操作示范并训练XR-2，再用实时人工干预产生的DAgger纠正数据后训练，研究示范规模和在线纠错两条扩展路径。

## 这篇到底在做什么

- **卡在哪里**：通用双臂操作策略受制于高质量、大规模人类示范稀缺，尤其难覆盖家庭任务多样性；仅靠固定离线数据也难修正策略实际执行时遇到的偏差。
- **关键解法**：工作搭建高吞吐数据管线和多阶段训练方案，以1,500小时示范训练XR-2 VLA；随后分别改变专家示范量，并加入人类实时干预得到的DAgger纠正数据，观察任务成功率随数据增长的变化。
- **拿什么证明**：明确发布1,500小时多样化双臂家庭任务示范；摘要称在所测试的数据范围内，增加专家示范和DAgger纠正数据都使成功率稳定上升，但未给具体成功率、任务数或曲线斜率。

## 值不值得读

- **和你的研究有什么关系**：对机器人学习和VLA研究者，这既是可复现的双臂数据资源，也提供了离线规模化与在策略纠错如何衔接的实证线索。
- **先别急着信**：摘要缺少任务覆盖、采集质量、机器人平台、数据许可细节及具体基线数字；所谓扩展趋势是否持续到范围外不能据此判断。
- **判断**：做双臂数据、VLA训练或DAgger者值得深入看数据说明和 scaling 曲线；其他读者可先把它视为重要资源论文。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-07/Scaling Bimanual Household Manipulation from 1,500 hours of Demonstrations to On.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learning generalist policies for robust bimanual manipulation is bottlenecked by the scarcity of high quality large scale human demonstration data. In this work, we release 1,500 hours of diverse bimanual manipulation demonstrations covering everyday household tasks, and use this comprehensive corpus to train XR-2, a powerful vision-language-action (VLA) model. Enabled by a purpose built high throughput data pipeline and a carefully designed multi stage training paradigm, XR-2 attains strong manipulation performance in our systematic experiments while retaining favorable training efficiency and high data utilization. We further study two critical scaling axes: varying the amount of expert demonstration data, and post training on DAgger correction data from real time human interventions. In both settings, task success rate improves steadily over the data ranges we probe, exhibiting a clear consistent scaling trend at our current data scale. These results validate both the learning capacity of XR-2 and the promising scaling properties of the released dataset, which we open source to support reproducible research on bimanual robot manipulation learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03591v1
- Authors: Jiafeng Xu, Qi Li, Yan Shen, Yiyu Ren, Travis Davies, Shaowen He, Ze Wang, Yifan Yang, Ran Cheng, Hao Dong
- Published: 2026-09-03T09:37:09Z
- Age days: 3

</details>
