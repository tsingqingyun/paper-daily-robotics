---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.37519v1"
published: "2026-09-29T13:10:14Z"
age_days: 0
score: 31
created: 2026-09-30
concepts: ["多模态基础模型", "智能体 Agent", "机器人学习", "具身智能评测与基准"]
---

# Video2STL: Grounding VLM-Generated Temporal Specifications for Robot Learning

> [!summary] 先说人话（基于摘要）
> Video2STL 把示范视频里的任务顺序转成可检查的时序逻辑，再据此训练机器人。VLM 负责描述事件结构，真实可执行轨迹负责确定阈值与时间范围。

## 问题

只有观察的视频没有动作标注，关键在于决定向机器人迁移什么。把视频压成相似度分数或直接生成奖励代码，会让任务的时间结构难以检查、落地和复用。

## 创新点或方法

VLM 从视频提取跨形态语义事件，生成参数化信号时序逻辑 STL 规范。成功机器人轨迹用于确定数值谓词和时间边界；短期规范产生密集奖励，长期因果监控器对有效任务前缀发放一次性进度奖励。

## 证据

四项操作任务平均 success-once/success-at-end 为 85.8%/67.0%，原生密集 PPO 为 81.5%/59.5%，Text2Reward 为 65.0%/42.3%。四足实验中，基于 Qwen-3.8 和 GPT-5.6 的策略在 0.3–2.1 m/s 速度范围内达到 100% 成功，并保持有竞争力的高速能效。

## 局限

规范落地需要成功机器人轨迹；需核查这些轨迹如何获得及数量，不能将其理解为完全无需机器人经验的视频学习。

- **判断**：值得精读规范落地和奖励构造，尤其适合研究长任务奖励设计、跨形态监督与可解释任务表示的人。

## 研究关联

对机器人学习和 VLM Agent，价值是提供可检查、可复用的中间任务表示，并把短期奖励与长期顺序约束分开。人或动物视频到机器人控制的迁移也有明确表示基础。

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Video2STL Grounding VLM-Generated Temporal Specifications for Robot Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Video-based policy learning is particularly promising, as it illustrates target behaviors without requiring action annotations or embodiment-matched demonstrations. A central challenge is deciding what information should be transferred from the video to the robot. Existing approaches commonly convert visual observations into scalar similarity or value signals, or ask foundation models to directly generate reward code. These approaches can make the temporal structure of a task difficult to inspect, ground, and reuse. We present Video2STL, a framework that converts observation-only videos into parametric Signal Temporal Logic (STL) specifications and uses the resulting formal representation for robot learning. A vision-language model extracts an embodiment-independent semantic event trace and constructs a bank of symbolic temporal specifications. The model determines the task structure, while numerical predicate thresholds and temporal bounds are grounded from successful robot trajectories. For policy learning, we separate short- and long-timescale temporal information: short-horizon specifications provide dense rewards through rolling-window quantitative robustness, while a causal monitor over a retained long-horizon specification provides one-time progress rewards for valid temporal prefixes. The same representation supports cross-embodiment transfer from human or animal videos to robot control. Across four manipulation tasks, Video2STL achieves $85.8\%$ average success-once and $67.0\%$ success-at-end, compared with $81.5\%/59.5\%$ for native dense PPO and $65.0\%/42.3\%$ for Text2Reward; in quadruped locomotion, Qwen-3.8 and GPT-5.6-based Video2STL policies achieve $100\%$ success across velocities from $0.3$ to $2.1\,\mathrm{m/s}$ while remaining competitive in high-speed energy efficiency. Project webpage: \href{https://video2stl.github.io/}{video2stl}.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37519v1
- Authors: Merve Atasever, Keyan Azbijari, Cagan Bakirci, Bo-Ruei Huang, Tolga Izdas, Zahra Shahrooei, Richard Yang, Erdem Biyik, Jyotirmoy V. Deshmukh
- Published: 2026-09-29T13:10:14Z
- Age days: 0

</details>
