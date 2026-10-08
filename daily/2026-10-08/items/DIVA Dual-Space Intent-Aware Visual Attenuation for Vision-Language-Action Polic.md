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
url: "https://arxiv.org/abs/2610.09144v1"
published: "2026-10-06T21:37:34Z"
age_days: 1
score: 27
created: 2026-10-08
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# DIVA: Dual-Space Intent-Aware Visual Attenuation for Vision-Language-Action Policies

> [!summary] 这篇论文到底做了什么（基于摘要）
> DIVA 让视觉语言动作策略根据任务，减弱无关画面对动作决策的影响。它保留所有视觉 token，但在进入主干前和主干内部都调低低相关内容的权重。

## 问题

任务是根据图像和语言要求输出机器人动作。常见 VLA 把密集图像块送入主干，保留了场景上下文，却没有显式机制控制不同图像块的影响强弱。瓶颈因此不只是看见什么，还包括背景或无关物体是否持续干扰当前动作。

### 用一个例子理解

理解用例（非论文实验）：输入“把杯子放进托盘”和桌面图像，背景有彩色海报；DIVA 估计各图像块与任务的关系，调低低相关内容的影响，再由 VLA 输出抓取与放置动作。这个例子说明处理链路，不代表论文验证过海报场景。

## 创新点或方法

旧做法把视觉块投影后交给主干处理；DIVA 先结合高层任务意图与低层视觉证据，为每个块估计相关性锚点。随后在入口重加权视觉 token，并在主干内部持续衰减低相关视觉状态。双处调节的动机是避免只在入口压低一次，后续计算仍让无关内容产生影响。它不删 token，也不需要外部定位监督。摘要没有说明训练损失、哪些参数更新或锚点的具体算法；推理时则用当前任务和视觉内容执行上述调节。

### 方法如何工作

1. 接收任务语言和视觉块，从意图与图像证据估计每块的相关性，为影响调节提供依据。
2. 在投影视觉 token 进入主干前重加权，让低相关内容从入口就减少影响。
3. 在主干内持续衰减低相关视觉状态，使相关性约束在后续计算中继续生效。
4. 保留完整视觉序列供策略生成动作；训练信号与动作生成细节，摘要只说明到此。

### 必要术语

- VLA：把视觉、语言与动作连接起来的策略；是 DIVA 调节的对象。
- 视觉 token：图像块转成的模型输入表示；DIVA 保留它们但改变影响强度。
- 相关性锚点：每个图像块与任务关联程度的估计；为两处衰减提供共同依据。
- 视觉衰减：减弱视觉表示参与计算的程度；区别于直接删除图像内容。

## 证据

摘要报告，在 LIBERO 上，DIVA 将 OpenVLA-OFT 平均成功率从 96.6% 提至 98.0%；零样本 LIBERO-Plus 分数从 69.6 提至 72.6。真机在与任务无关的视觉扰动下也有一致收益，但摘要未提供任务数、扰动种类、成功率或误差范围。因此有依据说它在所测基线和环境中有效，尚不能量化真机收益或判断跨模型普适性。

## 局限

关键风险是相关性估计出错：起初看似无关的障碍物，也可能影响动作安全；这是我的待核查问题，并非摘要报告的失败。还需核查两处衰减的独立贡献，以及真机扰动是否涵盖物体遮挡、位置变化等更复杂情况，不能把所述结果扩大为所有视觉变化下都稳健。

- **判断**：值得读到模块实现和双空间消融，重点确认收益来自任务相关调节，以及持续衰减是否确有必要。

## 研究关联

这里值得借鉴的是把“保留信息”和“控制影响”分开：场景内容不必被硬删，仍可按任务降低其参与决策的强度。当担心删掉视觉块会丢失上下文，但又确有无关干扰时，这种软调节值得尝试。

### 下一步读哪里

先检查相关性锚点怎样融合语言和视觉、衰减在哪些层执行、强度如何控制。再核查仅入口、仅内部和两者结合的消融，以及额外参数与推理耗时。真机部分应重点看扰动设置和保留潜在障碍信息的表现。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：27
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-08/DIVA Dual-Space Intent-Aware Visual Attenuation for Vision-Language-Action Polic.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) policies typically feed dense visual patch tokens into a language-action backbone, preserving scene context but offering no explicit mechanism to regulate how strongly different visual tokens influence policy computation. We introduce DIVA, a Dual-Space Intent-Aware Visual Attenuation module with an anchor-then-attenuate design. DIVA combines high-level task intent with low-level visual evidence to estimate patch-wise relevance anchors, then applies them in two complementary spaces: it reweights projected visual tokens before backbone entry and persistently attenuates low-relevance visual states within the backbone. DIVA preserves the full visual token sequence and requires no external grounding supervision. On LIBERO, DIVA improves OpenVLA-OFT from 96.6% to 98.0% average success and raises its zero-shot LIBERO-Plus score from 69.6 to 72.6. Real-world experiments further show consistent gains under task-irrelevant visual perturbations, supporting the robustness of intent-aware visual attenuation beyond simulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.09144v1
- Authors: Kaixi Feng, Guoheng Sun, Ziyao Wang, Yexiao He, Zheyu Shen, Ang Li
- Published: 2026-10-06T21:37:34Z
- Age days: 1

</details>
