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
url: "https://arxiv.org/abs/2610.09455v1"
published: "2026-10-07T05:11:50Z"
age_days: 0
score: 31
created: 2026-10-08
concepts: ["多模态基础模型", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# RLHND: Video Foundation Models as Physically Grounded Hand Trackers for Robot Learning

> [!summary] 这篇论文到底做了什么（基于摘要）
> RLHND 从第一人称单目视频同时估计手的姿态、接触位置和受力。它把预训练视频模型变成固定片段的特征提取器，利用跨帧的手部运动与物体交互知识，补足逐帧姿态回归缺少的物理线索。

## 问题

任务是把人类操作视频转成机器人学习可用的手部信息。许多已有跟踪器从裁剪帧回归姿态，对运动连续性和手物交互的先验有限，可能给出不准确或物理不一致的结果；即使姿态可用，缺少接触和力也难以描述操作如何发生。

### 用一个例子理解

理解用例（非论文实验）：输入一段第一人称拿起杯子的视频；RLHND 提取片段特征，输出手指角度、接触区域及力估计，再由另一个重定向过程转换为机器人手动作。这里的力不是从视频直接测量得到。

## 创新点或方法

旧做法主要盯单帧手部外观；RLHND 用 clean-latent conditioning 将 Cosmos 3 视频扩散骨干转成确定性的片段特征提取器，把预训练得到的运动与交互先验带入跟踪。姿态分支预测符合解剖约束的关节角，还可输入手形参数，维持同一人的手形一致。训练触觉分支时冻结姿态分支，预测手表面的密集接触和力；用基于 LBS 的特征铺展获取顶点特征，避免逐顶点注意力。推理时输入视频并输出这些估计，具体监督来源与损失未说明。

### 方法如何工作

1. 将视频片段送入改造后的预训练骨干，得到包含时间关系的确定性特征，为跟踪补充运动先验。
2. 从特征预测解剖上合理的关节角，必要时输入手形参数，减少同一人的形状漂移。
3. 冻结姿态分支后训练独立触觉分支，学习手表面的接触与力。
4. 通过 LBS 特征铺展得到顶点级信息，减少逐顶点注意力的代价，再输出姿态和触觉估计。

### 必要术语

- 确定性特征提取：将视频转成可重复使用的表示；本文不把骨干用于随机生成视频。
- 手形参数：描述手的形状；用于保持同一人的形状一致。
- LBS：线性混合蒙皮，通常用关节变换带动网格；本文借其结构铺展顶点特征。

## 证据

摘要称姿态、接触和力估计在多个基准上达到领先水平，并给出动作重定向和真机机器人实验。但没有数据集名称、基线、误差指标、数值或真机成功率。因此不能量化领先幅度，也不能判断姿态、触觉分别对机器人学习贡献多少；现有描述支持作者评估了跟踪及下游用途。

## 局限

单目视频预测出的力是模型估计，不能视为传感器直接测量；同样的可见动作可能对应不同受力。我会核查力标签如何获得、遮挡下的不确定性，以及真机实验究竟验证了触觉信息还是主要验证姿态重定向。

- **判断**：值得读方法和监督数据部分；能否借鉴，主要取决于视频特征如何提取、物理标签如何获得，而不是“使用了基础模型”这一点。

## 研究关联

值得借鉴的是把视频预训练模型用于估计，而不是生成视频：跨帧交互知识可以成为姿态与触觉预测的输入。若单帧外观不足以解释操作，片段特征比继续堆叠逐帧回归器更值得检查。

### 下一步读哪里

核查 clean-latent conditioning 的具体输入与提取层、手形条件来源、接触和力标签、LBS 铺展方式，以及下游实验是否隔离了触觉分支的收益。

- **概念**：多模态基础模型 世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-08/RLHND Video Foundation Models as Physically Grounded Hand Trackers for Robot Lea.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recently, approaches that leverage human video datasets for robot policy training have become increasingly prevalent. However, most existing hand trackers regress pose from cropped frames with limited priors on hand motion and object interaction, resulting in inaccurate and physically inconsistent estimates. Moreover, the lack of physical cues, e.g., contact and force, limits the use of human videos for robot policy training. To this end, we propose RLHND, a video foundation model-based hand tracking model that jointly estimates hand pose and realistic tactile information from monocular egocentric videos. RLHND turns the pre-trained Cosmos 3 video diffusion backbone into a deterministic clip-level feature extractor via clean-latent conditioning, carrying its learned priors on hand motion and hand-object interaction into tracking. For pose estimation, RLHND (i) predicts hand poses with anatomically plausible joint angles and (ii) enables optional conditioning on the shape parameter to maintain consistent hand shape within the same video and even across videos recorded by the same actor. For tactile estimation, a separate tactile expert stream, trained with the pose stream frozen, predicts dense contact and force over the hand surface. We further adopt LBS-based feature spreading to enable vertex-wise feature extraction without costly per-vertex attention. RLHND achieves state-of-the-art performance across various benchmark datasets for pose estimation, while also achieving state-of-the-art performance in contact and force estimation. Moreover, we demonstrate the utility of RLHND for robot learning through retargeting results and real-world robot experiments. The code will be publicly available at https://seungjun-moon.github.io/rlhnd/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.09455v1
- Authors: Seungjun Moon, Subin Jeon, Sangwoo Kim, Hanbyul Joo, Jinwoo Shin
- Published: 2026-10-07T05:11:50Z
- Age days: 0

</details>
