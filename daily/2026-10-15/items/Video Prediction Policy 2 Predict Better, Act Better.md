---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2610.10270"
published: "Wed, 14 Oct 2026 00:00:00 -0400"
age_days: 0
score: 39
created: 2026-10-15
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Video Prediction Policy 2: Predict Better, Act Better

> [!summary] 这篇论文到底做了什么（基于摘要）
> VPP2 先把视频模型训练得更懂操作事件，再把它压成单步视觉规划器，最后连接动作模块。它针对的是机器人“预测错了物体怎么动，动作也跟着错”的问题，同时避免接入动作学习时损伤视频能力。

## 问题

世界动作模型希望用视频预测知识帮助操作，但作者观察到已有模型在开放环境中经常预测错误运动。摘要将原因归为基础视频模型缺少操作训练，以及直接加入动作组件可能破坏原有泛化能力。

### 用一个例子理解

理解用例（非论文实验）：输入桌面画面和“把毛巾折起来”。视觉规划器预测固定时间范围内符合指令的变化，动作模块据此输出执行动作；再次观察后如何重规划，摘要未说明。

## 创新点或方法

旧做法直接把动作学习接到视频模型，本文分阶段处理：先用多样操作视频和细致描述继续预训练，以事件为单位学习；再后训练并蒸馏成固定预测时域的单步视觉规划器；最后通过 MoT 架构加入动作模块，学习从视觉变化到动作的隐式逆动力学。训练有多阶段，推理使用蒸馏后的规划器和动作模块；具体调用顺序、参数冻结策略与控制频率未说明。

### 方法如何工作

1. 整理多样操作视频并配详细描述，使训练数据覆盖指令对应的操作事件。
2. 继续预训练视频模型，改善对操作变化的预测，为后续动作学习提供基础。
3. 后训练并蒸馏为固定时域的单步视觉规划器，减少生成步骤；实际耗时未说明。
4. 通过 MoT 接入动作模块，学习视觉变化对应的动作，使预测能力进入机器人控制。

### 必要术语

- 事件级预训练：按操作事件组织视频学习；本文用它加强指令与变化的对应。
- 隐式逆动力学：从期望的状态变化学习该执行什么动作；本文用它连接视觉规划与控制。
- MoT：组织多个 Transformer 的架构；本文用来接入动作模块，具体交互方式未说明。

## 证据

摘要给出三组结果：开放任务的视频预测指令遵循成功率，VPP2-14B 比 Cosmos3-64B 高 11.0 个百分点；真机零样本 ALOHA 操作成功率，比最强基线高 18.5 个百分点，但未给基线名或绝对分数；在基准专项后训练后，LIBERO-Pro、LIBERO-OOD 和 RoboDojo 的成功率在评估方法中最高，未列数值。最后一组不能当作零样本证据，也未给消融来分离各阶段贡献。

## 局限

摘要未列作者明确局限。我的待核查问题是：哪些动作收益由预测改善带来，哪些来自新增数据或动作架构。预测分数与操作分数同时提高，还不足以确立因果关系；单步生成也不自动意味着满足实时控制，仍需延迟和闭环证据。

- **判断**：值得读完整训练流程及消融实验：真机零样本增益值得关注，但要判断能否借鉴，必须弄清数据、蒸馏和动作连接各自贡献。

## 研究关联

值得借鉴的是先把预测目标对准操作事件，再处理实时性与动作连接。如果基础模型对操作变化的预测本身不可靠，只优化动作头可能会继承这个错误；本文提供了分阶段检查预测质量和行动质量的思路。

### 下一步读哪里

先核查事件的划分与标注、蒸馏目标、预测时域和 MoT 的信息交互；再检查视频预测与操作成功的对应关系、阶段消融、零样本任务划分及推理延迟。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-15/Video Prediction Policy 2 Predict Better, Act Better.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.10270v3 Announce Type: replace-cross Abstract: World action models (WAMs) have emerged as an important class of generalist robot policies, aiming to transfer video prediction priors to action learning. However, we find that existing WAMs frequently produce incorrect motion predictions in open-ended environment, leading to erroneous actions. We attribute this limitation to two factors: (1) base video models are not optimized for manipulation, and (2) naively incorporating action components into video models can substantially degrade their generalization capabilities. We introduce Video Prediction Policy 2 (VPP2), a WAM that enables strong zero-shot generalization in both video prediction and action generation. First, we curate a large-scale, diverse dataset of manipulation videos to continue pretraining the base video foundation model. We annotate video clips with detailed captions and perform \textit{event-level} video pretraining to promote generalization across open-ended manipulation tasks. Second, we post-train and distill the video model into a single-step visual planner with fixed prediction horizon. Finally, we introduce action module via a mixture-of-transformers (MoT) architecture to learn implicit inverse dynamics model. Experiments demonstrate three key results: (1) VPP2-14B outperforms Cosmos3-64B by 11.0\% points in video prediction instruction-following success rate on open-ended tasks; (2) VPP2 surpasses the strongest baseline by 18.5\% points in success rate on real-world zero-shot ALOHA manipulation tasks; and (3) following benchmark-specific post-training, VPP2 achieves the highest success rates among evaluated methods on the challenging LIBERO-Pro, LIBERO-OOD, and RoboDojo benchmarks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.10270
- Authors: Yanjiang Guo, Haodong Yan, Zhide Zhong, Zhongru Zhang, Qingyuan Yang, Qingzhou Lu, Xiaoyu Chen, Yen-Jen Wang, Shuying Deng, Chenghan Yang, Puzhen Yuan, Chenxin Liu, Tun Ban, Xiang Zhu, Yichen Liu, Kun Feng, Haoang Li, Jianyu Chen
- Published: Wed, 14 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
