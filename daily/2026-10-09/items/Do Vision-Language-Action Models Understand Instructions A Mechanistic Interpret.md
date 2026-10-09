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
url: "https://arxiv.org/abs/2610.10178v1"
published: "2026-10-07T14:48:25Z"
age_days: 1
score: 30
created: 2026-10-09
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Do Vision-Language-Action Models Understand Instructions? A Mechanistic Interpretability Study on Language Grounding

> [!summary] 这篇论文到底做了什么（基于摘要）
> Language Grounding 通过改写指令并干预模型内部激活，检查 π₀.₅ 和 GR00T N1.7 的动作究竟怎样依赖语言。两者对方向词和空指令反应较强，但语言影响出现的位置，以及快速归因方法是否可信，都随模型而变。

## 问题

任务是在视觉语言动作模型中区分：动作来自指令，还是主要依赖画面和表面关联。仅看任务成功，难以知道语言是否真正参与决策。摘要指出，这类模型没有显式语言落地模块，而依赖视觉语言骨干的内在能力，因此需要控制指令变化并追踪动作生成内部的影响。

### 用一个例子理解

理解用例（非论文实验）：保持桌面图像不变，把“向左移动物体”改成“向右移动物体”。比较输出动作，再替换某层内部激活，观察方向变化是否随之改变，从而寻找语言影响动作的位置。

## 创新点或方法

从只观察改写指令后的输出，进一步用激活替换和归因替换检查内部因果作用。研究对 LIBERO 输入进行同义替换、语义尺度变化、方向破坏、随机物体替换和空字符串五种处理，再研究动作模块残差流中的影响位置。这是分析已有模型，不是训练新策略；具体激活替换方向、动作差异度量及采样设置，摘要未说明。

### 方法如何工作

1. 对同类输入构造不同指令扰动，得到可比较的语言条件，以减少视觉变化的干扰。
2. 比较动作生成反应，辨别模型对哪些语言内容敏感，但先不把敏感性等同于理解。
3. 干预动作模块残差流的激活，检查特定内部位置对输出差异的因果影响。
4. 比较归因替换、激活替换与表征几何，检验解释工具是否可靠，以及表示变化是否对应动作变化。

### 必要术语

- 语言落地：把指令含义联系到动作；本文检查这种联系是否实际发生。
- 激活替换：替换内部计算值并观察输出；本文用它检查因果影响。
- 归因替换：近似估计内部替换效应的方法；本文检验其可靠性。
- 表征几何：内部表示之间的相对结构；本文将其变化与动作效应比较。

## 证据

摘要报告两个模型对抽象改写和不存在物体的引用相对不敏感，对空指令尤其方向语言反应强。GR00T N1.7 的敏感性主要集中在早期、周期性出现的交叉注意力层；π₀.₅ 则分布在最早及部分后期层。GR00T 中，方向扰动可有较大因果效应，同时内部表征几何变化较小；π₀.₅ 未清楚呈现同样分离。归因替换与激活替换在 GR00T 上较一致，在 π₀.₅ 上不一致。摘要没有效应数值、成功率或误差范围。

## 局限

对语言变化敏感，并不自动等于正确理解；方向词可能强烈改变动作，却仍需检查改动是否符合任务。对不存在物体不敏感，也可能涉及视觉消歧。干预支持特定内部计算的因果影响，但范围限于所测模型和 LIBERO 输入，摘要没有真机部署证据。

- **判断**：值得深入读扰动设计与两种替换方法的对照，因为它既定位语言影响，也提醒我们解释工具不能跨模型直接照搬。

## 研究关联

值得借鉴的是先用直接干预校验便宜的归因工具，再用它解释模型。另一条启示是：内部表示看起来变化不大，也可能明显改变动作，不能单凭表示相似度认定指令无关紧要。

### 下一步读哪里

核查五类扰动是否改变任务可解性、效应怎样度量，以及激活替换使用什么参照；重点看归因替换在 π₀.₅ 上偏离的条件和表征几何指标的定义。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：30
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-09/Do Vision-Language-Action Models Understand Instructions A Mechanistic Interpret.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action models are designed to generalise across environments and task descriptions, raising the question of whether their action generation actually depends on the language instruction, or whether they largely rely on visual cues and superficial correlations. Robustness to variance in the visual and linguistic observation space is critical for real-world deployment, yet VLAs lack explicit grounding modules and instead rely on the intrinsic language grounding capabilities of their Vision-Language model backbones. For this reason, we conduct a controlled mechanistic interpretability study on the language grounding capabilities of two state-of-the-art Vision-Language-Action models, $π_{0.5}$ and GR00T N1.7, by applying activation and attribution patching to the residual stream of the action generation modules. We systematically corrupt the task instruction of input samples of the LIBERO benchmark following five strategies: synonym replacement, semantic scaling, directional corruption, random object substitution, and empty string. Our experiments find that both models are comparatively insensitive to abstract rephrasing and to referencing non-existent objects, but react strongly to empty task descriptions and, especially, to directional language. During action generation, this sensitivity is concentrated in different loci for each model: mainly in the early, periodic cross-attention layers for GR00T N1.7, versus distributed across the earliest and selected later layers for $π_{0.5}$. For GR00T N1.7, directional perturbations drive some of the largest causal effects while leaving the internal representational geometry comparatively unchanged, a dissociation we do not observe clearly for $π_{0.5}$. Finally, the reliability of attribution patching is model-dependent: it closely tracks activation patching for GR00T N1.7 but not for $π_{0.5}$.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.10178v1
- Authors: Theodor Wulff, Angelo Cangelosi
- Published: 2026-10-07T14:48:25Z
- Age days: 1

</details>
