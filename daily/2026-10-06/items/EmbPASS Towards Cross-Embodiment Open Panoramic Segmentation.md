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
url: "https://arxiv.org/abs/2610.03248v1"
published: "2026-10-02T12:58:24Z"
age_days: 3
score: 30
created: 2026-10-06
concepts: ["具身智能评测与基准"]
---

# EmbPASS: Towards Cross-Embodiment Open Panoramic Segmentation

> [!summary] 这篇论文到底做了什么（基于摘要）
> 同样是识别全景图里的道路、建筑和物体，换成无人机或四足机器人拍摄，模型就会遇到不同的视角与空间排列。EmbPASS 为这种跨平台分割建立统一测试集，并用 EPONet 的 RAMA 和 CAST 分别处理空间关系与语义迁移。

## 问题

任务是给覆盖周围 360 度的图像逐像素标注类别，还要支持开放词汇识别。真正的瓶颈是不同平台看到的场景结构不同：类别相同，也不意味着它们在图中的位置、尺度和关系相同。摘要指出，这类跨具身观察偏移缺少系统研究；它没有具体解释现有基线各自在哪种平台上失效。

### 用一个例子理解

理解用例（非论文实验）：输入一张四足机器人拍摄的全景图和待识别类别，EPONet 处理其中的空间关系并进行语义识别，输出每个像素的类别图；检查重点是低视角下的物体是否仍能被正确区分。

## 创新点或方法

通常在某种观察条件下学到的分割能力，未必能直接搬到另一种平台。本文先用统一类别体系组织车辆、无人机、穿戴设备和四足平台的数据，再在 EPONet 中加入关系感知度量适配器 RAMA 与内容自适应语义迁移 CAST，希望分别缓解空间建模和语义转移困难。摘要没有说明两者具体处理什么张量、如何训练，也没有交代推理时类别词汇如何输入；不能仅凭模块名补出实现。

### 方法如何工作

1. 把四类平台的数据映射到统一类别体系，得到可比较的标注，避免类别定义差异混入平台差异。
2. 将全景观察交给 EPONet，并用 RAMA 加强空间关系建模，以应对不同平台的观察布局；具体计算方式摘要未说明。
3. 用 CAST 做内容自适应语义迁移，服务开放词汇分割；训练目标与推理流程摘要只说明到此。
4. 输出像素类别并按平台平衡方式评估，检查综合表现是否改善；指标的具体汇总规则仍需核查。

### 必要术语

- 全景语义分割：给 360 度图像的每个像素分配类别；是本文的输出任务。
- 跨具身观察偏移：平台变化带来视角和空间布局变化；是本文要处理的主要困难。
- 开放词汇：识别范围可以涉及预设训练类别之外的语义；本文的具体类别协议待核查。
- mIoU：衡量预测区域与真实区域重合程度并对类别求平均；本文用它比较分割表现。

## 证据

摘要报告：EPONet 在 EmbPASS 上的平台平衡 mIoU 为 35.82%，比最强基线高 1.10%，并在已有全景分割基准上保持竞争力。这里的 1.10% 按摘要原文保留，其相对增幅或百分点口径未展开。结果支持综合指标上的优势，但缺少基线名称、各平台成绩、类别划分和消融，不能据此判断每个平台都改善，或优势主要来自哪个模块。

## 局限

摘要没有交代跨平台测试是否包含训练中未见的平台，也没有说明图像来自真实采集还是仿真。这些是待核查问题，直接影响它是在证明混合平台学习，还是更强的未知平台迁移能力。开放词汇的已见、未见类别设置同样需要确认。

- **判断**：值得先读基准划分与评分规则，再读 RAMA、CAST 的实现和消融；当前最清楚的贡献是把跨平台全景感知变成可比较的任务。

## 研究关联

值得借鉴的是把“换平台”单独作为评测变量，并统一类别定义。若只看混合数据上的总成绩，样本多或容易的平台可能掩盖困难平台；平台平衡评估能促使我们检查模型是否只是适应了主要数据来源。

### 下一步读哪里

我会先核查平台平衡指标的计算方式、训练测试的平台关系及开放词汇划分，再检查两个模块是否分别改善空间偏移与未见类别识别。还应确认数据来源、全景投影形式和使用预训练模型的条件。

- **概念**：具身智能评测与基准
- **筛选分数**：30
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-06/EmbPASS Towards Cross-Embodiment Open Panoramic Segmentation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Panoramic images provide a complete 360-degree field of view, enabling comprehensive scene understanding for embodied perception. However, heterogeneous embodied platforms exhibit substantial differences in observation viewpoints and spatial layouts, giving rise to cross-embodiment observation shifts that pose additional challenges to consistent and reliable panoramic perception, while systematic studies of this problem remain limited. To bridge this gap, we introduce a new task, termed Cross-Embodiment Open Panoramic Segmentation. Meanwhile, we establish EmbPASS, a multi-platform panoramic semantic segmentation benchmark spanning Vehicle, Drone, Wearable, and Quadruped platforms under a unified semantic taxonomy, providing a testbed for systematically studying cross-embodiment panoramic perception. We further propose EPONet, an open-vocabulary panoramic semantic segmentation network that integrates Relation-Aware Metric Adapter (RAMA) and Content-Adaptive Semantic Transfer (CAST) to enhance spatial modeling and semantic transfer under heterogeneous embodied observations. Extensive experiments show that EPONet achieves the best platform-balanced performance on EmbPASS with 35.82% mIoU, outperforming the strongest baseline by 1.10%, while remaining competitive on existing panoramic segmentation benchmarks. The source code and EmbPASS benchmark will be made publicly available at https://github.com/guopj1/EmbPASS.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.03248v1
- Authors: Pujun Guo, Yuanfan Zheng, Fei Teng, Mengfei Duan, Guoqiang Zhao, Yuheng Zhang, Kai Luo, Kailun Yang
- Published: 2026-10-02T12:58:24Z
- Age days: 3

</details>
