---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26578"
published: "Sat, 29 Aug 2026 00:00:00 -0400"
age_days: 0
score: 34
created: 2026-08-29
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes

> [!summary] 先说人话（基于摘要）
> TrapVLA研究一种更危险的VLA后门：隐蔽文本触发器不仅让机器人失败，还能指定它以何种方式失败。方法通过学习触发器诱导的动作残差，将策略推向预设偏移等故障行为。

## 问题

传统后门评测把任何任务失败都算攻击成功，无法衡量攻击者能否精确控制故障形态。VLA动作偏差可能只在少数时刻出现，使目标轨迹合成、注入和故障保真度测量都更困难。

## 创新点或方法

数据引擎生成目标故障轨迹，自动评测套件测量配置故障的忠实程度，并构建Trap-LIBERO与Trap-RoboTwin。TrapVLA针对策略动作显式学习由文本触发器引起的残差，而非仅训练一个导致笼统失败的后门。

## 证据

摘要称两个基准覆盖四类代表性故障，并在仿真及真实机器人上有效注入指定故障，同时大体保持干净数据性能；未给出成功率、干净性能下降或检测率数字。


## 局限

需全文核查触发器隐蔽性、四类故障的覆盖范围，以及“保持干净性能”与故障保真度的具体权衡。

- **判断**：做VLA部署、安全或评测应精读基准和攻击设定；只做常规策略学习可重点阅读威胁模型与评测部分。

## 研究关联

它为VLA安全评测提供了比“是否失败”更细的威胁模型，可测试机器人是否会被语言触发器稳定操纵成特定危险动作；与世界模型的直接关系较弱。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-29/TrapVLA Trapping Vision-Language-Action Models in Configured Failure Modes.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.26578v1 Announce Type: cross Abstract: This work introduces Configured Failure Trapping, a novel backdoor attack task against Vision-Language-Action (VLA) models, which aims to activate attacks through stealthy textual triggers and induce configured failure modes. Unlike prior backdoor attacks that treat any task failure as a successful attack, Configured Failure Trapping requires the attacker to control how the robot fails (e.g., causing the robot to grasp with a specified positional offset), making it substantially more challenging and hard to detect. To support the new task, we propose an effective data engine for synthesizing high-quality target trajectories and an automated suite for measuring configured-failure fidelity. Then, based on this foundation, we construct two new benchmarks, namely Trap-LIBERO and Trap-RoboTwin, that instantiate Configured Failure Trapping across four representative failure modes. To address this task, we identify sparse action deviation as a critical challenge and accordingly propose a novel method named TrapVLA, which explicitly learns trigger-induced action residuals to steer the policy toward the configured failure behavior. Extensive experiments across simulation benchmarks and real-world robotic settings show that TrapVLA effectively injects configured failure modes into VLA models while largely preserving performance on clean data. Project page: https://john-liua.github.io/TrapVLA/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26578
- Authors: Jun-Hui Liu, Kun-Yu Lin, Yi-Lin Wei, Xu-Han Chen, Yinghao Li, Zhuohao Li, Yuan-Ming Li, Qing Zhang, Xiaoyi Fan, Dongmei Jiang, Yan Li, Wei-Shi Zheng
- Published: Sat, 29 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
