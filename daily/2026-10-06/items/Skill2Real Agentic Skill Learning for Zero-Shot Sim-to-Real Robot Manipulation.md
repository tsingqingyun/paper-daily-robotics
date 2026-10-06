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
url: "https://arxiv.org/abs/2610.02788v1"
published: "2026-10-02T04:25:12Z"
age_days: 3
score: 33
created: 2026-10-06
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "Sim2Real", "具身智能评测与基准"]
---

# Skill2Real: Agentic Skill Learning for Zero-Shot Sim-to-Real Robot Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> Skill2Real 在仿真里积累经过验证的可执行技能，再把冻结技能库交给真机器人使用。它用共同 API 隔开任务知识与机器人底层差异，并让 PVG 分别负责提出程序、诊断结果和批准记忆更新。

## 问题

仿真到现实不仅有外观和动力学差异，还要迁移长任务的顺序与恢复办法。随机化可能把预算花在无关外观上；只生成代码又通常依赖已有动作原语，没有从试错中学到新的操作策略 [S3](https://arxiv.org/html/2610.02788v1#S1.p1.1) [S4](https://arxiv.org/html/2610.02788v1#S1.p2.1)。

### 用一个例子理解

理解用例（非论文实验）：输入“把抽屉里的杯子放到桌面”和 RGB-D 观测，Brain 调用局部取放技能，程序经共同 API 执行并检查返回结果；遇到抓取失败，按冻结恢复知识重新观察再尝试。

## 创新点或方法

本文把学习对象改成技能记忆和程序，而非迁移新训练的模型参数。Proposer 只读公开观测和 API 返回；Verifier 用仿真特权证据诊断，再转成公开信息可用的反馈；Governor 根据验证 rollout 决定是否收录更新。先学局部 Cerebellum 技能，再冻结它，学 Brain 的组合与恢复 [S6](https://arxiv.org/html/2610.02788v1#S1.p4.1) [S13](https://arxiv.org/html/2610.02788v1#S3.p1.1) [S14](https://arxiv.org/html/2610.02788v1#S3.F2)。部署读取真实观测和冻结记忆，不做任务微调；真实后端仍负责感知、标定和底层控制。

### 方法如何工作

1. 为仿真和真机定义语义相同的公开 API，使任务程序不绑定仿真隐藏状态。
2. Proposer 执行候选局部技能，Verifier 用特权证据找出失败原因并生成可部署反馈。
3. Governor 汇总验证结果，只把有证据的更新写入技能记忆。
4. 冻结局部库后学习长任务组合，再冻结两级记忆，通过真实后端执行与恢复。

### 必要术语

- 特权仿真证据：训练时能获得、部署时不可用的内部信息；本文只用来监督诊断。
- 共同 API：不同后端提供语义一致的操作接口；本文以它作为迁移边界。
- 技能记忆：可复用的程序知识、规则与限制；本文迁移它，而非新训练的模型参数。
- PVG：提出、验证诊断、批准入库三种职责；本文用它控制技能学习质量。

## 证据

Sol 在 LIBERO-90 学技能，Astra 测未训练的 Pro Long，成功率从无记忆 2.0% 经局部技能 35.3% 到完整层级 56.3% [S7](https://arxiv.org/html/2610.02788v1#S1.p5.1)；删除 Verifier 或 Governor 后为 39.0%、43.0% [S38](https://arxiv.org/html/2610.02788v1#S5.SS4.p2.1)。独立 Robosuite 七任务训练分别达 85.1%、89.4%，不能当作同一库的迁移成绩 [S7](https://arxiv.org/html/2610.02788v1#S1.p5.1)。真机 UR5e 四任务，每方法每任务 20 次，固定 Astra 和 API 后，平均完成率从 27.50% 到 78.75%，局部技能单独为 56.25% [S26](https://arxiv.org/html/2610.02788v1#S4.SS3.p1.1) [S27](https://arxiv.org/html/2610.02788v1#S4.SS4.p1.1) [S28](https://arxiv.org/html/2610.02788v1#S5.p1.1) [S29](https://arxiv.org/html/2610.02788v1#S5.F7) [S30](https://arxiv.org/html/2610.02788v1#S5.T1) [S31](https://arxiv.org/html/2610.02788v1#S5.T1.4) [S32](https://arxiv.org/html/2610.02788v1#S5.SS2.p1.1)，支持层级知识在该接口下有贡献。

## 局限

作者指出代码接口在狭窄空间缺少 VLA 那样紧密的反应控制，位置扰动落后于 Zetta [S35](https://arxiv.org/html/2610.02788v1#S5.SS3.p2.1)，并希望降低推理延迟 [S39](https://arxiv.org/html/2610.02788v1#S6.p3.1)。零样本指没有真实任务学习，仍依赖机器人专用后端。作者还明确技能文本不能隔离每条规则的因果贡献 [S40](https://arxiv.org/html/2610.02788v1#A5.SS7.SSS0.Px2.p1.1)；固定库对比的 55.3% [S34](https://arxiv.org/html/2610.02788v1#S5.SS3.p1.1) 与学习末期 56.3% 属不同设置。

- **判断**：值得读到 API 合同和技能入库证据：它展示了可迁移任务知识，但复现难点在后端能力与验证流程。

## 研究关联

值得借鉴的是监督信息可以比执行信息更丰富：仿真知道失败真因，但留下的修复规则必须能由部署时可见信息触发。同时把“建议修复”和“验证后入库”分开，避免一次偶然成功污染长期记忆。

### 下一步读哪里

先核查公开 API 到底提供哪些动作与感知能力 [S16](https://arxiv.org/html/2610.02788v1#S3.SS1.p2.1) [S17](https://arxiv.org/html/2610.02788v1#S3.SS1.p3.1) [S18](https://arxiv.org/html/2610.02788v1#S3.E1) [S19](https://arxiv.org/html/2610.02788v1#S3.SS1.p3.2) [S20](https://arxiv.org/html/2610.02788v1#S3.SS1.p4.1)，再追踪一次候选更新如何被诊断、验证和收录；按 [S40](https://arxiv.org/html/2610.02788v1#A5.SS7.SSS0.Px2.p1.1) 区分最终技能文本与完整学习证据，最后检查真实后端所需标定。

- **概念**：多模态基础模型 智能体 Agent 世界模型 Sim2Real 具身智能评测与基准
- **筛选分数**：33
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.02788v1
- 获取时间：2026-10-06T00:12:11.950475+00:00
- [S1] [Skill2Real: Agentic Skill Learning for Zero-Shot Sim-to-Real Robot Manipulation · 正文段落 1](https://arxiv.org/html/2610.02788v1#abstract1.1)
- [S2] [Skill2Real: Agentic Skill Learning for Zero-Shot Sim-to-Real Robot Manipulation · 正文段落 2](https://arxiv.org/html/2610.02788v1#S0.F1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.02788v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.02788v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.02788v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.02788v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.02788v1#S1.p5.1)
- [S8] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.02788v1#S1.I1.i1)
- [S9] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.02788v1#S1.I1.i3)
- [S10] [Sim-to-Real Robot Learning. · 正文段落 12](https://arxiv.org/html/2610.02788v1#S2.SS0.SSS0.Px1.p1.1)
- [S11] [Language Agents and Code Policies. · 正文段落 13](https://arxiv.org/html/2610.02788v1#S2.SS0.SSS0.Px2.p1.1)
- [S12] [Robot Skill Learning and Hierarchical Policies. · 正文段落 14](https://arxiv.org/html/2610.02788v1#S2.SS0.SSS0.Px3.p1.1)
- [S13] [3 Method · 正文段落 15](https://arxiv.org/html/2610.02788v1#S3.p1.1)
- [S14] [3 Method · 正文段落 16](https://arxiv.org/html/2610.02788v1#S3.F2)
- [S15] [3.1 Shared Code-Based Policy Interface · 正文段落 17](https://arxiv.org/html/2610.02788v1#S3.SS1.p1.1)
- [S16] [3.1 Shared Code-Based Policy Interface · 正文段落 18](https://arxiv.org/html/2610.02788v1#S3.SS1.p2.1)
- [S17] [3.1 Shared Code-Based Policy Interface · 正文段落 19](https://arxiv.org/html/2610.02788v1#S3.SS1.p3.1)
- [S18] [3.1 Shared Code-Based Policy Interface · 正文段落 20](https://arxiv.org/html/2610.02788v1#S3.E1)
- [S19] [3.1 Shared Code-Based Policy Interface · 正文段落 21](https://arxiv.org/html/2610.02788v1#S3.SS1.p3.2)
- [S20] [3.1 Shared Code-Based Policy Interface · 正文段落 22](https://arxiv.org/html/2610.02788v1#S3.SS1.p4.1)
- [S21] [3.1 Shared Code-Based Policy Interface · 正文段落 23](https://arxiv.org/html/2610.02788v1#S3.F4.2)
- [S22] [3.1 Shared Code-Based Policy Interface · 正文段落 24](https://arxiv.org/html/2610.02788v1#S3.F4.3)
- [S23] [3.4 Zero-Shot Sim-to-Real Deployment · 正文段落 35](https://arxiv.org/html/2610.02788v1#S3.SS4.p1.1)
- [S24] [4.1 Simulation Setup · 正文段落 36](https://arxiv.org/html/2610.02788v1#S4.F5)
- [S25] [4.1 Simulation Setup · 正文段落 37](https://arxiv.org/html/2610.02788v1#S4.SS1.p1.1)
- [S26] [4.3 Real-World Setup · 正文段落 40](https://arxiv.org/html/2610.02788v1#S4.SS3.p1.1)
- [S27] [4.4 Evaluation Setup · 正文段落 41](https://arxiv.org/html/2610.02788v1#S4.SS4.p1.1)
- [S28] [5 Results · 正文段落 42](https://arxiv.org/html/2610.02788v1#S5.p1.1)
- [S29] [5 Results · 正文段落 43](https://arxiv.org/html/2610.02788v1#S5.F7)
- [S30] [5.2 Zero-Shot Real-World Transfer · 正文段落 48](https://arxiv.org/html/2610.02788v1#S5.T1)
- [S31] [5.2 Zero-Shot Real-World Transfer · 正文段落 49](https://arxiv.org/html/2610.02788v1#S5.T1.4)
- [S32] [5.2 Zero-Shot Real-World Transfer · 正文段落 50](https://arxiv.org/html/2610.02788v1#S5.SS2.p1.1)
- [S33] [5.2 Zero-Shot Real-World Transfer · 正文段落 51](https://arxiv.org/html/2610.02788v1#S5.SS2.p2.1)
- [S34] [5.3 Zero-Shot Long-Horizon Generalization · 正文段落 52](https://arxiv.org/html/2610.02788v1#S5.SS3.p1.1)
- [S35] [5.3 Zero-Shot Long-Horizon Generalization · 正文段落 53](https://arxiv.org/html/2610.02788v1#S5.SS3.p2.1)
- [S36] [5.4 Verifier and Governor Ablations · 正文段落 54](https://arxiv.org/html/2610.02788v1#S5.F8)
- [S37] [5.4 Verifier and Governor Ablations · 正文段落 55](https://arxiv.org/html/2610.02788v1#S5.SS4.p1.1)
- [S38] [5.4 Verifier and Governor Ablations · 正文段落 56](https://arxiv.org/html/2610.02788v1#S5.SS4.p2.1)
- [S39] [6 Conclusion and Discussion · 正文段落 59](https://arxiv.org/html/2610.02788v1#S6.p3.1)
- [S40] [What the source records establish. · 正文段落 149](https://arxiv.org/html/2610.02788v1#A5.SS7.SSS0.Px2.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-06/Skill2Real Agentic Skill Learning for Zero-Shot Sim-to-Real Robot Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Transferring robotic skills from simulation to reality requires task knowledge that remains usable across differences in perception, dynamics, and embodiment. We introduce Skill2Real, an agentic policy framework that learns executable skills through a shared application programming interface (API). A Proposer-Verifier-Governor (PVG) loop uses privileged simulation evidence to diagnose outcomes and validate updates, while keeping learned skills grounded in public observations and API semantics. The Cerebellum first acquires local manipulation skills; the Brain then learns task-level composition with the Cerebellum frozen. Both memories transfer to the real robot without task-policy fine-tuning or skill-memory updates. As GPT-5.6 Sol learns skills on LIBERO-90, evaluating each frozen checkpoint with GPT-6 Astra raises LIBERO-Pro Long success from 2.0% to 56.3%, without training on Pro Long. Independent Robosuite training reaches 85.1% and 89.4% mean success with Sol and Opus 5 across seven tasks, respectively. Frozen Sol-trained LIBERO-90 skills achieve 78.75% mean completion across four real-world manipulation tasks with Astra. Removing the Verifier or Governor during LIBERO-90 training lowers final Pro Long success by 17.3 and 13.3 percentage points, respectively. These results support learning and transferring a hierarchy of executable skills through a common robot interface.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.02788v1
- Authors: Xincheng He, Siyu Ma, Chang Yu, Yunuo Chen, Yanjia Huang, Ying Nian Wu, Yin Yang, Chenfanfu Jiang
- Published: 2026-10-02T04:25:12Z
- Age days: 3

</details>
