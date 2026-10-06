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
url: "https://arxiv.org/abs/2610.02784v1"
published: "2026-10-02T04:19:13Z"
age_days: 3
score: 36
created: 2026-10-06
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# SimpleTouch: Can Vision-Language-Action Models Master Contact-Rich Manipulation Without Tactile Policy Pretraining?

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> SimpleTouch 给 π₀.₅ 增加独立触觉专家，让动作生成直接读取完整接触特征。它用任务示范同时教动作和未来触觉预测，在已有触觉编码器的前提下，省去额外触觉策略预训练和单独对齐阶段。

## 问题

插入、擦拭等任务中，画面相似也可能对应不同受力或滑动状态。触觉能补信息，但直接塞进视觉语言骨干未必能被正确使用；大规模触觉策略预训练或另做视觉触觉对齐又增加数据和阶段 [S3](https://arxiv.org/html/2610.02784v1#S1.p1.1) [S4](https://arxiv.org/html/2610.02784v1#S1.p2.1)。真正问题是少量示范怎样教已有策略使用接触信息。

### 用一个例子理解

理解用例（非论文实验）：输入插头图像、关节状态和指尖触觉，触觉专家保留局部接触差异，动作专家结合“插入”指令输出下一段移动；训练时再用后续触觉教它关注动作带来的接触变化。

## 创新点或方法

本文保留冻结 T3 编码器的全部当前触觉 token，交给独立 Transformer 处理，而非直接插入视觉语言骨干。动作专家每层通过注意力读取触觉缓存 [S16](https://arxiv.org/html/2610.02784v1#S3.SS3.p1.1) [S17](https://arxiv.org/html/2610.02784v1#S3.SS3.p1.2) [S18](https://arxiv.org/html/2610.02784v1#S3.SS3.p1.3)。训练共同更新视觉语言骨干、动作及触觉专家，并监督多个未来时刻的触觉特征；推理只处理当前触觉一次，反复复用缓存，不生成未来触觉 [S5](https://arxiv.org/html/2610.02784v1#S1.p3.1) [S6](https://arxiv.org/html/2610.02784v1#S1.p4.1)。

### 方法如何工作

1. 同步取得视觉、语言、身体状态和当前触觉，为同一次动作决策提供输入 [S11](https://arxiv.org/html/2610.02784v1#S3.SS1.p1.1)。
2. 冻结 T3 并保留完整当前 token，避免小数据训练破坏已有接触表示。
3. 触觉专家生成各层缓存，动作专家读取缓存，把接触细节转为行动依据。
4. 示范动作与多个未来触觉目标共同训练通路；部署仅使用当前缓存，省去预测生成。

### 必要术语

- 触觉表示预训练：先学如何描述接触；本文复用这种能力，并不从零学触觉。
- 触觉策略预训练：提前学触觉怎样影响行动；本文省去的是这一额外阶段。
- 多时域潜变量预测：预测多个未来时刻的压缩触觉特征；本文用它辅助训练。

## 证据

UniVTAC 六项仿真任务及四项真机任务，每方法每任务均用 50 条示范，分别测试 100 和 20 次 [S21](https://arxiv.org/html/2610.02784v1#S4.SS1.SSS0.Px1.p1.1)。指标为任务成功率的等权平均：仿真 77.5%，FTP-π₀.₅ 为 45.2%，预训练 FTP-1 为 66.7%，且六任务全部领先 [S23](https://arxiv.org/html/2610.02784v1#S4.SS2.SSS0.Px1.p1.1)。真机 71.3%，FTP-1 为 62.5%；USB 插入两者均只有 30% [S24](https://arxiv.org/html/2610.02784v1#S4.SS2.SSS0.Px2.p1.1)。这支持所测任务不必追加触觉策略预训练，不证明触觉预训练普遍无用。

## 局限

作者明确只测试视觉触觉传感器配平行夹爪，灵巧手、其他传感器及高频力控制尚未验证 [S31](https://arxiv.org/html/2610.02784v1#A6.p1.1)。节选给出消融定义和定性结论，未给对应数值，暂不能判断完整 token 与未来预测各贡献多少；真机每任务测试量也较小。

- **判断**：值得读到注意力接口和预测消融：关键是怎样让触觉参与行动，而不是仅增加一个传感器输入。

## 研究关联

可借鉴的是把“已有感知特征”与“学会据此行动”分开：保留接触空间细节，用独立通路和未来预测教策略使用它们，值得作为昂贵新预训练之前的尝试。

### 下一步读哪里

先看触觉缓存怎样进入各动作层 [S16](https://arxiv.org/html/2610.02784v1#S3.SS3.p1.1) [S17](https://arxiv.org/html/2610.02784v1#S3.SS3.p1.2) [S18](https://arxiv.org/html/2610.02784v1#S3.SS3.p1.3)，再核查未来预测的注意力屏蔽，避免训练泄漏未来信息；按 [S30](https://arxiv.org/html/2610.02784v1#A4.T9.2) 对照消融数值，确认预测收益与保留空间信息的收益。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：36
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.02784v1
- 获取时间：2026-10-06T00:12:09.049972+00:00
- [S1] [SimpleTouch: Can Vision-Language-Action Models Master Contact-Rich Manipulation Without Tactile Policy Pretraining? · 正文段落 1](https://arxiv.org/html/2610.02784v1#abstract1.1)
- [S2] [SimpleTouch: Can Vision-Language-Action Models Master Contact-Rich Manipulation Without Tactile Policy Pretraining? · 正文段落 2](https://arxiv.org/html/2610.02784v1#fig1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.02784v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.02784v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.02784v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.02784v1#S1.p4.1)
- [S7] [Generalist Policy Learning. · 正文段落 7](https://arxiv.org/html/2610.02784v1#S2.SS0.SSS0.Px1.p1.1)
- [S8] [Tactile Policy Learning. · 正文段落 8](https://arxiv.org/html/2610.02784v1#S2.SS0.SSS0.Px2.p1.1)
- [S9] [Pretrained Tactile Encoders. · 正文段落 9](https://arxiv.org/html/2610.02784v1#S2.SS0.SSS0.Px3.p1.1)
- [S10] [Pretrained Tactile Encoders. · 正文段落 10](https://arxiv.org/html/2610.02784v1#S2.F2)
- [S11] [3.1 Problem Formulation · 正文段落 11](https://arxiv.org/html/2610.02784v1#S3.SS1.p1.1)
- [S12] [3.1 Problem Formulation · 正文段落 13](https://arxiv.org/html/2610.02784v1#S3.SS1.p1.2)
- [S13] [3.1 Problem Formulation · 正文段落 14](https://arxiv.org/html/2610.02784v1#S3.SS1.p2.1)
- [S14] [3.2 Preserving Pretrained Tactile Features · 正文段落 15](https://arxiv.org/html/2610.02784v1#S3.SS2.p1.1)
- [S15] [3.2 Preserving Pretrained Tactile Features · 正文段落 16](https://arxiv.org/html/2610.02784v1#S3.E2)
- [S16] [3.3 A Tactile Expert as a Tactile–Action Interface · 正文段落 18](https://arxiv.org/html/2610.02784v1#S3.SS3.p1.1)
- [S17] [3.3 A Tactile Expert as a Tactile–Action Interface · 正文段落 20](https://arxiv.org/html/2610.02784v1#S3.SS3.p1.2)
- [S18] [3.3 A Tactile Expert as a Tactile–Action Interface · 正文段落 22](https://arxiv.org/html/2610.02784v1#S3.SS3.p1.3)
- [S19] [3.3 A Tactile Expert as a Tactile–Action Interface · 正文段落 23](https://arxiv.org/html/2610.02784v1#S3.F3)
- [S20] [4 Experiments · 正文段落 34](https://arxiv.org/html/2610.02784v1#S4.p1.1)
- [S21] [Benchmarks and Tasks. · 正文段落 35](https://arxiv.org/html/2610.02784v1#S4.SS1.SSS0.Px1.p1.1)
- [S22] [Baselines and Metrics. · 正文段落 36](https://arxiv.org/html/2610.02784v1#S4.SS1.SSS0.Px2.p1.1)
- [S23] [Simulation Results. · 正文段落 41](https://arxiv.org/html/2610.02784v1#S4.SS2.SSS0.Px1.p1.1)
- [S24] [Real-Robot Results. · 正文段落 42](https://arxiv.org/html/2610.02784v1#S4.SS2.SSS0.Px2.p1.1)
- [S25] [Real-Robot Results. · 正文段落 43](https://arxiv.org/html/2610.02784v1#S4.F5)
- [S26] [Future Tactile Prediction. · 正文段落 47](https://arxiv.org/html/2610.02784v1#S4.T3)
- [S27] [5 Conclusion · 正文段落 59](https://arxiv.org/html/2610.02784v1#S5.p1.1)
- [S28] [D.2 Representation and Prediction Ablations · 正文段落 122](https://arxiv.org/html/2610.02784v1#A4.SS2.p1.1)
- [S29] [D.2 Representation and Prediction Ablations · 正文段落 123](https://arxiv.org/html/2610.02784v1#A4.T9)
- [S30] [D.2 Representation and Prediction Ablations · 正文段落 124](https://arxiv.org/html/2610.02784v1#A4.T9.2)
- [S31] [Appendix F Limitations and Future Directions · 正文段落 143](https://arxiv.org/html/2610.02784v1#A6.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-06/SimpleTouch Can Vision-Language-Action Models Master Contact-Rich Manipulation W.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Tactile sensing provides essential contact information for robotic manipulation, yet incorporating it into pretrained vision-language-action (VLA) models remains challenging. A common concern is that simply introducing touch during task-specific fine-tuning may fail to bridge the cross-modal gap, yielding limited gains or even reduced success. Consequently, existing methods often rely on large-scale tactile policy pretraining or separate visuotactile alignment, adding data requirements and training stages. We introduce SimpleTouch, a simple VLA extension that augments $π_{0.5}$ with a tactile expert, to test whether these additional stages are necessary. Leveraging all tokens from a frozen pretrained tactile encoder, the expert learns from action supervision and multi-horizon prediction of future tactile latents. This single-stage training uses only task demonstrations, without additional tactile policy pretraining or separate alignment. With 50 demonstrations per task, SimpleTouch achieves the highest success rate among evaluated methods on all six UniVTAC tasks. Its average success rate reaches 77.5%, compared with 45.2% for FTP-$π_{0.5}$ and 66.7% for FTP-1, corresponding to gains of 32.3 and 10.8 percentage points, respectively. Across four real-world tasks, it averages 71.3%, exceeding FTP-1 by 8.8 percentage points. These results demonstrate that, given pretrained VLA and tactile representations, additional tactile policy pretraining is not a prerequisite for strong performance on these tasks, offering a simpler route to contact-rich manipulation. Project page: https://simpletouch-robot.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.02784v1
- Authors: Chen Yang, Linzhe Shi, Changjie Wu, Hang Zhang, Ronghan Chen, Lingjun Zhang, Xu Hu, Mu Xu, Jiansheng Fan, Chen Wang
- Published: 2026-10-02T04:19:13Z
- Age days: 3

</details>
