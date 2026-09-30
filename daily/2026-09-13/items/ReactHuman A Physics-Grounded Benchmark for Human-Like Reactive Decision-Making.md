---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.10895"
published: "Sat, 12 Sep 2026 00:00:00 -0400"
age_days: 0
score: 39
created: 2026-09-13
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# ReactHuman: A Physics-Grounded Benchmark for Human-Like Reactive Decision-Making in Embodied Multimodal LLMs

> [!summary] 先说人话（基于摘要）
> ReactHuman测试模型遇到盘子滑落、刀具坠落时，能否及时做出合理且安全的反应。它把模型的行动计划放进物理仿真实际执行，用后果检验模型是否理解眼前的运动。

## 问题

任务是突发家庭危险下的即时决策。视频问答只测被动理解，导航和整理评测偏向长时规划，都不能直接检验模型能否把物理判断转成安全反应。

## 创新点或方法

模型充当仿真人形机器人的决策核心，根据场景提交计划；240 Hz刚体仿真执行计划并生成精确真值。基准以五项指标覆盖合理性、安全性和物理依据，并加入外观与物性相反的物体，区分视觉刻板印象与运动证据。

## 证据

覆盖17类事件、超过1,000个可逐比特复现的场景，评测7个MLLM。摘要报告模型约每三次危险就处理失当一次，正确选择动作后仍可能出现米级拦截误差，且这些失败未随模型规模增大而减少。


## 局限

证据来自仿真人形机器人；需全文核查模型输出如何转换成执行动作，以及反应时限如何定义，才能判断失败应归因于决策、空间定位还是执行接口。

- **判断**：值得精读评测协议和错误分类，适合用于审计反应式安全能力；不能据此直接推断真实机器人安全性。

## 研究关联

对具身评测和多模态模型研究者，它提供了比物理问答更接近行动后果的诊断。对世界模型研究者，外观与动力学冲突的场景尤其适合检验模型是否真正利用运动信息。

- **概念**：多模态基础模型 智能体 Agent 世界模型 具身智能评测与基准
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-13/ReactHuman A Physics-Grounded Benchmark for Human-Like Reactive Decision-Making.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2609.10895v1 Announce Type: cross Abstract: Reacting to sudden physical hazards (catching a slipping plate, dodging a falling knife) is both a meaningful test of embodied intelligence and a hard requirement for deploying multimodal large language models (MLLMs) as the decision coreof household robots. Existing evaluations, however, probe intuitive physics passively through question answering over videos, or target deliberate, long-horizon tasks such as navigation and rearrangement; none measure whether a model can turn physical understanding into immediate, safety-critical action. We introduce ReactHuman, the first physics-grounded benchmark for human-like reactive decision-making, in which the evaluated MLLM acts as the brain of a simulated humanoid facing sudden household hazards; it spans 17 event families and over 1,000 bit-for-bit reproducible scenes with exact, annotation-free ground truth derived from 240 Hz rigid-body simulation, including adversarial objects whose appearance contradicts their physics (a foam anvil, a steel apple). We further design a five-metric suite that scores each reaction along three axes: reasonable, safe, and physically grounded. We physically execute every committed plan so that decisions have observable consequences. With this harness we evaluate seven representative MLLMs. Results show that reactive safety is far from solved: models mishandle roughly one hazard in three, act from fixed dispositions rather than the observed scene, trust appearance over motion, and miss interception points at meter scale even when the chosen action is correct; none of these failures shrink with model scale. ReactHuman thus offers both a fine-grained diagnosis and a scalable training signal toward physically grounded, safety-aware embodied agents. The benchmark can be found here: https://huggingface.co/datasets/Alan123/reacthuman-benchmark-scaled

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.10895
- Authors: Yizhan Li, Jianxin You, Mengyang Xiong, Yinhuan Chen, Zicheng Zhao, Dekun Wu, Dongqing Zhang, Bang Liu
- Published: Sat, 12 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
