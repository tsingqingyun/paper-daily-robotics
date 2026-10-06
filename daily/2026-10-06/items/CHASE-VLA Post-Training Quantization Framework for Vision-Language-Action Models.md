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
url: "https://arxiv.org/abs/2610.02666v1"
published: "2026-10-02T01:34:55Z"
age_days: 3
score: 28
created: 2026-10-06
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# CHASE-VLA: Post-Training Quantization Framework for Vision-Language-Action Models with Chunk-Aware Scale Estimation

> [!summary] 这篇论文到底做了什么（基于摘要）
> CHASE-VLA 要让 VLA 中反复运行的动作生成模块使用 4 位计算，同时保住任务成功率。它利用上一轮生成的动作段和当前去噪阶段调整量化尺度，避免一套固定尺度应付所有运动和阶段。

## 问题

VLA 从图像和语言生成连续机器人动作，其中扩散动作专家会在多次去噪和策略查询中反复调用。低位量化需要把数值压到有限档位，但激活范围会随去噪进度和计划运动改变。固定校准尺度可能截掉较大数值，或让较小数值失去精度，因此反复调用的模块尤其难压缩。

### 用一个例子理解

理解用例（非论文实验）：上一轮输出了“靠近杯子、夹住、抬起”的动作段，只执行了开头。新图像到来后，CHASE-VLA 将旧动作段连同当前去噪阶段交给尺度预测器，再用调整后的 4 位动作专家生成下一段动作；旧计划提供上下文，并不保证原样执行。

## 创新点或方法

旧做法主要依靠固定尺度匹配激活范围；CHASE-VLA 改为根据上一轮动作段与去噪步骤分组调整动作专家的激活尺度。上一轮动作段包含尚未执行的后续动作，可提供接下来运动的上下文，而且在当前查询前已生成，不需要偷看未来观察。它属于训练后量化，不修改预训练策略；量化准备阶段如何训练尺度预测器，摘要未说明。推理时预测器使用上述上下文，为动作专家的 MLP 和注意力投影提供 W4A4 量化所需尺度。

### 方法如何工作

1. 保留上一轮生成的动作段，包含未执行部分，得到当前查询可用的运动上下文。
2. 加入当前去噪步骤所属分组，补充动作专家所处的计算阶段，因为不同阶段的激活范围可能不同。
3. 据此调整激活量化尺度，使有限的 4 位档位更贴合当前数值范围；预测器具体结构摘要未说明。
4. 用 W4A4 的 MLP 和注意力投影继续生成动作段，减少这些反复调用线性层的存储和内存流量。

### 必要术语

- 训练后量化：在已有模型基础上降低数值位宽；本文无需修改预训练策略。
- W4A4：权重和激活都使用 4 位表示；本文用于动作专家中的指定线性投影。
- 量化尺度：连续数值与有限档位之间的换算间距；本文按运动上下文和去噪阶段调整它。
- 动作段：一次查询生成的一串动作；本文利用上一轮尚未执行的后续部分辅助尺度估计。

## 证据

摘要报告：在 LIBERO 上，π₀.₅ 的动作专家 MLP 和注意力投影均采用 W4A4 后，平均成功率为 97.3%，恢复到 FP16 水平，但未给出 FP16 的精确数字。被量化的动作专家线性层权重存储减少 73.4%；这些层的单动作段内存流量，在 π₀.₅ 和 GR00T N1.6 上分别减少 70.9% 和 71.2%。预测器开销最多占节省存储的 1.26%。这些是局部存储和流量结果，不能直接当作整个模型的压缩率或运行加速比。

## 局限

我的待核查问题是首轮没有历史动作段时如何处理，以及突发重规划时旧动作上下文是否失准。LIBERO 的成功率也不能直接证明真实机器人表现；摘要未报告真机验证、硬件延迟或整模型内存收益。

- **判断**：值得读到尺度预测器和实际部署测量，因为摘要给出了明确的精度与压缩证据，但是否更快仍需硬件结果支持。

## 研究关联

值得借鉴的是把策略自身已有的动作计划用作计算资源配置依据。输出不仅用于执行，也能帮助估计下一轮内部数值范围；当重复计算模块的分布随任务阶段变化时，这比始终使用固定尺度更有针对性。

### 下一步读哪里

优先核查尺度预测器的输入、校准数据和训练目标，再看没有历史动作、历史计划失效时的处理。实验重点检查固定尺度对照、去掉动作上下文或步骤分组的消融，以及实际硬件上的端到端延迟和总内存。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-06/CHASE-VLA Post-Training Quantization Framework for Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models map visual observations and language instructions to continuous robot actions, but a diffusion-based action expert (AE) poses a key challenge for low-bit post-training quantization (PTQ). The AE is repeatedly invoked across denoising steps and policy queries, where fixed calibration scales can be mismatched with activation ranges that vary with denoising progress and intended motion. We propose CHASE-VLA, a chunk-aware PTQ method that exploits a VLA-specific signal readily available from the policy: the generated action chunk, including its unexecuted future suffix. Rather than relying only on static scale matching for AE layers, CHASE-VLA combines the previously generated chunk as causal action context with denoising step group information to adapt AE activation scales. This enables W4A4 quantization of both MLP and attention projections in the repeated AE without modifying the pretrained policy. On LIBERO, CHASE-VLA achieves 97.3% average success rate on $π_{0.5}$ when both MLP and attention projections in the AE are quantized to W4A4, restoring FP16-level performance. CHASE-VLA also reduces the weight storage of the quantized AE linear layers by 73.4% and their single-chunk memory traffic by 70.9% and 71.2% on $π_{0.5}$ and GR00T N1.6, respectively, with a predictor overhead of at most 1.26% of the saved storage.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.02666v1
- Authors: Jin Hyun, Jung Gyu Min, Gyuhyun Jung, Youngjoo Lee
- Published: 2026-10-02T01:34:55Z
- Age days: 3

</details>
