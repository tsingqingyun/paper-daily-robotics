---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-08-24
---

# 2026-08-24 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[Just Noticeable Difference Modeling for Token Compression in Vision-Language-Action Models](items/Just%20Noticeable%20Difference%20Modeling%20for%20Token%20Compression%20in%20Vision-Language-Act.md) — Experiments on the LIBERO benchmark with OpenVLA and OpenVLA-OFT demonstrate that Action-JND consistently improves compression reliability, especially under aggressive compression ratios.

- **规模**：2259 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 15、多模态基础模型 12、机器人学习 11、智能体 Agent 10、视觉语言动作模型 VLA 9、世界模型 8、Sim2Real 1
- **源异常**：0
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [Just Noticeable Difference Modeling for Token Compression in Vision-Language-Action Models](items/Just%20Noticeable%20Difference%20Modeling%20for%20Token%20Compression%20in%20Vision-Language-Act.md)

- **创新点 / 方法**：Building on this progression, we introduce Action-JND, which extends JND modeling to embodied perception by defining noticeability through the language-conditioned action response of a vision-language-action (VLA) policy in closed-loop control.
- **证据**：Experiments on the LIBERO benchmark with OpenVLA and OpenVLA-OFT demonstrate that Action-JND consistently improves compression reliability, especially under aggressive compression ratios.

### 2. [ForeTime-VLA: Causal Future-Token Distillation from a World Action Model for Conveyor-Belt Manipulation](items/ForeTime-VLA%20Causal%20Future-Token%20Distillation%20from%20a%20World%20Action%20Model%20for%20Conv.md)

- **创新点 / 方法**：We introduce ForeTime-VLA, a dense pi0.5 policy that distills a future-aware, action-equivalent representation from a frozen Fast-WAM-derived teacher while remaining causal at inference.
- **证据**：In quantitative real-robot evaluation, ForeTime-VLA achieves 81.1% stationary and 58.9% slow-moving grasp success, exceeding the next-best reference by 12.2 and 22.2 percentage points, respectively.

### 3. [Stream3Dv2: Geometric-Semantic Fusion Enhanced Streaming Zero-Shot 3D Scene Understanding](items/Stream3Dv2%20Geometric-Semantic%20Fusion%20Enhanced%20Streaming%20Zero-Shot%203D%20Scene%20Under.md)

- **创新点 / 方法**：To address these critical limitations, we propose Stream3Dv2, a novel training-free framework designed for robust streaming 3D perception.
- **证据**：Extensive experiments on public datasets demonstrate that Stream3Dv2 consistently outperforms existing baselines in foundational open-vocabulary streaming 3D segmentation and detection.

### 4. [PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration](items/PhysCaP%20Grounding%20Code-as-Policy%20Agent%20with%20Physics-Informed%20Exploration.md)

- **创新点 / 方法**：We present PhysCaP, a Physics-Informed Code-as-Policy agent for active perception in robotic manipulation.
- **证据**：The results show that existing passive and naive interactive baselines either fail when physical properties are hidden or over-explore, whereas PhysCaP achieves comparable performance with fewer interactions and reduced execution time.

### 5. [Is Multimodal Speculative Decoding Ready for Diffusion-Based Parallel Drafting? A Survey and Empirical Diagnosis](items/Is%20Multimodal%20Speculative%20Decoding%20Ready%20for%20Diffusion-Based%20Parallel%20Drafting%20A.md)

- **创新点 / 方法**：We introduce a unified taxonomy that isolates drafter-side parallelism from orthogonal design choices such as tree construction and verification strategies.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

## 扫读 7 篇

