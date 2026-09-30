---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.07398v1"
published: "2026-09-07T12:12:32Z"
age_days: 1
score: 32
created: 2026-09-09
concepts: ["世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining

> [!summary] 先说人话（基于摘要）
> OpenWAM把世界—动作模型拆成可替换模块，系统研究哪些生成先验、表示和信息流真正帮助控制。它据此训练OpenWAM-α，并提供基础设施、评测协议、模型和数据配方。

## 这篇到底在做什么

- **卡在哪里**：现有世界—动作系统把生成骨干、视觉表示、架构、训练数据与推理过程紧密耦合，难以判断改进由哪个设计选择产生。
- **关键解法**：OpenWAM-Infra统一模块接口与训练部署流程，OpenWAM-Study开展受控实验。摘要归纳出强生成骨干与紧凑潜空间、独立动作容量、显式世界到动作信息流、同步联合去噪，以及人类第一视角与机器人数据单阶段联合训练等原则。
- **拿什么证明**：OpenWAM-α使用约6400小时人类第一视角与机器人数据，在8个仿真基准及真实机器人上评测，覆盖单臂、双臂和灵巧手。摘要称性能持续处于领先梯队，并称具身预训练主要改善域外泛化；摘要未给出可核查的结果数字。

## 值不值得读

- **和你的研究有什么关系**：对世界模型与VLA研究者，主要价值是可复用的受控研究平台，以及关于生成知识如何进入动作预测的具体设计假说。
- **先别急着信**：需核查受控实验是否匹配容量、数据和训练预算，以及所总结原则在不同骨干与任务上的适用范围。
- **判断**：优先精读消融和模块接口；它最值得借鉴的是设计归因能力，而汇总性能仍需查看完整结果。

## 研究关联

- **概念**：[[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-09/OpenWAM An Open, Modular Exploration Towards Systematic World-Action Model Pretr.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World-Action Models inherit world knowledge from video-generative priors, and channel it into executable control signals through embodied experience. Existing systems, however, are monolithic: the generative backbone, visual representation, architecture, information flow, inference procedure, and training data are tightly coupled, obscuring which design choices matter and why. We introduce OpenWAM, an open research stack that turns world-action pretraining into a controlled experimental program. OpenWAM-Infra factorizes the WAM design space into composable modules with unified training, inference, deployment, and evaluation. On this substrate, OpenWAM-Study examines three questions through controlled experiments: what to inherit, how world and action learning interact, and how their synergy scales; and distills three principles: upstream knowledge transfers through a sufficiently capable generative backbone and a compact, information-rich latent space; world-action synergy requires dedicated action capacity, explicit world-to-action information flow, and synchronized joint denoising; and embodied pretraining principally improves out-of-domain generalization, with one-stage co-training over egocentric and robot data integrating world coverage and action grounding. Composing these principles, we build OpenWAM-α, an open WAM pretrained on roughly 6,400 hours of egocentric human and robot data and evaluated across simulation and real-world benchmarks. Across the eight simulation benchmarks and the real-robot experiments, which together span embodiments from single-arm and bimanual manipulation to dexterous hands, OpenWAM-α delivers consistently excellent performance, sustaining its top-tier standing from simulation to the physical world. We release the full stack, including infrastructure, evaluation protocols, pretrained models, and data recipes, to facilitate future research.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.07398v1
- Authors: Yuran Wang, Siqiao Huang, Mingleyang Li, Chenhao Zhang, Jiaqi Liang, Weiyang Jin, Yue Chen, Xuemin Chi, Donghao Zhou, Qize Yu, Yu-Kai Wang, Yuhan Rui, Shenzhe Yao, Zhen Yuan, Zhenhao Shen, Kefei Zhu, Zijie Zhu, Ning Gao, Xiaowei Chi, Guanqi He, Shanghang Zhang, Hao Dong, Lin Shao, Hang Zhao
- Published: 2026-09-07T12:12:32Z
- Age days: 1

</details>
