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
url: "https://arxiv.org/abs/2610.14155"
published: "Wed, 14 Oct 2026 00:00:00 -0400"
age_days: 0
score: 39
created: 2026-10-15
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Axiom-0: Hierarchical Self-Refinement for Vision-Language-Action Policies

> [!summary] 这篇论文到底做了什么（基于摘要）
> Axiom-0 在两个位置改善 VLA：训练时约束视觉语言模型的中间特征，生成动作前再递归更新动作所依赖的条件。它既处理“内部信息好不好”，也处理“这些信息怎样交给动作生成器”。

## 问题

任务是在不同任务、布局和物体交互中可靠操作，摘要特别指出陌生任务组合仍会让现有 VLA 表现受限。作者关注的不只是感知是否识别正确，而是预训练模型的表征能否被动作生成过程有效使用。

### 用一个例子理解

理解用例（非论文实验）：输入厨房图像和“把杯子移到盘子旁边”；视觉语言模型产生场景特征，经过训练约束的中间表征进入 VAIR，条件信息被递归更新后，动作生成器输出一段机械臂动作。

## 创新点或方法

相比直接把视觉语言特征接给动作生成器，Axiom-0 增加两层细化。IVRR 在训练中通过可学习的特征投影和一致性监督，强化选定中间层的特征；VAIR 在动作生成前递归更新条件信息。受监督的视觉语言层、VAIR 和动作生成器联合优化。推理时不再计算训练监督，但仍经过 VAIR 更新条件再生成动作；一致性的具体目标、递归次数和更新公式未说明。

### 方法如何工作

1. 视觉语言模型处理图像和指令，得到供动作使用的中间信息。
2. 训练时用 IVRR 监督选定特征，使其满足一致性要求；具体一致性定义摘要未说明。
3. VAIR 递归加工条件，再交给动作生成器，目的是改善表征到动作的衔接。
4. 联合训练相关层和动作模块，使两处改动共同服务动作学习；推理时按加工后的条件输出动作块。

### 必要术语

- IVRR：模型内部表征细化；通过训练监督改善选定中间特征。
- VAIR：视觉语言与动作接口细化；在生成动作前递归更新条件。
- 动作块：一次生成的一段连续动作；本文以其生成延迟衡量部分推理开销。

## 证据

摘要报告，Axiom-0 在其 RoboCasa365 评测中整体成功率为 62.32%，比最高已公布榜单成绩 Paimon-0 的 58.1% 高 4.22 个百分点，比 Xiaomi-Robotics-1 参考结果高 4.92 个百分点。所测性能分析设置下，平均动作块生成延迟比后者增加 1.7%。这些数字支持该评测中的成功率收益及有限的额外生成开销；摘要未交代同条件复测、统计波动或真机结果。

## 局限

榜单成绩与作者评测是否使用完全相同的任务分布和协议，需要核查。1.7% 只对应所测动作块生成延迟，不能直接推成整机响应时间；两个细化组件分别贡献多少，也需要消融结果支持。这些均是摘要尚未回答的问题。

- **判断**：值得细读两个细化组件的目标函数和消融实验，因为真正可迁移的是监督与接口设计，而不只是榜单上的增幅。

## 研究关联

可借鉴的是把“表征质量”和“表征如何驱动动作”拆开处理。已有视觉语言骨干却难以完成新任务组合时，可以检查中间信息是否受到合适监督，以及动作模块拿到的条件是否需要进一步加工，而不只扩大模型。

### 下一步读哪里

优先核查 IVRR 要求哪些特征保持一致、投影如何学习、VAIR 递归是否共享参数；再检查新组合任务划分、单组件消融及延迟测量条件。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-15/Axiom-0 Hierarchical Self-Refinement for Vision-Language-Action Policies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.14155v1 Announce Type: new Abstract: Reliable manipulation requires policies that generalize across tasks, layouts, and object interactions. Vision-language-action (VLA) models combine pretrained multimodal understanding with learned control, but their performance remains limited on unfamiliar task compositions. We present Axiom-0, a VLA policy that addresses both the quality of its representations and their use in action generation through hierarchical self-refinement. Intra-VLM Representation Refinement (IVRR) strengthens selected intermediate features through consistency supervision with learned feature projections during training. VLM-Action Interface Refinement (VAIR) recursively updates the resulting conditioning before action generation. Joint optimization of the supervised VLM layers, VAIR, and the action generator connects the two components. On RoboCasa365, Axiom-0 achieves 62.32% overall success in our evaluation, exceeding the highest published leaderboard score (Paimon-0, 58.1%) by 4.22 percentage points and the Xiaomi-Robotics-1 reference by 4.92 points. Under the evaluated profiling setup, mean action-chunk generation latency increases by 1.7% over Xiaomi-Robotics-1. These results demonstrate improved task completion with modest inference overhead.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.14155
- Authors: Renbin Shu, Jing Yang, Xiangyuan You, Guolin Qiu, Yufei Xia, Yiming Zhu, Nanjun Dai, Fei Zhang, Feng Wu, Keke Tang
- Published: Wed, 14 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
