---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.36903v1"
published: "2026-09-29T07:25:29Z"
age_days: 0
score: 30
created: 2026-09-30
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# MultiTalk: Scaling Full-Duplex Speech Models to Long, Multi-Party, Bilingual Conversation

> [!summary] 先说人话（基于摘要）
> MultiTalk 让全双工语音模型在长时间、多人、中英双语对话中持续跟踪谁在说话、该回应谁。它同时补充大规模合成训练数据、真实录音评测和相应模型。

## 问题

现有系统难以兼顾长上下文与多人交互。开放多人语料规模小且不适配全双工建模，长音频基准偏被动听取，语音对话基准又多为短时双人交流。

## 创新点或方法

沿 Moshi 路线扩展双语长时多人建模，构造可控制轮替、重叠、打断、回应对象切换和长程指代的数据。用真实多人录音构建 MultiTalkBench，检测实体跟踪、话题连贯和回应对象选择。

## 证据

发布 5.76 万小时合成训练数据；MultiTalkBench 对话平均长 32.6 分钟。摘要报告模型在该基准显著优于 Moshi、MiniCPM-o-4.5 和 Qwen3-Omni-30B-A3B-Instruct，但未给出具体性能分数。

## 局限

需核查真实录音基准如何评估模型主动介入、打断与全双工响应，以及合成训练对自然多人对话的覆盖。

- **判断**：做社交机器人或语音 Agent 值得读数据与评测协议，机械操作研究者可略读。

## 研究关联

对社交机器人和语音 Agent，长程身份、指代与回应对象管理是实际交互能力。对运动控制 VLA 和世界模型的直接价值有限。

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/MultiTalk Scaling Full-Duplex Speech Models to Long, Multi-Party, Bilingual Conv.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

End-to-end full-duplex speech models have brought open-source machine conversation closer to human-like interaction, yet existing systems remain limited in two intertwined dimensions: long-context robustness and multi-party interaction. Real-world scenarios such as meetings, group lessons, and social-robot reception require a single model to track, contextualize, and respond to multiple speakers over extended durations. Progress is constrained by both data and evaluation: open multi-party speech corpora remain small and are not designed for codec-frame-level full-duplex modeling, while existing long-audio benchmarks focus on passive listening and speech-to-speech benchmarks are mostly short and dyadic. We extend the Moshi paradigm jointly along the long-horizon and multi-party axes in English and Chinese. First, we release 57.6k hours of synthetic training data ($\href{https://huggingface.co/datasets/MultiTalk/MultiTalkPT}{MultiTalkPT}$ and $\href{https://huggingface.co/datasets/MultiTalk/MultiTalkFT}{MultiTalkFT}$) for long-form, multi-party, English-Chinese full-duplex dialogue, with controllable length, participant count, turn-taking, overlap, backchannels, interruptions, addressee shifts, and long-range coreference. Second, we introduce $\href{https://huggingface.co/datasets/MultiTalk/MultiTalkBench}{MultiTalkBench}$, built from real human recordings, for evaluating long-form, multi-party, bilingual full-duplex dialogue. Conversations average 32.6 minutes and include probes for long-range entity tracking, topic coherence, and addressee selection. Third, we train a bilingual Moshi-style model that sustains coherent multi-party English-Chinese conversations over extended durations and substantially outperforms open-source baselines including Moshi, MiniCPM-o-4.5, and Qwen3-Omni-30B-A3B-Instruct on MultiTalkBench.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.36903v1
- Authors: Ke Wang, Houxing Ren, Zimu Lu, Yunqiao Yang, Zhuofan Zong, Mingjie Zhan, Hongsheng Li
- Published: 2026-09-29T07:25:29Z
- Age days: 0

</details>
