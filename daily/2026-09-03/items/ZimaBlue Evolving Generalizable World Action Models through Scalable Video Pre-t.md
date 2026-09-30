---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.00188v1"
published: "2026-08-31T18:09:52Z"
age_days: 2
score: 33
created: 2026-09-03
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# ZimaBlue: Evolving Generalizable World Action Models through Scalable Video Pre-training

> [!summary] 先说人话（基于摘要）
> ZimaBlue 把大规模无动作第一视角视频转成机器人控制能力：先做因果具身视频预训练，再以异构机器人轨迹完成视频—动作落地，最后适配目标机器人。Slow-Fast 双系统让大型世界模型提供表征、轻量分支以30 Hz出动作。

## 问题

机器人泛化需要大量物理经验，但带动作标签的轨迹昂贵且多样性有限；第一视角视频虽丰富，却没有机器人动作，难点是把其中的交互和动力学经验可靠映射到可执行控制。

## 创新点或方法

三阶段课程依次学习视频动力学、通过统一动作表征连接异构轨迹、再面向目标机器人专门化；异步 Slow 世界模型与 Fast 控制分支分离高容量时空建模和实时动作预测。

## 证据

真实机器人零样本评测中，从仅用目标机器人数据扩展到超过12万小时具身视频后，成功率由36.1%升至77.8%；Fast 分支在 RTX 4090 上达到30 Hz。摘要还称多个基准上表现强、未见任务增益尤其明显，但未给数字。


## 局限

摘要未交代12万小时数据构成、目标机器人专门化所需数据量及零样本定义；36.1%到77.8%的归因边界需重点核查。

- **判断**：值得精读训练课程、统一动作表示和零样本协议；它的规模效应非常醒目，但也最需要检查数据与评测是否严格隔离。

## 研究关联

这为世界模型和 VLA 提供了一条绕开机器人动作数据瓶颈的规模化路线，并展示生成式视频表征如何与实时控制解耦。

- **概念**：智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-03/ZimaBlue Evolving Generalizable World Action Models through Scalable Video Pre-t.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robotic manipulation faces a fundamental scaling challenge: robust generalization demands broad physical experience, yet action-labeled robot trajectories are expensive to collect and inherently limited in diversity. Egocentric videos offer a far more scalable source of embodied experience, capturing object interactions, contact dynamics, tool use, and long-horizon behaviors across diverse environments. The central challenge is how to convert this abundant but action-free experience into effective robot control. We introduce ZimaBlue, a scalable framework for learning generalizable World Action Models (WAMs) from large-scale video. ZimaBlue follows a three-stage training curriculum: it first performs causal embodied video pre-training on large-scale human and robot egocentric videos, then grounds the learned visual dynamics in heterogeneous robot trajectories through video-action mid-training with a unified action representation, and finally specializes the model to a target robot for deployment. To make generative WAMs practical for real-time control, ZimaBluefurther adopts an asynchronous Slow-Fast dual-system architecture, where a high-capacity Slow world model provides generalizable spatiotemporal representations and a lightweight Fast branch enables 30 Hz action prediction on NVIDIA RTX 4090. On real-robot zero-shot evaluations, scaling from target-robot data alone to over 120,000 hours of embodied video improves success from 36.1% to 77.8%. ZimaBlue further delivers strong performance across multiple benchmarks, with particularly pronounced gains on unseen tasks.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.00188v1
- Authors: Xionghao Wu, Yijun Yang, Shiyang Zhou, Haoze Sun, Jianhui Liu, Songsong Yu, Jiyao Zhang, Wenbo Li, Bo Wang, Guoqing Ma, Lin Song, Renjie Liao, Shenghe Zheng, Wei Tang, Xiaojuan Qi, Yanwei Li, Yuan Zhang, Zhuotao Tian, Haoyang Huang, Nan Duan
- Published: 2026-08-31T18:09:52Z
- Age days: 2

</details>
