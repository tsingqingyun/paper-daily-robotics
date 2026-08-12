---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-06-10
---

# 2026-06-10 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models](items/MemoryVLA%2B%2B%20Temporal%20Modeling%20via%20Memory%20and%20Imagination%20in%20Vision-Language-Acti.md) — For example, on real robots, it achieves +9%, +26%, +28% gains on general, memory-dependent, and imagination-dependent tasks.

- **规模**：2063 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 22、多模态基础模型 21、视觉语言动作模型 VLA 16、智能体 Agent 13、世界模型 10、机器人学习 9、Sim2Real 1
- **源异常**：0
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models](items/MemoryVLA%2B%2B%20Temporal%20Modeling%20via%20Memory%20and%20Imagination%20in%20Vision-Language-Acti.md)

- **创新点 / 方法**：Inspired by these mechanisms, we propose MemoryVLA++, a full temporal modeling framework that equips VLA models with memory and imagination for robotic manipulation.
- **证据**：For example, on real robots, it achieves +9%, +26%, +28% gains on general, memory-dependent, and imagination-dependent tasks.

### 2. [ProbeAct: Probe-Guided Training-Free Failure Recovery in Vision-Language-Action Models](items/ProbeAct%20Probe-Guided%20Training-Free%20Failure%20Recovery%20in%20Vision-Language-Action%20M.md)

- **创新点 / 方法**：We propose PROBEACT, a training-free runtime intervention frame-6 work that detects and recovers from grasping and placement failures in pre-7 trained VLA policies without modifying their weights or requiring additional8 demonstrations.
- **证据**：Evaluated on the LIBERO-plus benchmark, our framework acts as18 a universal safety net, improving the success rate of the OpenVLA-OFT model19 from 69.6% to 74.1%, while demonstrating broad applicability to both base and20 fine-tuned VLA policies.

### 3. [iMaC: Translating Actions into Motion and Contact Images for Embodied World Models](items/iMaC%20Translating%20Actions%20into%20Motion%20and%20Contact%20Images%20for%20Embodied%20World%20Model.md)

- **创新点 / 方法**：To address these limitations, this paper proposesiMac (Image as Action Control), a novel unified control paradigm that treats raw visual images as native action representations for embodied world models.
- **证据**：The results demonstrate that iMac outperforms vector-based action control baselines in prediction accuracy, task success rate and cross-scene generalization ability.

### 4. [VeriSpace: Spatially Grounded Action Verification for Vision-Language-Action Models](items/VeriSpace%20Spatially%20Grounded%20Action%20Verification%20for%20Vision-Language-Action%20Mode.md)

- **创新点 / 方法**：We present VeriSpace, a 3D-aware action verifier for test-time action selection in VLA systems.
- **证据**：Experiments on public benchmarks and real- world robotic manipulation tasks show that VeriSpace consistently improves decision reliability over both underlying VLA policies and prior verification-based methods, yielding substantial gains in both in-distribution and out-of-distribution settings.

### 5. [What Matters in Orchestrating Robot Policies: A Systematic Study of Hierarchical VLA Agents](items/What%20Matters%20in%20Orchestrating%20Robot%20Policies%20A%20Systematic%20Study%20of%20Hierarchical.md)

- **创新点 / 方法**：In this paper, we present a systematic study of Hi-VLA design for robot manipulation.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

## 扫读 7 篇

