---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-05-14
---

# 2026-05-14 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[RotVLA: Rotational Latent Action for Vision-Language-Action Model](items/RotVLA%20Rotational%20Latent%20Action%20for%20Vision-Language-Action%20Model.md) — With only 1.7B parameters and 1700+ hours of pretraining data, RotVLA achieves 98.2% on LIBERO and 89.6% / 88.5% on RoboTwin2.0 under clean and randomized settings, respectively.

- **规模**：2003 个候选 → 24 篇入选；回填 0 篇
- **主题**：多模态基础模型 17、视觉语言动作模型 VLA 17、具身智能评测与基准 16、智能体 Agent 13、世界模型 11、机器人学习 9
- **源异常**：0

## 必读 5 篇

### 1. [RotVLA: Rotational Latent Action for Vision-Language-Action Model](items/RotVLA%20Rotational%20Latent%20Action%20for%20Vision-Language-Action%20Model.md)

- **创新点 / 方法**：We introduce RotVLA, a VLA framework built on a continuous rotational latent action representation.
- **证据**：With only 1.7B parameters and 1700+ hours of pretraining data, RotVLA achieves 98.2% on LIBERO and 89.6% / 88.5% on RoboTwin2.0 under clean and randomized settings, respectively.

### 2. [D-VLA: A High-Concurrency Distributed Asynchronous Reinforcement Learning Framework for Vision-Language-Action Models](items/D-VLA%20A%20High-Concurrency%20Distributed%20Asynchronous%20Reinforcement%20Learning%20Framewo.md)

- **创新点 / 方法**：To address these challenges, we propose D-VLA, a high-concurrency, low- latency distributed RL framework for large-scale embodied foundation models.
- **证据**：Experiments on benchmarks like LIBERO show that D-VLA significantly outperforms mainstream RL frameworks in throughput and sampling efficiency for billion-parameter VLA models.

### 3. [World Action Models: The Next Frontier in Embodied AI](items/World%20Action%20Models%20The%20Next%20Frontier%20in%20Embodied%20AI.md)

- **创新点 / 方法**：Vision-Language-Action (VLA) models have achieved strong semantic generalization for embodied policy learning, yet they learn reactive observation-to-action mappings without explicitly modeling how the physical world evolves under intervention.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

### 4. [AttenA+: Rectifying Action Inequality in Robotic Foundation Models](items/AttenA%2B%20Rectifying%20Action%20Inequality%20in%20Robotic%20Foundation%20Models.md)

- **创新点 / 方法**：To rectify this, we introduce AttenA+, an architecture-agnostic framework that prioritizes kinematically critical segments via velocity-driven action attention.
- **证据**：Specifically, it improves OpenVLA-OFT to 98.6% (+1.5%) on the Libero benchmark and pushes FastWAM to 92.4% (+0.6%) on RoboTwin 2.0.

### 5. [Guide, Think, Act: Interactive Embodied Reasoning in Vision-Language-Action Models](items/Guide%2C%20Think%2C%20Act%20Interactive%20Embodied%20Reasoning%20in%20Vision-Language-Action%20Model.md)

- **创新点 / 方法**：In this paper, we propose GTA-VLA(Guide, Think, Act), an interactive Vision-Language- Action (VLA) framework that enables spatially steerable embodied reasoning by allowing users to guide robot policies with explicit visual cues.
- **证据**：On the in-domain SimplerEnv WidowX benchmark, our framework achieves a state- of-the-art 81.2% success rate.

## 扫读 7 篇

