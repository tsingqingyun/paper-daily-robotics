---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.24350v1"
published: "2026-09-21T09:43:41Z"
age_days: 1
score: 41
created: 2026-09-23
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models

> [!summary] 先说人话（基于摘要）
> LIBERO-VPro专门测试机器人执行途中“看不清、看到旧画面、不同视角不一致”时还能否正确行动。它揭示了标准成功率可能掩盖的视觉依赖和适应缺陷。

## 问题

常规操作评测默认视觉输入清晰、及时且一致，难以区分策略究竟依赖实时交互证据，还是依赖熟悉场景中的空间先验。

## 创新点或方法

在闭环执行时扰动视觉证据，覆盖证据退化、相机陈旧、视觉来源一致性及任务相关场景变化，比较VLA与WAM的不同失效模式。

## 证据

包含12类挑战、96种设置、3,296个任务条件组合；评测3个VLA和3个WAM，约19.6万次仿真及200次Franka真实运行。物体严重遮挡未必导致失败，但局部交互线索破坏、旧观测和任务前提变化会显著削弱表现。

## 局限

摘要未给出各模型、各扰动的成功率数字；架构差异还需结合具体模型与训练条件解读。

- **判断**：值得精读评测协议和失败案例，适合直接用于检查机器人基础模型的闭环可靠性。

## 研究关联

为具身评测提供更细的诊断轴，帮助研究者区分视觉定位、观测时效和行为适应问题，而非仅报告一个总体成功率。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：41
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/LIBERO-VPro Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Mod.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robotic foundation models achieve impressive performance on standard manipulation benchmarks, yet these evaluations typically assume clean, timely, and consistent visual observations throughout execution. We introduce LIBERO-VPro, a benchmark for systematically evaluating the closed-loop visual robustness of robotic foundation models by perturbing the visual evidence available during execution. LIBERO-VPro covers four complementary dimensions, including Visual Evidence Degradation, Camera Staleness, Visual Source Consistency, and Task-Relevant Scene Variation, spanning 12 challenge categories, 96 experimental settings, and 3,296 task-condition cases. We evaluate three vision-language-action models and three world-action models over approximately 196,000 simulated episodes, complemented by 200 real-world rollouts on a Franka Research 3. Our results reveal that strong nominal performance can mask substantial weaknesses in visual grounding and adaptation. Models often remain successful despite severe object-level occlusion, yet degrade sharply when local interaction cues are disrupted or familiar spatial priors are violated. They are also highly sensitive to stale or missing observations and struggle when changed task preconditions require behavioral adaptation. Finally, VLAs and WAMs exhibit distinct robustness profiles, showing that visual robustness is multi-dimensional and architecture-dependent. LIBERO-VPro provides a systematic diagnostic framework for developing robotic foundation models that can more reliably ground and adapt their actions under challenging visual conditions.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.24350v1
- Authors: Huiqiong Li, Zhiting Mei, Anirudha Majumdar, Jingjing Chen, Yu-Gang Jiang, Bin Zhu
- Published: 2026-09-21T09:43:41Z
- Age days: 1

</details>
