---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.30715v1"
published: "2026-09-25T02:43:24Z"
age_days: 3
score: 32
created: 2026-09-28
concepts: ["多模态基础模型", "世界模型", "具身智能评测与基准"]
---

# RoboMonitor: Label-Efficient Runtime Monitoring of Robot Task Execution via Predictive Representation Learning

> [!summary] 先说人话（基于摘要）
> RoboMonitor 给机器人配一个只看指令和相机的执行监控器，判断阶段、失败与完成。它先从已有操作轨迹学习预测表示，再用少量标注训练监控能力。

## 问题

策略能输出动作，却不能仅凭动作确认任务是否正常推进；而策略数据通常缺少监控所需的阶段和失败标注。瓶颈是用有限监督获得可靠、时间上稳定的执行判断。

## 创新点或方法

预训练联合动作条件未来特征预测、逆动力学和当前特征掩码预测，再将视觉与上下文编码器迁移到因果监控器。Temporal SFT 在窗口内各时刻提供监督，并约束窗口内及重叠窗口的一致性；部署只需任务指令与图像。

## 证据

预训练使用 25 小时、12 个任务、两种本体的多相机轨迹。四任务基准上，52 个标注回合、两个微调种子取得 93.1% 平均阶段准确率和 85.9% 宏召回；Qwen3-VL 消融中虚假阶段切换由 15.23% 降至 4.95%。闭环系统完成仿真 39/40、真机 35/40 次试验，未观察到误恢复触发。

## 局限

闭环成功率属于集成系统，不能全部归因于监控器；未观察到误触发也不代表不会漏报，需核查失败检测与完成判断的分项表现。

- **判断**：值得精读监督预算对照和闭环错误分析，适合需要为现有策略增加执行监控的团队。

## 研究关联

对具身评测与世界模型表示研究者，它展示了预测预训练如何服务于执行监控，而不只是动作生成。少标注监控和闭环恢复接口具有直接系统价值。

- **概念**：[[多模态基础模型]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/RoboMonitor Label-Efficient Runtime Monitoring of Robot Task Execution via Predi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Learned robot policies produce actions, but their outputs alone do not establish whether execution is progressing as intended. Robot execution monitoring requires identifying the current execution phase, detecting failures, and recognizing task completion from observations available during execution. Training such monitors requires annotations that are scarce in datasets collected for robot-policy learning. We present RoboMonitor, a label-efficient vision--language execution monitor that learns from these datasets before introducing monitoring supervision. We pre-train on 25 hours of multi-camera trajectories spanning 12 manipulation tasks and two robot embodiments, using action-conditioned future-feature prediction, inverse dynamics, and masked-present prediction. We then transfer the learned visual and context encoders to a causal monitor and apply temporal supervised fine-tuning (Temporal SFT), which combines supervision throughout each observation window with consistency objectives within and across overlapping windows. At deployment, RoboMonitor requires only the task instruction and camera observations. On a four-task monitoring benchmark, RoboMonitor trained with 52 labeled episodes achieves 93.1% mean phase accuracy and 85.9% macro recall over two fine-tuning seeds, exceeding Qwen3-VL and Robometer trained with the same monitoring supervision. Its phase accuracy also exceeds that of both Qwen3-VL and Robometer trained with 100 episodes. A Qwen3-VL ablation shows that Temporal SFT reduces mean spurious phase switching from 15.23% to 4.95%. In closed-loop deployment, the integrated system completes 39 of 40 simulated Toolbox Sorting trials and 35 of 40 real-world Reel Packing trials, with no false recovery triggers observed.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.30715v1
- Authors: Abhiroop Ajith, Gokul Narayanan, Kyle Coelho, Tingji Zhao, Yash Shahapurkar, Brian Zhu, Melih Erdogan, Ted Krubasik, Constantinos Chamzas, Eugen Solowjow
- Published: 2026-09-25T02:43:24Z
- Age days: 3

</details>
