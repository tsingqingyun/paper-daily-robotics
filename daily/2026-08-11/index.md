---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-08-11
---

# 2026-08-11 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation](items/SLIM-0.5B%20Learning%20Action-Grounded%20Predictive%20Latents%20for%20Robot%20Manipulation.md) — We propose SLIM (Self-supervised Latent Interaction Model), a compact 0.5B-parameter latent interaction policy.

- **规模**：2231 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 16、多模态基础模型 15、智能体 Agent 13、视觉语言动作模型 VLA 11、世界模型 10、机器人学习 8、Sim2Real 2
- **源异常**：0
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation](items/SLIM-0.5B%20Learning%20Action-Grounded%20Predictive%20Latents%20for%20Robot%20Manipulation.md)

- **创新点 / 方法**：We propose SLIM (Self-supervised Latent Interaction Model), a compact 0.5B-parameter latent interaction policy.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 2. [Skills in Weights, Memory in Code: Hybrid Learning for Memory-Dependent Robot Manipulation](items/Skills%20in%20Weights%2C%20Memory%20in%20Code%20Hybrid%20Learning%20for%20Memory-Dependent%20Robot%20Man.md)

- **创新点 / 方法**：To address this challenge, we propose HyMeS, a hybrid learning framework that leverages the reasoning and memory-management capabilities of coding agents to steer a Markovian VLA for memory-dependent manipulation.
- **证据**：On RoboMemArena, HyMeS improves mean cumulative success from 52.5% to 66.2% and mean task success from 41.3% to 60.1% over pi0.5, while outperforming PrediMem by 4.5 points in cumulative success and 14.5 points in task success.

### 3. [JEPA-WAM: Learning Vision-Language-Action Policies with Joint-Embedding World Modeling](items/JEPA-WAM%20Learning%20Vision-Language-Action%20Policies%20with%20Joint-Embedding%20World%20Mod.md)

- **创新点 / 方法**：We introduce JEPA-WAM, a latent WAM built in a pretrained V-JEPA space, which couples latent transition prediction with continuous action generation through a shared predictor.
- **证据**：On LIBERO-Plus, JEPA-WAM achieves 79.2%, the best result without large- scale robot-policy pretraining, while its pretrained $π_{0.5}$ instantiation reaches 86.3%, achieving the best overall performance.

### 4. [WorldSimProbe: Diagnosing Simulator Faithfulness in Action-Conditioned World Models for Embodied Manipulation](items/WorldSimProbe%20Diagnosing%20Simulator%20Faithfulness%20in%20Action-Conditioned%20World%20Mode.md)

- **创新点 / 方法**：To operationalize this contract, we introduce WorldSimProbe, comprising five controlled suites spanning local control sensitivity, global trajectory variation, source-diverse actions, interaction grounding, and dynamics.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 5. [Trajectory Divergence Horizon Decision for Reliable Dual-Arm Surgical Subtask Manipulation](items/Trajectory%20Divergence%20Horizon%20Decision%20for%20Reliable%20Dual-Arm%20Surgical%20Subtask%20Ma.md)

- **创新点 / 方法**：Surgical robotic systems are increasingly being adopted as clinical workload rises, motivating autonomous solutions for repetitive manipulation subtasks.
- **证据**：On real hardware with 20 trials per task setting, TDHD consistently improves performance over the latest VLA baselines: success increases from 55\% to 60\% for needle manipulation and from 55\% to 80\% for tissue manipulation, with the largest gains observed in the final manipulation stages.

## 扫读 7 篇

- [TrustRoboReward: Preference-Ordered Isotonic Score Editing for Multi-Paradigm Robot Reward Models](items/TrustRoboReward%20Preference-Ordered%20Isotonic%20Score%20Editing%20for%20Multi-Paradigm%20Rob.md) — Evaluated on our benchmark, Qwen3-VL-4B trained with POISE achieves an overall reward score of 77.96%, nearly matching GPT-5-mini (78.09%, gap 0.13%) and outperforming the strongest RoboReward-4B baseline by 10.13%.
- [RynnValue: Scaling Robotic Value Foundation Models with Temporal Distance](items/RynnValue%20Scaling%20Robotic%20Value%20Foundation%20Models%20with%20Temporal%20Distance.md) — We introduce RynnValue, an open-source value foundation model for robotic manipulation that replaces these anchors with temporal distance, the directed cost-to-go from an observation to the language-specified goal.
- [World Tokens: Enhancing Embodied Policies with Training-Time World Modeling](items/World%20Tokens%20Enhancing%20Embodied%20Policies%20with%20Training-Time%20World%20Modeling.md) — With a 2B backbone and no embodied action pretraining, World Tokens is highly competitive on LIBERO, attains the best reported averages on SIMPLER, substantially improves real-world R1 Pro success over a matched action-only baseline, and generates each action…
- [Efficient Real-World Online Reinforcement Learning for Robot Manipulation via Centralized Training and Critic Decomposition](items/Efficient%20Real-World%20Online%20Reinforcement%20Learning%20for%20Robot%20Manipulation%20via%20Ce.md) — Compared with a state-of-the-art baseline, our method improves the success rate from 60% to 80% on tennis ball pick-and-place, from 60% to 90% on banana pick-and-place, and from 25% to 95% on simulated block relocation, while also successfully accomplishing a…
- [RecoverFly: A Failure-Aware Reinforcement Learning Post-Training Framework for Aerial Vision-Language Navigation](items/RecoverFly%20A%20Failure-Aware%20Reinforcement%20Learning%20Post-Training%20Framework%20for%20Ae.md) — Moreover, compared to the AerialVLA initialization, RecoverFly improves success rate by 3.12 to 8.37 percentage points under a total rollout budget of about 30\% of the training-set size, validating its effectiveness, robustness, and generalization capabiliti…
- [VANE: Reliable Test-Time Training for Vision-Language-Action Models via Future Visual Representation Prediction](items/VANE%20Reliable%20Test-Time%20Training%20for%20Vision-Language-Action%20Models%20via%20Future%20Vi.md) — On SimplerEnv WidowX, VANE improves average success by $3.2$ percentage points over the corresponding TTT baseline.
- [FaLCon: Facet-Anchored Retrieval with Late Consensus for Sim2Real Text-Based Person Anomaly Search](items/FaLCon%20Facet-Anchored%20Retrieval%20with%20Late%20Consensus%20for%20Sim2Real%20Text-Based%20Pers.md) — Experiments on the PAB benchmark show that the proposed soft claim- aware retrieval achieves 86.44% mAP@10, substantially outperforming individual retrieval backbones.

