---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.23831v1"
published: "2026-08-24T21:19:50Z"
age_days: 1
score: 37
created: 2026-08-26
concepts: ["世界模型", "视觉语言动作模型 VLA", "机器人学习"]
---

# Learning to Act While Waiting: RL Finetuning of Generalist Robot Policies Under Inference Latency

> [!summary] 一句话结论（基于摘要）
> In this work, we introduce a latency-aware framework, Asynchronous RL with Intermediate Information (ARLI), that enables RL-based improvement of generalist policies under inference delays.

## 问题

We evaluate our approach across simulated and real-world manipulation tasks, and find that it enables effective finetuning under inference delays where standard RL fails entirely, even matching or exceeding the performance of standard RL in idealized no-latency settings.

## 创新点或方法

In this work, we introduce a latency-aware framework, Asynchronous RL with Intermediate Information (ARLI), that enables RL-based improvement of generalist policies under inference delays.

## 证据

摘要未报告明确实验结论；需阅读全文核查。

## 局限

摘要未明确说明；需阅读全文核查。


## 研究关联

- **概念**：世界模型 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-26/Learning to Act While Waiting RL Finetuning of Generalist Robot Policies Under I.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

While reinforcement learning (RL) allows generalist robot policies to continually improve during deployment, the large model size of modern generalist policies, such as VLAs, poses a fundamental obstacle to effective RL improvement. In particular, their severe inference latency---which can lead to pauses or jerky movements---can alter the effective environment dynamics and, if not correctly accounted for, break the Markov assumption that RL relies on, causing standard RL algorithms to fail completely. In this work, we introduce a latency-aware framework, Asynchronous RL with Intermediate Information (ARLI), that enables RL-based improvement of generalist policies under inference delays. Our framework builds on asynchronous inference approaches, which interleave action generation with execution to hide latency, and addresses its incompatibility with RL by providing a low-latency RL policy design that maximizes reactivity within the inference window through two contributions: state augmentations that restore near-Markovian structure by incorporating committed actions and a mid-inference observation. We evaluate our approach across simulated and real-world manipulation tasks, and find that it enables effective finetuning under inference delays where standard RL fails entirely, even matching or exceeding the performance of standard RL in idealized no-latency settings.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.23831v1
- Authors: Brian Zhu, Momen Khalil, E Harrison, Emanuele Poggi, Philipp Schmitt, Bernd Kast, Philine Meister, Pranav Atreya, Qiyang Li, Finn Ferchau, Cesar Colmenero, Yash Shahapurkar, Gokul Narayanan, Melih Erdogan, Kai Wurm, Georg von Wichert, Oier Mees, Eugen Solowjow, Andrew Wagenmaker, Sergey Levine
- Published: 2026-08-24T21:19:50Z
- Age days: 1

</details>