- [Humanoid Musical Robots as Experimental Interfaces for Music-Evoked Emotion](items/Humanoid%20Musical%20Robots%20as%20Experimental%20Interfaces%20for%20Music-Evoked%20Emotion.md) — We show that humanoid robots are well-suited as they enable parametric control of performance variables, reproducibility across trials, and the decoupling and recombination of auditory, visual, and interactive components.
- [A Collaborative Multi-Modality Interaction for VLA-based End-to-End Autonomous Driving](items/A%20Collaborative%20Multi-Modality%20Interaction%20for%20VLA-based%20End-to-End%20Autonomous%20D.md) — To this end, we propose a robust VLA-based end-to-end autonomous driving system that combines multi-modality interaction with multi-trajectory planning and optimization, enabling more reliable, interpretable, and safer driving decisions.
- [Logic-VLA: A Temporal Logic Conditioned Vision-Language-Action Model](items/Logic-VLA%20A%20Temporal%20Logic%20Conditioned%20Vision-Language-Action%20Model.md) — Across the evaluation benchmarks, Logic-VLA improves STL satisfaction rate over an STL-blind base policy by 24.8 to 40.7 percentage points (pp) while reducing nominal NL task success by at most 1.8 pp, showing that a single VLA can adapt its behavior to varyi…
- [Mining beyond Earth with Space Robots: Exploration, Sampling, and Extraction](items/Mining%20beyond%20Earth%20with%20Space%20Robots%20Exploration%2C%20Sampling%2C%20and%20Extraction.md) — Space resource acquisition and utilization, commonly referred to as Space Mining, represent critical pathways for enabling sustained human exploration and unlocking commercial opportunities in space.
- [ViTacPhys: Physical Property-Aware Grasping from Human Visual-Tactile Demonstrations](items/ViTacPhys%20Physical%20Property-Aware%20Grasping%20from%20Human%20Visual-Tactile%20Demonstrati.md) — On seen objects, it achieves 97.2% mass classification accuracy, 98.8% friction-coefficient classification accuracy, and a stiffness mean absolute percentage error (MAPE) of 5.51%.
- [VT-MUSE: Multimodal Unified Sequential Visuotactile Representation Learning for Manipulation](items/VT-MUSE%20Multimodal%20Unified%20Sequential%20Visuotactile%20Representation%20Learning%20for%20M.md) — On the simulation benchmark, VT-MUSE outperforms the strongest baseline evaluated on all tasks by 11 percentage points and also achieves substantial improvements in real-world experiments.
- [TaPeR: Probabilistic Recovery of Sparse Task Precedence Graphs from a Handful of Demonstrations](items/TaPeR%20Probabilistic%20Recovery%20of%20Sparse%20Task%20Precedence%20Graphs%20from%20a%20Handful%20of.md) — Finally, we demonstrate that the inferred graphs can be used to generate multiple valid robotic execution orders for the same task.

## 其余存档 12 篇

- [Rethinking Demonstration Unlearning in Imitation Learning for Robotics](items/Rethinking%20Demonstration%20Unlearning%20in%20Imitation%20Learning%20for%20Robotics.md) · [[世界模型]] [[机器人学习]]
- [Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning](items/Beyond%20Imitation%20Self-Improving%20Robot%20Policies%20via%20Off-Policy%20Q-Planning.md) · [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- [Belief Without Behavior: Measuring the Translation of Theory of Mind into Coordinated Social Action in Vision-Language Models](items/Belief%20Without%20Behavior%20Measuring%20the%20Translation%20of%20Theory%20of%20Mind%20into%20Coordin.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [Neural-Primitive: An Efficient End-to-end Local Planner with Primitive-based Imitation Learning for Autonomous Flight](items/Neural-Primitive%20An%20Efficient%20End-to-end%20Local%20Planner%20with%20Primitive-based%20Imit.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- [GhostTac: Manipulating Tactile Sensors without Physical Contact](items/GhostTac%20Manipulating%20Tactile%20Sensors%20without%20Physical%20Contact.md) · [[具身智能评测与基准]]
- [AudioWorldSim: Realistic Binaural Audio Datasets For World Models](items/AudioWorldSim%20Realistic%20Binaural%20Audio%20Datasets%20For%20World%20Models.md) · [[智能体 Agent]] [[世界模型]]
- [Koala Gripper: Co-designing Robotic Grippers and Data-Capture Devices for Scaling Dexterous Manipulation Learning](items/Koala%20Gripper%20Co-designing%20Robotic%20Grippers%20and%20Data-Capture%20Devices%20for%20Scaling.md) · [[智能体 Agent]] [[机器人学习]]
- [DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation](items/DECOWAM%20Decoupled%20Whole-Body%20World-Action%20Model%20for%20Legged%20Mobile%20Manipulation.md) · [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [CertVLA: Certified Defense against Physical Visual Attacks for Vision-Language-Action Models](items/CertVLA%20Certified%20Defense%20against%20Physical%20Visual%20Attacks%20for%20Vision-Language-Ac.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]]
- [SRL-MPC: Shape-Aware Reinforcement Learned Model Predictive Control](items/SRL-MPC%20Shape-Aware%20Reinforcement%20Learned%20Model%20Predictive%20Control.md) · [[机器人学习]] [[具身智能评测与基准]]
- [Teaching is a Process: The TOSS Framework for Modeling Human Teaching Decisions in Human-Interactive Robot Learning](items/Teaching%20is%20a%20Process%20The%20TOSS%20Framework%20for%20Modeling%20Human%20Teaching%20Decisions%20i.md) · [[机器人学习]]
- [Natural Sit-to-Stand Motion Synthesis For Humanoids via Guided Assistance Curricula and Staged Rewards](items/Natural%20Sit-to-Stand%20Motion%20Synthesis%20For%20Humanoids%20via%20Guided%20Assistance%20Curric.md) · [[机器人学习]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2259
- 入选条目：24
- 回填已见条目：0
- 最高分论文：Just Noticeable Difference Modeling for Token Compression in Vision-Language-Action Models
- 最高分论文发布时间：2026-08-21T15:59:37Z
- 主要技术对象分类：具身智能评测与基准 15、多模态基础模型 12、机器人学习 11、智能体 Agent 10、视觉语言动作模型 VLA 9、世界模型 8、Sim2Real 1
- 信息源错误：0
- 自动恢复信息源：0

</details>
