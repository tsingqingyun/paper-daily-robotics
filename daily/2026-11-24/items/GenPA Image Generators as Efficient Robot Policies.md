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
url: "https://arxiv.org/abs/2611.27446v1"
published: "2026-11-20T10:41:53Z"
age_days: 3
score: 33
created: 2026-11-24
concepts: ["世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# GenPA: Image Generators as Efficient Robot Policies

> [!summary] 这篇论文到底做了什么（基于摘要）
> GenPA 把预训练图像生成模型直接改成机器人动作预测器，并用它原有的图像训练方式辅助感知。部署时模型前向计算一次就回归一段动作，训练消融也表明，把当前场景的深度教给模型是一种有效配方。

## 问题

一类方法先让图像生成模型学会预测未来场景，再用这种能力辅助机器人控制。即使上线时已经省掉图像生成，训练里仍把未来预测当作主要视觉目标。GenPA 要检验的是，生成预训练习得的指令理解和空间感知能不能直接用于动作学习，以及控制究竟需要哪类额外视觉监督。

### 用一个例子理解

理解用例（非论文实验）。给机械臂一张桌面图像和把积木放进托盘的指令。训练时，示范动作教它怎么抓放，当前深度目标帮助骨干表示积木和托盘的空间位置。上线后策略读取观测，直接输出接下来一小段动作，例如靠近积木并准备夹取。

## 创新点或方法

GenPA 微调图像生成骨干，在上面接一个动作回归适配器，同时保留原有生成目标用于感知联合训练。借用骨干自带的图像编辑接口，同一套策略可以更换视觉训练目标，例如当前场景的深度、未来视觉预测或两者组合。这样可以在共同的架构里比较视觉目标。推理时只过一次骨干并回归动作块，省去生成视觉输出和对动作反复去噪。摘要没有说明深度标签来源或多项训练目标的权重。

### 方法如何工作

1. 从预训练图像生成骨干出发，接上摘要所述 1900 万参数的动作回归适配器，让视觉特征可以直接预测机器人动作。
2. 训练动作输出的同时，用原生图像编辑接口接入不同视觉目标，在共同策略架构下检验各监督配方。
3. 部署时做一次骨干前向并回归一段动作，让生成骨干的计算直接服务于控制输出。

### 必要术语

- 动作回归：从输入特征直接估计动作数值；GenPA 用它把视觉骨干接到机器人控制上。
- 当前深度监督：用当下场景中各处的距离作为训练目标；它让感知特征学习操作所需的空间几何。
- 动作块：一次输出的一小段动作序列；论文以它为单位报告推理耗时。

## 证据

摘要报告，GenPA 在仿真 LIBERO 和 LIBERO-Plus 的成功率分别为 99.10% 和 83.79%，也报告了真机操作结果，但未提供任务、成功率或对照细节。编译后在单张 H100 上，每个动作块耗时 20.9 毫秒，相对所选 VLA 和 WAM 基线加速 1.7 至 3.4 倍。摘要称当前深度监督在消融中有效，未列各配方成绩。这些证据支持所测任务和所报推理配置下的结论。

## 局限

我会核查深度监督的收益在哪些任务上最明显，以及深度标注的获取成本。20.9 毫秒是指定硬件和编译配置下每个动作块的推理数字，仍需查看计时是否包含预处理、传输和控制器开销，才能估算闭环延迟。

- **判断**：值得读到视觉目标消融和延迟拆解，分别确认当前几何监督的收益，以及单次前向实际节省的时间。

## 研究关联

借用生成骨干做控制时，可以把预训练学到的能力、训练时增加的视觉目标和上线时的输出分开设计。如果眼下的几何关系已经能解释操作失败，当前深度就值得作为低复杂度的训练对照。

### 下一步读哪里

核查动作适配器读取哪些特征、深度目标如何送进编辑接口，以及视觉目标对照是否使用相同数据和训练预算。延迟比较再核查动作块长度、编译条件和计时边界。

- **概念**：世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：33
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-24/GenPA Image Generators as Efficient Robot Policies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Pretrained visual generation models have shown great promise in robotic manipulation. However, a representative line of work still treats future visual prediction as the central link between visual generative pretraining and action learning, retaining it as a training objective even when future scenes are no longer generated at inference time. We argue that the instruction-following, spatial understanding, and visual imagination capabilities acquired through image generation pretraining can support control without future visual prediction: image generation models themselves can be directly adapted into powerful action learners. Building on this perspective, we propose GenPA, which fine-tunes an image generation backbone with a lightweight 19M-parameter action regression adapter and reuses its native generative objective for perception co-training. The native image-editing interface accommodates different visual targets without task-specific perception heads, enabling comparisons of current-scene perception, future prediction, and their combinations within a common policy architecture. At deployment, GenPA requires only a single backbone forward pass and action regression, without visual generation or iterative action denoising. Without additional large-scale robot-data pretraining, GenPA demonstrates strong control performance and robustness to perturbations across simulation benchmarks (99.10% success on LIBERO and 83.79% on LIBERO-Plus) and real-world manipulation tasks. Under compiled inference, GenPA takes 20.9 ms per action chunk on a single H100 GPU, achieving 1.7-3.4x speedups over strong VLA and WAM baselines. Our latency analysis further highlights architectural advantages of visual generation backbones for efficient robot control. Ablations across visual tasks and their combinations identify current-depth supervision as a simple, effective training recipe.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.27446v1
- Authors: Zian Deng, Tianyi Zhang, Zilong Zheng, Ziyu Liu, Tao Zhang, Yao Lyu, Shengbo Eben Li
- Published: 2026-11-20T10:41:53Z
- Age days: 3

</details>
