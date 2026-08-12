---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - VLA and Robot Foundation Models"
url: "https://arxiv.org/abs/2605.03269v2"
published: "2026-05-05T01:40:15Z"
score: 40
created: 2026-05-10
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# RLDX-1 Technical Report

## 为什么重要

自动筛选分数：40

连接概念：[[多模态基础模型]], [[世界模型]], [[视觉语言动作模型 VLA]], [[具身智能评测与基准]]

## 摘要

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

## 来源

- Source: arXiv Daily - VLA and Robot Foundation Models
- URL: https://arxiv.org/abs/2605.03269v2
- Authors: Dongyoung Kim, Huiwon Jang, Myungkyu Koo, Suhyeok Jang, Taeyoung Kim, Beomjun Kim, Byungjun Yoon, Changsung Jang, Daewon Choi, Dongsu Han, Donguk Lee, Heeseung Kwon, Hojin Jeon, Jaehyun Kang, Jaekyoung Bae, Jihyuk Lee, Jimin Lee, John Won, Joonwoo Ahn, Junhyeong Park, Junyoung Sung, Kyungmin Lee, Minseong Han, Minsung Yoon, Sejune Joo, Seonil Son, Seungcheol Park, Seunggeun Cho, Seungjun Moon, Seungku Kim, Yonghoon Dong, Yongjin Cho, Youngchan Kim, Chang Hwan Kim, Dohyeon Kim, Heecheol Kim, Heewon Lee, Hensen Ahn, Hyungkyu Ryu, Hyunsoo Choi, Hyunsoo Shin, Jaeheon Jung, Jaewoo Kim, Jinwook Kim, Joochul Chang, Joonsoo Kim, Junghun Park, Jungwoo Park, Junho Cho, Junhyeok Park, Junwon Lee, Kangwook Lee, Kwanghoon Kim, Kyoungwhan Choe, Manoj Bhadu, Nayoung Oh, Sangjun Kim, Sangwoo Kim, Seunghoon Shim, Seunghyun Kim, Seungjun Lee, Seungyup Ka, Sungryol Yang, Wook Jung, Yashu Shukla, Yeonjae Lee, Yeonwoo Bae, Jinwoo Shin
- Published: 2026-05-05T01:40:15Z

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
