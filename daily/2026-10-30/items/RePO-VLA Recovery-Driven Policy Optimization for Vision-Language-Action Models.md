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
url: "https://arxiv.org/abs/2605.09410"
published: "Thu, 29 Oct 2026 00:00:00 -0400"
age_days: 0
score: 35
created: 2026-10-30
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# RePO-VLA: Recovery-Driven Policy Optimization for Vision-Language-Action Models

> [!summary] 这篇论文到底做了什么（基于摘要）
> RePO-VLA 教机器人在操作偏离后接着把事情做成：把纠正轨迹单独拿出来学，再给正常、失败和恢复动作标上进展价值。部署时用固定的高价值 token 引导动作，无需额外的在线失败检测器或启发式重试。

## 问题

长流程、接触频繁的操作容易积累误差。只模仿成功过程，机器人很少学到物体歪了、接触错了之后该怎么办；直接丢弃失败轨迹，又浪费了其中仍然正确的前半段。恢复动作还有特殊难点：它应由当前的不利状态触发，不能依赖完整重演此前的错误。

### 用一个例子理解

理解用例（非论文实验）：双臂整理布料时，一角滑出夹爪。输入是当前画面、整理指令和高价值 token；策略依据训练中学过的恢复动作重新夹住布角，再继续展开。输出是一段纠正后的动作，而不是从头重复整个任务。

## 创新点或方法

本文把成功、恢复和失败数据分开使用。RAI 将纠正后缀切成独立片段，让策略从偏离状态直接学习恢复。PAS-VF 根据轨迹的时空特征、指令和成功参考评估进展，用可靠性衰减保留失败轨迹中有用的前缀，并给偏离或最终崩溃处低价值标签。规划器或人补充纠正轨迹，VCR 再训练策略偏向高进展动作。训练需要价值标注和恢复数据；推理只输入固定高价值 token。具体价值公式和 token 注入方式未说明。

### 方法如何工作

1. 把纠正后缀切成新片段，使不利状态直接对应恢复动作，减少对之前失败历史的依赖。
2. 用指令和成功参考评价轨迹进展，区分仍有用的失败前缀与真正偏离部分。
3. 由规划器或人从不利状态收集纠正过程，补足成功示范无法覆盖的动作。
4. 训练价值条件策略偏向高进展动作，部署时固定输入高价值 token，调用已学到的恢复行为。

### 必要术语

- RAI：把纠正过程作为独立起点来训练；用于建立偏离状态与修正动作的直接联系。
- PAS-VF：结合任务语义判断执行进展的价值函数；用于给不同阶段的动作提供标签。
- 成功流形：能够通向成功的一组状态和行为；本文用它描述恢复希望回到的区域。

## 证据

摘要报告在仿真及真机双臂任务上测试，并引入带标准化错误注入的 FRBench。对抗条件下，平均成功率从 20% 升至 75%；扩大规模的真机试验最高达到 80%（均来自摘要）。但摘要未指明 20% 对应哪个基线、平均覆盖哪些任务，也没有错误类型、样本量和方差。80% 是另一项最高结果，不能与平均 75% 直接合并比较。

## 局限

我会核查价值函数是否把看起来接近目标、实际已经不可恢复的状态评得过高，以及训练中的错误注入能否覆盖自然执行错误。固定高价值条件本身不保证找到恢复动作；摘要报告的鲁棒性范围仍受任务和扰动分布约束。

- **判断**：优先细读数据切片和价值标签设计，因为最值得复用的是怎样把失败经历整理成有效监督，数字收益还需要结合基线与错误设置判断。

## 研究关联

值得借鉴的是失败数据的使用粒度：一次失败执行不必整条判废，前段可能正确，后段可能已经恢复。将这些阶段区分开，才能教会策略“当前该继续、纠偏还是退出某种动作”，而不把错误和修正混学。

### 下一步读哪里

先核查 RAI 切片后保留哪些状态与历史信息，再看 PAS-VF 的参考轨迹、衰减规则及 VCR 训练目标。实验重点查 FRBench 错误强度、自然失败测试，以及分别移除三个组件后的恢复成功率。当前只有摘要依据。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


> 正文获取未成功，本卡仅依据摘要。原始错误：No supported versioned official arXiv HTML URL

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-30/RePO-VLA Recovery-Driven Policy Optimization for Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2605.09410v2 Announce Type: replace-cross Abstract: Vision-Language-Action (VLA) models remain brittle in long-horizon, contact-rich manipulation because success-only imitation provides little supervision for execution drift, while failed rollouts are often discarded. We introduce RePO-VLA, a recovery-driven policy optimization framework that assigns distinct roles to success, recovery, and failure trajectories. RePO-VLA first applies Recovery-Aware Initialization (RAI), slicing each corrective suffix into a new episode so corrective actions depend on the current adverse state rather than the preceding failure. It then learns a Progress-Aware Semantic Value Function (PAS-VF), aligning spatiotemporal trajectory features with instructions and successful references. The resulting labels salvage useful failure prefixes via reliability decay, while low-value labels mark drift and terminal breakdowns, teaching differences among nominal, failed, and corrective actions. The data engine turns adverse states into planner-generated or human-collected corrective rollouts, teaching recovery to the success manifold. Value-Conditioned Refinement (VCR) trains the policy to prefer high-progress actions. At deployment, a fixed high-value token biases actions toward the learned success manifold without online failure detectors or heuristic retries. We introduce the Failure-Recovery Benchmark (FRBench), with standardized error injection and recovery-focused evaluation. Across simulated and real-world bimanual tasks, RePO-VLA improves robustness, raising adversarial success from 20% to 75% on average and up to 80% in scaled real-world trials. Code and video results are available at https://1018weijia.github.io/RePO-VLA-Web/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2605.09410
- Authors: Weijia Liufu, Xiaoyu Guo, Ruiyi Chen, Jingzhi Liu, Kaidong Zhang, Xiwen Liang, Jianqi Lin, Dawei Sun, Yuze Wang, Rongtao Xu, Bingqian Lin, Bowen Yang, Tongtong Cao, Bowen Peng, Dongyu Zhang, Guangrun Wang, Min Wang, Liang Lin, Xiaodan Liang
- Published: Thu, 29 Oct 2026 00:00:00 -0400
- Age days: 0

</details>
