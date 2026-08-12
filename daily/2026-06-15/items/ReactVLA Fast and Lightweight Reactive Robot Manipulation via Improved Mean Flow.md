---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14255v1"
published: "2026-06-12T08:33:37Z"
age_days: 2
score: 41
created: 2026-06-15
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# ReactVLA: Fast and Lightweight Reactive Robot Manipulation via Improved Mean Flow Action Generation

> [!summary] 一句话结论（基于摘要）
> Experimental results show that \texttt{ReactVLA} consistently outperforms similarly sized VLA baselines, including SmolVLA and $π_0$.

## 关键点

- **问题**：However, their reliance on iterative sampling introduces substantial inference latency, which limits their applicability to reactive closed-loop robot manipulation.
- **创新点 / 方法**：To address this limitation, we propose \texttt{ReactVLA}, a lightweight and low-latency VLA framework for real-time robotic manipulation.
- **证据**：Experimental results show that \texttt{ReactVLA} consistently outperforms similarly sized VLA baselines, including SmolVLA and $π_0$.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：41
- **阅读状态**：摘要级快读；需要全文核查证据或局限

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Diffusion-based Vision-Language-Action (VLA) policies have demonstrated strong
capability in modeling expressive and multimodal action distributions. However, their
reliance on iterative sampling introduces substantial inference latency, which limits
their applicability to reactive closed-loop robot manipulation. To address this
limitation, we propose \texttt{ReactVLA}, a lightweight and low-latency VLA framework
for real-time robotic manipulation. \texttt{ReactVLA} combines two complementary
designs: (1) an improved Mean Flow (iMF) action generator that reduces expensive multi-
step diffusion sampling to one-to-few-step action generation, and (2) Attention
Residuals (AttnRes), a dynamic depth-wise feature routing mechanism that replaces
uniform residual accumulation to better preserve task-relevant multimodal
representations. We evaluate \texttt{ReactVLA} on large-scale simulation benchmarks,
including LIBERO and RoboIMI, as well as real-world robotic manipulation tasks.
Experimental results show that \texttt{ReactVLA} consistently outperforms similarly
sized VLA baselines, including SmolVLA and $π_0$. On challenging precision manipulation
tasks, \texttt{ReactVLA} achieves up to a 1.65$\times$ improvement in task performance
while providing more than a 4$\times$ increase in inference speed compared with leading
VLA models. Finally, it reduces real-world policy latency to below 38.6 ms, enabling
fast reactive control on physical robot platforms. Please check out our project website
at: https://game-loader.github.io/ReactVLA/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14255v1
- Authors: Yanzhao Guo, Wenkai Chen, Jianwei Zhang
- Published: 2026-06-12T08:33:37Z
- Age days: 2

</details>
