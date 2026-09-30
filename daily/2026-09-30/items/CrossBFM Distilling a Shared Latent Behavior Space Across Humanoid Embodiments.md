---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.38087v1"
published: "2026-09-29T17:40:11Z"
age_days: 0
score: 35
created: 2026-09-30
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# CrossBFM: Distilling a Shared Latent Behavior Space Across Humanoid Embodiments

> [!summary] 这篇论文到底做了什么（基于摘要）
> CrossBFM 让不同人形机器人共用一套“动作词汇”：用同一个向量表达要模仿的动作或到达的姿态，再由控制器落实成各自的关节运动。它用动作重定向建立身体之间的对应关系，减少为每种机器人从头学习独立行为空间的成本。

## 问题

行为基础模型可用一个向量指定模仿动作、目标姿态或奖励目标，但摘要指出，Forward-Backward 表示为单个机器人训练就需数百 GPU 小时。换机器人重新训练，还会得到语义不对应的潜在空间，使行为表示难以共享。

### 用一个例子理解

理解用例（非论文实验）：给两个形态相近的人形输入同一个抬手侧移示范；统一编码器产生共享行为表示，各自跟踪器据此输出适配身体的关节控制；目标是表达同一行为，同时允许实际关节动作不同。

## 创新点或方法

旧做法按机器人分别建立空间；CrossBFM 把已有行为空间当作迁移对象。动作重定向提供逐帧跨身体对应关系，一个没有机器人专属参数的统一编码器据此蒸馏共享表示；随后以常规 PPO 训练潜变量条件跟踪器，把表示转成全身控制。训练包含编码器蒸馏和控制器学习，不能理解为只训练编码器即可部署。推理时由三类提示得到潜变量，再驱动策略；提示编码公式及不同机器人跟踪器如何共享参数未说明。

### 方法如何工作

1. 把动作重定向到不同身体，建立逐帧对应，使编码器有依据识别跨形态的同一行为。
2. 通过统一编码器蒸馏共享潜在空间，让多个训练形态使用一致的行为表示。
3. 用 PPO 训练潜变量条件跟踪器，将抽象行为转为可执行全身控制。
4. 将动作、目标姿态或奖励提示转换为潜变量并执行，检查共享表示是否保留三种使用方式。

### 必要术语

- 潜在行为空间：用紧凑向量组织不同动作意图的空间；本文要跨机器人共享它。
- 动作重定向：把同一动作转换到不同身体结构上；本文用它建立逐帧对应。
- 潜变量条件跟踪器：根据行为向量输出身体控制的策略；负责把共享表示落实为动作。

## 证据

摘要报告编码器蒸馏少于一 GPU 小时，跟踪器另需 10 GPU 小时。三个蒸馏人形上，潜变量条件跟踪相对关节条件版本仅损失 0.025 rad，姿态间到达平滑且无跌倒，并支持全部 41 个奖励提示。编码器只用四分之一动作库时跟踪性能损失 5%；未见过但形态相近的机器人最高恢复已见机器人的 89% 跟踪表现。还报告三种提示与 flow 生成潜变量的真机验证，但未给真机分项数字。

## 局限

作者明确将跨形态泛化结论限定于形态相近机器人。我会重点核查：未见机器人是否仍需单独训练跟踪器，蒸馏依赖的教师成本是否计入，以及 0.025 rad 对应哪种聚合误差。无跌倒只描述所测条件，不能推出任意姿态安全；仿真量化与真机验证须分开看。

- **判断**：手上有多种形态相近的人形机器人时值得读。论文的泛化证据限于相近形态，不能直接推到完全不同的身体结构。

## 研究关联

做跨机器人迁移时，可以把“要做什么动作”和“这副身体怎样完成”分开：优先共享前者，保留适应身体的控制部分。评估迁移效果时也要分清，共享编码器能处理新身体，是否仍需要为新身体另训控制器。

### 下一步读哪里

下一步核查教师空间来源、重定向对应如何构造、统一编码器怎样接收不同形态，以及 GPU 时间的硬件和统计口径；检查未见机器人控制器训练条件及真机任务覆盖。

- **概念**：多模态基础模型 具身智能评测与基准
- **筛选分数**：35
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/CrossBFM Distilling a Shared Latent Behavior Space Across Humanoid Embodiments.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Behavior Foundation Models (BFMs) give humanoids a promptable policy over a latent behavior space, enabling one single vector to represent a motion to imitate, a pose to reach, or a reward to maximize. Forward-Backward representations successfully produce such spaces, but at the cost of hundreds of GPU-hours for a single robot. Moreover, when the training process is repeated for a second robot, it produces a second space unrelated to the first, resulting in embodiment-specific latents that do not unify or transfer. We address these problems with CrossBFM, treating the latent space as the transferable asset for various embodiments. As retargeting provides frame-level cross-embodiment correspondence, we propose a unified encoder architecture with no robot-specific parameters for distilling the behavior space to address all training embodiments simultaneously in less than a GPU-hour. Following this encoder, latent-conditioned trackers turn the distilled latent into whole-body control in a conventional PPO training manner in just 10 more GPU-hours. On three distilled humanoids, all three prompting modes transfer: motion tracking with latent-conditioned policy losing only $0.025$ rad to its joint-conditioned counterpart, smooth goal reaching between poses with no falls, and reward optimization for all $41$ reward prompts. Our experiments further reveal that 1) regressing the encoder on a quarter of the motion corpus costs only $5\%$ of tracking performance and 2) training the encoder on a subset of robots and evaluating on an unseen one recovers up to $89\%$ of the tracking performance of seen robots, demonstrating cross-embodiment generalization to morphologically similar robots. We also verify the pipeline on real robots across all three prompting modes and with flow-based generated latents. Project website: https://dotandung.github.io/crossbfm/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.38087v1
- Authors: Tan-Dzung Do, Tuan Dat Phuong, Nico Bohlinger, Cuc T. Trinh, Siwei Ju, Vien Anh Ngo, Jan Peters, Xinchao Wang, An T. Le
- Published: 2026-09-29T17:40:11Z
- Age days: 0

</details>
