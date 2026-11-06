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
url: "https://arxiv.org/abs/2611.06918v1"
published: "2026-11-04T18:59:58Z"
age_days: 1
score: 33
created: 2026-11-06
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# From Pixels to Actions - Towards Native Vision-Language-Action Policies

> [!summary] 这篇论文到底做了什么（基于摘要）
> NEO-VLA 让动作模块从主干网络的不同层读取视觉线索。图像小块从一开始就和语言一起处理，因此策略有机会在边缘、深度或局部几何线索最清楚的层取用它们。

## 问题

常见视觉语言动作模型先用独立视觉编码器压缩图像，再把结果交给动作模块。识别桌上有一个插头和控制插头对准孔口，需要的视觉细节不同。如果末层表示把局部边界、几何或细小状态变化压弱，动作模块就只能用压缩后的信息来决策。

### 用一个例子理解

理解用例（非论文实验）｜输入相机画面和指令“把插头插进左边接口”。主干一起处理图像小块和指令，较深的表示可以帮助确定目标是左侧接口，中间层可能保有孔口边缘。动作模块读取这些表示，输出接近和对齐的动作。

## 创新点或方法

NEO-VLA 用轻量的图像小块卷积把像素转为视觉 token，省去独立的视觉编码阶段。视觉 token 与语言在主干里共同更新，再由采用流匹配的动作模块读取不同深度、受指令影响的表示。这样，控制决策可以利用仍保有局部细节的中间层。训练方面，摘要提到全量微调和扩大规模的对照，但未交代训练目标如何搭配或跨层连接怎样实现。推理时，动作模块根据图像和指令形成的表示生成动作。

### 方法如何工作

1. 用轻量卷积把图像小块变成 token，让主干直接处理来自图像的局部输入。
2. 让视觉和语言在主干各层一起更新，使不同深度的视觉表示都能受指令影响。
3. 让动作模块读取多个深度的表示，把中间层仍保有的细节带入控制决策。
4. 用流匹配动作模块生成动作。摘要只说明到此，未给出动作表示和生成过程的实现细节。

### 必要术语

- 视觉 token：供网络处理的图像小块表示；NEO-VLA 用轻量卷积生成它们。
- 流匹配：学习怎样把简单的初始分布逐渐变成目标数据分布；本文用它生成机器人动作。
- 逐层探测：分别检查每层表示能读出哪些信息；本文用它定位动作相关信号较强的深度。

## 证据

摘要称，在受控比较中，NEO-VLA 这类原生结构优于带视觉编码器的结构。全量微调缩小了差距，单靠扩大规模也未追回差距。逐层探测显示，动作所需信号往往在末层之前最强。作者还报告不同操作设置和分布变化下的控制表现更稳，但摘要未列任务名称、指标、分数，也未区分仿真与真机结果。

## 局限

逐层探测说明某些信息容易从中间层读出来。要判断动作模块是否真的靠这些信息改善控制，我会查只改读取层的消融，同时核对数据、参数量和训练算力是否匹配。摘要也不足以判断鲁棒性结果能否外推到真机。

- **判断**：值得细读受控架构对照和逐层探测，并把两组结果对着看，才能判断哪种跨层读取值得复用。

## 研究关联

如果策略能识别物体，却总在最后几毫米对准失败，可以先测局部几何信息在哪些层仍然容易读出，再试让动作模块接入那些层。这样能把问题缩小到动作模块能拿到什么信息，并给架构改动一个可测的依据。

### 下一步读哪里

先查动作模块实际读取哪些层、用什么方式融合，再看只读末层的消融、探测的具体信号，以及全量微调和扩大规模时对照如何配平。

- **概念**：多模态基础模型 视觉语言动作模型 VLA
- **筛选分数**：33
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-06/From Pixels to Actions - Towards Native Vision-Language-Action Policies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action models are typically built on a simple premise: perception is first compressed by visual encoders, and action reasoning begins only afterwards. Yet manipulation often hinges on precisely the visual signals most vulnerable to this abstraction, e.g., local geometry, boundaries, depth, and subtle state changes. This raises a fundamental question: should action policies inherit a fixed visual endpoint, or directly access evolving visual computation? We introduce NEO-VLA, a structurally encoder-free vision-language-action framework. Images are tokenized by lightweight patch convolutional layers and evolve jointly with language throughout the backbone, allowing a flow-matching action expert to draw from instruction-conditioned visual representations at different depths. This simple change reveals a consistent pattern. Native architectures outperform encoder-based counterparts under controlled comparisons; full fine-tuning reduces but does not erase the gap, and additional scale alone cannot recover it. More strikingly, layer-wise probing shows that the action-critical signals often peak well before the final visual representation. Across diverse manipulation settings and distribution shifts, NEO-VLA consequently achieves stronger and more robust control. Together, these results suggest that embodied control benefits from access to visual representations across the computational hierarchy, rather than a fixed encoder output.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.06918v1
- Authors: Weichen Fan, Haiwen Diao, Penghao Wu, Siyuan Hu, Ziqi Huang, Tianqi Liu, Mingze Sun, Ziyi Wang, Zhongang Cai, Hanming Deng, Quan Wang, Lei Yang, Lewei Lu, Fangzhou Hong, Zhaoxi Chen, Dahua Lin, Ziwei Liu
- Published: 2026-11-04T18:59:58Z
- Age days: 1

</details>
