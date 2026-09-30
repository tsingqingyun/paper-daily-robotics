---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.25376v1"
published: "2026-09-21T20:15:26Z"
age_days: 2
score: 32
created: 2026-09-24
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# VLAQuantBench: Closed-Loop Evaluation of Post-Training Quantization for Vision-Language-Action Models

> [!summary] 先说人话（基于摘要）
> VLAQuantBench 表明，VLA 量化效果取决于量化哪些层、使用什么数值格式以及如何校准，不能简单按层数或统一配方判断。它通过闭环任务执行寻找可行的精度配置。

## 问题

训练后量化可节省内存，但数值误差会影响动作并持续改变后续观测。层范围、格式和校准的交互，使单一敏感层经验难以直接指导不同 VLA 的部署。

## 创新点或方法

系统控制量化范围、格式与校准设置，结合闭环仿真、固定观测回放和任务聚类区间分析失败与恢复，并补充真实内核和实体机器人测量。

## 证据

包含 409 次运行、94,574 个仿真回合。未校准 W4A4 下，π₀.₅ 动作头量化范围从 126 层扩大至 167 层，成功率由 7.0% 升至 70.5%；两回合校准消除了所测子集中的严重联合失败。保护 OpenVLA-OFT 一个含 28,672 参数的输出投影可恢复接近基线的成功率。

## 局限

同一平滑与裁剪配方会降低 π₀ 表现，也无法端到端恢复 OpenVLA-OFT；摘要未量化真实内核与实体实验的速度、内存收益。

- **判断**：有压缩部署需求应优先精读配置与实验记录，其价值在可复查的具体方案，不能外推成通用量化规则。

## 研究关联

对 VLA 部署和评测研究者，这是用实际闭环行为选择压缩配置的直接证据，也说明量化配方需要按模型核验。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/VLAQuantBench Closed-Loop Evaluation of Post-Training Quantization for Vision-La.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Post-training quantization reduces the memory requirements of vision-language-action (VLA) models, but precision selection must account for the interaction between layer scope, numerical format, and calibration. We introduce \textbf{VLAQuantBench}, a controlled evaluation with 409 runs and 94,574 simulation episodes: four models on LIBERO, with X-VLA additionally evaluated on three simulation benchmark families. Under uncalibrated W4A4 round-to-nearest quantization, expanding a $π_{0.5}$ action-head subset from 126 to 167 layers raises success from 7.0\% to 70.5\%. Fixed-observation replay confirms a corresponding numerical recovery. Two-episode calibration removes the severe joint failures in the tested subsets, whereas the same smoothing-and-clipping recipe lowers $π_0$ success and does not recover OpenVLA-OFT end-to-end. For OpenVLA-OFT, protecting one 28,672-parameter output projection instead restores near-baseline success: the remaining 441 eligible linear layers retain W3 on LIBERO-Long or eight-bit activations across all four suites. Task-clustered intervals support the large failure and recovery contrasts. These results establish recipe-dependent interactions and identify concrete precision assignments, rather than universal layer-sensitivity rules. Real-kernel and physical-robot measurements complement the accuracy analysis. Code, configurations, and episode records are publicly available at https://github.com/jiuyixu25/VLAQuantBench.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.25376v1
- Authors: Jiuyi Xu, Qing Jin, Meida Chen, Song Wang, Yang Sui, Yangming Shi
- Published: 2026-09-21T20:15:26Z
- Age days: 2

</details>
