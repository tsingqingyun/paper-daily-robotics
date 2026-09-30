---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.23478v1"
published: "2026-08-24T16:42:49Z"
age_days: 1
score: 38
created: 2026-08-26
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Act with Intent: Distilling Behavior Intent for Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> On SimplerEnv-Bridge, INDI improves GR00T-N1.7 from 64.3% to 84.7%, and on RoboCasa Kitchen it improves the controlled GR00T-N1.7 baseline from 64.1% to 70.3%, with consistent gains on $π_{0.5}$ across both benchmarks.

## 问题

Vision-Language-Action (VLA) models can turn multimodal context into robot actions, but their action decoders are still trained largely by behavior cloning.

## 创新点或方法

We propose Intention Distillation (INDI), which distills behavior-level intent into the action decoder.

## 证据

On SimplerEnv-Bridge, INDI improves GR00T-N1.7 from 64.3% to 84.7%, and on RoboCasa Kitchen it improves the controlled GR00T-N1.7 baseline from 64.1% to 70.3%, with consistent gains on $π_{0.5}$ across both benchmarks.

## 局限

摘要未明确说明；需阅读全文核查。


## 研究关联

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-26/Act with Intent Distilling Behavior Intent for Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models can turn multimodal context into robot actions, but their action decoders are still trained largely by behavior cloning. This supervises which motor command was demonstrated while leaving implicit the local objective served by the behavior under the instruction. Future-based supervision enriches action learning with frames, latent observations, trajectories, or motion representations, but these signals capture particular realizations of what may happen rather than the shared semantic objective of the forthcoming behavior. We propose Intention Distillation (INDI), which distills behavior-level intent into the action decoder. During training, a frozen teacher VLM interprets a demonstrated segment from the current observation, instruction, coarse action summary, and corresponding execution video. From its standard inputs, the deployed VLA recovers the resulting multimodal intent representation at an intermediate decoder layer and uses it to organize action prediction together with representations of how the behavior unfolds and what it achieves. On SimplerEnv-Bridge, INDI improves GR00T-N1.7 from 64.3% to 84.7%, and on RoboCasa Kitchen it improves the controlled GR00T-N1.7 baseline from 64.1% to 70.3%, with consistent gains on $π_{0.5}$ across both benchmarks. In real-world tasks, INDI improves average success from 62.0% to 68.7%, with gains of up to 12.0 pp on longer-horizon tasks. Further analyses show that the recovered latent is used by the decoder, captures behavior objective and execution progress, and organizes downstream predictions in an objective-dependent manner. These results show that action decoders benefit from explicitly modeling the semantic objective of the behavior they generate.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.23478v1
- Authors: Sangoh Lee, Sangwoo Mo, Wook-Shin Han
- Published: 2026-08-24T16:42:49Z
- Age days: 1

</details>
