---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.22794v1"
published: "2026-06-22T03:10:19Z"
age_days: 1
score: 33
created: 2026-06-24
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# UniFS: Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> Experiments on LIBERO show that UniFS achieves state-of- the-art performance (98.3\% average success rate, a 2.5\% gain over VLA-Adapter baseline) while reducing average inference latency from 36.5~ms to 17.8~ms (2.1$\times$ speedup).

## 关键点

- **问题**：Mainstream Fast-Slow dual system vision-language-action models decouple a high-frequency action expert from a low-frequency vision-language model for efficiency, yet they face a fundamental frequency dilemma: large update gaps cause semantic drift from stale context, while small gaps erode the intended computational s…
- **创新点 / 方法**：Inspired by multi-timescale neural processing in the human brain, we introduce UniFS, a unified fast-to-slow architecture that resolves these challenges through three key designs.
- **证据**：Experiments on LIBERO show that UniFS achieves state-of- the-art performance (98.3\% average success rate, a 2.5\% gain over VLA-Adapter baseline) while reducing average inference latency from 36.5~ms to 17.8~ms (2.1$\times$ speedup).
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-24/UniFS Unified Fast-to-Slow Hierarchical Architecture for Vision-Language-Action.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Mainstream Fast-Slow dual system vision-language-action models decouple a high-frequency
action expert from a low-frequency vision-language model for efficiency, yet they face a
fundamental frequency dilemma: large update gaps cause semantic drift from stale
context, while small gaps erode the intended computational savings. Moreover, because
the action expert receives only the VLM's final-layer representation at a single fixed
frequency, rich intermediate features are discarded, limiting both information coupling
and manipulation precision. Inspired by multi-timescale neural processing in the human
brain, we introduce UniFS, a unified fast-to-slow architecture that resolves these
challenges through three key designs. First, we stratify the VLM layers into groups with
progressively decreasing update frequencies, enabling shallow layers to capture fast-
changing dynamics while deeper layers cache stable semantic context. Second, a latent
vector inversion mechanism re-routes the interaction order between multi-scale VLM
features and the action expert, aligning fast-varying representations with fine-grained
action decoding and slow-varying ones with coarse planning. Third, a multi-level
supervision strategy enforces a coarse-to-fine learning hierarchy across temporal
scales. Together, these designs enable richer cross-frequency information transfer
within a single backbone, while the low-frequency pathways additionally preserve
temporal context across steps. Experiments on LIBERO show that UniFS achieves state-of-
the-art performance (98.3\% average success rate, a 2.5\% gain over VLA-Adapter
baseline) while reducing average inference latency from 36.5~ms to 17.8~ms (2.1$\times$
speedup). Real-robot experiments on a Franka platform further validate its practical
applicability. Code is opensourced at https://github.com/linsun449/UniFS.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.22794v1
- Authors: Lin Sun, Zhiwei Guan, Conglin Wang, Zihong Chen, Jianhai Yu, Zongsheng Li, Boyong He, Tao Sun, Jiale Cao, Lige Liu
- Published: 2026-06-22T03:10:19Z
- Age days: 1

</details>