- [MotionWAM: Towards Foundation World Action Models for Real-Time Humanoid Loco-Manipulation](items/MotionWAM%20Towards%20Foundation%20World%20Action%20Models%20for%20Real-Time%20Humanoid%20Loco-Man.md) — On nine real-world Unitree G1 tasks, MotionWAM runs in real time, substantially outperforms Vision- Language-Action (VLA) baselines fine-tuned on the same demonstrations by over 30% in overall success rate, and executes task-driven foot interaction that decou…
- [SARM2: Multi-Task Stage Aware Reward Modeling for Self Improving Robotic Manipulation](items/SARM2%20Multi-Task%20Stage%20Aware%20Reward%20Modeling%20for%20Self%20Improving%20Robotic%20Manipula.md) — On a 10-task benchmark, RM reduces value-estimation MSE by 80% over the strongest baselines; when used in SPIRAL, it improves task success from around 50% to near-perfect performance on Folding Shorts (58% to 100%) and Cleaning Whiteboard (50% to 90%), showin…
- [Your Model Already Knows: Attention-Guided Safety Filter for Vision-Language-Action Models](items/Your%20Model%20Already%20Knows%20Attention-Guided%20Safety%20Filter%20for%20Vision-Language-Acti.md) — On the dynamic variant, where the oracle's init-time target assignment becomes stale, our method substantially outperforms it by 43%, on average.
- [Harness Engineering for Physical AI: Robot Middleware Is the Harness Layer](items/Harness%20Engineering%20for%20Physical%20AI%20Robot%20Middleware%20Is%20the%20Harness%20Layer.md) — The robotics community has not yet adopted this framing, and we propose that robot middleware is that harness.
- [Dexterous Point Policy: Learning Point-based Dexterous Hand Policies from Human Demonstrations](items/Dexterous%20Point%20Policy%20Learning%20Point-based%20Dexterous%20Hand%20Policies%20from%20Human%20D.md) — To address this, we introduce Dexterous Point Policy, a framework that learns dexterous manipulation policies directly from human videos and requires no robot demonstrations.
- [Uncovering Vulnerability of Vision-Language-Action Models under Joint-Level Physical Faults](items/Uncovering%20Vulnerability%20of%20Vision-Language-Action%20Models%20under%20Joint-Level%20Phys.md) — We also show that performance drops cannot be attributed solely to physical infeasibility, since feasible faults such as increased joint friction can still substantially reduce success rates and induce closed-loop execution mismatch.
- [AllDayNav: Lifelong Navigation via Real-World Reinforcement Learning](items/AllDayNav%20Lifelong%20Navigation%20via%20Real-World%20Reinforcement%20Learning.md) — Experiments in both synthetic and real-world environments across cross-room, cross-episode, and cross-task scenarios show that AllDayNav achieves success rates approaching $100\%$ and consistently surpasses strong map-based, VLM, and RL baselines in path effi…

## 其余存档 12 篇

- [Act on What You See: Unlocking Safe Social Navigation in Vision-Language-Action Models](items/Act%20on%20What%20You%20See%20Unlocking%20Safe%20Social%20Navigation%20in%20Vision-Language-Action%20M.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [A Practical Recipe Towards Improving Sim-and-Real Correlation for VLA Evaluation](items/A%20Practical%20Recipe%20Towards%20Improving%20Sim-and-Real%20Correlation%20for%20VLA%20Evaluation.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [TORL-VLA: Tactile Guided Online Reinforcement Learning for Contact-Rich Manipulation](items/TORL-VLA%20Tactile%20Guided%20Online%20Reinforcement%20Learning%20for%20Contact-Rich%20Manipulat.md) · [[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- [Task Robustness via Re-Labelling Vision-Action Robot Data](items/Task%20Robustness%20via%20Re-Labelling%20Vision-Action%20Robot%20Data.md) · [[多模态基础模型]] [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- [CT-VAM: A Cerebello-Thalamic-Inspired Vision-Action Model for Efficient Visuomotor Control](items/CT-VAM%20A%20Cerebello-Thalamic-Inspired%20Vision-Action%20Model%20for%20Efficient%20Visuomoto.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [LIBERO-Occ: Evaluating and Improving Vision-Language-Action Models under Scene-Induced Occlusion via Viewpoint Imagination](items/LIBERO-Occ%20Evaluating%20and%20Improving%20Vision-Language-Action%20Models%20under%20Scene-In.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies](items/ReCoVLA%20VLM-Guided%20Reward%20Compilation%20for%20Failure%20Recovery%20in%20Vision-Language-Ac.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]] [[Sim2Real]]
- [Safe-RULE: Safe Reinforcement UnLEarning](items/Safe-RULE%20Safe%20Reinforcement%20UnLEarning.md) · [[机器人学习]] [[具身智能评测与基准]]
- [Beyond APIs: Probing the Limits of MLLMs in Physical Tool Use](items/Beyond%20APIs%20Probing%20the%20Limits%20of%20MLLMs%20in%20Physical%20Tool%20Use.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [Exploration of Foundation Model-Based Robots in Patient and Elderly Care](items/Exploration%20of%20Foundation%20Model-Based%20Robots%20in%20Patient%20and%20Elderly%20Care.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [IMPACT: Learning Internal-Model Predictive Control for Forceful Robotic Manipulation](items/IMPACT%20Learning%20Internal-Model%20Predictive%20Control%20for%20Forceful%20Robotic%20Manipulat.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [Rethinking Embodied Navigation via Relational Inductive Bias](items/Rethinking%20Embodied%20Navigation%20via%20Relational%20Inductive%20Bias.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2063
- 入选条目：24
- 回填已见条目：0
- 最高分论文：MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models
- 最高分论文发布时间：2026-06-08T17:59:53Z
- 主要技术对象分类：具身智能评测与基准 22、多模态基础模型 21、视觉语言动作模型 VLA 16、智能体 Agent 13、世界模型 10、机器人学习 9、Sim2Real 1
- 信息源错误：0

</details>
