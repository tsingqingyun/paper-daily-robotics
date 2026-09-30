---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.25606v1"
published: "2026-09-22T02:58:36Z"
age_days: 1
score: 32
created: 2026-09-24
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# CableVLA: Simulation-Privileged Global-Local Representation Learning for Cable Routing

> [!summary] 先说人话（基于摘要）
> CableVLA 同时学习线缆整体形态与局部接触变化，再在接触阶段用触觉残差修正动作。仿真中的额外信息被用于训练部署时可用的视觉与触觉表示。

## 问题

线缆布线既要维持全局拓扑，又要应对不断变化的局部接触；单靠视觉动作基线难以兼顾这两个尺度。

## 创新点或方法

TopoHead 将节点物理信息及当前、未来线缆拓扑蒸馏到因果视觉上下文。TacSense 用帧级与 taxel 分支学习电阻阵列接触动态，并接受仿真运动学与接触事件监督；接触门控启用力触觉残差，修正冻结策略接下来八个机械臂与夹爪动作。

## 证据

345 次 MuJoCo 评测中，成功率从 π₀.₅-V 视觉基线的 62.6% 提升到 84.9%。TacSense 的滑移转换识别优于参数量相近的 CNN-LSTM，冻结编码器探测仍保留优势；另有拓扑预测、57 任务触觉评测及跨仿真和真实迁移比较。

## 局限

摘要没有给出跨仿真和真实零样本迁移的结果数字，仿真成功率提升不能直接视为真实部署收益。

- **判断**：做柔性物体和触觉 VLA 值得精读，重点核查特权信息如何退出部署流程以及真实迁移结果。

## 研究关联

对 VLA 和机器人学习研究者，它具体展示了如何把仿真特权监督转化为部署表征，并在冻结基础策略的条件下加入局部接触修正。

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/CableVLA Simulation-Privileged Global-Local Representation Learning for Cable Ro.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Cable routing requires coordinated control of global cable topology and changing local contacts. We present CableVLA, an end-to-end multimodal vision-language-action framework that converts simulation-privileged supervision into deployable cable-topology and tactile representations. TopoHead distills node-level physics and current and future cable-topology information into causal visual context for the action expert. TacSense uses complementary frame and taxel branches to learn contact dynamics from resistive arrays, with simulator-derived kinematics and contact events providing supervision beyond the measured force map. A contact gate activates force-tactile residuals that refine the next 8 arm-and-gripper actions of a frozen topology-conditioned policy. Across 345 MuJoCo evaluations, CableVLA improves success from 62.6% for the $π_{0.5}$-V visual baseline to 84.9%. TacSense achieves pronounced gains in slip-transition recognition over a CNN-LSTM baseline with a similar parameter count, and this advantage persists under frozen-encoder probes. Topology prediction and 57-task tactile evaluations assess representation quality, while policy adaptation studies evaluate downstream control performance. Cross-simulator and real-robot comparisons further examine zero-shot policy transfer under changes in dynamics and sensing.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.25606v1
- Authors: Zhifei Teng, Bo Feng, Xiang Zou, Jinpeng Xiao, Min Li, Zhouping Yin, Yiqun Li
- Published: 2026-09-22T02:58:36Z
- Age days: 1

</details>
