---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-07-24
---

# 2026-07-24 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[ReferTrack: Referring Then Tracking for Embodied Visual Tracking](items/ReferTrack%20Referring%20Then%20Tracking%20for%20Embodied%20Visual%20Tracking.md) — On EVT-Bench, ReferTrack achieves state-of-the-art single-view performance with success rates of 89.4%, 73.3%, and 74.1% on the single-target, distracted, and ambiguity tracking splits, respectively -- matching or even surpassing several multi-camera baseline…

- **规模**：2141 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 17、多模态基础模型 14、智能体 Agent 13、世界模型 12、机器人学习 8、视觉语言动作模型 VLA 7、Sim2Real 1
- **源异常**：1
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [ReferTrack: Referring Then Tracking for Embodied Visual Tracking](items/ReferTrack%20Referring%20Then%20Tracking%20for%20Embodied%20Visual%20Tracking.md)

- **创新点 / 方法**：To address this, we introduce ReferTrack, a referring-then-tracking paradigm that grounds EVT using a single forward-facing camera.
- **证据**：On EVT-Bench, ReferTrack achieves state-of-the-art single-view performance with success rates of 89.4%, 73.3%, and 74.1% on the single-target, distracted, and ambiguity tracking splits, respectively -- matching or even surpassing several multi-camera baselines on identification-heavy tasks.

### 2. [Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents](items/Agentic%20Real2Sim%20Physics-based%20World%20Modeling%20with%20Vision-Language%20Agents.md)

- **创新点 / 方法**：We introduce \textit{Agentic Real2Sim}, a framework for generalized physical world modeling with vision-language agents, converting a real-world recording of object-robot interaction into a simulatable episodic twin which preserves observations, geometries, robot interactions, and object states.
- **证据**：The framework's agentic decisions can be driven by an open-weight VLM backend at a small fraction of the cost of frontier models, while attaining comparable conversion success rate.

### 3. [RoboInter1.5: A Holistic Intermediate Representation Suite for Embodied World Modeling and Robotic Manipulation](items/RoboInter1.5%20A%20Holistic%20Intermediate%20Representation%20Suite%20for%20Embodied%20World%20Mod.md)

- **创新点 / 方法**：Building on our prior work, RoboInter1.0, we present RoboInter1.5, an extended and holistic suite of intermediate representations for both robotic manipulation and embodied world modeling.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 4. [Closing the Lab-to-Store Gap: A Data-Efficient Post-Training and Experience-Driven Learning VLA Framework for Retail Humanoids](items/Closing%20the%20Lab-to-Store%20Gap%20A%20Data-Efficient%20Post-Training%20and%20Experience-Drive.md)

- **创新点 / 方法**：This paper presents DEED (Data-Efficient Post-Training and Experience-Driven Learning), a systems- level approach evaluated on a supermarket chip-restocking task using a Unitree G1-Edu humanoid robot and the GR00T N1.6 foundation model.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 5. [AXIS: A Growable Community-Driven Data Engine for Scalable Robot Manipulation](items/AXIS%20A%20Growable%20Community-Driven%20Data%20Engine%20for%20Scalable%20Robot%20Manipulation.md)

- **创新点 / 方法**：We present AXIS, a growable community-driven data engine and benchmark for scalable robot learning, which enables browser-based teleoperation for large-scale demonstration collection, automatically generates and validates new manipulation tasks, and transforms community- collected demonstrations into training-ready da…
- **证据**：Continual pretraining on AXIS substantially improves the overall success rate of $π_{0.5}$ by 5.8%, outperforms the model pretrained on RoboCasa365 by 37.3%, and exhibits consistent scaling with increasing data volume, with the largest gains observed under layout, sensor-noise, and camera perturbations.

## 扫读 7 篇

