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
url: "https://arxiv.org/abs/2510.08464"
published: "Thu, 15 Oct 2026 00:00:00 -0400"
age_days: 0
score: 34
created: 2026-10-16
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered

> [!summary] 这篇论文到底做了什么（基于摘要）
> 这篇发现 VLA 剪枝后可能明显失去任务能力，并增加安全违规。GLUESTICK 利用原始模型和剪枝模型之间的权重关系，预先计算修正项，在推理时补偿损失，无需额外训练。

## 问题

机器人边缘设备受到体积、重量、功耗和成本约束，需要压缩模型。剪枝在语言和视觉语言模型中已有大量应用，但 VLA 研究较少；这里的危险是，删减权重不仅影响预测质量，还可能改变机器人的实际动作。

### 用一个例子理解

理解用例（非论文实验）：输入一个原始抓取 VLA 及其剪枝版本；GLUESTICK 根据两者权重计算纠正项；部署后每层带着修正执行，输出机器人动作，再实际测量成功率、违规、内存和延迟。

## 创新点或方法

旧做法直接使用剪枝后的权重，本文先通过谱分析研究 VLA 权重的结构与脆弱性，再在稠密模型和剪枝模型之间做权重空间插值，计算一次性的纠正项。推理时，每个剪枝层应用该项，以较小开销恢复能力。它不需要恢复训练，且不绑定某一种剪枝算法；纠正项的表示和计算公式，摘要未说明。

### 方法如何工作

1. 对 VLA 剪枝并测试行为，识别能力下降和安全违规增加，而不只统计参数减少量。
2. 分析权重的谱结构，寻找能解释剪枝脆弱性的性质；具体发现摘要未展开。
3. 利用稠密与剪枝权重的插值计算纠正项，为后续推理预先准备补偿。
4. 在剪枝层推理时应用纠正项，再检查能力恢复是否足以抵偿新增开销。

### 必要术语

- 剪枝：删去或置零部分权重以减少资源需求；本文研究它对动作能力的影响。
- 稠密模型：剪枝前保留完整权重的模型；本文将它作为能力基准和修正计算的参照。
- 谱分析：研究权重矩阵的谱性质；本文用它分析模型为何容易受剪枝影响。

## 证据

摘要称实验覆盖不同 VLA 架构与领域，相对剪枝模型可恢复能力，成功率最高恢复到原模型的 100%，安全表现接近稠密模型水平，同时最高节省 5 GB 内存、加速至 1.75 倍。但未提供任务名称、具体基线、稀疏率、安全违规定义及逐项结果。这些最高值不能默认来自同一配置，“恢复到 100%”也不等于所有任务都百分之百成功。

## 局限

我会核查谱结构与行为退化之间的证据：观察到对应关系，并不足以单独证明因果。还需要看纠正项的存储与计算成本是否已计入收益，以及安全测试在仿真还是真机中完成；摘要未区分。

- **判断**：有剪枝部署需求时值得读到公式和逐任务结果，关键是确认修正项怎样保留压缩收益，以及安全恢复是否稳定。

## 研究关联

可借鉴的是把压缩评估落实到动作后果：内存和速度达标后，还要重新测任务完成与安全行为。本文也提示，部分剪枝损失可能通过部署时的补偿恢复，不一定都要靠重新训练。

### 下一步读哪里

先核查插值系数如何确定、修正项是否保持稀疏计算优势；再逐配置对照成功率、安全指标、内存和速度，确认最高收益各自对应什么条件。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-16/Don't Run with Scissors Pruning Breaks VLA Models but They Can Be Recovered.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2510.08464v2 Announce Type: replace Abstract: Vision-Language-Action (VLA) models are a promising paradigm for field robotics, but their deployment is bottlenecked by strict edge SWaP-C constraints. Compression techniques such as quantization, distillation, and pruning are well-established for LLMs and VLMs. Pruning, however, remains particularly underexplored for VLA models. We surprisingly find that pruning VLA models yields drastic performance degradation and increased safety violations. Through spectral analysis, we identify structural properties of VLA weights that help explain this fragility. Based on this insight, we introduce GLUESTICK, a post-pruning recovery method that restores much of the original model's capability while preserving sparsity benefits. GLUESTICK computes a one-time corrective term by interpolating between the dense and pruned models in weight space. At inference, each pruned layer applies this correction to recover lost performance with minimal overhead. Our approach requires no additional training and is agnostic to the pruning algorithm. Across diverse VLA architectures and domains, GLUESTICK recovers up to 100% of the success rate and restores safety to near-dense levels, while saving up to 5 GB of memory and achieving up to 1.75x speedup. Additional material can be found at: https://gluestick-vla.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2510.08464
- Authors: Jason Jabbour, Dong-Ki Kim, Max Smith, Jay Patrikar, Radhika Ghosal, Youhui Wang, Ali Agha, Vijay Janapa Reddi, Shayegan Omidshafiei
- Published: Thu, 15 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