- [Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models](items/Towards%20Long-horizon%20Embodied%20Agents%20with%20Tool-Aligned%20Vision-Language-Action%20Mo.md) — Experiments show that VLAs-as-Tools improves the success rate of $π_{0.5}$ by 4.8 points on LIBERO-Long and 23.1 points on RoboTwin, and further enhances invocation fidelity by 15.0 points as measured by Non-biased Rate.
- [Embodied Multi-Agent Coordination by Aligning World Models Through Dialogue](items/Embodied%20Multi-Agent%20Coordination%20by%20Aligning%20World%20Models%20Through%20Dialogue.md) — To evaluate whether dialogue leads to genuine world- model alignment rather than superficial coordination, we propose a framework for measuring world-model alignment defined over per-agent world graphs: observation convergence (do private world models align o…
- [TMRL: Diffusion Timestep-Modulated Pretraining Enables Exploration for Efficient Policy Finetuning](items/TMRL%20Diffusion%20Timestep-Modulated%20Pretraining%20Enables%20Exploration%20for%20Efficient.md) — Integrating seamlessly with arbitrary policy inputs, e.g., states, 3D point clouds, or image-based VLA policies, we show that TMRL improves RL fine-tuning sample efficiency.
- [FrameSkip: Learning from Fewer but More Informative Frames in VLA Training](items/FrameSkip%20Learning%20from%20Fewer%20but%20More%20Informative%20Frames%20in%20VLA%20Training.md) — Across RoboCasa-GR1, SimplerEnv, and LIBERO, FrameSkip improves the success-retention trade-off over full-frame training and simpler frame selection variants, achieving a macro-average success rate of 76.15% across the three benchmarks compared with 66.50% fo…
- [BlockVLA: Accelerating Autoregressive VLA via Block Diffusion Finetuning](items/BlockVLA%20Accelerating%20Autoregressive%20VLA%20via%20Block%20Diffusion%20Finetuning.md) — Experimental results demonstrate that our BlockVLA achieves a 3.3$\times$ inference acceleration over standard discrete diffusion baselines.
- [What to Ignore, What to React: Visually Robust RL Fine-Tuning of VLA Models](items/What%20to%20Ignore%2C%20What%20to%20React%20Visually%20Robust%20RL%20Fine-Tuning%20of%20VLA%20Models.md) — Our method consistently improves over standard PPO, achieving average improvements of 16.62% on $π_{0.5}$ and 9.10% on OpenVLA.
- [SenseNova-U1: Unifying Multimodal Understanding and Generation with NEO-unify Architecture](items/SenseNova-U1%20Unifying%20Multimodal%20Understanding%20and%20Generation%20with%20NEO-unify%20Arc.md) — Beyond performance, we show detailed model design, data preprocessing, pre-/post-training, and inference strategies to support community research.

## 其余存档 12 篇

- [What Limits Vision-and-Language Navigation ?](items/What%20Limits%20Vision-and-Language%20Navigation.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]]
- [Reinforcing VLAs in Task-Agnostic World Models](items/Reinforcing%20VLAs%20in%20Task-Agnostic%20World%20Models.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- [TouchAnything: A Dataset and Framework for Bimanual Tactile Estimation from Egocentric Video](items/TouchAnything%20A%20Dataset%20and%20Framework%20for%20Bimanual%20Tactile%20Estimation%20from%20Egoce.md) · [[世界模型]] [[具身智能评测与基准]]
- [SafeManip: A Property-Driven Benchmark for Temporal Safety Evaluation in Robotic Manipulation](items/SafeManip%20A%20Property-Driven%20Benchmark%20for%20Temporal%20Safety%20Evaluation%20in%20Robotic.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [EgoEV-HandPose: Egocentric 3D Hand Pose Estimation and Gesture Recognition with Stereo Event Cameras](items/EgoEV-HandPose%20Egocentric%203D%20Hand%20Pose%20Estimation%20and%20Gesture%20Recognition%20with%20S.md) · [[具身智能评测与基准]]
- [Realtime-VLA FLASH: Speculative Inference Framework for Diffusion-based VLAs](items/Realtime-VLA%20FLASH%20Speculative%20Inference%20Framework%20for%20Diffusion-based%20VLAs.md) · [[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]]
- [Think Twice, Act Once: Verifier-Guided Action Selection For Embodied Agents](items/Think%20Twice%2C%20Act%20Once%20Verifier-Guided%20Action%20Selection%20For%20Embodied%20Agents.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [Premover: Fast Vision-Language-Action Control by Acting Before Instructions Are Complete](items/Premover%20Fast%20Vision-Language-Action%20Control%20by%20Acting%20Before%20Instructions%20Are%20C.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [Learning POMDP World Models from Observations with Language-Model Priors](items/Learning%20POMDP%20World%20Models%20from%20Observations%20with%20Language-Model%20Priors.md) · [[智能体 Agent]] [[世界模型]]
- [GuidedVLA: Specifying Task-Relevant Factors via Plug-and-Play Action Attention Specialization](items/GuidedVLA%20Specifying%20Task-Relevant%20Factors%20via%20Plug-and-Play%20Action%20Attention%20Sp.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- [From Imagined Futures to Executable Actions: Mixture of Latent Actions for Robot Manipulation](items/From%20Imagined%20Futures%20to%20Executable%20Actions%20Mixture%20of%20Latent%20Actions%20for%20Robot.md) · [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- [X-Imitator: Spatial-Aware Imitation Learning via Bidirectional Action-Pose Interaction](items/X-Imitator%20Spatial-Aware%20Imitation%20Learning%20via%20Bidirectional%20Action-Pose%20Intera.md) · [[机器人学习]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2003
- 入选条目：24
- 回填已见条目：0
- 最高分论文：RotVLA: Rotational Latent Action for Vision-Language-Action Model
- 最高分论文发布时间：2026-05-13T11:58:02Z
- 主要技术对象分类：多模态基础模型 17、视觉语言动作模型 VLA 17、具身智能评测与基准 16、智能体 Agent 13、世界模型 11、机器人学习 9
- 信息源错误：0

</details>
