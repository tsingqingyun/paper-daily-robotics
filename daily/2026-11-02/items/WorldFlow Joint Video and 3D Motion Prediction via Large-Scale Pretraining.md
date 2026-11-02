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
url: "https://arxiv.org/abs/2610.39278v1"
published: "2026-10-29T03:30:27Z"
age_days: 3
score: 29
created: 2026-11-02
concepts: ["世界模型", "具身智能评测与基准"]
---

# WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> WorldFlow 同时生成未来视频和指定三维点的运动轨迹，让“画面怎么变”和“物体实际往哪里走”一起学习。关键是把三维位移也变成生成单元，与视频共享注意力和去噪过程。

## 问题

任务是根据单张图、文字指令和三维查询点预测未来运动。视频模型把几何藏在像素里，先生成再追踪会增加恢复运动的环节；只学轨迹又浪费了视频提供的变化线索。动作条件模型还依赖特定机器人，查询点则能集中描述任务相关区域。[S3](https://arxiv.org/html/2610.39278v1#S0.F1) [S4](https://arxiv.org/html/2610.39278v1#S1.p1.1) [S5](https://arxiv.org/html/2610.39278v1#S1.p2.1)

### 用一个例子理解

理解用例（非论文实验）：输入桌面照片、“把杯子移到盘子右侧”和杯身查询点；模型联合生成搬动视频与这些点的三维位移，输出可视未来和杯子的运动路径，不直接输出机械臂关节命令。

## 创新点或方法

旧做法分开生成视频或轨迹；本文把带初始几何的位移单元对齐到视频时空网格，使两种输出在生成时交换信息。训练从预训练 Cosmos-Nano 初始化，用成对视频与轨迹联合流匹配，并约束位移、方向和终点；推理保留观测条件，从噪声联合生成，再把位移恢复为米制轨迹，使用40步采样。[S11](https://arxiv.org/html/2610.39278v1#S3.SS2.p1.1) [S12](https://arxiv.org/html/2610.39278v1#S3.F2) [S13](https://arxiv.org/html/2610.39278v1#S3.SS3.SSS0.Px1.p1.1) [S14](https://arxiv.org/html/2610.39278v1#S3.SS4.SSS1.p1.1) [S15](https://arxiv.org/html/2610.39278v1#S3.SS4.SSS2.p1.1) [S16](https://arxiv.org/html/2610.39278v1#S3.SS4.SSS2.p2.2) [S23](https://arxiv.org/html/2610.39278v1#S4.SS2.SSS0.Px2.p1.1) [S24](https://arxiv.org/html/2610.39278v1#S4.SS2.SSS0.Px2.p2.1) [S25](https://arxiv.org/html/2610.39278v1#S4.SS2.SSS0.Px2.p3.1)

### 方法如何工作

1. 编码图片和文字，并保留查询点初始几何，为未来预测提供场景与任务条件。
2. 把带噪位移嵌入并对齐视频网格，让轨迹生成能访问相关视觉变化。
3. 联合去噪视频和位移；训练额外约束局部运动与终点，减少轨迹累计偏差。
4. 解码视频，恢复位移尺度并从初始位置累加，得到米制三维轨迹。[S12](https://arxiv.org/html/2610.39278v1#S3.F2)

### 必要术语

- 查询点：指定要预测运动的三维位置；决定本文把几何输出集中在哪里。
- 联合流匹配：学习从噪声走向目标的变化方向；本文同时学习视频与位移的生成。
- ADE/FDE：整段平均位置误差/最终位置误差；分别检查路径与终点是否准确。

## 证据

单帧预测协议覆盖仿真 Sim7、真实交互 Real3 和空间指令 SpatialCog，对比直接轨迹生成及视频生成后追踪。三组 ADE 分别为0.051、0.081、0.060米，均优于所测学习方法，但 Real3 相对最强外部基线仅改善4.7%。同骨干、数据和优化的 flow-only 消融在 SpatialCog 的 ADE/FDE 为0.136/0.248米，联合生成降至0.060/0.078米，较直接支持视觉监督的作用。[S26](https://arxiv.org/html/2610.39278v1#S4.SS3.SSS2.p1.1) [S27](https://arxiv.org/html/2610.39278v1#S4.SS3.SSS2.p2.1) [S28](https://arxiv.org/html/2610.39278v1#S4.SS3.SSS2.p3.1) [S29](https://arxiv.org/html/2610.39278v1#S4.T1.3.1) [S30](https://arxiv.org/html/2610.39278v1#S4.T1) [S31](https://arxiv.org/html/2610.39278v1#S4.SS3.SSS3.Px1.p1.1)

## 局限

作者明确指出查询点须预先给定，自动提取的轨迹监督带噪声。[S35](https://arxiv.org/html/2610.39278v1#S5.p2.1) 真实视频上的预测不等于真机闭环控制；Real3 的静止参考 ADE 为0.062米，甚至低于模型0.081米，说明平均误差还须结合运动幅度解读。[S29](https://arxiv.org/html/2610.39278v1#S4.T1.3.1) 训练末期专门细化 SpatialCog，跨域收益不能直接等同于零样本迁移。

- **判断**：值得读到联合生成、查询点编码和受控消融：它较清楚地证明了视频监督能帮助轨迹预测，但控制收益仍待验证。

## 研究关联

值得借鉴的是：需要几何输出时，可以把几何直接纳入生成目标，同时利用视频监督，而不必把生成像素当作必经中间结果。同一生成器的视频交给追踪器，轨迹仍逊于直接输出，进一步支持这个选择。[S32](https://arxiv.org/html/2610.39278v1#S4.SS3.SSS3.Px2.p1.1)

### 下一步读哪里

先读[S11](https://arxiv.org/html/2610.39278v1#S3.SS2.p1.1) [S12](https://arxiv.org/html/2610.39278v1#S3.F2) [S13](https://arxiv.org/html/2610.39278v1#S3.SS3.SSS0.Px1.p1.1) [S14](https://arxiv.org/html/2610.39278v1#S3.SS4.SSS1.p1.1) [S15](https://arxiv.org/html/2610.39278v1#S3.SS4.SSS2.p1.1)，核查位移与视频位置如何对齐；再对照[S29](https://arxiv.org/html/2610.39278v1#S4.T1.3.1) [S30](https://arxiv.org/html/2610.39278v1#S4.T1) [S31](https://arxiv.org/html/2610.39278v1#S4.SS3.SSS3.Px1.p1.1) [S32](https://arxiv.org/html/2610.39278v1#S4.SS3.SSS3.Px2.p1.1)看联合生成和追踪的差别。复现前应确认三维查询点来源、域归一化尺度及训练测试划分。

- **概念**：世界模型 具身智能评测与基准
- **筛选分数**：29
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.39278v1
- 获取时间：2026-11-02T01:18:49.541486+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2610.39278v1#p1.1)
- [S2] [WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining · 正文段落 2](https://arxiv.org/html/2610.39278v1#abstract1.1)
- [S3] [WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining · 正文段落 3](https://arxiv.org/html/2610.39278v1#S0.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.39278v1#S1.p1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.39278v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.39278v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.39278v1#S1.I1.i2)
- [S8] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.39278v1#S1.I1.i3)
- [S9] [2.1 Predictive World Models: From Pixels to Actions · 正文段落 12](https://arxiv.org/html/2610.39278v1#S2.SS1.p1.1)
- [S10] [2.2 3D Motion Modeling: From Tracking to Forecasting · 正文段落 13](https://arxiv.org/html/2610.39278v1#S2.SS2.p1.1)
- [S11] [3.2 Architecture · 正文段落 20](https://arxiv.org/html/2610.39278v1#S3.SS2.p1.1)
- [S12] [3.2 Architecture · 正文段落 22](https://arxiv.org/html/2610.39278v1#S3.F2)
- [S13] [3.3 3D Flow Tokenization · 正文段落 24](https://arxiv.org/html/2610.39278v1#S3.SS3.SSS0.Px1.p1.1)
- [S14] [3.4.1 Joint flow matching · 正文段落 38](https://arxiv.org/html/2610.39278v1#S3.SS4.SSS1.p1.1)
- [S15] [3.4.2 Auxiliary motion objectives · 正文段落 41](https://arxiv.org/html/2610.39278v1#S3.SS4.SSS2.p1.1)
- [S16] [3.4.2 Auxiliary motion objectives · 正文段落 44](https://arxiv.org/html/2610.39278v1#S3.SS4.SSS2.p2.2)
- [S17] [4.1 Datasets · 正文段落 45](https://arxiv.org/html/2610.39278v1#S4.SS1.p1.1)
- [S18] [4.1 Datasets · 正文段落 46](https://arxiv.org/html/2610.39278v1#S4.I1.i1)
- [S19] [4.1 Datasets · 正文段落 47](https://arxiv.org/html/2610.39278v1#S4.I1.i2)
- [S20] [4.1 Datasets · 正文段落 48](https://arxiv.org/html/2610.39278v1#S4.I1.i3)
- [S21] [4.1 Datasets · 正文段落 49](https://arxiv.org/html/2610.39278v1#S4.I1.i4)
- [S22] [4.2 Training Configuration and Strategy · 正文段落 52](https://arxiv.org/html/2610.39278v1#S4.SS2.SSS0.Px1.p1.1)
- [S23] [4.2 Training Configuration and Strategy · 正文段落 53](https://arxiv.org/html/2610.39278v1#S4.SS2.SSS0.Px2.p1.1)
- [S24] [4.2 Training Configuration and Strategy · 正文段落 54](https://arxiv.org/html/2610.39278v1#S4.SS2.SSS0.Px2.p2.1)
- [S25] [4.2 Training Configuration and Strategy · 正文段落 55](https://arxiv.org/html/2610.39278v1#S4.SS2.SSS0.Px2.p3.1)
- [S26] [4.3.2 Quantitative Evaluation on WorldFlowBench · 正文段落 57](https://arxiv.org/html/2610.39278v1#S4.SS3.SSS2.p1.1)
- [S27] [4.3.2 Quantitative Evaluation on WorldFlowBench · 正文段落 58](https://arxiv.org/html/2610.39278v1#S4.SS3.SSS2.p2.1)
- [S28] [4.3.2 Quantitative Evaluation on WorldFlowBench · 正文段落 59](https://arxiv.org/html/2610.39278v1#S4.SS3.SSS2.p3.1)
- [S29] [4.3.2 Quantitative Evaluation on WorldFlowBench · 正文段落 61](https://arxiv.org/html/2610.39278v1#S4.T1.3.1)
- [S30] [4.3.2 Quantitative Evaluation on WorldFlowBench · 正文段落 62](https://arxiv.org/html/2610.39278v1#S4.T1)
- [S31] [4.3.3 Ablation Studies · 正文段落 63](https://arxiv.org/html/2610.39278v1#S4.SS3.SSS3.Px1.p1.1)
- [S32] [4.3.3 Ablation Studies · 正文段落 64](https://arxiv.org/html/2610.39278v1#S4.SS3.SSS3.Px2.p1.1)
- [S33] [4.3.3 Ablation Studies · 正文段落 65](https://arxiv.org/html/2610.39278v1#S4.SS3.SSS3.Px3.p1.1)
- [S34] [5 Conclusion · 正文段落 71](https://arxiv.org/html/2610.39278v1#S5.p1.1)
- [S35] [5 Conclusion · 正文段落 72](https://arxiv.org/html/2610.39278v1#S5.p2.1)
- [S36] [References · 正文段落 74](https://arxiv.org/html/2610.39278v1#p3.1)
- [S37] [A.2 Dataset Statistics · 正文段落 87](https://arxiv.org/html/2610.39278v1#A1.SS2.p3.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-02/WorldFlow Joint Video and 3D Motion Prediction via Large-Scale Pretraining.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Predicting future physical states stands as a central challenge in embodied intelligence. Existing video world models leave 3D dynamics implicit, action-based formulations remain tied to specific robot configurations, and 3D motion prediction models use flow-only supervision, providing a limited learning signal for physical dynamics. To circumvent these limitations, we introduce \method{}, a generative world model that jointly predicts future video and query-based 3D trajectories. By parameterizing 3D motion as continuous displacement tokens aligned with the video grid, a unified Mixture-of-Transformers (MoT) backbone jointly denoises both modalities under a rectified-flow objective. This formulation couples explicit geometric dynamics with visual evolution, effectively unlocking the physical commonsense embedded within pretrained video models. To empirically scale and validate this unified architecture, we train \method{} on a heterogeneous mixture of 1.44 million object-level samples spanning simulated and real-world domains. We further introduce WorldFlowBench, comprising 1,678 evaluation samples from 11 data sources across simulated and real-world interactions, including spatial reasoning tasks. Across all three evaluation sets, WorldFlow achieves the lowest average displacement error (ADE) and final displacement error (FDE) among the evaluated learning-based methods. Notably, on the challenging SpatialCog set, WorldFlow achieves an ADE of 0.060 m, a 54.2\% reduction compared with the strongest external baseline. It also reduces ADE and FDE by 55.9\% and 68.5\%, respectively, compared with its flow-only variant. Project page: https://worldflow-rbs.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.39278v1
- Authors: Yuhao Lu, Jiongxu Chen, Hexiang Wei, Jiajin Wu, Juelin Li, Mingjian Liang, Fan Yang, Zhuowei Liang, Zihao Liu, Zhennan Wang, Sheng Wang, Lin Shao
- Published: 2026-10-29T03:30:27Z
- Age days: 3

</details>
