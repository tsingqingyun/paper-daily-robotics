---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2610.27040"
published: "Wed, 21 Oct 2026 00:00:00 -0400"
age_days: 0
score: 35
created: 2026-10-22
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# ACE-Brain-0.6: Scaling Spatial Grounding for Physical Foundation Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> ACE-Brain-0.6 把机器人操作录像和多种视觉数据转成可验证的目标定位训练样本，用约 150 万条样本微调 Qwen3.5-9B。核心思路是先加强“该与画面哪里互动”的判断，为后续操作提供更可靠的位置依据。

## 问题

机器人即使理解任务，也需要从干扰物中找到正确的交互对象和位置。作者观察到 Astra 的广泛操作能力伴随较强空间感知，因此选择扩大视觉定位监督。摘要没有给出旧定位方法失败的具体对照，不能把这种动机写成已经证实的操作瓶颈因果关系。

### 用一个例子理解

理解用例（非论文实验）：输入杂乱桌面图像和“找到红柄杯子的把手”；模型识别相关对象并输出定位结果，供后续系统选择交互位置。这里仅演示定位的用途，不代表论文验证了抓取成功。

## 创新点或方法

做法从收集多来源数据开始：自动标注机器人操作记录，与其他视觉数据共同转成可验证的定位监督，再微调 Qwen3.5-9B 得到 ACE-Brain-0.6。训练时扩大的是定位样本及场景覆盖；推理时由微调模型处理视觉定位任务。摘要没有说明自动标注工具、验证规则、输出坐标格式，也没有描述接入动作控制器的过程。

### 方法如何工作

1. 收集机器人操作记录与多来源视觉数据，增加可覆盖的定位场景。
2. 自动标注操作记录，并把数据转成可验证的定位监督；具体验证方式摘要未说明。
3. 用约 150 万样本微调 Qwen3.5-9B，使模型学习从视觉与任务信息中定位相关目标。
4. 在七个公开基准评估，并在固定微调设置下比较 successive 数据扩充的汇总表现，以检查数据扩展是否有效。

### 必要术语

- 视觉定位（grounding）：把任务中的对象或位置描述对应到图像里的具体区域；本文训练和评测的核心能力。
- 可验证监督：带有可检查目标答案的训练信号；本文用它组织定位数据，但摘要未说明检查规则。
- 空间感知：判断对象在哪里及其空间关系的能力；本文希望通过定位训练加强这部分基础。

## 证据

摘要报告，约 150 万样本训练后，模型在七个公开定位基准中的四个超过 Astra，总体平均分为 75.41，对方为 73.68。固定 Qwen3.5-9B 微调设置、逐次扩大数据集合时，汇总定位成绩持续改善。这支持数据扩充方案对定位有效；但数量和场景覆盖同时改变，无法单独归因于样本数量。摘要未提供分项指标定义、误差范围或机器人任务成功率。

## 局限

定位基准领先不等于端到端控制领先。我的待核查问题是自动标签如何验真、不同数据来源各贡献多少，以及训练与公开基准是否有重叠。这些问题影响结论可信度，但输入不足以判断作者是否已完成相关检查。

- **判断**：值得深入读数据生成与验证流程，它比总榜排名更可能被复用；把结果解释为通用机器人操作能力提升，目前证据还不够。

## 研究关联

可借鉴的是把机器人记录转成更容易检查对错的感知监督，再与其他来源补足场景覆盖。若目标是改善交互对象定位，这种数据建设路线有直接依据；是否进一步改善完整操作，需要另测。

### 下一步读哪里

先查机器人记录如何自动标注、何谓可验证，以及不同来源如何去重和配比；再看七个基准的分项成绩、平均分计算方式、逐批数据实验的训练预算和是否有下游操作验证。

- **概念**：多模态基础模型 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-22/ACE-Brain-0.6 Scaling Spatial Grounding for Physical Foundation Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.27040v1 Announce Type: new Abstract: General-purpose multimodal models, including GPT-6 Astra and Claude Opus 5.5, demonstrate broad capabilities in embodied manipulation. Our analysis indicates that this generality is accompanied by strong spatial perception, as Astra can determine where to interact with task-relevant entities amid visual distractors. Because spatial perception connects high-level reasoning to the physical scene, we investigate scaling visual grounding to strengthen the perceptual foundation of general embodied operation. We develop a unified data pipeline that combines robot manipulation recordings with complementary visual data from diverse sources. After automatically annotating the robot recordings, the pipeline converts the collected data into verifiable grounding supervision. Fine-tuning Qwen3.5-9B on approximately 1.5 million samples produced by this pipeline yields ACE-Brain-0.6. The model outperforms GPT-6 Astra on four of seven public grounding benchmarks, with an overall average score of 75.41 compared with Astra's 73.68. Under a fixed Qwen3.5-9B fine-tuning setup, aggregate grounding performance improves steadily as successive data releases expand the training collection to cover a broader range of grounding scenarios. These results show that scaling verifiable grounding supervision from diverse sources can strengthen the spatial perception of an open 9B model for general embodied operation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.27040
- Authors: Yinhe Wang, Tao Tao, Zexin He, Shuang Luo, Wei Mao, Yao Mu, Feng Pan, Hanming Deng, Lewei Lu, Zhi Hou, Xingang Pan, Dahua Lin, Dacheng Tao, Xiaogang Wang
- Published: Wed, 21 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
