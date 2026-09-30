---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.37655v1"
published: "2026-09-29T14:17:49Z"
age_days: 0
score: 31
created: 2026-09-30
concepts: ["多模态基础模型", "智能体 Agent", "Sim2Real", "具身智能评测与基准"]
---

# Exemplar2VQA: A Scalable Exemplar-Driven Visual Question Answering Generation Framework via Multi-Agent Coding

> [!summary] 先说人话（基于摘要）
> Exemplar2VQA 从少量空间问答模板出发，让多个编码智能体在仿真中批量生成三维问答。几何答案交由确定性代码计算，降低语言模型直接编写答案时的空间计算错误。

## 问题

复杂三维空间问答数据不足，人工标注成本高；直接让 LLM 合成问答，又受限于其空间和几何计算能力。数据规模与答案可靠性难以兼顾。

## 创新点或方法

输入静态、以物体为中心的空间问题模板，多智能体调用几何工具库生成并执行代码，在模拟环境中扩展场景与问答。生成数据用于微调 MLLM，将空间数值推理从语言生成转交给可执行计算。

## 证据

仅使用生成的室内合成数据微调 Qwen2.5-VL 3B/7B，摘要报告在多类基准上提升，并迁移到室外和混合场景。摘要未给出可核查的结果数字。

## 局限

方法起点是静态物体空间查询，不能据此推断动态交互或接触推理能力；需核查答案验证流程与训练测试场景重合情况。

- **判断**：做空间问答数据者值得读工具库和模板扩展，机器人控制研究者可略读，避免把感知收益等同技能收益。

## 研究关联

对多模态空间智能与 Agent 数据构建，提供了程序化监督来源。对 Sim2Real 的证据是问答能力跨场景迁移，摘要未展示机器人动作迁移。

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Exemplar2VQA A Scalable Exemplar-Driven Visual Question Answering Generation Fra.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Advancing spatial intelligence in Multimodal Large Language Models (MLLMs) is bottlenecked by the scarcity of complex, scalable 3D question-answer (QA) data. While manual annotation is labor-intensive, directly utilizing LLMs to synthesize these QA pairs often fails due to their inherent deficiencies in spatial and geometric computation. We introduce Exemplar2VQA, a scalable exemplar-driven visual question answering generation framework that rapidly synthesizes large-scale spatial QA pairs in simulated environments via multi-agent coding. By equipping collaborative agents with a meticulously designed library of geometric utilities, Exemplar2VQA bypasses LLMs' spatial reasoning flaws through deterministic code execution. Crucially, the framework exhibits remarkable versatility: taking diverse static object-centric spatial query templates as exemplars, it seamlessly and autonomously scales them into massive, high-fidelity synthetic datasets. Fine-tuning Qwen2.5-VL (3B/7B) exclusively on Exemplar2VQA-generated synthetic indoor data yields significant performance improvements across various diverse benchmarks. Furthermore, its effectiveness is not limited to in-domain indoor datasets but also robustly extends to outdoor and mixed-scene benchmarks. These results establish Exemplar2VQA as a scalable and powerful paradigm for bridging the sim-to-real gap in Embodied AI. Our code is at https://github.com/yingjiayu12/Exemplar2VQA

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.37655v1
- Authors: Jiayu Ying, Qijian Tian, Ruijie Xu, Xinnan Zhu, Daoguo Dong, Jiachen Xu, Xin Tan
- Published: 2026-09-29T14:17:49Z
- Age days: 0

</details>
