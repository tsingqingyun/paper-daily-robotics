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
url: "https://arxiv.org/abs/2610.37330v1"
published: "2026-10-27T14:37:30Z"
age_days: 1
score: 35
created: 2026-10-29
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Tokens of Motion: Primitive Motion Learning for Human-Humanoid Skill Transfer

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> M-PACT 把人手运动拆成可复用的局部表示，再用小型机器人专用解码器把它们变成运动。输入 abstract 实为另一方法 AFIL；这里依据与标题一致的正文[S1](https://arxiv.org/html/2610.37330v1#abstract1.1)及后续节选解释 M-PACT。

## 问题

任务是把人类操作经验迁移到人形机器人。直接模仿整条人手轨迹，既要学任务顺序，又要处理身体和运动范围差异，容易把局部动作与场景绑死，且人手可做的轨迹未必机器人可达。[S2](https://arxiv.org/html/2610.37330v1#S1.p1.1) [S5](https://arxiv.org/html/2610.37330v1#S1.p3.1) 本文要分开“可复用的运动结构”和“某个身体怎样实现它”。

### 用一个例子理解

理解用例（非论文实验）：输入人类把小盒子移到架上的手部轨迹；先切分并编码各段平移、转腕和开合，再由适配后的机器人解码器结合起始状态输出运动。这个过程不保证架子位置对机器人可达。

## 创新点或方法

旧做法整段迁移或按语义子任务分解；本文先用SkillSeg从三维手轨迹中学习局部分段，再由EPMT分别编码平移、旋转和手部开合。平移、开合离散化，旋转保留连续表示，并非所有运动都变成离散token。[S12](https://arxiv.org/html/2610.37330v1#S3.SS1.p2.1) [S18](https://arxiv.org/html/2610.37330v1#S3.SS4.SSS0.Px1.p1.2) 迁移时冻结分段器、编码器和词表，只训练目标身体的状态条件解码器。上下文预测扩展CC-EPMT则从片段起点的信息预测表示。训练需要运动轨迹；执行可解码给定表示，也可根据状态、视觉和指令预测下一片段。[S13](https://arxiv.org/html/2610.37330v1#S3.SS1.p3.1) [S31](https://arxiv.org/html/2610.37330v1#S4.SS3.p1.1)

### 方法如何工作

1. 把人手与机器人轨迹映射到可比较的状态约定，减小身体差异造成的表示偏移。
2. SkillSeg寻找局部运动边界，使重复运动不必绑定整条任务轨迹。
3. EPMT分别编码平移、旋转与开合，并学习从表示和初始状态还原运动效果。
4. 冻结共享表示，只适配目标解码器；需要自主执行时，再由上下文预测下一运动表示。

### 必要术语

- 运动原语：局部可复用运动单元；本文并不要求它对应预定义的语义子任务。
- 因子化表示：分别表示平移、旋转和开合；让不同运动成分可以单独编码。
- 身体专用解码器：将共享表示和当前状态映射为目标身体运动的模块；是迁移时主要适配部分。

## 证据

在EgoDex学习表示，HoloAssist测试冻结迁移，HumanoidEveryday适配机器人解码器。后者的端点平移、旋转、开合中位误差为3.442厘米、0.901度、0.229厘米；平移按人等效尺度报告。开合归一化误差1.388，反而不如保持不变。[S24](https://arxiv.org/html/2610.37330v1#S4.p3.1) [S27](https://arxiv.org/html/2610.37330v1#S4.T1.2.1) 分段对比中，学习分段的平移误差3.022厘米，固定窗口3.451厘米，但各方法目标片段不同，且学习版本为单种子前期模型。[S28](https://arxiv.org/html/2610.37330v1#S4.SS1.p2.1) [S29](https://arxiv.org/html/2610.37330v1#S4.T2) [S30](https://arxiv.org/html/2610.37330v1#S4.T2.2) 真机有重建、迁移及闭环操作定性展示，不能据此推出任务成功率。[S31](https://arxiv.org/html/2610.37330v1#S4.SS3.p1.1) [S32](https://arxiv.org/html/2610.37330v1#S4.SS3.p2.1)

## 局限

作者明确说明坐标对齐不保证机器人可达。[S15](https://arxiv.org/html/2610.37330v1#S3.SS2.p2.1) 主要量化证据是运动重建，重建准确不等于抓取和接触任务成功。正文摘要提到约100条机器人示范的适配，但所给结果未列这档数据量的具体误差；我的待核查问题是少样本曲线及上下文预测错误如何累积到真实执行。

- **判断**：值得深入读表示与解码分离的实验；目前最扎实的结论是运动词汇可复用，完整操作能力应另查闭环量化证据。

## 研究关联

可以借鉴的是把可复用表示固定下来，只重新学习身体相关的实现映射。它把“词汇迁移失败”和“新机器人解码失败”拆开检查，也避免每换身体就重学整套运动表示。

### 下一步读哪里

先沿[S14](https://arxiv.org/html/2610.37330v1#S3.SS2.p1.1) [S15](https://arxiv.org/html/2610.37330v1#S3.SS2.p2.1)检查坐标、臂长和开合校准，再读[S21](https://arxiv.org/html/2610.37330v1#S3.SS5.SSS0.Px1.p1.2)解码器训练；随后核查约100条示范对应的结果、CC-EPMT预测指标与真机成功统计，区分重建和自主选择能力。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.37330v1
- 获取时间：2026-10-29T00:42:06.448164+00:00
- [S1] [Tokens of Motion: Primitive Motion Learning for Human-Humanoid Skill Transfer · 正文段落 1](https://arxiv.org/html/2610.37330v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2610.37330v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.37330v1#S1.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.37330v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.37330v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.37330v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.37330v1#S1.I1.i1)
- [S8] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.37330v1#S1.I1.i3)
- [S9] [2 Related Work · 正文段落 10](https://arxiv.org/html/2610.37330v1#S2.p1.1)
- [S10] [2 Related Work · 正文段落 11](https://arxiv.org/html/2610.37330v1#S2.p2.1)
- [S11] [3.1 Framework Overview · 正文段落 13](https://arxiv.org/html/2610.37330v1#S3.SS1.p1.1)
- [S12] [3.1 Framework Overview · 正文段落 14](https://arxiv.org/html/2610.37330v1#S3.SS1.p2.1)
- [S13] [3.1 Framework Overview · 正文段落 15](https://arxiv.org/html/2610.37330v1#S3.SS1.p3.1)
- [S14] [3.2 Shared Cross-Embodiment Motion Representation · 正文段落 17](https://arxiv.org/html/2610.37330v1#S3.SS2.p1.1)
- [S15] [3.2 Shared Cross-Embodiment Motion Representation · 正文段落 18](https://arxiv.org/html/2610.37330v1#S3.SS2.p2.1)
- [S16] [3.3 SkillSeg: Self-Supervised Motion Segmentation · 正文段落 24](https://arxiv.org/html/2610.37330v1#S3.SS3.p2.2)
- [S17] [3.3 SkillSeg: Self-Supervised Motion Segmentation · 正文段落 25](https://arxiv.org/html/2610.37330v1#S3.SS3.p3.1)
- [S18] [Segment features and factorized encoding. · 正文段落 29](https://arxiv.org/html/2610.37330v1#S3.SS4.SSS0.Px1.p1.2)
- [S19] [Segment features and factorized encoding. · 正文段落 33](https://arxiv.org/html/2610.37330v1#S3.SS4.SSS0.Px1.p1.4)
- [S20] [Target-embodiment adaptation. · 正文段落 41](https://arxiv.org/html/2610.37330v1#S3.SS5.SSS0.Px1.p1.1)
- [S21] [Target-embodiment adaptation. · 正文段落 43](https://arxiv.org/html/2610.37330v1#S3.SS5.SSS0.Px1.p1.2)
- [S22] [4 Experiments · 正文段落 59](https://arxiv.org/html/2610.37330v1#S4.p1.1)
- [S23] [4 Experiments · 正文段落 60](https://arxiv.org/html/2610.37330v1#S4.p2.1)
- [S24] [4 Experiments · 正文段落 61](https://arxiv.org/html/2610.37330v1#S4.p3.1)
- [S25] [4.1 EPMT Reconstruction, Transfer, and Ablations · 正文段落 62](https://arxiv.org/html/2610.37330v1#S4.SS1.p1.1)
- [S26] [4.1 EPMT Reconstruction, Transfer, and Ablations · 正文段落 63](https://arxiv.org/html/2610.37330v1#S4.T1)
- [S27] [4.1 EPMT Reconstruction, Transfer, and Ablations · 正文段落 64](https://arxiv.org/html/2610.37330v1#S4.T1.2.1)
- [S28] [4.1 EPMT Reconstruction, Transfer, and Ablations · 正文段落 65](https://arxiv.org/html/2610.37330v1#S4.SS1.p2.1)
- [S29] [4.1 EPMT Reconstruction, Transfer, and Ablations · 正文段落 66](https://arxiv.org/html/2610.37330v1#S4.T2)
- [S30] [4.1 EPMT Reconstruction, Transfer, and Ablations · 正文段落 67](https://arxiv.org/html/2610.37330v1#S4.T2.2)
- [S31] [4.3 Real World Experiments · 正文段落 77](https://arxiv.org/html/2610.37330v1#S4.SS3.p1.1)
- [S32] [4.3 Real World Experiments · 正文段落 78](https://arxiv.org/html/2610.37330v1#S4.SS3.p2.1)
- [S33] [5 Conclusion · 正文段落 79](https://arxiv.org/html/2610.37330v1#S5.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-29/Tokens of Motion Primitive Motion Learning for Human-Humanoid Skill Transfer.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models provide a promising paradigm for scalable robotic manipulation, yet their reliance on success-only behavioral cloning leaves them brittle; lacking corrective training signals, minor execution errors rapidly compound into unrecoverable, out-of-distribution failures. To address this limitation, we propose Adaptive Failure-Informed Learning (AFIL), an end-to-end framework that leverages failure trajectories as adaptive negative guidance for diffusion- and flow-based VLA policies. AFIL uses a pretrained VLA to generate failure rollouts online, avoiding the need for handcrafted failure-mode design or human-in-the-loop recovery. It then jointly trains Dual Action Generators (DAGs) for successful and failed behaviors while sharing a common vision-language backbone, enabling efficient failure-aware policy learning with limited parameter overhead. During sampling, the failure generator adaptively steers action generation away from failure-prone regions and toward more reliable success modes, with guidance strength determined by the per-diffusion-step distance between success and failure distributions. Experiments across in-domain and out-of-domain robotic manipulation tasks, covering both short- and long-horizon settings, show that AFIL consistently improves task success rates and robustness over existing VLA baselines, demonstrating its effectiveness, efficiency, and generality.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.37330v1
- Authors: Hanwen Ren, Meng Zheng, Wenzhe Cui, Benjamin Planche, Zhongpai Gao, Anwesa Choudhuri, Terrence Chen, Ziyan Wu
- Published: 2026-10-27T14:37:30Z
- Age days: 1

</details>
