---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.38154v1"
published: "2026-09-29T17:58:49Z"
age_days: 0
score: 29
created: 2026-09-30
concepts: ["多模态基础模型", "世界模型"]
---

# LongLive-Plug: Once-for-All Distillation for Video Generation

> [!summary] 先说人话（基于摘要）
> LongLive-Plug 把视频生成加速和长上下文纠错能力蒸馏成可复用 LoRA，让兼容的下游模型直接挂载。目标是减少每个专用模型都重复蒸馏的成本。

## 问题

视频扩散模型分化出多种专用模型后，少步采样或长视频能力的蒸馏通常要逐个重复执行。相似能力不能复用，造成重复训练。

## 创新点或方法

在基础模型上分别学习单次前向 CFG、少步采样和自回归长上下文纠错 LoRA，再免训练迁移到兼容模型。CFG LoRA 可通过推理权重控制引导强度，并与少步 LoRA 组合；部分新增条件分支或扩展输出通道的模型也能使用。

## 证据

在三个骨干家族、八类任务的 54 个下游模型上验证免训练部署，任务包括世界建模、机器人、编辑和多模态生成。摘要未给出具体速度、质量或机器人任务收益数字。

## 局限

复用限定于兼容模型，且按骨干家族蒸馏；需核查兼容条件和跨任务质量损失，不能理解为任意模型通用。

- **判断**：维护视频世界模型系列者值得细读适配器兼容性实验，机器人策略研究者先看其动作预测保真度证据。

## 研究关联

对世界模型研究者，可能降低维护多种视频预测模型的重复蒸馏成本。对机器人研究的实际收益仍取决于加速后是否保留动作相关预测能力。

- **概念**：[[多模态基础模型]] [[世界模型]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/LongLive-Plug Once-for-All Distillation for Video Generation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Video diffusion models are increasingly developed into specialized models for diverse downstream tasks, and this development often includes a distillation stage, for example to accelerate sampling or to improve long-video generation. This stage is typically repeated for every specialized model. We introduce LongLive-Plug, a once-for-all distillation framework that learns reusable capabilities as LoRAs on a base model for training-free, plug-and-play deployment to compatible downstream models. These capabilities include single-pass classifier-free guidance, few-step sampling, and long-context error correction for autoregressive generation. The adapters remain reusable even when downstream models add conditioning branches, expand output channels. Despite training at a fixed guidance scale, our dedicated CFG LoRA provides text guidance control through its inference weight. Combining it with a few-step LoRA simultaneously preserves few-step generation and CFG controllability on downstream tasks. We verify training-free deployment on 54 downstream models across three backbone families and eight task categories, including world modeling, robotics, editing, and multimodal generation. The approach may support additional compatible models. Each capability can thus be distilled once per backbone family and reused without per-target retraining.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.38154v1
- Authors: Shuai Yang, Luozhou Wang, Wei Huang, ZhiFei Chen, Bohan Zhang, Xiao Fu, Qianli Ma, Chen-Hsuan Lin, Weian Mao, Bryan Chu, Song Han, Yukang Chen
- Published: 2026-09-29T17:58:49Z
- Age days: 0

</details>
