---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.10895v1"
published: "2026-09-09T22:56:21Z"
age_days: 2
score: 39
created: 2026-09-12
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# ReactHuman: A Physics-Grounded Benchmark for Human-Like Reactive Decision-Making in Embodied Multimodal LLMs

> [!summary] 先说人话（基于摘要）
> 机器人看懂危险，不代表来得及做对。ReactHuman让多模态模型在物理仿真中处理突发家庭事故，并实际执行其计划，检查反应是否合理、安全且符合物理。

## 这篇到底在做什么

- **卡在哪里**：任务是滑落、坠落等危险发生时的即时决策。现有视频问答只考察被动理解，导航和整理评测偏向长程规划，无法衡量物理理解能否转化为紧急动作。
- **关键解法**：模型充当模拟人形机器人的决策核心，在17类事件、逾1000个可精确复现场景中提交计划；240 Hz刚体仿真提供真值和执行后果。五项指标覆盖合理性、安全性与物理依据，并用外观和物性矛盾的物体测试判断来源。
- **拿什么证明**：评测七个MLLM，报告模型约每三次危险处理失误一次；存在固定反应倾向、过度相信外观，以及动作类型正确但拦截位置出现米级误差。摘要称这些失败未随模型规模增大而减轻。

## 值不值得读

- **和你的研究有什么关系**：对具身评测和世界模型研究者，价值在于把物理判断落实为有后果的动作测试，可区分危险识别、策略选择与空间执行问题。
- **先别急着信**：证据来自模拟危险场景；需要全文核查模型获得哪些观测、决策时间预算，以及计划执行接口如何影响误差。
- **判断**：值得精读评测协议与失败分类，适合检验模型物理理解是否真正支持安全行动。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-12/ReactHuman A Physics-Grounded Benchmark for Human-Like Reactive Decision-Making.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reacting to sudden physical hazards (catching a slipping plate, dodging a falling knife) is both a meaningful test of embodied intelligence and a hard requirement for deploying multimodal large language models (MLLMs) as the decision coreof household robots. Existing evaluations, however, probe intuitive physics passively through question answering over videos, or target deliberate, long-horizon tasks such as navigation and rearrangement; none measure whether a model can turn physical understanding into immediate, safety-critical action. We introduce ReactHuman, the first physics-grounded benchmark for human-like reactive decision-making, in which the evaluated MLLM acts as the brain of a simulated humanoid facing sudden household hazards; it spans 17 event families and over 1,000 bit-for-bit reproducible scenes with exact, annotation-free ground truth derived from 240 Hz rigid-body simulation, including adversarial objects whose appearance contradicts their physics (a foam anvil, a steel apple). We further design a five-metric suite that scores each reaction along three axes: reasonable, safe, and physically grounded. We physically execute every committed plan so that decisions have observable consequences. With this harness we evaluate seven representative MLLMs. Results show that reactive safety is far from solved: models mishandle roughly one hazard in three, act from fixed dispositions rather than the observed scene, trust appearance over motion, and miss interception points at meter scale even when the chosen action is correct; none of these failures shrink with model scale. ReactHuman thus offers both a fine-grained diagnosis and a scalable training signal toward physically grounded, safety-aware embodied agents. The benchmark can be found here: https://huggingface.co/datasets/Alan123/reacthuman-benchmark-scaled

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.10895v1
- Authors: Yizhan Li, Jianxin You, Mengyang Xiong, Yinhuan Chen, Zicheng Zhao, Dekun Wu, Dongqing Zhang, Bang Liu
- Published: 2026-09-09T22:56:21Z
- Age days: 2

</details>
