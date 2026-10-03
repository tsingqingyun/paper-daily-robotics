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
url: "https://arxiv.org/abs/2610.02204"
published: "Fri, 02 Oct 2026 00:00:00 -0400"
age_days: 0
score: 35
created: 2026-10-03
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents

> [!summary] 这篇论文到底做了什么（基于摘要）
> RPG 不更新模型权重，而是让机器人在仿真中练习、诊断失败，并修改可复用技能和系统提示。每项修改经过跨任务测试后才保留，最终由多模态 LLM 调用这些技能完成操作。

## 问题

任务是提高多种机器人操作任务的可靠性。通常需要人工开发和维护技能、设计奖励，并把感知与控制接起来，成本很高。RPG 要自动承担其中的诊断和系统修改工作；摘要没有逐一分析既有方法为什么失败。

### 用一个例子理解

理解用例（非论文实验）：离线视频显示把积木放入盒子；系统构造仿真练习，发现抓取后频繁碰到盒沿，于是修改放置技能和调用提示；通过其他任务测试后保留修改，真机执行时输出相应技能调用和控制动作。

## 创新点或方法

从离线数据中识别操作能力并构造相关仿真练习，RPG 用执行反馈、模拟器内部状态和数据视频判断失败原因，然后新增或修改符号技能、修订系统提示。候选改动单独测试，合并后再做跨任务评估，合格才留下。所谓改进发生在技能库和提示层，模型权重不变；测试时多模态 LLM 使用保留的提示和技能协调感知与控制，不再依赖练习时的特权状态。

### 方法如何工作

1. 从离线数据识别操作能力，构造仿真练习，使系统获得可反复试错的任务。
2. 执行练习并结合反馈、模拟器状态与视频诊断失败，为修改提供依据。
3. 据此更新技能库和系统提示，把一次诊断转成可复用的执行规则。
4. 分别测试候选改动和合并版本，保留跨任务表现合格的修订。
5. 冻结改进后的系统，由多模态 LLM 调用技能协调真实执行。

### 必要术语

- 符号技能：可命名、可调用的操作程序；本文通过新增和修改它们积累能力。
- 特权模拟器状态：仿真直接提供的内部信息；本文用它辅助练习阶段的失败诊断。
- 跨任务评估：把修改放到多个任务上检查；本文用它决定哪些改动可以保留。

## 证据

摘要报告，在 22 个操作任务的留出初始条件上，成功率从第一轮练习后的 28.6% 增至第 15 轮后的 95.0%，超过 ASPIRE 的 75.5% 和使用 GPT-6 Astra Pro 的 CaP-Agent0 的 60.0%。经过共同的校准与硬件适配，冻结系统在三个真机任务上各做十次、合计 30 次均成功。前者是留出初始条件，不能自动读成未见任务；后者是真机结果，但任务覆盖有限。

## 局限

摘要没有明确列出局限。我会核查仿真练习任务如何构造、诊断是否依赖难以获得的特权信息，以及校准与硬件适配需要多少人工。30 次成功支持这三个任务上的可行性，无法据此认定长期部署不会失败。

- **判断**：值得读完整的改进与保留流程，尤其是如何防止修好一个任务却破坏其他任务；这是机制中最值得复用的部分。

## 研究关联

它提示我们，能力改进也可以来自执行系统本身：把反复出现的失败转成可调用技能，并用跨任务检查约束修改。在模型权重不便调整、且已有仿真和技能接口时，这条路线值得尝试。

### 下一步读哪里

下一步检查技能的表示与修改权限、失败诊断依据、候选改动的接受标准，以及单独修改和合并修改的评估方式；核查留出初始条件与真机适配的具体设置。

- **概念**：多模态基础模型 智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-03/Reconstruct, Practice, Go Real Guided Self-Improvement for Embodied Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2610.02204v1 Announce Type: new Abstract: Building reliable robot capabilities across diverse tasks requires substantial human effort to develop and maintain skills, design rewards, and integrate perception with control. We present Reconstruct, Practice, Go Real (RPG), a framework for autonomous improvement of robot execution systems without updating model weights. RPG identifies manipulation capabilities in an offline dataset and constructs related practice tasks in simulation. During practice, RPG uses execution feedback, privileged simulator state, and available dataset videos to diagnose failures. It develops new reusable symbolic skills, refines existing skills, and revises the system prompt based on these diagnoses. Cross-task evaluation tests individual candidate changes and merged revisions before they are retained for reuse. At test time, a multimodal LLM uses the resulting system prompt and skill library to coordinate perception and robot control. On held-out initializations of 22 manipulation tasks, RPG improves task success from 28.6% after the first practice round to 95.0% after 15 rounds, outperforming all evaluated baselines, including ASPIRE (75.5%) and CaP-Agent0 powered by GPT-6 Astra Pro (60.0%). After a common calibration and hardware-adaptation procedure, the frozen system succeeds in all 30 physical trials, with ten trials on each of three tasks. Project Website: https://rpg-robot.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.02204
- Authors: Yen-Jen Wang, Haozhe Jiang, Shuying Deng, Haoru Xue, Weirui Ye, Rocky Duan, Nika Haghtalab, S. Shankar Sastry, Pieter Abbeel, Haozhi Qi
- Published: Fri, 02 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
