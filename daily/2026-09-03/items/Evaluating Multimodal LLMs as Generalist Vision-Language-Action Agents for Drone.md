---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.01404v1"
published: "2026-09-01T15:27:43Z"
age_days: 1
score: 32
created: 2026-09-03
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Evaluating Multimodal LLMs as Generalist Vision-Language-Action Agents for Drone Control: Commanding, Approaching, Tracking and Searching

> [!summary] 先说人话（基于摘要）
> DroneCATS-Agent 直接让多模态大模型通过提示声明的动作空间控制无人机，并用 DroneCATS 分别测试接近、跟踪、搜索和多机指挥。结果显示主要失败并非飞行，而是持续遵守动作协议和正确宣布结束。

## 这篇到底在做什么

- **卡在哪里**：既有系统常缩窄 MLLM 的决策权限，难以判断它能否成为真正的通用控制代理；即使空间导航正确，错误终止、犹豫或跨视角复制命令也会使整局失败。
- **关键解法**：架构把 MLLM 设计成可替换组件，不微调、也不用函数调用 schema；模型自行偏航、搜索、不确定时推理和宣告到达，并将模型作为基准中的自变量，覆盖到2B小模型。
- **拿什么证明**：摘要称小型开放模型常比前沿模型更可靠地进入成功半径，却因过早或遗漏到达声明而失败；多机任务中，小模型会把同一坐标盲目复制到不同视图。未给出可核查数字。

## 值不值得读

- **和你的研究有什么关系**：对具身 Agent 和边缘 VLA，基准把“协议纪律与终止”从导航能力中单独暴露出来，提示部署评测不能只看轨迹或空间距离。
- **先别急着信**：摘要没有列出模型、场景规模、控制频率和统计结果；“小模型导航更可靠”的普遍性需结合完整协议判断。
- **判断**：值得读基准定义和错误分类，尤其适合研究终止动作与代理协议；不应仅凭摘要把结果外推到真实复杂飞行。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-03/Evaluating Multimodal LLMs as Generalist Vision-Language-Action Agents for Drone.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Multimodal Large Language Models (MLLMs) are strong perceivers of images and video. We ask how far that reach extends into acting: dropping an MLLM directly into a drone's control loop, with its entire action space declared solely in the prompt. Recent systems approach this setting but increasingly narrow the model's decision-making. We widen it back. We introduce DroneCATS-Agent, an architecture where the MLLM is a swappable component, and DroneCATS, a benchmark treating the model as the independent variable. Beyond merely flying toward a pixel, our agent entrusts the model to yaw and search, deliberate when unsure, and self-declare arrival---all without fine-tuning or function-calling schemas. Evaluating frontier and open models across four core capabilities---approaching a visible target, tracking a moving one, searching outside the initial view, and commanding a multi-drone fleet---reveals that even the simplest embodied settings are far from solved. Crucially, to identify what breaks first at the edge, our roster scales down to 2B parameters. The findings expose a stark paradox: it is not the flying that fails. Small open models often navigate into the success radius more reliably than frontier models, yet lose the episode by declaring arrival prematurely or not at all. Multi-drone commanding amplifies this divide, with small models failing by blindly copying a single coordinate across distinct views. Viewed as vision-language-action agents, the models' spatial perception holds up, but their action protocol does not. What separates a deployable edge model from a frontier model is not navigation, but the discipline to sustain a declared protocol and emit the correct terminating action. The open problem is closing this gap at onboard compute costs---yielding a fast model that plans persistently and knows exactly when it is done---and DroneCATS is built to measure that distance.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.01404v1
- Authors: Jaewoo Park, Minyoung Lee, Sukmin Seo, Moonbin Yim, Hyunwook Yoon, Dohoon Ryu, Daehee Kim, Myungseo Song, Jihyuk Byun, Seunggyu Chang, Taeho Kil, Jiseob Kim, Bado Lee, Geewook Kim
- Published: 2026-09-01T15:27:43Z
- Age days: 1

</details>
