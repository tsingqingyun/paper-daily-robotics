---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2604.22591"
published: "Mon, 07 Sep 2026 00:00:00 -0400"
age_days: 0
score: 30
created: 2026-09-08
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# RedVLA: Physical Red Teaming for Vision-Language-Action Models

> [!summary] 先说人话（基于摘要）
> RedVLA 主动构造能诱发机器人危险行为的场景，帮助部署前发现风险。它先把风险因素放到任务关键交互区域，再迭代调整以稳定触发问题。

## 这篇到底在做什么

- **卡在哪里**：现有机制不足以在部署前系统暴露 VLA 的物理安全风险，普通任务成功评测无法充分覆盖危险执行。
- **关键解法**：从正常轨迹定位关键交互区域，在保持场景有效和任务可行的前提下放置风险因素；使用轨迹特征引导的无梯度优化放大风险，并用生成数据构建 SimpleVLA-Guard。
- **拿什么证明**：在六个 VLA 上发现多种不安全行为，十次优化迭代内攻击成功率最高达到 95.5%；摘要未给出安全防护模块的改善数字。

## 值不值得读

- **和你的研究有什么关系**：为具身评测提供主动寻找失效场景的方法，可用于检验 VLA 在高任务成功率之外的物理风险。
- **先别急着信**：最高攻击成功率对应定向优化场景，不能解释为自然部署中的事故概率；还需核查风险判定和防护效果。
- **判断**：值得精读风险构造与评测协议，防护方案则需依据全文结果单独判断。

## 研究关联

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-08/RedVLA Physical Red Teaming for Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2604.22591v2 Announce Type: replace Abstract: The real-world deployment of Vision-Language-Action (VLA) models remains limited by the risk of unpredictable and irreversible physical harm. However, we currently lack effective mechanisms to proactively detect these physical safety risks before deployment. To address this gap, we propose \textbf{RedVLA}, the first red teaming framework for physical safety in VLA models. We systematically uncover unsafe behaviors through a two-stage process: (I) \textbf{Risk Scenario Synthesis} constructs a valid and task-feasible initial risk scene. Specifically, it identifies critical interaction regions from benign trajectories and positions the risk factor within these regions, aiming to entangle it with the VLA's execution flow and elicit a target unsafe behavior. (II) \textbf{Risk Amplification} ensures stable elicitation across heterogeneous models. It iteratively refines the risk factor state through gradient-free optimization guided by trajectory features. Experiments on six representative VLA models show that RedVLA uncovers diverse unsafe behaviors and achieves the ASR up to 95.5\% within 10 optimization iterations. To mitigate these risks, we further propose SimpleVLA-Guard, a lightweight safety guard built from RedVLA-generated data. Our data, assets, and code are available \href{https://redvla.github.io}{here}.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2604.22591
- Authors: Yuhao Zhang, Borong Zhang, Jiaming Fan, Jiachen Shen, Yishuai Cai, Yaodong Yang, Jiaming Ji
- Published: Mon, 07 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
