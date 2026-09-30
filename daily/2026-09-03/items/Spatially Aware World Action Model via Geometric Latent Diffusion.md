---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.02531v1"
published: "2026-09-02T12:42:37Z"
age_days: 0
score: 28
created: 2026-09-03
concepts: ["世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Spatially Aware World Action Model via Geometric Latent Diffusion

> [!summary] 先说人话（基于摘要）
> SA-WAM 在同一个视频扩散骨干中联合预测动作、未来 RGB 和深度，让 World Action Model 获得显式3D意识。它用非线性编码把无界深度映射到冻结 VAE 的有界输入域，从而保留视频预训练先验。

## 问题

现有 WAM 虽继承大规模视频先验，却只处理 RGB，缺乏对几何结构的显式建模；这会限制空间变化环境中的未来状态预测和动作选择。

## 创新点或方法

方法复用预训练视频模型与冻结 VAE tokenizer，对深度作有界非线性编码，然后在单一扩散模型中联合生成 RGB、深度和动作；区别于另训3D编码器，它避免3D专用 tokenizer 微调。

## 证据

摘要称在 RoboCasa、LIBERO-Plus 达到 SOTA，同时改善未来状态预测；在 UR5 真实机器人上超过强基线，随机化环境增益明显，并分析预测质量与 rollout 成功的相关性。未给数字。


## 局限

摘要没有说明深度来自传感器还是估计器、训练和部署是否都需深度输入，以及相关性是否能支持因果结论。

- **判断**：值得精读深度编码、联合目标与真实机器人随机化实验；这是结构简洁但潜在影响较大的 WAM 改造。

## 研究关联

对世界模型和 VLA 研究者，它提供低成本注入几何信息的办法，并直接研究世界预测质量是否与控制成功一致。

- **概念**：世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-03/Spatially Aware World Action Model via Geometric Latent Diffusion.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World Action Models (WAMs) leverage the capabilities of large-scale pretrained video diffusion models to jointly predict future observations and actions, inheriting rich visual and physical priors from internet-scale video. This has made them a promising paradigm for robot policy learning, yet the prevailing models operate exclusively on RGB observations and do not leverage 3D information. To bridge this gap, we introduce a Spatially Aware World Action Model (SA-WAM), which repurposes a pretrained video model for joint action, RGB, and depth prediction, enabling 3D-aware world modeling and action prediction within a single diffusion backbone. We use a nonlinear encoding that maps the unbounded depth signal into the bounded input domain expected by the frozen VAE tokenizer. This allows us to reuse the tokenizer without 3D-specific fine-tuning, incorporating geometric information without sacrificing the pretrained priors. SA-WAM achieves state-of-the-art results on the RoboCasa and LIBERO-Plus benchmarks, while simultaneously improving future-state predictions. Furthermore, SA-WAM outperforms strong baselines in real-world evaluation using a UR5 robotic arm, with strong gains in randomized environments. We analyze the correlation between world model prediction quality and rollout success, providing insights into WAM performance and avenues for its improvement.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.02531v1
- Authors: Javier Alejandro Lopetegui Gonzalez, Paul Pacaud, Cordelia Schmid
- Published: 2026-09-02T12:42:37Z
- Age days: 0

</details>