- [EA-Nav: Learning Safe Visual Navigation Policies with Embodiment Awareness](items/EA-Nav%20Learning%20Safe%20Visual%20Navigation%20Policies%20with%20Embodiment%20Awareness.md) — Experimental results show that the proposed method effectively improves navigation performance across different embodiment settings, demonstrating the effectiveness of incorporating embodiment geometry into embodied navigation.
- [KineBench: Benchmarking Embodied World Models via IDM-Free Kinematic Grounding](items/KineBench%20Benchmarking%20Embodied%20World%20Models%20via%20IDM-Free%20Kinematic%20Grounding.md) — To reduce this ambiguity, we present KineBench, an IDM-free closed-loop benchmark for EWMs, built upon an explicit kinematic grounding pipeline.
- [NavVerse: Benchmarking Indoor-to-Outdoor Embodied Navigation in Continuous Robot Simulation](items/NavVerse%20Benchmarking%20Indoor-to-Outdoor%20Embodied%20Navigation%20in%20Continuous%20Robot.md) — We introduce NavVerse, a physics-enabled benchmark for indoor-to-outdoor embodied navigation.
- [TransBiolab: A Real-World Multi-View Dataset of Cluttered Transparent Biomedical Objects](items/TransBiolab%20A%20Real-World%20Multi-View%20Dataset%20of%20Cluttered%20Transparent%20Biomedical.md) — To address this gap, we present TrainsBiolab, a real-world RGB-D dataset of cluttered transparent biomedical objects captured as calibrated multi-view sequences.
- [GS-Agent: Creating 4D Physical Worlds With Generative Simulation](items/GS-Agent%20Creating%204D%20Physical%20Worlds%20With%20Generative%20Simulation.md) — Experimental results show that GS-Agent effectively converts natural language into diverse and physically plausible 4D worlds exhibiting rich interactions among liquids, deformable objects, and rigid bodies, while achieving cinematic camera and lighting contr…
- [HyWorldVLA: A Vision-Language-Action Model with Hybrid World Modeling for Autonomous Driving](items/HyWorldVLA%20A%20Vision-Language-Action%20Model%20with%20Hybrid%20World%20Modeling%20for%20Autonom.md) — Extensive experiments on NAVSIM v1 and v2 benchmarks demonstrate that HyWorldVLA significantly outperforms both pixel-based and latent-based world model baselines.
- [ModPack: An Extensible Teleoperation Interface for Bimanual Mobile Manipulation](items/ModPack%20An%20Extensible%20Teleoperation%20Interface%20for%20Bimanual%20Mobile%20Manipulation.md) — We present ModPack, a modular and extensible teleoperation system designed to support diverse robot embodiments and task requirements within a unified framework.

## 其余存档 12 篇

- [Expert Behavior Prior Reinforcement Learning](items/Expert%20Behavior%20Prior%20Reinforcement%20Learning.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [Clinical Pathways as Safety Specifications for Physical AI in Hospital Wards](items/Clinical%20Pathways%20as%20Safety%20Specifications%20for%20Physical%20AI%20in%20Hospital%20Wards.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [LENS: LLM-guided Environment Simplification for Planning and Control in Clutter](items/LENS%20LLM-guided%20Environment%20Simplification%20for%20Planning%20and%20Control%20in%20Clutter.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]]
- [DocOps: A Verifiable Benchmark for Autonomous Agents in Complex Document Operations](items/DocOps%20A%20Verifiable%20Benchmark%20for%20Autonomous%20Agents%20in%20Complex%20Document%20Operatio.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [Masked Visual Actions for Unified World Modeling](items/Masked%20Visual%20Actions%20for%20Unified%20World%20Modeling.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [ExpertVerse: A General-Purpose Benchmark for Expert-Level Reasoning in Knowledge-Intensive Visual Synthesis](items/ExpertVerse%20A%20General-Purpose%20Benchmark%20for%20Expert-Level%20Reasoning%20in%20Knowledge-.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [Beyond Episodic Evaluation: Memory Architectural Bottlenecks in Sequential Embodied Question Answering](items/Beyond%20Episodic%20Evaluation%20Memory%20Architectural%20Bottlenecks%20in%20Sequential%20Embodi.md) · [[智能体 Agent]] [[具身智能评测与基准]]
- [TableVerse: A Large-scale Tabletop Dataset with Real-world Grounded Layouts for Generalizable Manipulation](items/TableVerse%20A%20Large-scale%20Tabletop%20Dataset%20with%20Real-world%20Grounded%20Layouts%20for%20G.md) · [[世界模型]] [[机器人学习]]
- [Scale Up Strategically: Learning Compositional Generalization via Bias-Aware Evaluation and Data Collection for Robotic Manipulation](items/Scale%20Up%20Strategically%20Learning%20Compositional%20Generalization%20via%20Bias-Aware%20Eval.md) · [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- [URF: A Unified Robot Control-Policy Framework for Stable Contact Aware Manipulation](items/URF%20A%20Unified%20Robot%20Control-Policy%20Framework%20for%20Stable%20Contact%20Aware%20Manipulati.md) · [[多模态基础模型]] [[机器人学习]] [[具身智能评测与基准]]
- [ODeform: Learning Continuous 4D Motion for Shape Deformation with Neural ODEs](items/ODeform%20Learning%20Continuous%204D%20Motion%20for%20Shape%20Deformation%20with%20Neural%20ODEs.md) · [[世界模型]]
- [Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning](items/Towards%20Miniature%20Humanoid%20Tele-Loco-Manipulation%20Using%20Virtual%20Reality%20and%20Rein.md) · [[机器人学习]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2141
- 入选条目：24
- 回填已见条目：0
- 最高分论文：ReferTrack: Referring Then Tracking for Embodied Visual Tracking
- 最高分论文发布时间：2026-07-22T12:05:13Z
- 主要技术对象分类：具身智能评测与基准 17、多模态基础模型 14、智能体 Agent 13、世界模型 12、机器人学习 8、视觉语言动作模型 VLA 7、Sim2Real 1
- 信息源错误：1

### 信息源错误

- MIT Technology Review AI: <urlopen error EOF occurred in violation of protocol (_ssl.c:1129)>

</details>
