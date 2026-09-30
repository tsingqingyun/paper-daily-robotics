---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.37771v1"
published: "2026-09-29T15:12:55Z"
age_days: 0
score: 35
created: 2026-09-30
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Faster and Better? Benchmark Bugs and Design Limitations Distort the Evaluation of Vision-Language-Action Acceleration

> [!summary] 先说人话（基于摘要）
> 这篇论文检查了为什么近似原策略计算的 VLA 加速方法，有时反而拿到更高成功率。作者发现部分收益来自基准漏洞或过宽判定，修复后甚至会逆转方法排名。

## 问题

成功率本身不能区分操作能力提升与评测缺陷。任务实现错误、初始化与复现问题，以及忽视动作质量的成功标准，都可能让加速方法获得虚假的优势。

## 创新点或方法

从异常收益任务出发，将物体轨迹与成功判定接受区域对照，定位并分类漏洞，再扩展审计到七个基准。针对设计限制，收紧成功检查、修正不现实的物体质量，并加入偏好平滑动作的评分。

## 证据

在包括 RoboTwin、LIBERO-Plus、VLABench 的七个基准中发现 22 个漏洞和 4 项设计限制。修复漏洞使某任务的基线从末位升至首位；另一任务处理设计限制后，基线由落后加速方法 21 个百分点变为领先 5 个百分点。

## 局限

这些案例说明部分收益可能是评测伪影，不能据此否定所有加速收益；需核查各漏洞影响的版本、任务和修复后的完整排名。

- **判断**：本期优先精读，尤其适合正在报告 VLA 加速成功率的人；它可能改变实验设置和结论，而不仅是补充背景。

## 研究关联

对 VLA 加速与具身评测，这是直接影响结论可信度的工作。世界模型或策略学习若沿用这些任务判定，也应检查相同问题，但摘要未直接评估它们。

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Faster and Better Benchmark Bugs and Design Limitations Distort the Evaluation o.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Simulated manipulation benchmarks are the standard tool for evaluating vision-language-action (VLA) policies and the acceleration methods that reduce their inference latency for on-robot deployment. On these benchmarks, we observe that some training-free acceleration methods, which approximate the baseline policy's computation, achieve higher measured success rates than the baseline itself. Success rates alone cannot establish whether such gains come from better task execution or from evaluation flaws. We therefore investigate two kinds of benchmark flaws behind these gains: bugs, where the implementation does not match the intended task or evaluation protocol, and design limitations, where success criteria and simulation settings do not fully capture how acceleration affects task execution. Starting from tasks with anomalous gains, we localize root causes by plotting object trajectories against checker acceptance regions, and classify the resulting bugs into task consistency, initialization, and reproducibility. Extending this audit to seven benchmarks, including RoboTwin, LIBERO-Plus, and VLABench, we identify 22 bugs of these types and 4 design limitations. For the latter, we revise permissive success checkers, correct unrealistic object masses, and add a motion-aware score that favors smoother actions. Experiments show that bug fixes can reverse method rankings, moving the baseline from last to first on one task. Addressing design limitations can likewise remove anomalous gains: on another task, the baseline moves from 21 percentage points behind an accelerated method to 5 points ahead. Gains attributed to acceleration can therefore be artifacts of the benchmark rather than better task execution. We release our bug fixes and revised benchmark settings to support trustworthy evaluation of VLA acceleration.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37771v1
- Authors: Qiwei Chen, Kaijun Zhou, Nuohui Shi, Zhiyang Li, Yuxuan Feng, Jinyu Gu
- Published: 2026-09-29T15:12:55Z
- Age days: 0

</details>
