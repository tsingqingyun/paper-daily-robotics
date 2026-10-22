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
url: "https://arxiv.org/abs/2610.27698"
published: "Wed, 21 Oct 2026 00:00:00 -0400"
age_days: 0
score: 38
created: 2026-10-22
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs

> [!summary] 这篇论文到底做了什么（基于摘要）
> VLA-Retain 检查视觉微调的副作用：模型适应新视角或传感器噪声后，其他变化条件下是否退步。它把每个微调模型与自己的原始版本比较，发现目标条件涨得多，并不能说明其他能力保留得好。

## 问题

任务是评估 VLA 针对视觉条件适配后的操作鲁棒性。已有鲁棒性评测只看未微调模型，适配研究又常只报告目标条件收益，因此看不清修复一个维度是否损伤另一个维度。要回答它，还必须排除架构差异，以及无扰动任务整体退步带来的混淆。

### 用一个例子理解

理解用例（非论文实验）：输入基础策略及侧面相机示范，先微调视觉模块；随后分别测试新视角、光照变化和噪声条件，输出各维度相对基础策略的成功率变化，检查新视角收益是否伴随其他退步。

## 创新点或方法

从“只报告适配目标上的提升”，改成同时比较目标与非目标维度。五个开放 VLA 分别在相机视角或传感器噪声数据上微调，再与各自基础检查点比较，在 LIBERO-Plus 的七个扰动维度上测试。研究还比较更广训练覆盖与不同调参策略。训练阶段改变视觉适配方式，推理阶段测结果；具体更新哪些参数、训练量如何匹配，摘要未说明。

### 方法如何工作

1. 为每个 VLA 保留基础检查点，建立同模型对照，减少架构差异干扰。
2. 分别用视角或噪声数据微调，形成有明确目标条件的适配版本。
3. 在七个扰动维度测试并分别计算目标与非目标变化，揭示收益是否伴随能力损失。
4. 结合无扰动对照、扩大数据覆盖和不同调参策略，检查退步能否由一般性能损失解释，以及是否容易缓解。

### 必要术语

- 目标维度：微调直接针对的变化条件；用于衡量适配收益。
- 非目标保留：其他变化条件下的能力是否保住；本文用相对基础模型的变化检验。
- 百分点：两个百分率直接相减的单位；不同于相对提升百分比。
- DELTA 式特征保持：约束适配后的特征保留原有信息的思路；本文比较其对不同模型的影响，具体形式未说明。

## 证据

摘要报告，10 个模型—训练域组合中有 8 个平均非目标收益为负。视角微调后，X-VLA 目标提升 69.4 个百分点，其他维度平均下降 4.6 点；OpenVLA-OFT 分别提升 39.3 和 1.4 点。DELTA 式特征保持使 X-VLA 平均非目标收益达到 +1.2 点，却使 OpenVLA-OFT 降至 −23.1 点。摘要还称无扰动任务的退步不能完全解释这些回归，扩大覆盖也未消除逐维度退步。缺少绝对成功率、置信区间及具体条件结果。

## 局限

这些结果证明所测设置中的收益与退步并存，还不能解释内部机制。特征保持策略在两个模型上方向相反，也不足以单独确定是哪项架构差异导致；需要控制变量。基准结果不能直接代替真机长期部署验证。

- **判断**：值得细读实验设计与逐维度结果；它最有用的贡献是改变适配成功的判据，而不是给出一种通用最佳微调法。

## 研究关联

直接可借鉴的是给适配实验加一张“非目标条件成绩单”，并始终与同模型原始版本比较。这样才能看出一次微调究竟扩大了可用范围，还是用其他条件的能力换来目标涨分。

### 下一步读哪里

先查七个扰动维度与训练测试划分，再看逐模型结果、无扰动对照和随机种子；重点核查 DELTA 式约束施加在哪些特征上，以及不同训练覆盖是否使用可比预算。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-22/VLA-Retain Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.27698v1 Announce Type: cross Abstract: Vision-language-action (VLA) models transfer knowledge from large-scale pretraining into robot control, but their manipulation performance remains sensitive to changes in observation conditions, which recent work addresses by fine-tuning the visual module on target-domain data. However, it remains unclear how such adaptation affects robustness beyond the target condition, as existing robustness benchmarks only evaluate models without fine-tuning and adaptation studies only report the target gain. Measuring this cross-dimension effect requires separating target gains from off-target changes, isolating adaptation effects from architectural differences, ruling out generic forgetting, and comparing tuning choices. Therefore, we introduce VLA-Retain, a benchmark that compares five open VLA models, tuned on Camera-view or Sensor-noise data, with their own base checkpoints on LIBERO-Plus dataset spanning seven perturbation dimensions. Our study reveals four findings. First, targeted vision tuning is not local, and its target gain does not predict retention. Mean off-target gain is negative in 8 of 10 model--domain configurations. Under Camera-view tuning, X-VLA gains $69.4$ percentage points on the target but loses $4.6$ points on average elsewhere, whereas OpenVLA-OFT gains $39.3$ and $1.4$ points, respectively. Second, these regressions are not explained only by performance loss on the same tasks without perturbations. Third, broader training coverage raises overall gain over target-specific training but does not eliminate dimension-level regressions. Fourth, tuning strategies are model-dependent, as DELTA-style feature preservation raises X-VLA's mean off-target gain to $+1.2$ points but lowers OpenVLA-OFT's to $-23.1$. Overall, these findings show that target-domain success alone is insufficient and highlight cross-dimensional retention as a key criterion for targeted VLA adaptation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.27698
- Authors: Borui Xu, Han Chen, Bingsheng He, Ming Wu, Jason Zeng, Michael Heinrich
- Published: Wed, 21 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
