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
url: "https://arxiv.org/abs/2610.41009v1"
published: "2026-10-29T21:42:17Z"
age_days: 4
score: 34
created: 2026-11-03
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# STAR: Steering Action Representations during Inference

> [!summary] 这篇论文到底做了什么（基于摘要）
> STAR 要解决的是：VLA 越接近输出动作，内部表示反而可能丢掉与任务有关的物体信息。它不重新训练模型，而是在推理时平滑后几层的表示更新，让较早层中与物体有关的更新方向继续影响最终动作。

## 问题

任务是根据图像和语言操纵物体。作者的探测实验发现，临近动作输出的表示没有充分保留视觉定位信息；模型看到了目标，并不保证生成动作时仍充分利用目标。这里针对的是预训练 VLA 原有计算过程中的信息保留问题，摘要没有比较其他修补方案为何失败。

### 用一个例子理解

理解用例（非论文实验）：输入“抓起红杯”和桌面图像；VLA 逐层计算动作时，STAR 将较早的物体相关更新部分保留到后层，并根据近期关节状态调整混合程度；输出仍是原动作接口上的机器人指令。

## 创新点或方法

旧做法让各层依次更新动作表示；STAR 对后几层的残差更新做指数移动平均，使当前更新继承前面更新的一部分，从而保留物体相关方向。它还读取近期本体状态来调节混合强度：执行动态变化快时更保守，避免过度沿用先前方向。训练阶段不变，推理阶段增加这些计算，权重和架构均不修改。具体层位、系数及状态变化的计算方式未说明。

### 方法如何工作

1. 图像和指令进入原 VLA，得到逐层变化的动作表示，为正常动作预测提供基础。
2. STAR 对后层残差更新做指数移动平均，让较早更新方向继续参与计算，以减少物体信息流失。
3. 近期本体状态用于调整混合强度，动态变化快时采取保守混合，降低旧方向干扰当前执行的风险。
4. 调整后的表示继续生成动作；摘要只说明到此，具体输出头和控制频率未交代。

### 必要术语

- 残差更新：一层给已有表示增加的改变量；STAR 平滑的是这些改变量。
- 指数移动平均：将历史量按逐渐衰减的权重混合；用于延续较早层的更新方向。
- 本体状态：机器人自身关节位置等状态；本文用近期状态调节混合强度。

## 证据

摘要报告，在机器人操作基准上，后层物体感知能力改善，平均任务成功率增加 4.0 个百分点。未给出基准名称、所用 VLA、物体感知指标、分任务成绩、试验次数及仿真与真机划分，也未明确全部对比对象。因此可以支持这批实验中的平均收益，尚不能判断收益是否普遍、稳定或集中在少数任务。

## 局限

作者明确报告了后层视觉信息保留不足，但摘要没有给出 STAR 的失效条件。我的待核查问题是：快速接触、目标切换时，旧方向会不会妨碍必要的新动作？物体感知和成功率同时改善，也不足以单独证明前者就是后者提升的原因。

- **判断**：值得读到更新公式和分任务消融，因为它提供了一种无需训练的具体干预，但是否好用取决于混合位置与动态调节。

## 研究关联

这里值得借鉴的是修补位置：当模型早期已经获得有用视觉信息，问题可能出在信息传到动作端的过程中。若探测证据也显示这种断裂，可以先尝试推理时保留更新方向，再决定是否投入重新训练。

### 下一步读哪里

先核查残差更新如何取出、哪些层参与平均，以及本体状态如何控制系数；再找不使用动态调节的消融、不同 VLA 的结果和推理开销。摘要没有正文节选，以上均需进一步核查。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-03/STAR Steering Action Representations during Inference.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action models (VLAs) map language instructions and visual observations to robot actions, showing strong capabilities across robotic manipulation tasks. However, in our probing experiment, we find that action representations near the action output do not fully preserve task-relevant visual grounding. Motivated by this late-layer grounding gap, we introduce STAR, for STeering Action Representations, a training-free inference method for pre-trained VLAs. STAR applies an exponential moving average over late-layer residual updates, allowing later action representations to inherit object-aware update directions from earlier layers without model updates or architectural changes. It further uses recent proprioceptive states to adapt the mixing strength, using conservative mixing when execution dynamics change rapidly. Experiments on robot manipulation benchmarks show that STAR improves late-layer object awareness and increases average task success rates by 4.0 percentage points. Our code is available at https://github.com/PKU-VaLuE-Lab/STAR.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.41009v1
- Authors: Guangyu Zhao, Yongchang Zhang, Haoxuan Ru, Kaichen He, Haoran Wen, Kun Zhan, Zeyu Zhang, Yin Li, Yiwu Zhong
- Published: 2026-10-29T21:42:17Z
- Age days: 4

</details>
