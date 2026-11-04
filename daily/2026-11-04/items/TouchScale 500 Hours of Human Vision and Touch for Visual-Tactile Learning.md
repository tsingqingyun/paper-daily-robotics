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
url: "https://arxiv.org/abs/2610.10288"
published: "Tue, 03 Nov 2026 00:00:00 -0500"
age_days: 0
score: 36
created: 2026-11-04
concepts: ["具身智能评测与基准"]
---

# TouchScale: 500 Hours of Human Vision and Touch for Visual-Tactile Learning

> [!summary] 这篇论文到底做了什么（基于摘要）
> TouchScale 把人操作物体时的视频和双手触觉同步记录下来，让模型学习画面背后的接触信息。它的关键是用同一套设备和采集流程积累 500 小时数据，从而更清楚地检验增加数据量是否有用。

## 问题

任务是从视觉学习接触、识别动作，并把人的操作经验用于机器人。视频能拍到手靠近物体，却没有直接记录哪里接触、压力如何；已有视觉触觉数据规模较小，大资源又常混用传感器和标注流程，因此效果变化可能来自设备差异，难以归因于数据量。

### 用一个例子理解

理解用例（非论文实验）：输入一段人拿海绵擦桌的视频及同步手部触觉；训练时把手指画面与接触区域对应起来；模型随后对新画面预测接触区域。它说明监督如何进入学习，不代表论文验证了擦桌任务。

## 创新点或方法

过去主要靠视频，或拼接不同来源的触觉数据；TouchScale 改为统一穿戴设备，同步采集第一视角 RGB-D、腕部 RGB 和双手全手密集触觉，覆盖约 2K 个预定义任务描述。训练时分别用于触觉预测、视觉编码器预训练和机器人策略的视觉触觉中间训练。推理时具体需要哪些输入、机器人是否仍需触觉传感器，摘要未说明。

### 方法如何工作

1. 用统一设备记录人的操作，同时得到多视角画面和双手触觉，补上视频无法直接记录的接触信息。
2. 按时间对齐不同信号，使同一瞬间的视觉变化能对应实际接触；具体同步精度摘要未说明。
3. 用配对数据训练感知模型，并用于机器人策略中间训练；具体损失和接口摘要只说明到此。
4. 固定采集条件、增加数据子集规模，再测跨传感器预测和真机成功率，以观察规模收益。

### 必要术语

- RGB-D：彩色画面加深度；在本文中记录第一视角外观与空间信息。
- 接触 IoU：预测接触区域与真实区域的交集占并集的比例；衡量接触位置预测。
- 中间训练：在最终任务训练前增加一段训练；本文借此把人的视觉触觉经验用于机器人策略。

## 证据

摘要报告：相较既有触觉数据，用完整 TouchScale 训练后，在未见触觉传感器数据上的零样本接触 IoU 从 0.134 升至 0.383；视觉编码器在三个动作识别基准上优于所比较的数据集，但未给准确率。四项接触密集真机任务的平均成功率从 22.5% 升至 57.5%。固定设备和流程后，增加数据量的两类结果总体上升；这支持该采集条件下的规模收益，尚不能推出任意触觉数据都有同样效果。

## 局限

我的待核查问题是：未见传感器测试如何对齐接触标签，以及真机各组是否使用相同训练预算。摘要没有提供这些条件，也未列作者明确局限；现有结果不能单独证明收益全部来自触觉，而非视觉覆盖或训练量。

- **判断**：值得细读数据采集协议和规模消融，因为它最有用的贡献是让“接触数据越多是否越好”变成可检验的问题。

## 研究关联

值得借鉴的是让数据规模实验尽量少受采集差异干扰。若要判断接触监督是否值得继续采集，固定设备和流程、逐步增加训练数据，比直接比较几个来源不同的数据集更容易解释。

### 下一步读哪里

先核查时间同步、触觉标定与接触标签定义，再看数据规模实验是否固定训练步数，以及机器人中间训练如何连接到最终策略。

- **概念**：具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-04/TouchScale 500 Hours of Human Vision and Touch for Visual-Tactile Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.10288v3 Announce Type: replace Abstract: Large-scale egocentric human interaction data is becoming an important source of physical supervision for embodied learning, yet video alone leaves the contact and pressure that characterize physical interaction unrecorded. Recent visual-tactile datasets provide this missing supervision, but their synchronized tactile data remain far smaller in volume than human video. Moreover, the largest resources often merge recordings from different sensors or annotation procedures, which makes the effect of data scale difficult to isolate. We therefore introduce TouchScale, a 500-hour dataset of contact-rich human interaction recorded with a single unified wearable setup. Its approximately 2K predefined task descriptions span everyday activities and structured manipulation, and each recording temporally aligns egocentric RGB-D video with wrist RGB video and dense full-hand bimanual tactile measurements. Compared with prior tactile data, training on the full TouchScale raises zero-shot contact IoU on data from an unseen tactile sensor from 0.134 to 0.383. Pretraining a visual encoder on TouchScale also yields the highest action recognition accuracy on three benchmarks among the compared visual-tactile datasets. Used for visual-tactile mid-training of a robot policy, TouchScale improves the average real-world success rate across four contact-rich manipulation tasks from 22.5% to 57.5%. With the sensor and collection protocol held fixed, both zero-shot tactile prediction and robot success show an overall upward trend as more TouchScale data is used. These results suggest that human visual-tactile data collected at scale with consistent sensing benefits both perception and robot manipulation. We will publicly release TouchScale, including all synchronized visual-tactile recordings and reconstructed object models, to support future research on scalable visual-tactile learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.10288
- Authors: Dayou Li, Hao Wang, Qianqian Yang, Zihao Zhu, Haoquan Fang, Ziyao Zeng, Yan Han, Zihan Wang, Yan Wang, Baoru Huang, Dilin Wang, Kenji Shimada, Yiyue Luo, Manling Li, Teresa Lv, Mustafa Mukadam, Rakesh Ranjan, Ruohan Zhang, Qi He, Changliu Liu, Xu Chen, Marco Pavone, Bangya Liu, Jiachen Li, Masayoshi Tomizuka, Zhiwen Fan
- Published: Tue, 03 Nov 2026 00:00:00 -0500
- Age days: 0

</details>
