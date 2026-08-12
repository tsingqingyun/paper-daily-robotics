---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-07-03
---

# 2026-07-03 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今日最值得关注：[2026 BAIR Graduate Showcase](items/2026%20BAIR%20Graduate%20Showcase.md) — Looking for: Research scientist / Research Engineer Vongani Maluleke Email: vongani_maluleke@berkeley.edu Website: https://people.eecs.berkeley.edu/~vongani_maluleke/ Advisor(s): Jitendra Malik and Angjoo Kanazawa Research Blurb: Vongani Maluleke is a PhD can…

- **规模**：2112 个候选 → 24 篇入选；回填 0 篇
- **主题**：具身智能评测与基准 18、多模态基础模型 18、视觉语言动作模型 VLA 15、世界模型 12、机器人学习 9、智能体 Agent 6
- **源异常**：0
- **需要更高精度**：从“必读”选择论文，进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [2026 BAIR Graduate Showcase](items/2026%20BAIR%20Graduate%20Showcase.md)

- **创新点 / 方法**：I believe bridging the gap between these methods of scaling computation, presents a key open challenge in the field: how can we develop methods which turn the inferences drawn at test-time back into learned representations that the model can hold onto across interactions.
- **证据**：Looking for: Research scientist / Research Engineer Vongani Maluleke Email: vongani_maluleke@berkeley.edu Website: https://people.eecs.berkeley.edu/~vongani_maluleke/ Advisor(s): Jitendra Malik and Angjoo Kanazawa Research Blurb: Vongani Maluleke is a PhD candidate at UC Berkeley (BAIR, advised by Jitendra Malik and A…

### 2. [Neuro-Symbolic Safety Guidance for Vision-Language-Action Models via Constrained Flow Matching](items/Neuro-Symbolic%20Safety%20Guidance%20for%20Vision-Language-Action%20Models%20via%20Constrained.md)

- **创新点 / 方法**：In this paper, we propose a neuro-symbolic safety guidance mechanism for flow matching based VLAs that enables predictive collision avoidance.
- **证据**：On the SafeLIBERO benchmark, our method achieves 82.8% collision avoidance and 81.6% task success, a 6.3% and 19.8% improvement respectively over single- step methods, with the largest gains on long-horizon tasks where compounding distribution shift is most pronounced.

### 3. [Human-Centric Transferable Tactile Pre-Training for Dexterous Robotic Manipulation](items/Human-Centric%20Transferable%20Tactile%20Pre-Training%20for%20Dexterous%20Robotic%20Manipulati.md)

- **创新点 / 方法**：In this paper, we present H-Tac, a large- scale tactile-action dataset with 160-hour egocentric human videos containing more than 300 tasks and 135k episodes.
- **证据**：Extensive experiments in simulation and on real robots demonstrate that our model achieves superior performance, exhibiting robust generalization and fine-grained manipulation capabilities.

### 4. [WorldSample: Closed-loop Real-robot RL with World Modelling](items/WorldSample%20Closed-loop%20Real-robot%20RL%20with%20World%20Modelling.md)

- **创新点 / 方法**：To address this challenge, we propose WorldSample, a physically grounded data augmentation framework for real-robot RL that closes a real-synthetic loop between physical rollouts, world-model generation, and policy improvement.
- **证据**：Experiments on robot manipulation tasks involving contact-rich and precise tasks show that WorldSample improves policy success rate by 28% while reducing training steps by 59% compared with baselines.

### 5. [VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action Horizon](items/VLA-Corrector%20Lightweight%20Detect-and-Correct%20Inference%20for%20Adaptive%20Action%20Horiz.md)

- **创新点 / 方法**：To address this limitation, we propose VLA-Corrector, a lightweight corrective inference framework for action-chunked VLA policies.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。

## 扫读 7 篇

