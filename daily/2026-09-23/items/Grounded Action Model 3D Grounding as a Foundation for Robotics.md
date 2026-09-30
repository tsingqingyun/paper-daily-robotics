---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.23863v1"
published: "2026-09-20T20:35:39Z"
age_days: 2
score: 49
created: 2026-09-23
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Grounded Action Model: 3D Grounding as a Foundation for Robotics

> [!summary] 先说人话（基于摘要）
> Grounded Action Models（GAM）先明确“操作哪个物体、它在三维空间哪里”，再预测动作。它把语言、点或框提示统一成带真实尺度几何的物体表示，减少策略从机器人示范中自行摸索空间定位的负担。

## 问题

操作策略需要目标身份与精确空间位置，但语言或视频生成预训练并不直接要求这种度量空间定位，现有模型因此依赖机器人示范隐式补齐这一能力。

## 创新点或方法

将多种提示转换为包含目标视觉特征和度量几何的物体中心表示，再与机器人状态历史通过多流 Transformer 融合，输出动作块；也可接受高层规划器指令，充当底层控制器。

## 证据

RoboTwin 2.0 的50项任务平均成功率55.3%，Spatial Forcing为52.0%；场景随机化下47.6%，Abot-M0为30.4%。LIBERO-PRO为61%，π₀.₅为53%。YAM视觉变化下成功17/20，对照为4/20；与Molmo2组合的Franka长程任务ID/OOD步骤完成率为64.7%/49.8%。

## 局限

需要核查三维表示的获取方式及其误差敏感性；动作策略只用干净场景示范，不等于所有上游模块都未接触相关变化。长程结果是步骤完成率。

- **判断**：值得精读表示构造与扰动实验：跨基准和真实机器人结果都支持三维目标定位这一设计方向。

## 研究关联

对VLA和分层机器人系统研究者，价值在于把目标定位变成明确的策略接口，既便于研究空间泛化，也方便Agent通过点、框等方式指定操作对象。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：49
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/Grounded Action Model 3D Grounding as a Foundation for Robotics.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Manipulation policies must know which objects matter and where they are, yet the pretrained backbones that current robot foundation models build on, from language in vision-language-action models (VLAs) to video generation in world-action models (WAMs), do not directly require this metric grounding, leaving it to be learned implicitly from robot demonstrations. We propose Grounded Action Models (GAMs), a new paradigm of robot foundation models built with 3D grounding. GAM can be conditioned using language, points, or box prompts, which are first transformed into a shared object-centric representation of the selected objects. This representation captures target-focused visual features and metric object geometry, which is mixed with robot state history through a multi-stream transformer to predict action chunks. Although GAMs can be run autonomously, they can also serve as a low-level controller that a high-level planner controls using its various input modalities, allowing for long-horizon and memory-dependent manipulation. On RoboTwin 2.0, GAM achieves an average success rate of 55.3% across 50 tasks (vs. 52.0% for Spatial Forcing), including 47.6% under scene randomization (vs. 30.4% for Abot-M0), with its action policy trained only on clean-scene demonstrations. On LIBERO-PRO, it achieves a state-of-the-art average success rate of 61% (vs. 53% for $π_{0.5}$) across 16 perturbation settings, with the largest gains when targets are relocated or newly designated. On two real robots, GAM retains 17/20 successes under visual shift on a bimanual YAM versus 4/20 for $π_{0.5}$, while its composition with a Molmo2 planner on a Franka achieves 64.7% ID and 49.8% OOD step completion on long-horizon and memory-dependent tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.23863v1
- Authors: Gehao Zhang, Weikai Huang, Shailesh Shailesh, Yiyan Peng, Jiafei Duan, Ranjay Krishna
- Published: 2026-09-20T20:35:39Z
- Age days: 2

</details>
