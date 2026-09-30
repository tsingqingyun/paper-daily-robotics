---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.29208v1"
published: "2026-08-29T11:44:18Z"
age_days: 2
score: 40
created: 2026-09-01
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# AdaVLA: Adaptive Step Flow Matching for Training-free Acceleration of Vision-Language-Action Models

> [!summary] 先说人话（基于摘要）
> AdaVLA 在不训练、不访问原数据的条件下加速 flow-matching VLA：用流轨迹曲率估计生成置信度，动态减少 ODE 步数并调整 MLP 剪枝率。

## 问题

VLA 的计算开销妨碍端侧实时响应，而许多加速方法依赖微调或私有训练数据；现有工作又多盯着 VLM 成本，忽略 flow matching 推理中的迭代 ODE 求解。

## 创新点或方法

它在在线推理时读取 flow matching 轨迹并计算曲率指标，以此决定每次动作生成需要多少求解步，以及按高效重要性评估采用何种 MLP 剪枝率。与固定步数、只压缩 VLM 或需离线训练的方案相比，它同时适配求解和网络计算且无需训练数据。

## 证据

在 Jetson AGX Orin 的 LIBERO 实验中，π₀.₅ 和 X-VLA 分别加速 1.87 倍和 2.24 倍，成功率仅有可忽略下降；摘要还称在 SmolVLA 真实机器人任务上验证了鲁棒性，但未给具体数字。


## 局限

“可忽略”的成功率损失没有量化，曲率是否在分布外或高精度接触动作中可靠代表置信度需要全文核查。

- **判断**：部署型 VLA 研究者值得精读；核心指标简单且可移植，但价值最终取决于速度—成功率曲线而非单个加速倍数。

## 研究关联

这是面向 VLA 端侧部署的直接工程收益，特别适合拿不到训练集或不能修改权重的模型，也为延迟敏感具身评测提供动态计算基线。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：40
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-01/AdaVLA Adaptive Step Flow Matching for Training-free Acceleration of Vision-Lang.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models, built upon Vision-Language Models (VLMs), have significantly enhanced robotic capabilities by leveraging internet-scale knowledge and multimodal reasoning. However, the intensive computational overhead of VLAs constrains on-device deployment, hindering real-time responses to environmental changes. While various acceleration techniques have been proposed, they often rely on fine-tuning or access to training datasets, which are frequently unavailable due to privacy and proprietary concerns. Moreover, although flow-matching-based VLAs have emerged as efficient alternatives to standard diffusion models, current acceleration efforts largely target VLM inference costs, failing to address the iterative ODE solving process inherent in flow matching inference. To address these limitations, we propose AdaVLA, an online, training-free adaptive framework for fast yet accurate flow-matching-based Vision-Language-Action models. We introduce a novel metric derived from the flow matching trajectory curvature to quantify action generation confidence during inference. This metric enables the dynamic reduction of inference steps and the adaptive adjustment of MLP pruning ratios through an efficiently computed importance evaluation, requiring no access to training data. Experimental results on the LIBERO benchmark using a Jetson AGX Orin device demonstrate that our method achieves $1.87\times$ and $2.24\times$ speedups for $π_{0.5}$ and X-VLA, respectively, with negligible degradation in success rates. Furthermore, we validate the robustness of our approach on real-world robotic tasks using SmolVLA.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.29208v1
- Authors: Sunghwan Han, Youngtae Han, Youngmin Yi
- Published: 2026-08-29T11:44:18Z
- Age days: 2

</details>
