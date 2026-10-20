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
url: "https://arxiv.org/abs/2610.22951"
published: "Mon, 19 Oct 2026 00:00:00 -0400"
age_days: 0
score: 44
created: 2026-10-20
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# MambaAct: Efficient Mamba Action Experts for Flow-Matching Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> MambaAct 保留 π₀.₅ 的视觉语言编码部分，把反复生成动作的 Transformer 专家换成更小的 Mamba 专家。它先压缩视觉语言信息，再用压缩结果调节动作计算，减少每轮去噪的开销。

## 问题

机器人需要及时输出动作，而流匹配 VLA 要反复调用动作专家，逐步把带噪动作变成可执行动作。即使单次计算不算很慢，多轮重复也会累积延迟；动作专家因此成为明确的优化对象。

### 用一个例子理解

理解用例（非论文实验）：输入桌面图像和“抓起红杯子”；编码器产生视觉语言信息，压缩器形成条件，Mamba 专家反复修正带噪动作序列；输出可供机器人执行的一段动作。

## 创新点或方法

原动作专家使用 Transformer；本文用 Mamba 混合带噪连续动作序列中的信息，同时用 Context Compressor 把视觉语言前缀压成紧凑条件，门控并调节各个 Mamba 动作块，避免反复进行逐 token 交叉注意力。训练方面，摘要报告独立微调，但没有说明编码器是否冻结及具体损失；推理仍采用迭代去噪，改的是每次调用的计算。

### 方法如何工作

1. 用保留的预训练编码器处理图像与指令，得到任务条件。
2. 将前缀 token 压成紧凑信号，减少后续动作计算读取条件的成本。
3. 用条件调节 Mamba 动作块，并混合带噪动作序列中的依赖信息。
4. 反复调用动作专家完成去噪，最终得到动作序列；具体训练和采样细节摘要未说明。

### 必要术语

- 流匹配：学习把带噪样本逐步变成目标样本的生成方式；本文用于生成连续动作。
- 动作专家：专门生成动作的网络；本文替换并缩小这一部分。
- 交叉注意力：让一组表示逐项读取另一组信息；本文用压缩条件减少对此类重复计算的依赖。

## 证据

摘要称动作专家缩小至约十分之一，流匹配去噪延迟在 LIBERO 降低 64.8%，真机部署降低 58.8%。三个独立微调种子下，LIBERO 平均成功率增加 1.08 个百分点，并在 LIBERO-Plus 和真机基准维持收益。摘要未给硬件、绝对延迟和方差；这些结果支持减少动作生成开销，不能直接理解成整套机器人控制延迟同比下降。

## 局限

我的待核查问题是条件压缩会不会损失细粒度空间信息，以及收益是否依赖动作序列长度。成功率增加 1.08 个百分点需要结合方差判断稳定性；仿真与真机的延迟降幅也应分别看待。

- **判断**：若关注 VLA 实时控制，值得读到模块实现和计时设置；它的主要说服力是明确减少反复执行的计算。

## 研究关联

可借鉴的是先优化被反复调用的部分，并把昂贵条件信息压成便宜的调节信号。对于迭代动作生成，这能让一次结构改动在每轮计算中重复节省时间。

### 下一步读哪里

先查压缩条件如何注入动作块，再查模块消融；重点核对计时硬件、去噪步数、动作长度，以及包含视觉编码的端到端延迟。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：44
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-20/MambaAct Efficient Mamba Action Experts for Flow-Matching Vision-Language-Action.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.22951v1 Announce Type: new Abstract: Vision-language-action (VLA) models have shown strong promise for generalist robotic manipulation, but their inference cost remains a major bottleneck for real-time control. This limitation is especially pronounced in flow-matching VLAs such as $\pi_{0.5}$, where the action expert is evaluated repeatedly during iterative denoising. We introduce MambaAct, an efficient Mamba action expert for flow-matching VLA policies. MambaAct retains the pretrained visual-language prefix encoder of $\pi_{0.5}$, while replacing its transformer-based action expert with a compact Mamba-based action expert. Within this expert, Mamba serves as the action mixer that models dependencies across the noisy continuous-action sequence. To preserve visual-language conditioning without repeated token-level cross-attention, MambaAct uses a lightweight Context Compressor to map Vision-language model (VLM) prefix tokens into a compact conditioning signal that gates and modulates each Mamba action block. MambaAct uses a $10\times$ smaller action expert and reduces flow-matching denoising latency by $64.8\%$ on LIBERO and $58.8\%$ in real-world deployment, while improving mean LIBERO success by $1.08$ percentage points across three independent fine-tuning seeds and maintaining gains on LIBERO-Plus and real-world benchmarks. Our code and model weights are publicly available at https://github.com/giakhuyendihoc/MambaAct.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.22951
- Authors: Khuyen Pham, Tran Nguyen Le, Edoardo Fazzari, Cesare Stefanini
- Published: Mon, 19 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
