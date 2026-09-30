---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.04958"
published: "Mon, 07 Sep 2026 00:00:00 -0400"
age_days: 0
score: 30
created: 2026-09-08
concepts: ["多模态基础模型", "机器人学习", "具身智能评测与基准"]
---

# MINT: A Unified Model for World-Space Camera and Hand Motion Estimation from Scalable Egocentric Pipeline Supervision

> [!summary] 先说人话（基于摘要）
> MINT 从第一视角 RGB 视频联合估计相机与双手运动，再转换为世界坐标轨迹。它借助 EGOPIPELINE 生成的大规模伪标签训练统一模型。

## 这篇到底在做什么

- **卡在哪里**：现有系统将相机运动、深度、手部重建和轨迹修正拆成多个阶段，计算开销大且难以联合建模；高质量联合标注又稀缺。
- **关键解法**：共享时空视频表征同时预测相机轨迹、相机坐标系手部状态和逐帧手部存在性，通过显式坐标变换得到世界坐标手轨迹；先伪标签预训练，再用少量高质量标注微调。
- **拿什么证明**：报告发布 1,021 小时轨迹数据，并声称可零样本泛化到未见数据集；准确率改进和加速数字均为“[xxx]”占位符，摘要未给出可核查的性能结果数字。

## 值不值得读

- **和你的研究有什么关系**：对机器人学习，潜在价值是将人类第一视角视频转成几何轨迹监督；摘要尚未展示这些轨迹用于机器人训练的收益。
- **先别急着信**：结果占位符直接限制证据可信度，需优先核查完整结果及伪标签的几何误差。
- **判断**：先看数据与标注流水线，性能判断暂缓；完整数字补齐后再决定是否精读模型。

## 研究关联

- **概念**：[[多模态基础模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-08/MINT A Unified Model for World-Space Camera and Hand Motion Estimation from Scal.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.04958v1 Announce Type: cross Abstract: Recovering camera and hand motion in world coordinates from egocentric video is a key capability for activity understanding, robot learning, and augmented reality. Existing systems typically decompose this problem into separate stages for camera motion, depth, hand reconstruction, and trajectory refinement, resulting in substantial computational overhead and preventing the joint modeling of camera and hand motion. We introduce MINT (Minting IN-the-Wild Trajectories), the first foundation model that directly produces complete world-space two-hand trajectories from ego-centric RGB video. From a single shared spatiotemporal video representation, MINT jointly predicts the camera trajectory, camera-frame hand states, and per-frame hand presence, and then produces world-space hand motion via explicit coordinate transformations. Training such a model at scale is challenging, since paired world-space camera and hand annotations are scarce. We therefore develop an open-source labeling EGOPIPELINE that converts large collections of public egocentric videos into structured camera-and-hand trajectory supervision. MINT is first pretrained on these large-scale pseudo-labels and then fine-tuned on a small set of high-quality joint annotations. Across public benchmarks, MINT achieves [xxx] improvement in world-space hand trajectory accuracy, [xxx] improvement in camera trajectory estimation, and [xxx] faster end-to-end trajectory generation than the labeling pipeline, while generalizing zero-shot to unseen egocentric datasets. We release the model, training and inference code, labeling pipeline, and a curated 1,021-hour egocentric trajectory dataset.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.04958
- Authors: Zijie Zhu, Weiren Cai, Yizhou Wang, Zhenjie Yang, Yide Liu, Jiahao Chen, Guanqi He
- Published: Mon, 07 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