## 其余存档 12 篇

- [SAIN: Structure-Aware Interactive Navigation with Active Dialogue Grounding for Mobile Robot](items/SAIN%20Structure-Aware%20Interactive%20Navigation%20with%20Active%20Dialogue%20Grounding%20for%20M.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [Multi-Submap Implicit Neural SLAM with Local-to-Global Loop Closure for Large-Scale Scene Reconstruction](items/Multi-Submap%20Implicit%20Neural%20SLAM%20with%20Local-to-Global%20Loop%20Closure%20for%20Large-Sc.md) · [[多模态基础模型]] [[世界模型]] [[具身智能评测与基准]]
- [Latent World Models with Monotone Planning Costs for Image-Goal Navigation](items/Latent%20World%20Models%20with%20Monotone%20Planning%20Costs%20for%20Image-Goal%20Navigation.md) · [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]]
- [Multi-modal Interactive Control of Robotic Arm based on Offline Large Language Models](items/Multi-modal%20Interactive%20Control%20of%20Robotic%20Arm%20based%20on%20Offline%20Large%20Language%20M.md) · [[多模态基础模型]] [[智能体 Agent]]
- [SpeedTuning: Speeding Up Policy Execution with Lightweight Reinforcement Learning](items/SpeedTuning%20Speeding%20Up%20Policy%20Execution%20with%20Lightweight%20Reinforcement%20Learning.md) · [[机器人学习]] [[具身智能评测与基准]]
- [OnEvoMemory: Evolving Memory through Online Robot Rollouts for Pretrained Robot Policies](items/OnEvoMemory%20Evolving%20Memory%20through%20Online%20Robot%20Rollouts%20for%20Pretrained%20Robot%20P.md) · [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- [Energy-Structured Latent World Models with Neural Time Fields for Physically Constistent Open-World Motion Planning](items/Energy-Structured%20Latent%20World%20Models%20with%20Neural%20Time%20Fields%20for%20Physically%20Con.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [Efficient Human-Contact Representation for Human-Scene Interaction](items/Efficient%20Human-Contact%20Representation%20for%20Human-Scene%20Interaction.md) · [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [WA-SpecDec: World-Aware Speculative Decoding for Vision-Language-Action Models](items/WA-SpecDec%20World-Aware%20Speculative%20Decoding%20for%20Vision-Language-Action%20Models.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]]
- [Spatiotemporal Context-dependent Personalized Movement Compensation in Delayed Telemanipulation](items/Spatiotemporal%20Context-dependent%20Personalized%20Movement%20Compensation%20in%20Delayed%20T.md) · [[世界模型]] [[具身智能评测与基准]]
- [Compiling and Benchmarking Task-State Horizons for Embodied Agents](items/Compiling%20and%20Benchmarking%20Task-State%20Horizons%20for%20Embodied%20Agents.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [EgoTrack3D: A Modular Framework for Egocentric 3D Object Tracking](items/EgoTrack3D%20A%20Modular%20Framework%20for%20Egocentric%203D%20Object%20Tracking.md) · [[世界模型]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2231
- 入选条目：24
- 回填已见条目：0
- 最高分论文：SLIM-0.5B: Learning Action-Grounded Predictive Latents for Robot Manipulation
- 最高分论文发布时间：2026-08-10T15:58:39Z
- 主要技术对象分类：具身智能评测与基准 16、多模态基础模型 15、智能体 Agent 13、视觉语言动作模型 VLA 11、世界模型 10、机器人学习 8、Sim2Real 2
- 信息源错误：0

</details>
