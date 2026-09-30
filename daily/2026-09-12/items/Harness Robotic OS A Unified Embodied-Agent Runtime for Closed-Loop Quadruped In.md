---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.11225v1"
published: "2026-09-10T08:25:46Z"
age_days: 1
score: 30
created: 2026-09-12
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# Harness Robotic OS: A Unified Embodied-Agent Runtime for Closed-Loop Quadruped Inspection

> [!summary] 先说人话（基于摘要）
> HROS把四足巡检中的导航、场景理解、语音交互和告警报告接成可追溯闭环。Argos是它在住宅社区巡检中的具体实现。

## 这篇到底在做什么

- **卡在哪里**：巡检系统需要协调异构感知、自治能力、知识和业务响应；任务专用接口让上下文共享、经验复用与受控更新变得困难。
- **关键解法**：系统划分机器人运行时、自治技能、认知Agent及交互运营层，以共享上下文连接物理状态与推理，加入分层记忆和流式语音；执行轨迹生成版本化候选更新，并经安全门控控制适配。
- **拿什么证明**：住宅物业实验报告航点可达率100%、室外定位误差低于10 cm、局部障碍响应延迟低于200 ms、代表性危险检测率85%—95%，告警送达与结构化报告生成成功率99%。

## 值不值得读

- **和你的研究有什么关系**：适合研究多模态Agent如何嵌入真实机器人业务闭环，特别是状态共享、交互和运维接口。
- **先别急着信**：需核查实验规模、危险类别与检测率口径；所列结果验证巡检闭环，但未单独证明记忆或自演进机制带来的提升。
- **判断**：系统集成研究者值得读架构与运行记录，算法研究者可重点查看模块评估是否充分。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-12/Harness Robotic OS A Unified Embodied-Agent Runtime for Closed-Loop Quadruped In.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Autonomous property inspection requires more than robust robot navigation: a deployable system must connect heterogeneous sensing, reusable autonomy capabilities, multimodal scene understanding, human interaction, and enterprise response within a traceable operational loop. Existing quadruped inspection systems commonly integrate these functions through task-specific interfaces, making contextual coordination, knowledge reuse, and controlled adaptation difficult. This paper presents \textit{Harness Robotic OS} (HROS), a unified embodied-agent runtime, and Argos, its realization for residential-community inspection. HROS organizes the system into robot runtime, embodied autonomy skills, cognitive agent runtime, and interaction and operations planes. A shared context connects physical state with agent reasoning; streaming ASR/TTS supports voice-based mission interaction; hierarchical working, episodic, and semantic memory preserves operational knowledge; and a safety-gated self-evolution loop converts execution traces into versioned candidate updates without permitting unconstrained online modification. The Argos prototype integrates a Vbot quadruped, Fast-LIO2 localization and mapping, Hobot-Stereo depth perception, PCT-Planner global planning, EGO-Planner local motion generation, and OpenClaw-orchestrated Qwen3-VL inspection analysis. Experiments in a residential property environment achieved 100\% waypoint reachability, outdoor localization error below 10~cm, local obstacle-response latency below 200~ms, representative hazard-detection rates of 85--95\%, and 99\% success in alarm delivery and structured-report generation. These results validate the deployed navigation and inspection closed loop, while HROS provides an extensible software foundation for memory-augmented, voice-aware, and continuously improvable embodied inspection agents.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.11225v1
- Authors: Yaoyuan Yan, Zhiyou Heng, Haoxiang Jie, Gang Liu, Hongjie Yan, Wei Zhou
- Published: 2026-09-10T08:25:46Z
- Age days: 1

</details>
