---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.12904v1"
published: "2026-08-13T07:41:14Z"
age_days: 3
score: 24
created: 2026-08-16
concepts: ["多模态基础模型", "世界模型", "具身智能评测与基准"]
---

# HounsWorld: A Multimodal World Model for Hidden Patient-State Readout, Reconstruction, and Simulation

> [!summary] 一句话结论（基于摘要）
> To operationalize this view, we introduce HounsBench, a computed tomography (CT) centric patient-state benchmark that unifies these three task families with patient-disjoint splits and per-family metrics, and HounsWorld, a 3B multimodal world model that treat…

## 关键点

- **问题**：We formulate CT-centered intelligence as inference over a shared latent patient state, under which readout, reconstruction, and simulation all become state-dependent prediction problems.
- **创新点 / 方法**：To operationalize this view, we introduce HounsBench, a computed tomography (CT) centric patient-state benchmark that unifies these three task families with patient-disjoint splits and per-family metrics, and HounsWorld, a 3B multimodal world model that treats volumetric scans and language as observations of the share…
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-16/HounsWorld A Multimodal World Model for Hidden Patient-State Readout, Reconstruc.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Clinical intelligence requires estimating a patient's underlying condition from incomplete observations rather than learning isolated mappings from scans to answers. Volumetric medical images provide dense observations of anatomy, attenuation, and lesions, whereas clinical language provides sparse but complementary semantic observations. We formulate CT-centered intelligence as inference over a shared latent patient state, under which readout, reconstruction, and simulation all become state-dependent prediction problems. To operationalize this view, we introduce HounsBench, a computed tomography (CT) centric patient-state benchmark that unifies these three task families with patient-disjoint splits and per-family metrics, and HounsWorld, a 3B multimodal world model that treats volumetric scans and language as observations of the shared state through Joint Understanding-Generation Learning. A shared transformer forms an implicit patient-state estimate and supports three outputs: query-conditioned answers that read out the state, reports and captions that reconstruct it in language, and condition-specific CT volumes for low-dose denoising, virtual contrast enhancement, and anatomy-constrained text-and-mask-to-volume generation. Zero-initialized CT adapters preserve pretrained multimodal mappings, while condition-explicit Hounsfield-unit window sampling exposes clinically meaningful density observations. HounsWorld shows strong performance across all three task families while consistently improving CT understanding through clinically structured completion. Our project is available at https://github.com/byhwhite/HounsWorld.git

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.12904v1
- Authors: Yunhao Bai, Zhongwei Qiu, Guangyu Guo, Yiming Huang, Tony C. W. Mok, Qinji Yu, Ling Zhang, Yan Wang
- Published: 2026-08-13T07:41:14Z
- Age days: 3

</details>
