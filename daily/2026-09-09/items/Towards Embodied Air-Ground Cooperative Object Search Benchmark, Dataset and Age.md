---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08402v1"
published: "2026-09-08T08:13:00Z"
age_days: 0
score: 27
created: 2026-09-09
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Towards Embodied Air-Ground Cooperative Object Search: Benchmark, Dataset and Agentic Method

> [!summary] 先说人话（基于摘要）
> AGOS-Agent用明确的“空中搜索—交接—地面核验”流程组织无人机和地面车协作找目标车辆。它把复杂协调交给协议和工具，让VLM主要负责场景理解与决策。

## 这篇到底在做什么

- **卡在哪里**：空地协同搜索需要把俯视发现与地面细节验证连接起来，并根据多视角参考确认目标；通用VLM直接承担动态协作时面临协调难题，也缺少专门评测。
- **关键解法**：提出AGOS-Bench及自动生成示范轨迹的AGOS-Dataset，覆盖三级难度。训练自由的AGOS-Agent通过工具与搜索、交接、验证协议组织UAV和UGV合作。
- **拿什么证明**：数据集包含7700段轨迹。9种VLM中，8种成功率提升，全部减少决策步数；困难划分上，Gemini-3.6-Flash的SR从8.6%升至55.7%，SPL从7.6%升至44.0%。

## 值不值得读

- **和你的研究有什么关系**：对多具身Agent评测提供任务、数据和协作基线，也说明固定协作流程可能显著影响VLM系统表现，不能把系统增益全部归于骨干能力。
- **先别急着信**：需核查工具提供了哪些感知与导航能力、对照是否具有相同权限，以及基准是否包含真实空地平台验证。
- **判断**：多机器人Agent方向值得精读协议与对照设置，困难集的大幅提升值得拆解。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：27
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-09/Towards Embodied Air-Ground Cooperative Object Search Benchmark, Dataset and Age.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Air-Ground Object Search (AGOS) in urban environments is a challenging embodied task, which requires an Unmanned Aerial Vehicle (UAV) and an Unmanned Ground Vehicle (UGV) to jointly search for and verify a specified target vehicle from multi-view visual references. To study this underexplored problem, we introduce AGOS-Bench, the first dedicated benchmark for evaluating whether general-purpose Vision-Language Models (VLMs) can integrate aerial discoveries and ground-level verification through UAV-UGV cooperation. We further provide AGOS-Dataset as the companion resource of exemplary trajectories constructed by an automatic pipeline. It consists of 7.7k episodes for searching objects of diverse categories and attributes, spanning three difficulty levels. To address the AGOS task, we propose AGOS-Agent, a training-free and tool-augmented approach. The agentic method relieves VLMs from complex and dynamic coordination via a deliberate search-handoff-verify cooperation protocol, only demanding VLMs for scene understanding and decision-making. Extensive experiments on nine VLMs show that AGOS-Agent improves overall success rate for eight of the nine evaluated backbones while reducing decision steps for all nine. On the hard split, the SR and SPL of Gemini-3.6-Flash increase from 8.6% to 55.7% and from 7.6% to 44.0%, respectively.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08402v1
- Authors: Boao Yu, Zimo Chen, Junreng Rao, Yue Hu, Zhengqiu Zhu, Yong Zhao, Rusheng Ju
- Published: 2026-09-08T08:13:00Z
- Age days: 0

</details>
