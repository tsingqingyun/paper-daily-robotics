---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.30965v1"
published: "2026-09-25T08:16:16Z"
age_days: 3
score: 32
created: 2026-09-28
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# FRAM: Trajectory-Guided Visual Feature Selection for Compact Language-Conditioned Robot Manipulation

> [!summary] 先说人话（基于摘要）
> FRAM 先预测末端将走过哪里，再沿这些位置从当前图像读取局部特征来生成动作。用未来运动指导视觉信息选择，让一个较小策略也能完成较强的语言条件操作。

## 问题

机器人操作 VLA 往往参数量较大；这里的任务是用紧凑策略保留操作表现。核心问题是如何筛选与即将执行的运动有关的视觉信息，而不是仅扩大模型。

## 创新点或方法

预测轨迹的图像坐标作为空间指针，读取当前图像局部特征，将动作所需信息组织为参考位置、视觉状态和未来运动。轨迹标签由示范与相机几何自动生成，无需人工标注。

## 证据

含冻结语言编码器共 138.7M 参数，四个 LIBERO 标准套件平均成功率 92.2%，对照 3.3B 参数 π₀ 为 94.2%；不额外训练的 LIBERO-Plus 为 67.3%。消融支持未来轨迹与局部特征的作用，真机双臂 UR5e 展示仅用腕部相机叠杯及选臂、换臂。

## 局限

参数量差异不能直接等同于速度或训练成本差异；需核查与 π₀ 的训练和评估条件，真机部分未给出成功率。

- **判断**：值得精读模型结构和轨迹预测消融，是今天小模型操作方向证据较具体的一篇。

## 研究关联

对紧凑 VLA 和机器人学习研究者，提供了将预测运动变成视觉选择机制的方案。基准、消融和真机展示分别支持性能、组件作用及执行可行性。

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/FRAM Trajectory-Guided Visual Feature Selection for Compact Language-Conditioned.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action models achieve strong performance in robot manipulation, but often require large numbers of parameters. In this work, we propose the Future Representation Action Model (FRAM), a small policy that explicitly links the future end-effector trajectory to the current visual input. FRAM uses the image coordinates of the predicted trajectory as spatial pointers and reads local visual features related to the motion from the current image. This organizes the information for action generation into the reference position (Where), the visual state (What), and the future motion (Future). Trajectory labels are generated automatically from demonstrations and camera geometry, so no manual annotation is needed. With 138.7M parameters, including a frozen language encoder, FRAM reaches an average success rate of 92.2% over the four standard LIBERO suites, close to the 94.2% of $π_0$ with 3.3B parameters. Without extra training, it also reaches an average of 67.3% on LIBERO-Plus. Ablations confirm that both the future trajectory and the local visual features improve performance and robustness. On a real dual-arm UR5e, FRAM stacks cups using only wrist cameras, including choosing and switching between the left and right arms. These results show that selecting visual information based on future motion is an effective way to obtain both high performance and robustness in a small robot policy.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.30965v1
- Authors: Hiroshi Ito, Hyogo Hiruma, Yoshiki Kanai, Takahiro Yoshida, Akira Kanazawa, Hiroki Yamada
- Published: 2026-09-25T08:16:16Z
- Age days: 3

</details>
