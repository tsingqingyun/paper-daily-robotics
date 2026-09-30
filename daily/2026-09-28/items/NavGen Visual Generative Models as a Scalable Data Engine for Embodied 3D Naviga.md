---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.30770v1"
published: "2026-09-25T03:49:44Z"
age_days: 3
score: 28
created: 2026-09-28
concepts: ["多模态基础模型", "Sim2Real", "具身智能评测与基准"]
---

# NavGen: Visual Generative Models as a Scalable Data Engine for Embodied 3D Navigation

> [!summary] 先说人话（基于摘要）
> NavGen 用文本到视频生成室内外导航片段，扩充无人机视觉语言导航训练数据。它通过风格多样化补充难收集的长尾场景，并用真实飞行检验迁移。

## 问题

三维具身导航的数据来源存在取舍：仿真可扩展但有视觉域差异，真实飞行观测可靠却采集昂贵。核心目标是以生成视频扩大场景与长尾覆盖。

## 创新点或方法

文本到视频流水线生成 VLN 回合，配合风格多样化形成约 400K 回合的数据集。使用这些数据训练模型，并以世界动作模型范式部署到真实飞行任务。

## 证据

数据集约含 400K 导航回合；摘要报告模型通常随数据规模增大而改善，并优于使用现有数据集训练的模型。真实不同导航任务与环境中的最终成功率为 75%，未给出试验数量和分项结果。

## 局限

需核查视频如何获得一致的导航指令、动作或轨迹监督，以及生成内容的几何和运动一致性如何保证；摘要没有解释这些关键接口。

- **判断**：值得读数据生成与真机评测协议，确认监督构建方式后再判断是否能复用。

## 研究关联

对具身数据生成和 Sim2Real 研究者，它提供了生成式视觉数据服务真实导航的案例，值得检查生成规模能否转化为控制收益。

- **概念**：[[多模态基础模型]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/NavGen Visual Generative Models as a Scalable Data Engine for Embodied 3D Naviga.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

General-purpose robot models increasingly rely on large and diverse datasets. For embodied 3D navigation, however, existing data sources face a fundamental trade-off: simulated data can be generated at scale but often suffer from the visual sim-to-real gap, whereas real-world flight data provide realistic observations but are costly to collect. This paper studies another direction: the use of high-fidelity visual generative models as scalable data engines for embodied 3D navigation. We introduce NavGen, a text-to-video data generation pipeline that produces diverse vision-language navigation (VLN) episodes across indoor and outdoor scenes. We also propose a style-diversification method that scales up long-tail data that are difficult and costly to collect. The resulting dataset contains approximately 400K navigation episodes. We evaluate our dataset against existing UAV navigation datasets across multiple metrics, and find that the model trained on our data generally improves with scale, outperforming those trained on existing datasets. To validate real-world transferability, we deploy the trained model in world-action-model paradigm to real-world flying experiments. The final model achieves a 75\% success rate across different navigation tasks and environments.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.30770v1
- Authors: Xijie Huang, Yongyang Wan, Chengbin Dong, Zimo Ding, Mo Zhu, Yijin Wang, Zhiyang Liu, Fei Gao, Yuze Wu, Xin Zhou
- Published: 2026-09-25T03:49:44Z
- Age days: 3

</details>
