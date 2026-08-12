---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09593v1"
published: "2026-08-10T13:27:09Z"
age_days: 1
score: 25
created: 2026-08-12
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# MADBench: A Benchmark for Modality-Aware Audio Deepfake Detection

> [!summary] 一句话结论（基于摘要）
> We introduce MADBench, the first benchmark that treats speech and environmental audio as distinct acoustic components, enabling component-aware evaluation of audio deepfake detection across independently manipulated forgery sources.

## 关键点

- **问题**：Recent advances in speech synthesis and audio generation have made high-fidelity acoustic forgery low-cost and difficult to attribute, enabling a realistic attack scenario in which speech and background audio are independently manipulated over otherwise authentic video.
- **创新点 / 方法**：We introduce MADBench, the first benchmark that treats speech and environmental audio as distinct acoustic components, enabling component-aware evaluation of audio deepfake detection across independently manipulated forgery sources.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[具身智能评测与基准]]
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-12/MADBench A Benchmark for Modality-Aware Audio Deepfake Detection.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Recent advances in speech synthesis and audio generation have made high-fidelity
acoustic forgery low-cost and difficult to attribute, enabling a realistic attack
scenario in which speech and background audio are independently manipulated over
otherwise authentic video. Yet existing research either focuses on visual manipulation,
addresses speech detection in isolation, or conflates speech and non-speech audio as a
single undifferentiated audio stream, overlooking the distinct forensic challenges posed
by background audio. This conflation is consequential: the two acoustic components arise
from fundamentally different generative mechanisms, exhibit distinct artifact profiles,
and pose different challenges to detection systems. We introduce MADBench, the first
benchmark that treats speech and environmental audio as distinct acoustic components,
enabling component-aware evaluation of audio deepfake detection across independently
manipulated forgery sources. We benchmark representative state-of-the-art detectors and
multimodal large language models under a unified protocol. Our experiments reveal that
environmental audio manipulation is more detectable than synthetic speech across
general-purpose encoders, while existing pretrained detectors fail on both acoustic
components, and manipulated environmental audio asymmetrically degrades speech deepfake
detection, findings entirely invisible under the single-label paradigm of prior
benchmarks. MADBench establishes a rigorous foundation for future research into robust,
component-aware audio deepfake detection.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09593v1
- Authors: Yanqiu Li, Yang Xiao, Jisheng Bai, Bin Chen, Hong Jia, Ting Dang
- Published: 2026-08-10T13:27:09Z
- Age days: 1

</details>
