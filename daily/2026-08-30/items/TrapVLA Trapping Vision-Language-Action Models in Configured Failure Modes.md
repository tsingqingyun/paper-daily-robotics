---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26578v1"
published: "2026-08-27T03:44:49Z"
age_days: 2
score: 34
created: 2026-08-30
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes

> [!summary] 先说人话（基于摘要）
> TrapVLA研究一种更危险也更具体的 VLA 后门：隐蔽文本触发器不仅让任务失败，还能指定机器人以何种偏差方式失败。核心是学习触发器诱导的动作残差。

## 问题

传统后门评测把任何失败都算攻击成功，无法衡量攻击者能否精确控制故障形态；配置化失败还面临目标轨迹难合成、稀疏动作偏差难学习和故障一致性难度量。

## 创新点或方法

数据引擎合成指定失败轨迹，自动评测套件衡量失败模式忠实度，并构建 Trap-LIBERO、Trap-RoboTwin。TrapVLA显式学习文本触发器对应的动作残差，把正常策略推向指定位置偏移等故障。

## 证据

摘要称在模拟与真实机器人中能注入四类配置化故障，同时大体保持干净数据性能；未给出攻击成功率、干净性能下降或检测率数字。


## 局限

需全文核查触发器隐蔽性、四种失败的覆盖范围，以及干净性能“基本保持”的定量幅度。

- **判断**：安全研究者值得精读任务定义和指标；若只做控制性能，读基准与威胁模型即可。

## 研究关联

对 VLA 安全和具身评测研究者，它把威胁模型从“让机器人坏掉”推进到“控制机器人怎么坏”，两个基准也可用于防御和审计。对世界模型本身的直接价值有限。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-30/TrapVLA Trapping Vision-Language-Action Models in Configured Failure Modes.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

This work introduces Configured Failure Trapping, a novel backdoor attack task against Vision-Language-Action (VLA) models, which aims to activate attacks through stealthy textual triggers and induce configured failure modes. Unlike prior backdoor attacks that treat any task failure as a successful attack, Configured Failure Trapping requires the attacker to control how the robot fails (e.g., causing the robot to grasp with a specified positional offset), making it substantially more challenging and hard to detect. To support the new task, we propose an effective data engine for synthesizing high-quality target trajectories and an automated suite for measuring configured-failure fidelity. Then, based on this foundation, we construct two new benchmarks, namely Trap-LIBERO and Trap-RoboTwin, that instantiate Configured Failure Trapping across four representative failure modes. To address this task, we identify sparse action deviation as a critical challenge and accordingly propose a novel method named TrapVLA, which explicitly learns trigger-induced action residuals to steer the policy toward the configured failure behavior. Extensive experiments across simulation benchmarks and real-world robotic settings show that TrapVLA effectively injects configured failure modes into VLA models while largely preserving performance on clean data. Project page: https://john-liua.github.io/TrapVLA/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26578v1
- Authors: Jun-Hui Liu, Kun-Yu Lin, Yi-Lin Wei, Xu-Han Chen, Yinghao Li, Zhuohao Li, Yuan-Ming Li, Qing Zhang, Xiaoyi Fan, Dongmei Jiang, Yan Li, Wei-Shi Zheng
- Published: 2026-08-27T03:44:49Z
- Age days: 2

</details>
