---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: body-excerpts
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2610.10270v1"
published: "2026-10-07T15:40:02Z"
age_days: 1
score: 39
created: 2026-10-09
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Video Prediction Policy 2: Predict Better, Act Better

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> VPP2 先把视频模型训练成能按指令预测操作过程的模型，再压缩预测计算并接入动作专家。巧处是先学清完整动作事件，再统一预测时间尺度，避免视频先验在动作训练中被扰乱。

## 问题

世界动作模型想靠预测未来指导操作，但新场景里预测错了，动作也会错。作者认为普通视频模型偏重画面生成而非准确操作，直接加入动作组件还会损伤已有预测能力 [S3](https://arxiv.org/html/2610.10270v1#S1.p1.1) [S4](https://arxiv.org/html/2610.10270v1#S1.p2.1)。

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子倒扣到盘子上”和当前多视角图像；规划器明确对象与动作，视频模型预测翻转和放置过程，动作专家据内部表示输出机器人动作段。

## 创新点或方法

旧做法直接利用通用视频模型学动作；本文先用详细标注的完整操作事件继续训练 Wan2.1，再改成固定时长预测，解决不同事件时长与动作难对齐的问题。随后一致性蒸馏成单步预测器，训练读取视频内部表示的动作专家；早期冻结视频主体，仅用 LoRA 适配。推理时 VLM 将开放指令细化成子任务，视频模型预测未来，动作专家生成动作段，而非从生成图片做手工轨迹提取 [S5](https://arxiv.org/html/2610.10270v1#S1.p3.1) [S15](https://arxiv.org/html/2610.10270v1#S3.p1.1) [S26](https://arxiv.org/html/2610.10270v1#S3.SS1.p4.1) [S32](https://arxiv.org/html/2610.10270v1#S3.SS2.p1.1)。

### 方法如何工作

1. 用详细子任务描述配完整事件，学会从初始观察预测有语义连贯性的过程。
2. 改为固定时长片段，使未来表示有统一时间尺度，便于对应动作。
3. 将多步生成蒸馏成单步预测，降低在线等待时间。
4. 训练动作专家读取预测表示，并限制早期对视频主体的改动，减少新动作训练的干扰。
5. 部署时细化指令、预测未来并生成短动作段，将学习到的过程用于执行。

### 必要术语

- 事件级训练：预测完整子任务过程；先学语义与变化的对应。
- 一致性蒸馏：学习用更少计算得到原多步生成的结果；用于加速预测。
- 逆动力学：从状态变化推断所需动作；本文由动作专家隐式学习。

## 证据

视频指令遵循测试中，人手/机器人得分分别为 0.80/0.90，Cosmos3-64B 为 0.70/0.78 [S38](https://arxiv.org/html/2610.10270v1#S4.T2.1)。真机 ALOHA 十类零样本任务平均成功率 58.5%，π₀.₅ 为 40.0%，Fast-WAM 为 20.5% [S6](https://arxiv.org/html/2610.10270v1#S1.p4.1)。专门后训练后，LIBERO-Pro 为 45.0% 对最强基线 11.0%，LIBERO-OOD 为 63.9%，RoboDojo 为 29.47% [S6](https://arxiv.org/html/2610.10270v1#S1.p4.1)。后三项不能当零样本结果；视频测试样本量和判定细节未提供。

## 局限

节选没有明确局限段。我的待核查问题是蒸馏和动作训练后保留多少预测能力，以及增益中数据、规划器和训练顺序各占多少。约 0.22 秒是视频加动作计算延迟 [S33](https://arxiv.org/html/2610.10270v1#S3.SS2.p2.1)，不能直接视作含高层规划的端到端延迟；更准预测导致更好动作仍需受控比较。

- **判断**：值得深入读训练顺序和消融，因为它解释了视频先验如何变得可用，比只研究动作头更有启发。

## 研究关联

值得借鉴的是区分两种学习目标：完整事件建立“这条指令会产生什么过程”，固定时长预测建立“接下来多久会发生什么”。这让语义学习和动作时间对齐各有合适的数据单位。

### 下一步读哪里

沿 [S16](https://arxiv.org/html/2610.10270v1#S3.SS1.p1.1) [S26](https://arxiv.org/html/2610.10270v1#S3.SS1.p4.1) [S30](https://arxiv.org/html/2610.10270v1#S3.SS1.p6.1) [S32](https://arxiv.org/html/2610.10270v1#S3.SS2.p1.1) 检查各阶段数据与冻结设置；再核查事件训练、蒸馏和高层规划器的消融，以及零样本任务与训练数据的划分。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.10270v1
- 获取时间：2026-10-09T00:15:44.533828+00:00
- [S1] [Video Prediction Policy 2: Predict Better, Act Better · 正文段落 1](https://arxiv.org/html/2610.10270v1#abstract1.1)
- [S2] [Video Prediction Policy 2: Predict Better, Act Better · 正文段落 2](https://arxiv.org/html/2610.10270v1#S0.F1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.10270v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.10270v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.10270v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.10270v1#S1.p4.1)
- [S7] [2 Data Process Pipeline · 正文段落 7](https://arxiv.org/html/2610.10270v1#S2.p1.1)
- [S8] [2 Data Process Pipeline · 正文段落 8](https://arxiv.org/html/2610.10270v1#S2.p2.1)
- [S9] [2 Data Process Pipeline · 正文段落 10](https://arxiv.org/html/2610.10270v1#S2.T1)
- [S10] [2 Data Process Pipeline · 正文段落 14](https://arxiv.org/html/2610.10270v1#S2.p5.1)
- [S11] [2 Data Process Pipeline · 正文段落 15](https://arxiv.org/html/2610.10270v1#S2.F3)
- [S12] [2 Data Process Pipeline · 正文段落 16](https://arxiv.org/html/2610.10270v1#S2.p6.1)
- [S13] [2 Data Process Pipeline · 正文段落 17](https://arxiv.org/html/2610.10270v1#S2.p7.1)
- [S14] [2 Data Process Pipeline · 正文段落 18](https://arxiv.org/html/2610.10270v1#S2.p8.1)
- [S15] [3 VPP2: A Generalist Policy with Zero-shot Capability · 正文段落 19](https://arxiv.org/html/2610.10270v1#S3.p1.1)
- [S16] [3.1 Video Prediction Model Training Pipeline · 正文段落 20](https://arxiv.org/html/2610.10270v1#S3.SS1.p1.1)
- [S17] [3.1 Video Prediction Model Training Pipeline · 正文段落 21](https://arxiv.org/html/2610.10270v1#S3.SS1.p2.1)
- [S18] [3.1 Video Prediction Model Training Pipeline · 正文段落 22](https://arxiv.org/html/2610.10270v1#S3.E1)
- [S19] [3.1 Video Prediction Model Training Pipeline · 正文段落 23](https://arxiv.org/html/2610.10270v1#S3.SS1.p2.2)
- [S20] [3.1 Video Prediction Model Training Pipeline · 正文段落 24](https://arxiv.org/html/2610.10270v1#S3.E2)
- [S21] [3.1 Video Prediction Model Training Pipeline · 正文段落 25](https://arxiv.org/html/2610.10270v1#S3.SS1.p2.3)
- [S22] [3.1 Video Prediction Model Training Pipeline · 正文段落 26](https://arxiv.org/html/2610.10270v1#S3.E3)
- [S23] [3.1 Video Prediction Model Training Pipeline · 正文段落 27](https://arxiv.org/html/2610.10270v1#S3.SS1.p2.4)
- [S24] [3.1 Video Prediction Model Training Pipeline · 正文段落 28](https://arxiv.org/html/2610.10270v1#S3.SS1.p3.1)
- [S25] [3.1 Video Prediction Model Training Pipeline · 正文段落 29](https://arxiv.org/html/2610.10270v1#S3.F4)
- [S26] [3.1 Video Prediction Model Training Pipeline · 正文段落 30](https://arxiv.org/html/2610.10270v1#S3.SS1.p4.1)
- [S27] [3.1 Video Prediction Model Training Pipeline · 正文段落 31](https://arxiv.org/html/2610.10270v1#S3.SS1.p5.1)
- [S28] [3.1 Video Prediction Model Training Pipeline · 正文段落 32](https://arxiv.org/html/2610.10270v1#S3.E4)
- [S29] [3.1 Video Prediction Model Training Pipeline · 正文段落 33](https://arxiv.org/html/2610.10270v1#S3.SS1.p5.2)
- [S30] [3.1 Video Prediction Model Training Pipeline · 正文段落 34](https://arxiv.org/html/2610.10270v1#S3.SS1.p6.1)
- [S31] [3.1 Video Prediction Model Training Pipeline · 正文段落 35](https://arxiv.org/html/2610.10270v1#S3.E5)
- [S32] [3.2 Action Modeling · 正文段落 37](https://arxiv.org/html/2610.10270v1#S3.SS2.p1.1)
- [S33] [3.2 Action Modeling · 正文段落 38](https://arxiv.org/html/2610.10270v1#S3.SS2.p2.1)
- [S34] [3.3 VLM for High-level Planning. · 正文段落 40](https://arxiv.org/html/2610.10270v1#S3.SS3.p2.1)
- [S35] [3.3 VLM for High-level Planning. · 正文段落 41](https://arxiv.org/html/2610.10270v1#S3.F5)
- [S36] [4 Experiments · 正文段落 42](https://arxiv.org/html/2610.10270v1#S4.p1.1)
- [S37] [4.1 Video Prediction Quality analyses · 正文段落 43](https://arxiv.org/html/2610.10270v1#S4.SS1.p1.1)
- [S38] [4.1 Video Prediction Quality analyses · 正文段落 46](https://arxiv.org/html/2610.10270v1#S4.T2.1)
- [S39] [6 Conclusion · 正文段落 65](https://arxiv.org/html/2610.10270v1#S6.p1.1)
- [S40] [C.1 Detailed LIBERO Results · 正文段落 77](https://arxiv.org/html/2610.10270v1#A3.SS1.p1.1)
- [S41] [C.1 Detailed LIBERO Results · 正文段落 78](https://arxiv.org/html/2610.10270v1#A3.T5.2)
- [S42] [C.1 Detailed LIBERO Results · 正文段落 79](https://arxiv.org/html/2610.10270v1#A3.T5)
- [S43] [C.2 Detailed RoboDojo Results · 正文段落 80](https://arxiv.org/html/2610.10270v1#A3.SS2.p1.1)
- [S44] [C.2 Detailed RoboDojo Results · 正文段落 81](https://arxiv.org/html/2610.10270v1#A3.SS2.p2.1)
- [S45] [C.2 Detailed RoboDojo Results · 正文段落 82](https://arxiv.org/html/2610.10270v1#A3.T6.2)
- [S46] [C.2 Detailed RoboDojo Results · 正文段落 83](https://arxiv.org/html/2610.10270v1#A3.T6)
- [S47] [C.2 Detailed RoboDojo Results · 正文段落 84](https://arxiv.org/html/2610.10270v1#A3.T7.2)
- [S48] [C.2 Detailed RoboDojo Results · 正文段落 85](https://arxiv.org/html/2610.10270v1#A3.T7)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-09/Video Prediction Policy 2 Predict Better, Act Better.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World action models (WAMs) have emerged as an important class of generalist robot policies, aiming to transfer video prediction priors to action learning. However, we find that existing WAMs frequently produce incorrect motion predictions in open-ended environment, leading to erroneous actions. We attribute this limitation to two factors: (1) base video models are not optimized for manipulation, and (2) naively incorporating action components into video models can substantially degrade their generalization capabilities. We introduce Video Prediction Policy 2 (VPP2), a WAM that enables strong zero-shot generalization in both video prediction and action generation. First, we curate a large-scale, diverse dataset of manipulation videos to continue pretraining the base video foundation model. We annotate video clips with detailed captions and perform \textit{event-level} video pretraining to promote generalization across open-ended manipulation tasks. Second, we post-train and distill the video model into a single-step visual planner with fixed prediction horizon. Finally, we introduce action module via a mixture-of-transformers (MoT) architecture to learn implicit inverse dynamics model. Experiments demonstrate three key results: (1) VPP2-14B outperforms Cosmos3-64B by 11.0\% points in video prediction instruction-following success rate on open-ended tasks; (2) VPP2 surpasses the strongest baseline by 18.5\% points in success rate on real-world zero-shot ALOHA manipulation tasks; and (3) following benchmark-specific post-training, VPP2 achieves the highest success rates among evaluated methods on the challenging LIBERO-Pro, LIBERO-OOD, and RoboDojo benchmarks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.10270v1
- Authors: Yanjiang Guo, Haodong Yan, Zhide Zhong, Zhongru Zhang, Qingyuan Yang, Qingzhou Lu, Xiaoyu Chen, Yen-Jen Wang, Shuying Deng, Chenghan Yang, Puzhen Yuan, Chenxin Liu, Tun Ban, Xiang Zhu, Yichen Liu, Kun Feng, Haoang Li, Jianyu Chen
- Published: 2026-10-07T15:40:02Z
- Age days: 1

</details>
