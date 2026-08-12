---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.11324v1"
published: "2026-06-09T18:07:50Z"
age_days: 2
score: 48
created: 2026-06-12
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models

> [!summary] 一句话结论（基于摘要）
> With only 8B parameters, Embodied-R1.5 achieves SOTA on 16 out of 24 embodied VLM benchmarks, surpassing leading models like Gemini-Robotics-ER-1.5 and GPT-5.4.

## 关键点

- **问题**：We introduce Embodied-R1.5, a unified Embodied Foundation Model (EFM) that integrates comprehensive embodied reasoning capabilities, spanning embodied cognition, task planning, correction, and pointing, within a single architecture toward general physical intelligence.
- **创新点 / 方法**：We introduce Embodied-R1.5, a unified Embodied Foundation Model (EFM) that integrates comprehensive embodied reasoning capabilities, spanning embodied cognition, task planning, correction, and pointing, within a single architecture toward general physical intelligence.
- **证据**：With only 8B parameters, Embodied-R1.5 achieves SOTA on 16 out of 24 embodied VLM benchmarks, surpassing leading models like Gemini-Robotics-ER-1.5 and GPT-5.4.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：48
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

We introduce Embodied-R1.5, a unified Embodied Foundation Model (EFM) that integrates
comprehensive embodied reasoning capabilities, spanning embodied cognition, task
planning, correction, and pointing, within a single architecture toward general physical
intelligence. Leveraging three automated data construction pipelines to significantly
expand the data coverage of critical capabilities, we build a large-scale data system of
over 15B tokens, and design a multi-task balanced RL recipe to alleviate heterogeneous
task conflicts. We further introduce a Planner-Grounder-Corrector (PGC) closed-loop
framework that enables a single model to autonomously execute and self-correct over
long-horizon tasks. With only 8B parameters, Embodied-R1.5 achieves SOTA on 16 out of 24
embodied VLM benchmarks, surpassing leading models like Gemini-Robotics-ER-1.5 and
GPT-5.4. Benefiting from the internalized embodied capabilities, Embodied-R1.5 can be
fine-tuned into a VLA with only a small amount of data, outperforming leading VLA models
like $π_{0.5}$ across 4 popular manipulation benchmark suites. We further conduct
extensive zero-shot real-robot experiments, validating performance in instruction
following, affordance grounding, articulated object manipulation, and long-horizon
complex tasks, demonstrating strong generalization to the physical world. We open-source
model weights, datasets, training code, and EmbodiedEvalKit, an evaluation framework
tailored for embodied tasks, to facilitate future research in EFMs.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.11324v1
- Authors: Yifu Yuan, Yaoting Huang, Xianze Yao, Yutong Li, Shuoheng Zhang, Linqi Han, Pengyi Li, Jiangeng Sun, Wenting Jia, Zhao Zhang, Yuhao Liu, Ruihao Liao, Yucheng Hu, Qiyu Wu, Yuxiao Li, Zibin Dong, Fei Ni, Yan Zheng, Shuyang Gu, Yi Ma, Hongyao Tang, Han Hu, Jianye Hao
- Published: 2026-06-09T18:07:50Z
- Age days: 2

</details>
