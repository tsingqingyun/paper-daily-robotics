---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.24124v1"
published: "2026-09-21T05:23:37Z"
age_days: 1
score: 35
created: 2026-09-23
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# ActiveArena: Benchmarking and Understanding Active Perception in Robotic Manipulation

> [!summary] 先说人话（基于摘要）
> ActiveArena测试机器人能否主动换视角、通过交互找信息，并记住此前看到的证据。它把“会不会获取信息”从普通操作成功率中单独拿出来研究。

## 问题

现有基准难以评估主动获取和维护信息的能力；这些任务仅凭被动观测难以解决，需要多轮观察、交互及基于记忆的推理。

## 创新点或方法

提供可控视角和大工作空间的模拟器，构建带记忆标注和ID/OOD协议的任务集，并用13种模块化VLA配置研究记忆写入、容量、本体状态、子任务监督和规划。

## 证据

基准含5类、35项任务。结果显示显著ID/OOD差距；均匀记忆采样、可靠写入下的更大容量、本体状态和子任务监督改善OOD表现；规划器使用稀疏记忆即可接近最佳配置。摘要未给出可核查的成功率数字。

## 局限

记忆容量收益以可靠写入为条件，不能理解为记忆越多越好；摘要未报告真实机器人验证。

- **判断**：做主动感知或记忆VLA值得精读任务协议及受控对照。

## 研究关联

为VLA记忆与Agent主动感知提供受控实验平台，能检验收益究竟来自存得更多、写得更好，还是主动获取了关键证据。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/ActiveArena Benchmarking and Understanding Active Perception in Robotic Manipula.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Active perception and manipulation are crucial for robots to interact with complex scenes. Existing benchmarks struggle to evaluate how robots effectively acquire and maintain information in memory in an active manner. To this end, we introduce ActiveArena-Sim, an active-perception simulator with controllable viewpoints and large-scale workspaces as the foundation. Built on this, we propose ActiveArena-Bench, which comprises 35 tasks across 5 fine-grained categories, covering visual exploration and interactive information acquisition. Each task is difficult to solve from passive observations alone, requiring multi-round evidence acquisition and memory-based reasoning. The benchmark provides rich memory annotations, standardized training data, and ID/OOD protocols featuring disjoint scenes, unseen distractor configurations, and novel backgrounds. Moreover, we present ActiveArena-VLA, a modular suite of 13 vision-language-action configurations for controlled studies of memory writing, memory capacity, proprioceptive state, subtask supervision, and high-level planning in active perception. Benchmark results reveal a substantial ID-OOD gap: uniform memory sampling, increased memory capacity under reliable write policies, proprioceptive inputs, and subtask supervision improve OOD generalization, while planner-guided memory management and decision-making achieve performance close to the best-performing configuration using only sparse memory. ActiveArena thus provides a unified testbed to develop and diagnose models for active perception and manipulation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.24124v1
- Authors: Yibo Li, Enshen Zhou, Rui Chen, Yanjun Ding, Mengzhen Liu, Yi Han, Jiabo Zhan, Lipeng Wang, Shanghang Zhang, Lu Sheng
- Published: 2026-09-21T05:23:37Z
- Age days: 1

</details>