- [Learning to Move Before Learning to Do: Task-Agnostic pretraining for VLAs](items/Learning%20to%20Move%20Before%20Learning%20to%20Do%20Task-Agnostic%20pretraining%20for%20VLAs.md) — Building on this Decomposition Hypothesis, we propose Task-Agnostic Pretraining (TAP), a two-stage framework that first learns transferable motor priors from cheap, unlabeled interaction data -- including discarded off-task trajectories and autonomous robot p…
- [ABot-M0.5: Unified Mobility-and-Manipulation World Action Model](items/ABot-M0.5%20Unified%20Mobility-and-Manipulation%20World%20Action%20Model.md) — Experiments on challenging mobile and fine-grained manipulation benchmarks demonstrate that ABot-M0.5 achieves state-of-the-art performance in both long-horizon task success and finegrained control accuracy.
- [Bridge-WA: Predicting Where and How the World Changes for Robotic Action](items/Bridge-WA%20Predicting%20Where%20and%20How%20the%20World%20Changes%20for%20Robotic%20Action.md) — Across VLABench, RoboTwin2.0, LIBERO-Plus and real-robot evaluations, Bridge-WA improves task success, progress, and robustness, with particularly clear gains under out-of-distribution visual shifts.
- [Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots](items/Embodied.cpp%20A%20Portable%20Inference%20Runtime%20of%20Embodied%20AI%20Models%20on%20Heterogeneous.md) — The VLA deployments achieve successful closed-loop execution with 100.0% and 91.0% task success rates, respectively.
- [PhysMani: Physics-principled 3D World Model for Dynamic Object Manipulation](items/PhysMani%20Physics-principled%203D%20World%20Model%20for%20Dynamic%20Object%20Manipulation.md) — We introduce PhysMani-Bench, a dynamic manipulation benchmark with 16 tasks, and demonstrate a superior success rate over strong baselines in both simulation and real-world robot experiments.
- [VLAFlow: A Unified Training Framework for Vision-Language-Action Models via Co-training and Future Latent Alignment](items/VLAFlow%20A%20Unified%20Training%20Framework%20for%20Vision-Language-Action%20Models%20via%20Co-tr.md) — In contrast, language supervision helps preserve vision-language generalization, while future latent alignment improves state-transition and action- outcome modeling.
- [FurnitureVLA: Learning Long-Horizon Bimanual Furniture Assembly with Vision-Language-Action Model](items/FurnitureVLA%20Learning%20Long-Horizon%20Bimanual%20Furniture%20Assembly%20with%20Vision-Langu.md) — FurnitureVLA improves average simulation success from 48% to 80% compared to baselines across three furniture types, with an additional 21% gain from our design factor study.

## 其余存档 12 篇

- [Coachable agents for interactive gameplay](items/Coachable%20agents%20for%20interactive%20gameplay.md) · [[多模态基础模型]] [[智能体 Agent]] [[机器人学习]]
- [CoFL-S: Spatially Queryable Sector Flow Fields for Local Language-Conditioned Navigation](items/CoFL-S%20Spatially%20Queryable%20Sector%20Flow%20Fields%20for%20Local%20Language-Conditioned%20Nav.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [One Demonstration Is Enough for Real-World Robotic Reinforcement Learning](items/One%20Demonstration%20Is%20Enough%20for%20Real-World%20Robotic%20Reinforcement%20Learning.md) · [[机器人学习]] [[具身智能评测与基准]]
- [From Forgeries to Foundation Models: A Systematic Survey of Identity Document Attack and Detection](items/From%20Forgeries%20to%20Foundation%20Models%20A%20Systematic%20Survey%20of%20Identity%20Document%20Att.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [DeWorldSG: Depth-Aware 3D Semantic Scene Graph Generation via World-Model Priors](items/DeWorldSG%20Depth-Aware%203D%20Semantic%20Scene%20Graph%20Generation%20via%20World-Model%20Priors.md) · [[世界模型]]
- [Cross4D-JEPA: Dense Cross-modal Correspondence Distillation for 4D Point Cloud Representation Learning](items/Cross4D-JEPA%20Dense%20Cross-modal%20Correspondence%20Distillation%20for%204D%20Point%20Cloud%20Re.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [The Moving Eye: Enhancing VLA Spatial Generalization via Hybrid Dynamic Data Collection](items/The%20Moving%20Eye%20Enhancing%20VLA%20Spatial%20Generalization%20via%20Hybrid%20Dynamic%20Data%20Coll.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]]
- [Guided Action Flow: Q-Guided Inference for Flow-Matching Vision-Language-Action Policies](items/Guided%20Action%20Flow%20Q-Guided%20Inference%20for%20Flow-Matching%20Vision-Language-Action%20P.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]]
- [Domain Arithmetic: One-Shot VLA Adaptation under Environmental Shifts](items/Domain%20Arithmetic%20One-Shot%20VLA%20Adaptation%20under%20Environmental%20Shifts.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- [LIME: Learning Intent-aware Camera Motion from Egocentric Video](items/LIME%20Learning%20Intent-aware%20Camera%20Motion%20from%20Egocentric%20Video.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]]
- [From Technical Metrics to User Perception: A User Study of a Multimodal Human-Robot Interaction System for Object Detection and Grasping](items/From%20Technical%20Metrics%20to%20User%20Perception%20A%20User%20Study%20of%20a%20Multimodal%20Human-Rob.md) · [[多模态基础模型]] [[具身智能评测与基准]]
- [ComplexMimic: Human-Scene Interaction Imitation in Complex 3D Environments](items/ComplexMimic%20Human-Scene%20Interaction%20Imitation%20in%20Complex%203D%20Environments.md) · [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源错误</summary>

- 候选数量：2112
- 入选条目：24
- 回填已见条目：0
- 最高分论文：2026 BAIR Graduate Showcase
- 最高分论文发布时间：Wed, 01 Jul 2026 02:00:00 -0700
- 主要技术对象分类：具身智能评测与基准 18、多模态基础模型 18、视觉语言动作模型 VLA 15、世界模型 12、机器人学习 9、智能体 Agent 6
- 信息源错误：0

</details>
