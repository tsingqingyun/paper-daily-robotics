---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - VLA and Robot Foundation Models"
url: "https://arxiv.org/abs/2605.03269v2"
published: "2026-05-05T01:40:15Z"
age_days: 
score: 40
created: 2026-05-10
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# RLDX-1 Technical Report

> [!summary] 一句话结论（基于摘要）
> Through empirical evaluation, we show that RLDX-1 consistently outperforms recent frontier VLAs (e.g.

## 关键点

- **问题**：broad scene understanding and language-conditioned generalization) inherited from pre-trained Vision-Language Models, they still struggle with complex real-world tasks requiring broader functional capabilities (e.g.
- **创新点 / 方法**：To address this, we introduce RLDX-1, a general-purpose robotic policy for dexterous manipulation built on the Multi-Stream Action Transformer (MSAT), an architecture that unifies these capabilities by integrating heterogeneous modalities through modality-specific streams with cross-modal joint self-attention.
- **证据**：Through empirical evaluation, we show that RLDX-1 consistently outperforms recent frontier VLAs (e.g.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：40
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-05-10/RLDX-1 Technical Report.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

While Vision-Language-Action models (VLAs) have shown remarkable progress toward human-
like generalist robotic policies through the versatile intelligence (i.e. broad scene
understanding and language-conditioned generalization) inherited from pre-trained
Vision-Language Models, they still struggle with complex real-world tasks requiring
broader functional capabilities (e.g. motion awareness, long-term memory, and physical
sensing). To address this, we introduce RLDX-1, a general-purpose robotic policy for
dexterous manipulation built on the Multi-Stream Action Transformer (MSAT), an
architecture that unifies these capabilities by integrating heterogeneous modalities
through modality-specific streams with cross-modal joint self-attention. RLDX-1 further
combines this architecture with system-level design choices, including data synthesis
for rare manipulation scenarios, learning procedures specialized for human-like
manipulation, and inference optimizations for real-time deployment. Through empirical
evaluation, we show that RLDX-1 consistently outperforms recent frontier VLAs (e.g.
$π_{0.5}$ and GR00T N1.6) across both simulation benchmarks and real-world tasks that
require broad functional capabilities beyond general versatility. In particular, RLDX-1
shows superiority in ALLEX humanoid tasks by achieving success rates of 86.8% while
$π_{0.5}$ and GR00T N1.6 achieve around 40%, highlighting the ability of RLDX-1 to
control a high-DoF humanoid robot under diverse functional demands. Together, these
results position RLDX-1 as a promising step toward reliable VLAs for complex, contact-
rich, and dynamic real-world dexterous manipulation.

### 来源

- Source: arXiv Daily - VLA and Robot Foundation Models
- URL: https://arxiv.org/abs/2605.03269v2
- Authors: Dongyoung Kim, Huiwon Jang, Myungkyu Koo, Suhyeok Jang, Taeyoung Kim, Beomjun Kim, Byungjun Yoon, Changsung Jang, Daewon Choi, Dongsu Han, Donguk Lee, Heeseung Kwon, Hojin Jeon, Jaehyun Kang, Jaekyoung Bae, Jihyuk Lee, Jimin Lee, John Won, Joonwoo Ahn, Junhyeong Park, Junyoung Sung, Kyungmin Lee, Minseong Han, Minsung Yoon, Sejune Joo, Seonil Son, Seungcheol Park, Seunggeun Cho, Seungjun Moon, Seungku Kim, Yonghoon Dong, Yongjin Cho, Youngchan Kim, Chang Hwan Kim, Dohyeon Kim, Heecheol Kim, Heewon Lee, Hensen Ahn, Hyungkyu Ryu, Hyunsoo Choi, Hyunsoo Shin, Jaeheon Jung, Jaewoo Kim, Jinwook Kim, Joochul Chang, Joonsoo Kim, Junghun Park, Jungwoo Park, Junho Cho, Junhyeok Park, Junwon Lee, Kangwook Lee, Kwanghoon Kim, Kyoungwhan Choe, Manoj Bhadu, Nayoung Oh, Sangjun Kim, Sangwoo Kim, Seunghoon Shim, Seunghyun Kim, Seungjun Lee, Seungyup Ka, Sungryol Yang, Wook Jung, Yashu Shukla, Yeonjae Lee, Yeonwoo Bae, Jinwoo Shin
- Published: 2026-05-05T01:40:15Z
- Age days: 

</details>
