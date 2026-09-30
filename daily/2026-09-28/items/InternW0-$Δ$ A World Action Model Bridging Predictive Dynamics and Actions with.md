---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.31394v1"
published: "2026-09-25T15:24:25Z"
age_days: 2
score: 40
created: 2026-09-28
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# InternW0-$Δ$: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data

> [!summary] 先说人话（基于摘要）
> InternW0-Δ 将视频预测、语义、几何和动作专家接到一起，训练统一的世界动作模型。Causal Imprint 让动作专家直接使用与未来变化有关的表示，推理时无需先展开未来视频。

## 问题

通用机器人操作需要同时利用视觉动力学、场景语义、几何和运动知识。核心瓶颈是如何把不同预训练模型的先验整合进动作生成，摘要没有具体拆解既有方法的失败结果。

## 创新点或方法

MoT 框架连接预训练视频专家与动作专家，由冻结 VLM 提供语义指导；4D 模型通过仅训练时使用的蒸馏注入几何和运动先验。Causal Imprint 利用训练时的未来监督形成预测表示，异构数据则统一到共同状态动作表示。

## 证据

处理后的训练语料超过 20K 小时，包含机器人、UMI、第一人称人类示范和 Ego2Robot 数据。摘要报告在仿真基准与真机平台上优于先前方法，但未给出可核查的性能数字；开放资源仍以未来发布表述，部分数据受许可限制。

## 局限

需全文区分数据规模、各专家先验和 Causal Imprint 的贡献，并核查统一状态动作表示的具体定义；摘要不足以归因性能提升。

- **判断**：值得深入读架构与数据处理部分，但应等具体对照结果和开放资源确认后再评估复现投入。

## 研究关联

对世界模型与 VLA 研究者，价值在于多种预训练先验如何进入同一动作模型，以及如何用训练期未来监督减少部署时的视频展开需求。统一异构数据的流程也值得关注。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：40
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/InternW0-$Δ$ A World Action Model Bridging Predictive Dynamics and Actions with.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

World Action Models (WAMs) jointly model visual dynamics and action generation for generalist robot manipulation. A central challenge is to integrate priors from large-scale pretrained models---including visual dynamics, scene semantics, geometry, and motion---into a unified framework for robot action generation. We introduce InternW0-$Δ$, a unified WAM pretrained on a heterogeneous corpus that outperforms prior methods across simulation benchmarks and real-robot platforms. InternW0-$Δ$ combines pretrained visual dynamics, scene-level semantics, 4D geometric and motion priors, and action generation within a Mixture-of-Transformers (MoT) framework. A pretrained video expert and an action expert interact under semantic guidance from a frozen VLM, while a pretrained 4D foundation model injects geometric and motion priors through training-only distillation. We further introduce Causal Imprint, which learns future-relevant scene changes from training-only future supervision and provides predictive representations directly to the action expert without future-video rollout at inference. For large-scale joint training, we construct a heterogeneous corpus of robot demonstrations, UMI data, egocentric human demonstrations, and Ego2Robot data, curated and aligned under a common state-action representation. The resulting corpus contains over 20K hours of processed training data, to our knowledge the largest open-source corpus of its kind. We pretrain InternW0-$Δ$ on this corpus and demonstrate strong performance across simulation benchmarks and real-robot platforms. We will open source the training code, model weights, infrastructure, data-processing pipeline, and processed data where licenses permit. Project page: https://internrobotics.github.io/InternW0-Delta/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.31394v1
- Authors: Xingyu Miao, Zizun Li, Baole Fang, Kaiwen Song, Tenghui Wang, Hanxue Zhang, Yating Wang, Xudong Li, Yuping He, Xueyuan Wei, Chao Gao, Xijie Yang, Yingxiang Xu, Kerui Ren, Wenqi Guo, Jianjun Zhou, Xinzhe Wang, Weiguang Zhao, Ni Yang, Zetao Cai, Yufei Xue, Hengjie Li, Zeyu He, Yuanzhen Zhou, Rong Fu, Jianyang Zhang, Siwei Cui, Fuxian Huang, Yunsong Zhou, Xing Gao, Yifei Yao, Qiaojun Yu, Kailin Li, Ming Zhou, Mu Huang, Xinyue Li, Wenze Cui, Bingqi Jiang, Xueyue Zhu, Junting Dong, Haoyu Guo, Tao Lu, Mulin Yu, Bowen Zhou, Bin Zhao, Tianfan Xue, Weinan Zhang, Chunhua Shen
- Published: 2026-09-25T15:24:25Z
- Age days: 2

</details>
