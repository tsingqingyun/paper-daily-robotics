---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2607.14695v1"
published: "2026-07-16T07:56:43Z"
age_days: 1
score: 36
created: 2026-07-18
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Reflex: Real-Time VLA Control through Streaming Inference

> [!summary] 一句话结论（基于摘要）
> On LIBERO and Kinetix benchmarks, Reflex achieves a 2.58$\times$ inference speedup and 50Hz stable streaming, reducing reaction latency by up to 54\% and enabling efficient deployment without performance degradation.

## 关键点

- **问题**：Flow matching Vision-Language-Action (VLA) models promise precise continuous control, but their iterative denoising nature introduces fundamental incompatibilities with real- time robotics: global timestep injection invalidates KV-caching, forcing a choice between slow $O(N^2)$ re-computation or mathematically incorre…
- **创新点 / 方法**：We present \textbf{Reflex}, a framework that enables \textit{real-time streaming inference} for flow matching policies by exploiting the \textit{Timestep-Invariance Property} -- that perception encoders are functionally independent of the denoising loop.
- **证据**：On LIBERO and Kinetix benchmarks, Reflex achieves a 2.58$\times$ inference speedup and 50Hz stable streaming, reducing reaction latency by up to 54\% and enabling efficient deployment without performance degradation.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：36
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-07-18/Reflex Real-Time VLA Control through Streaming Inference.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Flow matching Vision-Language-Action (VLA) models promise precise continuous control,
but their iterative denoising nature introduces fundamental incompatibilities with real-
time robotics: global timestep injection invalidates KV-caching, forcing a choice
between slow $O(N^2)$ re-computation or mathematically incorrect cache reuse. We present
\textbf{Reflex}, a framework that enables \textit{real-time streaming inference} for
flow matching policies by exploiting the \textit{Timestep-Invariance Property} -- that
perception encoders are functionally independent of the denoising loop. Reflex
partitions the attention context into static, sliding, and dynamic regions, enabling
$O(1)$ incremental cache updates while preserving full-batch-equivalent attention
outputs for fixed inputs. To ensure stability under continuous high-frequency inference,
we introduce \textit{AdaRMSNorm}, an adaptive normalization layer that prevents BFloat16
numerical collapse by gating on flow phase. We further maximize throughput through an
\textit{async pipeline} that decouples visual encoding from action generation, combined
with \textit{operator fusion} that reduces kernel overhead. On LIBERO and Kinetix
benchmarks, Reflex achieves a 2.58$\times$ inference speedup and 50Hz stable streaming,
reducing reaction latency by up to 54\% and enabling efficient deployment without
performance degradation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2607.14695v1
- Authors: Yuanchun Guo, Bingyan Liu
- Published: 2026-07-16T07:56:43Z
- Age days: 1

</details>
