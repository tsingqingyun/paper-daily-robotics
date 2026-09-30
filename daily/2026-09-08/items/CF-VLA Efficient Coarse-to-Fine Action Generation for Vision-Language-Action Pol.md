---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2604.24622"
published: "Mon, 07 Sep 2026 00:00:00 -0400"
age_days: 0
score: 33
created: 2026-09-08
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# CF-VLA: Efficient Coarse-to-Fine Action Generation for Vision-Language-Action Policies

> [!summary] 先说人话（基于摘要）
> CF-VLA 先生成有动作结构的粗略起点，再用一步修正得到动作。它通过改善生成起点减少流式 VLA 的采样成本。

## 这篇到底在做什么

- **卡在哪里**：从无信息高斯噪声恢复动作结构通常需要多步推理，实时控制下容易陷入速度与动作质量的取舍。
- **关键解法**：粗阶段学习终点速度的条件后验，将噪声变为结构化初始化；细阶段在固定时间做局部修正。训练先学习受控粗预测器，再联合优化两阶段。
- **拿什么证明**：CALVIN、LIBERO 上优于现有 NFE=2 方法，若干指标达到或超过 NFE=10 的 π0.5；动作采样延迟降低 75.4%，真机平均成功率 83.0%，比 MIP 和 π0.5 分别高 19.5、4.0 个百分点。

## 值不值得读

- **和你的研究有什么关系**：直接服务 VLA 实时推理，可用于研究低函数评估次数下如何保留动作生成质量。
- **先别急着信**：需核查延迟比较的硬件与计算边界；动作采样加速不等于整个感知到执行闭环同比加速。
- **判断**：优先精读两阶段目标与速度测量，摘要同时给出了明确延迟和真机收益。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-08/CF-VLA Efficient Coarse-to-Fine Action Generation for Vision-Language-Action Pol.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2604.24622v4 Announce Type: replace-cross Abstract: Flow-based vision-language-action (VLA) policies offer strong expressivity for action generation, but suffer from a fundamental inefficiency: multi-step inference is required to recover action structure from uninformative Gaussian noise, leading to a poor efficiency-quality trade-off under real-time constraints. We address this issue by rethinking the role of the starting point in generative action modeling. Instead of shortening the sampling trajectory, we propose CF-VLA, a coarse-to-fine two-stage formulation that restructures action generation into a coarse initialization step that constructs an action-aware starting point, followed by a single-step local refinement that corrects residual errors. Concretely, the coarse stage learns a conditional posterior over endpoint velocity to transform Gaussian noise into a structured initialization, while the fine stage performs a fixed-time refinement from this initialization. To stabilize training, we introduce a stepwise strategy that first learns a controlled coarse predictor and then performs joint optimization. Experiments on CALVIN and LIBERO show that our method establishes a strong efficiency-performance frontier under low-NFE (Number of Function Evaluations) regimes: it consistently outperforms existing NFE=2 methods, matches or surpasses the NFE=10 $\pi_{0.5}$ baseline on several metrics, reduces action sampling latency by 75.4%, and achieves the best average real-robot success rate of 83.0%, outperforming MIP by 19.5 points and $\pi_{0.5}$ by 4.0 points. These results suggest that structured, coarse-to-fine generation enables both strong performance and efficient inference. Our code is available at https://github.com/EmbodiedAI-RoboTron/CF-VLA.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2604.24622
- Authors: Fan Du, Feng Yan, Jianxiong Wu, Xinrun Xu, Weiye Zhang, Weinong Wang, Yu Guo, Bin Qian, Zhihai He, Fei Wang, Heng Yang
- Published: Mon, 07 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
