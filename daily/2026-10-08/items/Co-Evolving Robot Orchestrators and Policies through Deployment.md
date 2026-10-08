---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: body-excerpts
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2610.09228v1"
published: "2026-10-06T23:44:35Z"
age_days: 1
score: 38
created: 2026-10-08
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习"]
---

# Co-Evolving Robot Orchestrators and Policies through Deployment

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> Robo-COP 让机器人从自己的任务尝试中收集有效技能，择机训练新策略，验证后才替换旧策略。它还重审“这个技能别交给 VLA”之类旧记忆，让调度方式跟上能力变化。

## 问题

调度器能绕开冻结策略的弱点，却不能修好弱技能；单独更新策略，又会让旧调度经验过时。部署尝试常失败，只留整次成功会浪费有效片段，而直接上线新检查点可能退步。[S4](https://arxiv.org/html/2610.09228v1#S1.p2.1) [S5](https://arxiv.org/html/2610.09228v1#S1.p3.1)

### 用一个例子理解

理解用例（非论文实验）：输入“把积木放进盒子”；机器人抓起后掉落，系统保留完整抓取片段而拒收失败放置；积累相关数据后训练候选，验证通过才输出新的部署策略和修订后的调用建议。

## 创新点或方法

本文把部署、训练、验证接成循环。脚本和 VLA 动作统一记录，文字与视频判断器筛出技能片段，包括失败任务中的正确步骤。控制器决定等还是训练；训练用累计数据从预训练检查点做 LoRA 微调。执行期间先试候选并保留回退，检查目标技能、任务表现和旧技能，再决定采用并重审策略相关记忆。[S18](https://arxiv.org/html/2610.09228v1#S3.SS1.SSS0.Px2.p1.1) [S19](https://arxiv.org/html/2610.09228v1#S3.SS2.SSS0.Px1.p1.1) [S20](https://arxiv.org/html/2610.09228v1#S3.SS2.SSS0.Px1.p2.1) [S21](https://arxiv.org/html/2610.09228v1#S3.SS2.SSS0.Px2.p1.1) [S22](https://arxiv.org/html/2610.09228v1#S3.SS2.SSS0.Px2.p2.1) [S23](https://arxiv.org/html/2610.09228v1#S3.SS3.SSS0.Px1.p1.1) [S24](https://arxiv.org/html/2610.09228v1#S3.SS3.SSS0.Px1.p2.1) [S25](https://arxiv.org/html/2610.09228v1#S3.E1) [S26](https://arxiv.org/html/2610.09228v1#S3.SS3.SSS0.Px1.p2.2) [S27](https://arxiv.org/html/2610.09228v1#alg1) [S28](https://arxiv.org/html/2610.09228v1#S3.SS3.SSS0.Px1.p3.1) [S29](https://arxiv.org/html/2610.09228v1#S3.SS3.SSS0.Px2.p1.1)

### 方法如何工作

1. 完成实际任务并统一记录脚本与策略动作，为后续训练提供同一格式的数据。
2. 逐段判断技能结果，保留有效片段，避免整次失败掩盖正确步骤。
3. 结合重复失败与数据覆盖决定是否训练，使更新针对已有证据。
4. 让候选试做目标技能并保留回退，分开统计候选能力和最终任务结果。
5. 通过检查才采用候选，并重审旧记忆，使后续调用匹配实际能力。

### 必要术语

- 调度器：决定何时调用策略或脚本的上层程序；组织任务执行。
- 技能级验证：检查一个具体动作段是否完成；避免回退救场掩盖候选失败。
- LoRA：通过少量附加参数调整模型；用于训练候选策略。

## 证据

十个 RoboLab 仿真任务各100次部署学习、50个共享留出初始状态；平均留出成功率冻结调度器64.8%，Robo-COP 73.8%，固定周期且不验证65.8%。[摘要、S32、S43–S44] 真机三任务各50次学习、20次测试，均值38.3%→50.0%；增益集中在带盖容器任务35%→70%，另两任务持平。[S33](https://arxiv.org/html/2610.09228v1#S4.SS3.p1.1) [S39](https://arxiv.org/html/2610.09228v1#S4.T2.6) 说明完整流程在这些任务有效，并非每次训练都会改善。

## 局限

本文明确训练时暂停部署，候选调用不足也会被弃用。[S22](https://arxiv.org/html/2610.09228v1#S3.SS2.SSS0.Px2.p2.1) [S26](https://arxiv.org/html/2610.09228v1#S3.SS3.SSS0.Px1.p2.2) 验证只检查有足够观察的旧技能，不能保证所有能力不退化。我的待核查问题是判断器误收片段的频率和训练时间成本；总对比也不能单独归因于记忆修订。

- **判断**：值得细读数据筛选和候选验证规则，因为决定成败的是哪些经验能学、学完怎样确认可用。

## 研究关联

最可借鉴的是把新检查点当候选，并把“这个工具能做什么”的记忆与工具版本一起维护。否则能力更新了，调度器仍可能沿用绕开它的旧建议。

### 下一步读哪里

读[S20](https://arxiv.org/html/2610.09228v1#S3.SS2.SSS0.Px1.p2.1)核查片段接受标准，[S23](https://arxiv.org/html/2610.09228v1#S3.SS3.SSS0.Px1.p1.1) [S24](https://arxiv.org/html/2610.09228v1#S3.SS3.SSS0.Px1.p2.1) [S25](https://arxiv.org/html/2610.09228v1#S3.E1) [S26](https://arxiv.org/html/2610.09228v1#S3.SS3.SSS0.Px1.p2.2) [S27](https://arxiv.org/html/2610.09228v1#alg1) [S28](https://arxiv.org/html/2610.09228v1#S3.SS3.SSS0.Px1.p3.1)核查回退后如何给候选计分；下一步检查附录中的窗口、阈值和停止条件，以及记忆修订消融与部署成本。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习
- **筛选分数**：38
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.09228v1
- 获取时间：2026-10-08T01:54:40.194086+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2610.09228v1#p1.1)
- [S2] [Co-Evolving Robot Orchestrators and Policies through Deployment · 正文段落 2](https://arxiv.org/html/2610.09228v1#abstract1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.09228v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.09228v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.09228v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.09228v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.09228v1#S1.F1)
- [S8] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.09228v1#S1.I1.i1)
- [S9] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.09228v1#S1.I1.i2)
- [S10] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.09228v1#S1.I1.i3)
- [S11] [1 Introduction · 正文段落 12](https://arxiv.org/html/2610.09228v1#S1.I1.i4)
- [S12] [Agentic robot orchestration. · 正文段落 13](https://arxiv.org/html/2610.09228v1#S2.SS0.SSS0.Px1.p1.1)
- [S13] [Generating robot-policy data. · 正文段落 14](https://arxiv.org/html/2610.09228v1#S2.SS0.SSS0.Px2.p1.1)
- [S14] [Policy improvement during deployment. · 正文段落 15](https://arxiv.org/html/2610.09228v1#S2.SS0.SSS0.Px3.p1.1)
- [S15] [Policy improvement during deployment. · 正文段落 16](https://arxiv.org/html/2610.09228v1#S2.F2)
- [S16] [3 Method · 正文段落 17](https://arxiv.org/html/2610.09228v1#S3.p1.1)
- [S17] [Acting and reflecting. · 正文段落 18](https://arxiv.org/html/2610.09228v1#S3.SS1.SSS0.Px1.p1.1)
- [S18] [Action unification. · 正文段落 19](https://arxiv.org/html/2610.09228v1#S3.SS1.SSS0.Px2.p1.1)
- [S19] [From execution to labeled skills. · 正文段落 20](https://arxiv.org/html/2610.09228v1#S3.SS2.SSS0.Px1.p1.1)
- [S20] [From execution to labeled skills. · 正文段落 22](https://arxiv.org/html/2610.09228v1#S3.SS2.SSS0.Px1.p2.1)
- [S21] [Deciding when to train. · 正文段落 23](https://arxiv.org/html/2610.09228v1#S3.SS2.SSS0.Px2.p1.1)
- [S22] [Deciding when to train. · 正文段落 24](https://arxiv.org/html/2610.09228v1#S3.SS2.SSS0.Px2.p2.1)
- [S23] [Candidate policy verification. · 正文段落 25](https://arxiv.org/html/2610.09228v1#S3.SS3.SSS0.Px1.p1.1)
- [S24] [Candidate policy verification. · 正文段落 26](https://arxiv.org/html/2610.09228v1#S3.SS3.SSS0.Px1.p2.1)
- [S25] [Candidate policy verification. · 正文段落 27](https://arxiv.org/html/2610.09228v1#S3.E1)
- [S26] [Candidate policy verification. · 正文段落 28](https://arxiv.org/html/2610.09228v1#S3.SS3.SSS0.Px1.p2.2)
- [S27] [Candidate policy verification. · 正文段落 29](https://arxiv.org/html/2610.09228v1#alg1)
- [S28] [Candidate policy verification. · 正文段落 30](https://arxiv.org/html/2610.09228v1#S3.SS3.SSS0.Px1.p3.1)
- [S29] [Policy adoption and memory revision. · 正文段落 31](https://arxiv.org/html/2610.09228v1#S3.SS3.SSS0.Px2.p1.1)
- [S30] [4 Experiments · 正文段落 33](https://arxiv.org/html/2610.09228v1#S4.p1.1)
- [S31] [4.1 Experimental setup · 正文段落 34](https://arxiv.org/html/2610.09228v1#S4.F4)
- [S32] [4.2 Simulation results · 正文段落 38](https://arxiv.org/html/2610.09228v1#S4.F5)
- [S33] [4.3 Real-world experiments · 正文段落 49](https://arxiv.org/html/2610.09228v1#S4.SS3.p1.1)
- [S34] [4.3 Real-world experiments · 正文段落 50](https://arxiv.org/html/2610.09228v1#S4.F7.3.1)
- [S35] [4.3 Real-world experiments · 正文段落 51](https://arxiv.org/html/2610.09228v1#S4.F7.4.1)
- [S36] [4.3 Real-world experiments · 正文段落 52](https://arxiv.org/html/2610.09228v1#S4.F7.5.1)
- [S37] [4.3 Real-world experiments · 正文段落 53](https://arxiv.org/html/2610.09228v1#S4.F7)
- [S38] [4.3 Real-world experiments · 正文段落 54](https://arxiv.org/html/2610.09228v1#S4.T2)
- [S39] [4.3 Real-world experiments · 正文段落 55](https://arxiv.org/html/2610.09228v1#S4.T2.6)
- [S40] [Results. · 正文段落 56](https://arxiv.org/html/2610.09228v1#S4.SS3.SSS0.Px1.p1.1)
- [S41] [5 Conclusion · 正文段落 57](https://arxiv.org/html/2610.09228v1#S5.p1.1)
- [S42] [Appendix H Additional simulation results · 正文段落 105](https://arxiv.org/html/2610.09228v1#A8.p1.1)
- [S43] [Appendix H Additional simulation results · 正文段落 106](https://arxiv.org/html/2610.09228v1#A8.T5)
- [S44] [Appendix H Additional simulation results · 正文段落 108](https://arxiv.org/html/2610.09228v1#A8.T6)
- [S45] [Appendix I Real-world executions · 正文段落 121](https://arxiv.org/html/2610.09228v1#A9.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-08/Co-Evolving Robot Orchestrators and Policies through Deployment.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) policies trained on large datasets are capable within their training domains, yet they still fail to generalize to the variety of situations a robot meets in real-world deployment. Agentic robot systems complement the policy with a vision-language model (VLM) orchestrator that learns when to call the policy, how to instruct it, and when to use scripted skills instead. However, because the harness is built around a frozen policy that has limited language steerability, the orchestrator can avoid the policy's failures but never overcome them. The policy becomes the bottleneck of the whole system. Fine-tuning the policy can remove this bottleneck, but updating it alone decouples it from an orchestrator tuned to its old behavior. We propose Robo-COP, in which the orchestrator and policy co-evolve during deployment. Robo-COP curates skill demonstrations from its own executions, fine-tunes the policy when this data can address recurring failures, and adopts each new policy only after it improves the skills it was trained for. Across ten simulated RoboLab tasks, Robo-COP raises mean held-out success from 64.8% to 73.8% over the same harness with a frozen policy, while fine-tuning on a fixed schedule without verification reaches only 65.8%. On three real-world tasks, Robo-COP raises held-out success from 38.3% to 50.0%. Robo-COP turns deployment into a self-improving flywheel in which robots learn by doing, with each improvement in execution producing better data for the next round of learning. Videos and code are available at https://robo-cop.pages.dev/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.09228v1
- Authors: Xilun Zhang, Maggie Wang, Erik Bauer, Hong-Xing Yu, Huang Huang, Jiajun Wu, Marco Pavone
- Published: 2026-10-06T23:44:35Z
- Age days: 1

</details>
