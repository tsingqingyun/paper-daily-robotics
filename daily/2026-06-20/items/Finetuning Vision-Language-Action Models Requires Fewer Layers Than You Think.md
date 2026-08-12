---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.20246v1"
published: "2026-06-18T13:57:12Z"
age_days: 1
score: 41
created: 2026-06-20
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think

> [!summary] 一句话结论（基于摘要）
> To exploit this, we introduce a structural compression pipeline that is entirely training-free, bypassing the need of existing methods to load full-scale models to learn optimized token reductions or dynamic layer selectors.

## 关键点

- **问题**：Vision-Language-Action (VLA) models pre-trained on massive video-robot datasets have revolutionized robotic manipulation, yet their multi-billion parameter architectures impose prohibitive computational burdens during downstream fine-tuning and real-time inference.
- **创新点 / 方法**：To exploit this, we introduce a structural compression pipeline that is entirely training-free, bypassing the need of existing methods to load full-scale models to learn optimized token reductions or dynamic layer selectors.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：41
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-20/Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models pre-trained on massive video-robot datasets have
revolutionized robotic manipulation, yet their multi-billion parameter architectures
impose prohibitive computational burdens during downstream fine-tuning and real-time
inference. In this work, we reveal a highly non-trivial architectural characteristic of
these continuous control foundation policies (e.g., pi_0, GR00T-N1.5): despite being
trained on diverse physical trajectories, they exhibit severe layer-wise
representational redundancy. To exploit this, we introduce a structural compression
pipeline that is entirely training-free, bypassing the need of existing methods to load
full-scale models to learn optimized token reductions or dynamic layer selectors.
Instead, using only a single forward pass via Centered Kernel Alignment to identify
redundant layer features, we remove twin layers to permanently compress the model depth
by up to 50% across both the VLM backbone and the continuous control policy head.
Downstream fine-tuning of this streamlined architecture yields a dual acceleration
benefit: a 40-50% reduction in training time and up to 30% faster real-time inference,
while matching or exceeding full-scale base model performance. We comprehensively
validate our method across three simulation benchmarks (LIBERO, RoboCasa, SimplerEnv)
and 10 diverse real-world manipulation tasks across 4 unique robotic embodiments. These
results prove that advanced VLAs require significantly fewer layers than previously
assumed, offering a highly compute-efficient paradigm for scalable robot learning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.20246v1
- Authors: Gia-Binh Nguyen, Trong-Bao Ho, Thien-Loc Ha, Khoa Vo, Philip Lund Møller, Quang T. Nguyen, Long Dinh, Tuan Dam, Vu Duong, Tung M. Luu, Trung Le, Tran Nguyen Le, Minh Vu, An Thai Le, Ngan Le, Daniel Sonntag, James Zou, Jan Peters, Duy M. H. Nguyen, Ngo Anh Vien
- Published: 2026-06-18T13:57:12Z
- Age days: 1

</details>
