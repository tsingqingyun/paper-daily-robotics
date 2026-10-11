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
url: "https://arxiv.org/abs/2610.12266v1"
published: "2026-10-08T16:32:28Z"
age_days: 2
score: 28
created: 2026-10-11
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# DVD: Dynamic Vector Decoding for Efficient MLLM-based Perception

> [!summary] 这篇论文到底做了什么（基于摘要）
> DVD 把框、掩码等几何结果转换成紧凑的离散 token，再用轻量解码器还原。这样，多模态模型不用逐个输出长串坐标文字，同时尝试缓解固定坐标量化的范围和精度限制。

## 问题

任务包括二维目标定位、掩码输出和三维框预测。瓶颈在于怎样让语言模型输出几何数据：坐标写成文本会消耗大量 token；把坐标映射到固定范围的格点，则限制可表示范围和定位精度。这对空间范围很大、又要求精确定位的三维任务尤其麻烦。

### 用一个例子理解

理解用例（非论文实验）：输入房间图像和“圈出椅子”的请求，模型输出代表椅子框的紧凑 token，解码器把它还原为坐标，应用据此绘制框。

## 创新点或方法

旧做法直接输出坐标文字或固定量化坐标；DVD 先把不同几何表示展平成一维向量序列，再在高维空间中映射为紧凑离散 token，最后通过轻量去 token 化器还原框或掩码。关键是让模型预测紧凑的几何编码，而不是承担冗长数字表达。训练阶段需要建立向量与 token 的映射并接入多模态模型，但码本如何学习、损失如何设置、是否联合训练，摘要未说明；推理阶段则明确包含输出 token 后的几何还原。

### 方法如何工作

1. 把框或掩码转换成一维向量序列，让不同感知输出进入统一表示流程。
2. 将向量映射成紧凑离散 token，减少模型需要生成的序列长度。
3. 让多模态模型输出这些 token；模型与编码器的具体训练关系，摘要只说明到此。
4. 用轻量解码器还原几何结果，从而交给定位、绘制或其他下游程序使用。

### 必要术语

- 量化：把连续数值归入离散类别；固定范围量化是本文要缓解的限制来源。
- 向量序列：按顺序排列的数值组；用于统一承载不同几何输出。
- 去 token 化器：把离散编码还原成几何数值的模块；决定压缩输出能否准确恢复。

## 证据

摘要列出 RefCOCO 系列、SUN-RGBD、KITTI、Hypersim 和 nuScenes，覆盖二维与三维感知，声称任务表现更好，token 开销和推理延迟明显减少。但未列对比方法、具体指标、数值、硬件和计时范围，因此只能确认作者报告了这些方向的收益，无法判断优势大小或端到端加速比例。

## 局限

我会核查紧凑编码是否牺牲细边界、小物体或远距离目标的精度，以及超出训练坐标范围时如何表现。摘要所说的范围限制得到缓解，并不能证明表示在任意空间范围内都可靠；也不能把感知成绩直接当成机器人控制效果。

- **判断**：值得读编码方法和效率实验，但在看到精度、压缩率与完整延迟的共同对比前，还不能判断它是否适合替换现有输出方式。

## 研究关联

当输出本身是结构化几何量时，可以先研究怎样编码输出，而不必默认把所有数字写成自然语言 token。值得尝试的条件是：解码成本和重建误差足够小，能抵消压缩编码引入的负担。

### 下一步读哪里

重点核查二维框、掩码与三维框怎样展平，离散编码怎样处理尺度和范围，重建误差如何衡量；再检查延迟是否包含视觉编码和去 token 化，并确认对比使用相同模型与硬件。

- **概念**：多模态基础模型 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-11/DVD Dynamic Vector Decoding for Efficient MLLM-based Perception.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Multimodal large language models have made remarkable progress in bridging vision and language, facilitating various perception tasks essential for human-machine interaction, robotics, and autonomous driving. However, existing MLLM-based perception methods predominantly rely on text-based coordinate representation, which suffers from excessive token overhead, or fixed-range quantization, which suffers from range and precision constraints, especially for 3D domains with unbounded spatial range and high localization accuracy requirements. To address these challenges, we propose a dynamic vector decoding method named DVD, which unifies the representation of 2D and 3D perception tasks. Specifically, we first transform diverse perceptual representation (i.e., 2D bounding boxes, 2D masks, and 3D bounding boxes) into 1D vector sequences, which are then mapped to compact discrete tokens in the high-dimensional space. Then, a lightweight de-tokenizer enables seamless integration with MLLMs by decoding output tokens back to original 2D and 3D perceptual representations. Extensive experiments on 2D and 3D perception benchmarks including RefCOCO series, SUN-RGBD, KITTI, Hypersim, nuScenes demonstrate that DVD achieves superior performance in 2D and 3D tasks and reduces significantly the token overhead and inference latency. DVD provides an efficient and general framework for integrating perception capabilities into MLLMs, overcoming the inherent limitations of existing methods.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12266v1
- Authors: Jinghua Hou, Zhe Liu, Hengshuang Zhao
- Published: 2026-10-08T16:32:28Z
- Age days: 2

</details>
