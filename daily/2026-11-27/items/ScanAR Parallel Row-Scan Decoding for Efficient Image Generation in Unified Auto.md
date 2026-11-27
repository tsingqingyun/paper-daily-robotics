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
url: "https://arxiv.org/abs/2611.33761v1"
published: "2026-11-25T04:18:55Z"
age_days: 1
score: 30
created: 2026-11-27
concepts: ["多模态基础模型"]
---

# ScanAR: Parallel Row-Scan Decoding for Efficient Image Generation in Unified Autoregressive Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> ScanAR 把逐格生成图像改成先逐格生成首行，再一轮生成一整行。它复用统一自回归模型原有的词表和预测头，把视觉解码深度从 HW 降到摘要所写的 H+W。

## 问题

统一自回归模型用同一个预测头生成文本和图像。图像有 H×W 个视觉 token，逐格扫描时每格都要等上一格完成，串行等待就成了推理瓶颈。摘要指出，有些加速方案要改分词器、预测头或接口，另一些保留模型接口的方案很难兼顾高并行度和图像质量。

### 用一个例子理解

理解用例（非论文实验）。输入是“生成一张桌边放着红杯子的图”。假设图像编码成 3 行 4 列。模型先依次生成首行四格，随后从首行相应列的位置并行生成第二行四格，再从第二行生成第三行，最后把完整的视觉 token 网格还原成图像。

## 创新点或方法

ScanAR 改的是视觉 token 由哪个位置发起预测。第一行照旧从左到右生成；之后一行的各个位置，由上一行与它垂直对齐的位置发起预测，所以这些位置可以同一轮输出。文本等非视觉 token 保留原有的自回归规则。训练时可从头学习这种对应关系，也可在已有模型上做后训练。推理时按行调度，复用骨干、词表和输出头。垂直对齐描述的是预测位置的配对，摘要未说明注意力掩码让每个位置实际看到哪些上下文。

### 方法如何工作

1. 把图像位置看成行列网格，确定第一行之后每格对应上一行的哪个预测位置。
2. 用这种对应关系训练或后训练模型，使共享输出头学会按新的位置关系预测。
3. 推理时串行生成第一行，为后续每一列建立可用的预测位置。
4. 以上一行发起整行预测，重复到最后一行，再按模型原有方式把视觉 token 解码成图像。

### 必要术语

- 视觉 token：用离散编号表示的图像内容单元；本文按它们在网格里的位置组织预测。
- 解码深度：生成过程中必须前后等待的轮数；本文以按行并行减少这些轮数。
- 共享预测头：把模型内部表示映射到词表输出的模块；本文让图像和文本继续共用它。

## 证据

据摘要，Emu3.5-Image-34B 经后训练后，GenEval 为 82.36，在使用同样训练数据的后训练加速方法中最高。在相同推理设置下生成 512×512 图像，相比逐格解码快 13.8 倍。在 ImageNet 从头训练的实验中，作者报告每个测试模型尺寸的吞吐量均最高，FID 与逐格解码的 LlamaGen 相当。对 Xiaomi-Robotics-U0 34B，摘要报告具身场景、图文交错和视频生成的整体质量得以保持，但未给这些任务的具体指标。13.8 倍对应指定模型和设置。

## 局限

摘要没有说明逐行并行是否更容易破坏细线条、文字或横向纹理。我会查逐类样本及质量分布，并核对测速的硬件、批量大小和端到端计时范围。解码轮数下降和实测提速是两个需要分别判断的量。

- **判断**：值得读到训练目标、注意力掩码和计时设置。这几处决定能否复现逐行预测，也决定测到的速度和画质能否与你的设置直接比较。

## 研究关联

如果慢在模型必须接连做许多次预测，且输出有规则的空间布局，可以先检查哪些位置必须彼此等待。改变预测依赖能直接减少等待轮数，同时保留与其他模态共用的模型接口。

### 下一步读哪里

先看预测目标怎样从序列中的下一格改成下一行的同列格，再查注意力和缓存怎样配合行级解码。对照 GenEval、FID 和测速设置，核查各指标覆盖的模型、分辨率和批量。

- **概念**：多模态基础模型
- **筛选分数**：30
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-27/ScanAR Parallel Row-Scan Decoding for Efficient Image Generation in Unified Auto.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Unified multimodal autoregressive (AR) models represent text and images in one token sequence and generate all modalities with a shared next-token prediction head. Their image generation, however, decodes an $H\times W$ visual grid token by token in raster order, which takes $HW$ sequential steps and dominates inference time. Existing acceleration methods for visual AR generation either change the tokenizer, the prediction head, or the model interface, or keep the model but cannot reach high parallelism without losing quality, so they do not carry over to unified AR models. We propose ScanAR, a row-scan parallel decoding method that only redefines the predecessors of visual tokens. The first visual row is generated from left to right as usual, and each later row is generated in a single parallel step, with every token predicted from the vertically aligned token of the previous row. Nonvisual tokens keep the standard autoregressive rule. ScanAR reduces the visual decoding depth from $HW$ to $H+W$ without changing the backbone, vocabulary, or output head and without adding parameters, and it supports both training from scratch and lightweight post-training. On Emu3.5-Image-34B, ScanAR post-training reaches a GenEval score of 82.36, the best among post-training acceleration methods trained on the same data, and generates $512\times512$ images $13.8\times$ faster than raster decoding under the same inference setting. On ImageNet, ScanAR trained from scratch has the highest throughput at every model size with FID comparable to raster LlamaGen. On the 34B Xiaomi-Robotics-U0 model, ScanAR preserves the overall quality of embodied scene generation, interleaved image-text generation, and video generation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.33761v1
- Authors: Jingen Qu, Xi Chen, Yingbo Tang, Xinghang Li, Tao Kong
- Published: 2026-11-25T04:18:55Z
- Age days: 1

</details>
