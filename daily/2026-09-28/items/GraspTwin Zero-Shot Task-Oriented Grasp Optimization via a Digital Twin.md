---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.30543v1"
published: "2026-09-24T20:50:26Z"
age_days: 3
score: 30
created: 2026-09-28
concepts: ["多模态基础模型", "世界模型", "Sim2Real", "具身智能评测与基准"]
---

# GraspTwin: Zero-Shot Task-Oriented Grasp Optimization via a Digital Twin

> [!summary] 先说人话（基于摘要）
> GraspTwin 先让基础模型提出符合任务用途的抓法，再在数字孪生里优化到物理上可执行。语义建议只是优化起点，最终抓取由仿真测试筛选。

## 问题

任务导向抓取既要抓得稳，又要方便后续操作。传统学习方法可能忽略用途，基础模型提出的位置则可能缺少精细物理依据，出现语义正确但实际抓不到的问题。

## 创新点或方法

从单帧 RGB-D 构建环境数字孪生，结合任务与物体可供性生成抓取建议。使用带 Thompson 采样的贝叶斯优化批量搜索附近位姿，在域随机化物理 rollout 中并行评估，再执行优化后的抓取。

## 证据

摘要报告完整零样本真机迁移耗时数分钟，任务导向抓取成功相对其他先进流水线最高改善 33%；未明确该数字是相对增幅还是百分点，也未给出任务数量和绝对成功率。

## 局限

需核查单次观测构建的孪生如何处理不可见几何与物理属性，以及数分钟预算和最高增益分别对应哪些条件。

- **判断**：值得读孪生构建和优化预算细节，适合允许执行前花时间验证抓取的任务。

## 研究关联

对 Sim2Real 与机器人基础模型研究者，展示了如何把语义先验接到可测量的物理验证上。数字孪生在这里承担候选抓取评估，而非仅用于生成训练数据。

- **概念**：[[多模态基础模型]] [[世界模型]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：30
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/GraspTwin Zero-Shot Task-Oriented Grasp Optimization via a Digital Twin.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

As robots transition from structured factory settings into homes, they are required to interact with an ever-increasing variety of objects. Many tasks require grasping, and often it is not sufficient to just pick up the target object. Consider a task like "pouring coffee" --- to facilitate the subsequent pouring, the robot should grasp the mug by its handle. Existing learning-based approaches for grasping either find robust and collision-free grasps that are largely agnostic to the task (e.g., picking up the mug by its rim), or leverage foundation models to propose task-appropriate grasp locations that lack fine-grained physical grounding (e.g., reaching for and missing the handle). In this work, we bridge these approaches with a real-to-sim-to-real framework. Based on a single RGB-D observation, we construct a digital twin of the environment, query a large foundation model to propose grasps that align with the object's affordances and task description, and then optimize the proposals to ensure robustness and plausibility before executing the result on the real robot. Our key insight is that the grasp proposals of the foundation model should be regarded as semantic priors that serve as seeds for local, gradient-free optimization. We leverage Bayesian optimization with Thompson sampling to draw batches of nearby poses, which are subsequently evaluated in parallel under domain-randomized physics rollouts. The resulting grasp is both task-oriented and physically feasible for execution by the robot arm. Our full zero-shot real-world transfer only takes a few minutes and improves task-oriented grasping success by up to 33% as compared to other state-of-the-art pipelines. Our code is available here: https://github.com/VT-Collab/GraspTwin/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.30543v1
- Authors: Daniel J. Evans, Yinlong Dai, Simon Stepputtis, Dylan P. Losey
- Published: 2026-09-24T20:50:26Z
- Age days: 3

</details>
