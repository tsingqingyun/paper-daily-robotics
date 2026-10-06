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
url: "https://arxiv.org/abs/2610.02204v1"
published: "2026-10-01T17:59:50Z"
age_days: 4
score: 33
created: 2026-10-06
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents

> [!summary] 这篇论文到底做了什么（基于摘要）
> RPG 让机器人先从离线数据中找出可练习的能力，再在仿真里反复诊断失败、修改技能和系统提示词。它不更新模型权重，而是通过跨任务测试筛选修改，最终把积累的执行知识交给多模态 LLM 使用。

## 问题

任务是提高多种机器人操作的可靠性。开发者通常要人工维护技能、设计奖励并连接感知和控制；RPG 针对的是这种持续调试成本。它把人工发现错误、修改执行规则的工作变成仿真练习循环，而非单纯扩大策略训练。

### 用一个例子理解

理解用例（非论文实验）：输入一段抽屉操作数据；系统构造仿真练习，利用失败反馈发现某条操作规则不合适，修改技能并测试其他任务。通过检查后，输出更新的技能库和提示词，供测试时 LLM 调用；具体故障类型为自拟。

## 创新点或方法

旧做法依赖人维护执行系统；RPG 从离线数据识别能力并构造相关练习任务，结合执行反馈、仿真器特权状态和数据视频诊断失败，然后新增或修改符号技能、修订系统提示词。单项改动及合并版本经过跨任务评估后才保留。练习阶段更新的是程序和提示词；测试阶段，多模态 LLM 使用最终技能库协调感知与控制，模型权重不变。

### 方法如何工作

1. 从离线数据识别操作能力并构造仿真练习，让改进有明确的任务来源。
2. 结合执行反馈、仿真内部状态和视频诊断失败，得到修改技能或提示词的依据。
3. 生成新技能及修订，分别测试单项改动和合并版本，以检查收益与相互干扰。
4. 保留通过跨任务评估的修改，测试时由多模态 LLM 使用这些知识协调感知和控制。

### 必要术语

- 特权状态：仿真器可直接提供、相机未必能观察到的内部信息；本文用于练习阶段诊断。
- 符号技能：用明确操作规则表达的可复用技能；本文修改它来改善执行。
- 冻结系统：测试时不再继续修改的系统；本文用它进行实体试验。

## 证据

摘要报告：在 22 个操作任务的留出初始状态上，成功率由首轮练习后的 28.6% 升至 15 轮后的 95.0%；ASPIRE 为 75.5%，使用 GPT-6 Astra Pro 的 CaP-Agent0 为 60.0%。这些结果支持多轮练习后的执行改进，但不能单独拆出各模块贡献。实体部分经过共同校准和硬件适配，冻结系统在三个任务、每个十次、合计 30 次试验中全部成功。

## 局限

仿真练习能访问真实部署时通常没有的内部状态，因此要检查诊断如何转化为部署可用知识。30 次实体成功只覆盖三个任务，且经过校准和硬件适配，不能解释成无需适配的广泛迁移。统计波动和各修改机制的贡献仍需核查。

- **判断**：值得深入读改动筛选与跨任务评估，因为这两处决定它能否持续积累有效技能，而非只修好当前练习。

## 研究关联

值得借鉴的是把执行知识当作可以提出修改、检验和积累的对象。模型会调用工具但反复犯流程错误时，可以先检查技能和提示词是否可修正，同时用其他任务测试防止局部修补造成退化。

### 下一步读哪里

优先查失败诊断实例、候选改动如何比较及合并后怎样复测，再查 22 个任务的逐任务结果。实体部分要核查三项任务、校准内容和硬件适配是否包含人工修订。

- **概念**：多模态基础模型 智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：33
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-06/Reconstruct, Practice, Go Real Guided Self-Improvement for Embodied Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Building reliable robot capabilities across diverse tasks requires substantial human effort to develop and maintain skills, design rewards, and integrate perception with control. We present Reconstruct, Practice, Go Real (RPG), a framework for autonomous improvement of robot execution systems without updating model weights. RPG identifies manipulation capabilities in an offline dataset and constructs related practice tasks in simulation. During practice, RPG uses execution feedback, privileged simulator state, and available dataset videos to diagnose failures. It develops new reusable symbolic skills, refines existing skills, and revises the system prompt based on these diagnoses. Cross-task evaluation tests individual candidate changes and merged revisions before they are retained for reuse. At test time, a multimodal LLM uses the resulting system prompt and skill library to coordinate perception and robot control. On held-out initializations of 22 manipulation tasks, RPG improves task success from 28.6% after the first practice round to 95.0% after 15 rounds, outperforming all evaluated baselines, including ASPIRE (75.5%) and CaP-Agent0 powered by GPT-6 Astra Pro (60.0%). After a common calibration and hardware-adaptation procedure, the frozen system succeeds in all 30 physical trials, with ten trials on each of three tasks. Project Website: https://rpg-robot.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.02204v1
- Authors: Yen-Jen Wang, Haozhe Jiang, Shuying Deng, Haoru Xue, Weirui Ye, Rocky Duan, Nika Haghtalab, S. Shankar Sastry, Pieter Abbeel, Haozhi Qi
- Published: 2026-10-01T17:59:50Z
- Age days: 4

</details>
