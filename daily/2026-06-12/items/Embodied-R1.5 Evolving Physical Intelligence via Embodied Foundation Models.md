---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.11324v1"
published: "2026-06-09T18:07:50Z"
age_days: 2
score: 48
created: 2026-06-12
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models

## 为什么重要

自动筛选分数：48

连接概念：[[多模态基础模型]], [[智能体 Agent]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

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

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.11324v1
- Authors: Yifu Yuan, Yaoting Huang, Xianze Yao, Yutong Li, Shuoheng Zhang, Linqi Han, Pengyi Li, Jiangeng Sun, Wenting Jia, Zhao Zhang, Yuhao Liu, Ruihao Liao, Yucheng Hu, Qiyu Wu, Yuxiao Li, Zibin Dong, Fei Ni, Yan Zheng, Shuyang Gu, Yi Ma, Hongyao Tang, Han Hu, Jianye Hao
- Published: 2026-06-09T18:07:50Z
- Age days: 2

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
