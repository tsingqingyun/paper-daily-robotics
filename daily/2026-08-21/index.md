---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-08-21
---

# 2026-08-21 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[The Embodiment Gap in Robot Foundation Models](items/The%20Embodiment%20Gap%20in%20Robot%20Foundation%20Models.md) — We also propose a reporting framework for adaptation work that success rate alone does not reveal.

- **规模**：2258 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 18、多模态基础模型 13、世界模型 11、智能体 Agent 11、机器人学习 7、视觉语言动作模型 VLA 7、Sim2Real 1
- **源异常**：0
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [The Embodiment Gap in Robot Foundation Models](items/The%20Embodiment%20Gap%20in%20Robot%20Foundation%20Models.md)

- **创新点 / 方法**：Robot foundation models (RFMs), including vision-language-action (VLA) policies, are often discussed through a scaling view: more data, larger models, and broader benchmarks should improve generalization.
- **证据**：We also propose a reporting framework for adaptation work that success rate alone does not reveal.

### 2. [Revisiting the "Push-T" Robot Manipulation Task with Agentic Robotics](items/Revisiting%20the%20Push-T%20Robot%20Manipulation%20Task%20with%20Agentic%20Robotics.md)

- **创新点 / 方法**：The robot must use a single point of contact to push a T-shaped block into a target pose.
- **证据**：Results suggest that the agent found the 2D gym simulation online, and used sim experiments to learn push mechanics, iteratively optimizing to achieve 100% success rate using 46% fewer steps than the best diffusion policy trained with 200 human demonstrations.

### 3. [RoboEdit: Turning Human Manipulation Videos into Scalable Robot Experience](items/RoboEdit%20Turning%20Human%20Manipulation%20Videos%20into%20Scalable%20Robot%20Experience.md)

- **创新点 / 方法**：We present RoboEdit, a human-to-robot video editing suite that transforms human manipulation videos into action-consistent, physically plausible robot videos with aligned 3D hand states.
- **证据**：Experiments show that RoboEdit achieves state-of-the-art editing quality and supports downstream robot control policies in real-world manipulation tasks.

### 4. [Vision-Language Models for Egocentric Video: From Hand-Object Interaction to Embodied AI](items/Vision-Language%20Models%20for%20Egocentric%20Video%20From%20Hand-Object%20Interaction%20to%20Embo.md)

- **创新点 / 方法**：Egocentric video captures activities from the wearer's perspective, providing a direct view of human attention, hand--object interaction, and goal-directed behavior.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 5. [Human-Centric Intelligence in the Era of Foundation Models: A Survey](items/Human-Centric%20Intelligence%20in%20the%20Era%20of%20Foundation%20Models%20A%20Survey.md)

- **创新点 / 方法**：To bridge these divides and rethink human-centric intelligence in the foundation-model era, we introduce a full-spectrum human context taxonomy that integrates six interconnected levels by viewing humans as observable subjects through visual appearance and spatial geometry, as dynamic actors through kinematic dynamics…
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

## 扫读 7 篇

- [EATR-Stereo: Embodiment-Aware Token Routing of Paired Stereo Evidence for Humanoid Vision-Language-Action Control](items/EATR-Stereo%20Embodiment-Aware%20Token%20Routing%20of%20Paired%20Stereo%20Evidence%20for%20Humanoi.md) — EATR-Stereo achieves 60.0% full-task success, 100.0% grasp success, and 80.0% stage success.
- [LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories](items/LabDex%20A%20Hierarchical%20Benchmark%20for%20Dexterous%20Manipulation%20in%20Laboratories.md) — To bridge this gap, we introduce LabDex, a large-scale real-world dataset and benchmark for dexterous manipulation in chemistry laboratories, organized around a hierarchical task taxonomy spanning atomic skills, compositional tasks, and long-horizon experimen…
- [A Comprehensive Review of Large Language Models for Nanophotonics: From Surrogate Modeling to Autonomous Design](items/A%20Comprehensive%20Review%20of%20Large%20Language%20Models%20for%20Nanophotonics%20From%20Surrogate.md) — Metasurfaces have revolutionized the development of photonic devices by enabling unprecedented precision in light manipulation.
- [Beyond Placement and Articulation: Usage-Driven Code Scenes for Embodied Interaction](items/Beyond%20Placement%20and%20Articulation%20Usage-Driven%20Code%20Scenes%20for%20Embodied%20Interact.md) — To address this problem, we present RoomWright, an agentic usage-driven framework for generating 3D scenes represented entirely as code for embodied interaction.
- [Breaking the weakest link to evade vision language models](items/Breaking%20the%20weakest%20link%20to%20evade%20vision%20language%20models.md) — To efficiently generate adversarial examples, we propose a gradient-based attack method that performs optimization exclusively on the vision encoder of the VLM rather than on the entire multimodal architecture.
- [CL4D: Contrastive Language-4D Pretraining for Vision-Language Reasoning in Dynamic Scenes](items/CL4D%20Contrastive%20Language-4D%20Pretraining%20for%20Vision-Language%20Reasoning%20in%20Dynami.md) — Extensive experiments across multiple 4D human action benchmarks demonstrate that CL4D achieves state-of-the-art performance, with improvements of approximately ~16.75% over prior methods.
- [Orienteering Problem with Uncertain Time-Varying Rewards: Framework and Benchmark for Everyday Service Robotics](items/Orienteering%20Problem%20with%20Uncertain%20Time-Varying%20Rewards%20Framework%20and%20Benchmark.md) — We present the orienteering problem with uncertain time-varying rewards (OP-UTVR), a novel variant of the orienteering problem (OP).

