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
url: "https://arxiv.org/abs/2610.34717"
published: "Thu, 29 Oct 2026 00:00:00 -0400"
age_days: 0
score: 31
created: 2026-10-30
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# VLA-HWBench: Where the Time Goes When VLA Models Run on Edge Hardware

> [!summary] 这篇论文到底做了什么（基于摘要）
> VLA-HWBench 拆开测量 VLA 在机器人边缘硬件上的推理时间，发现动作如何生成比参数量更能解释快慢。它还显示，优化模型计算后，预处理和未融合算子可能成为下一处主要开销。

## 问题

机器人闭环控制需要及时得到动作，但任务成功率无法说明模型能否按时响应。摘要指出，既有分析覆盖的动作生成方式有限、阶段拆分最多只有三段，也缺少相同模型上推理优化的比较，因此难以判断该改模型、软件还是硬件。

### 用一个例子理解

理解用例（非论文实验）：输入两个候选 VLA 和相同观测；逐段测量图像处理、模型计算及动作输出耗时，发现总延迟差异主要来自动作生成次数，再据控制周期选择模型与优化位置。

## 创新点或方法

这是一项测量研究，没有提出新的策略训练法。它把 18 个开放 VLA 放到 NVIDIA Jetson AGX Thor 和 AMD Ryzen AI Max+ PRO 395 上，用七阶段拆分检查时间，并比较推理优化。分析把动作生成方式、参数量和阶段开销联系起来，再观察优化如何移动瓶颈。具体七阶段名称、输入形状和计时边界未在摘要列出。

### 方法如何工作

1. 在两种硬件上运行受测 VLA，获得具体配置下的推理延迟。
2. 将调用拆为七阶段，定位时间花在哪里；摘要未列出完整阶段定义。
3. 比较动作生成方式与参数量对延迟差异的解释，识别选型时更有用的特征。
4. 应用推理优化后重新测量，观察瓶颈转移，并据阶段特征判断软件或带宽限制。

### 必要术语

- 动作块：一次生成的一段连续动作；本文关注它如何影响推理与控制的时间关系。
- 内核融合：把多个计算操作合并执行；本文测量其与低比特权重结合的收益。
- 四比特权重：用较少位数存储模型权重；本文将其用于降低推理开销。
- 内存带宽：单位时间能搬运的数据量；本文发现它限制 Jetson 上部分少 token 阶段。

## 证据

摘要报告：动作生成策略在 Jetson 的 19 种配置中主导 14 种，延迟跨度在 Jetson 为 82 倍、AMD 为 157 倍，参数量最多解释 15% 的延迟方差。融合内核配合四比特权重，使 π₀.₅ 和 GR00T N1.7 比使用 torch.compile 的 PyTorch 快 2.6—2.9 倍，但仅覆盖这两模型的 Jetson 实现。GR00T N1.7 的 CPU 预处理时间占比从 12% 升至 39%。这些支持受测配置下的部署判断，不能当作所有 VLA 的固定速度排名。

## 局限

这是跨配置的性能分析，参数量解释度低不等于缩小模型没有因果收益。预处理占比增加也不代表它绝对变慢。我的待核查问题是各模型动作块长度、控制频率和精度是否可比；动作块长虽然摊薄生成成本，也需检查新观测何时能影响后续动作。

- **判断**：值得读到测量协议和逐阶段结果，它能帮助避免根据模型大小或单个算子速度做部署决策。

## 研究关联

最直接的启示是先检查动作生成轮数和整个调用过程，再凭参数量判断能否部署。模型算子加速后，应重新测量端到端时间，因为原来较小的 CPU 工作可能决定下一轮优化收益。

### 下一步读哪里

先核查七阶段边界、预热与同步方式、精度和批量设置；再看动作块长度及控制周期如何对应。还应确认融合与量化的加速是否伴随任务成功率变化，以及硬件瓶颈判断依据。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-30/VLA-HWBench Where the Time Goes When VLA Models Run on Edge Hardware.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.34717v2 Announce Type: replace-cross Abstract: Vision-language-action (VLA) models increasingly run on edge devices aboard robots, where inference latency constrains closed-loop robot control. However, it remains unclear how to design VLA models, their inference software and edge hardware so that robots can run VLA inference in real time. Most VLA models report only task success, while prior studies cover limited action-generation strategies, divide inference into at most three stages, and lack comparisons of inference optimizations on the same models. Therefore, we introduce VLA-HWBench, a benchmark that measures 18 open VLA models on NVIDIA Jetson AGX Thor and AMD Ryzen AI Max+ PRO 395, with a seven-stage inference breakdown. Our study reveals three insights. First, action-generation strategy matters more than model size. It dominates 14 of 19 Jetson configurations, latency varies by $82\times$ on Jetson and $157\times$ on AMD, and parameter count explains at most 15% of latency variance. Models that generate long action chunks in a few flow-matching steps keep up with control, whereas token-by-token decoding does not. Second, kernel fusion with 4-bit weights helps most, running $\pi_{0.5}$ and GR00T N1.7 2.6-2.9$\times$ faster than PyTorch with torch.compile, but it exists for only these two models and only on the Jetson. Optimization also moves the time to the stages it shortens least, as CPU preprocessing grows from 12% to 39% of the GR00T N1.7 call. Third, after optimization, memory bandwidth limits only the stages that process few tokens on the Jetson, such as the denoising steps, whereas software limits all other stages, from unfused kernels to serial preprocessing on the host CPU. Overall, low-latency edge VLAs should use few action-generation iterations, inference software should extend kernel fusion and low-bit weights to more models and platforms, and edge hardware needs high memory bandwidth and a fast host CPU.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.34717
- Authors: Borui Xu, Hongshi Tan, Wenqi Jiang, Bingsheng He, Ming Wu, Jason Zeng, Michael Heinrich
- Published: Thu, 29 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