## 其余存档 12 篇

- [GigaBrain-WBC-0.5: A Behavior World Model for Robust Whole-Body Control with Environment Interaction](items/GigaBrain-WBC-0.5%20A%20Behavior%20World%20Model%20for%20Robust%20Whole-Body%20Control%20with%20Envi.md) · [[世界模型]] [[具身智能评测与基准]]
- [OVIP-SG: Open-Vocabulary Instance-Preserving Scene Graphs for Mapping and Retrieval of Small, Fine-Grained Objects](items/OVIP-SG%20Open-Vocabulary%20Instance-Preserving%20Scene%20Graphs%20for%20Mapping%20and%20Retriev.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [GS-VLA: Plug-and-Play Viewpoint Canonicalization for Frozen VLA Policies via Gaussian Splatting](items/GS-VLA%20Plug-and-Play%20Viewpoint%20Canonicalization%20for%20Frozen%20VLA%20Policies%20via%20Gaus.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [SoftVTBench: A Deformation-Aware Visuo-Tactile Dataset and Benchmark for Deformable-Object Manipulation](items/SoftVTBench%20A%20Deformation-Aware%20Visuo-Tactile%20Dataset%20and%20Benchmark%20for%20Deformab.md) · [[多模态基础模型]] [[机器人学习]] [[具身智能评测与基准]]
- [Role-Conditioned Sub-Token Routing for Efficient Vision-Language-Action Policies](items/Role-Conditioned%20Sub-Token%20Routing%20for%20Efficient%20Vision-Language-Action%20Policies.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]]
- [Iterative Grasp Pose Refinement: A Deep Reinforcement Learning Approach for 2D Vision](items/Iterative%20Grasp%20Pose%20Refinement%20A%20Deep%20Reinforcement%20Learning%20Approach%20for%202D%20Vi.md) · [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- [Beyond the Transcript: Detecting Covert Co ordination in Latent Multi-Agent Communication](items/Beyond%20the%20Transcript%20Detecting%20Covert%20Co%20ordination%20in%20Latent%20Multi-Agent%20Commu.md) · [[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [Dream2Reward: Transition-Alignment Reward Models from Positive Demonstrations for Robotic Manipulation](items/Dream2Reward%20Transition-Alignment%20Reward%20Models%20from%20Positive%20Demonstrations%20for.md) · [[机器人学习]] [[具身智能评测与基准]]
- [Reinforced Planning with Latent World Models](items/Reinforced%20Planning%20with%20Latent%20World%20Models.md) · [[智能体 Agent]] [[世界模型]]
- [HarnessEval-W: Agentifying the Evaluation of Visual Worlds](items/HarnessEval-W%20Agentifying%20the%20Evaluation%20of%20Visual%20Worlds.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [Hydra-0: Action Flow for Generalist World Modeling and Control](items/Hydra-0%20Action%20Flow%20for%20Generalist%20World%20Modeling%20and%20Control.md) · [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- [Beyond Instrument Motion: Recognizing Tissue Tension Toward Surgical Skill Assessment](items/Beyond%20Instrument%20Motion%20Recognizing%20Tissue%20Tension%20Toward%20Surgical%20Skill%20Assess.md) · [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2258
- 入选条目：24
- 回填已见条目：0
- 最高分论文：The Embodiment Gap in Robot Foundation Models
- 最高分论文发布时间：2026-08-19T01:55:04Z
- 主要技术对象分类：具身智能评测与基准 18、多模态基础模型 13、世界模型 11、智能体 Agent 11、机器人学习 7、视觉语言动作模型 VLA 7、Sim2Real 1
- 信息源错误：0
- 自动恢复信息源：0

</details>
