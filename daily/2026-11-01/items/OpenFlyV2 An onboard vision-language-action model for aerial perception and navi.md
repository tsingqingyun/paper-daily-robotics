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
url: "https://arxiv.org/abs/2610.39287v1"
published: "2026-10-29T03:35:30Z"
age_days: 2
score: 33
created: 2026-11-01
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# OpenFlyV2: An onboard vision-language-action model for aerial perception and navigation

> [!summary] 这篇论文到底做了什么（基于摘要）
> OpenFlyV2把看懂语言和环境、空间判断及飞行路点生成放进同一个机载模型。它用共享视觉语言表示、小型动作专家和时序信息复用，在受限算力上持续输出飞行指引。

## 问题

任务是让无人机理解语言指令并持续根据视觉导航。摘要指出既有系统常只擅长单项能力、依赖机外计算，或无法在资源受限平台上维持闭环运行。瓶颈因此不只是理解指令，还包括让理解与动作生成在机载计算预算内反复运转。

### 用一个例子理解

理解用例（非论文实验）：输入是前视图像和“飞到红色门附近”。共享表示定位目标并理解空间关系，动作专家输出接下来的一组飞行路点；无人机移动后获取新图像，再生成下一组，逐步接近目标。

## 创新点或方法

相较能力分散或依赖机外计算的系统，OpenFlyV2让语义理解、语言定位、空间推理和控制共享视觉语言表示，再由紧凑动作专家生成短时域飞行路点。运动感知时序记忆与动作先验用于减少闭环计算开销，但摘要未说明缓存什么、如何更新或怎样减少计算。训练数据来自仿真，包括约7万条导航轨迹和6万组视觉语言问答；具体训练阶段及损失未说明。推理时在机上连续生成动作块，再以新观测更新导航。

### 方法如何工作

1. 用仿真导航轨迹与视觉语言数据学习任务所需能力；摘要未说明两类数据如何联合训练。
2. 将当前视觉和语言组织为共享表示，为理解目标与生成动作提供共同上下文。
3. 结合运动感知时序记忆和动作先验降低闭环计算成本；具体机制摘要只说明到此。
4. 由动作专家生成含12个路点的动作块，并在机载平台以10 Hz重复生成，用后续观测继续导航。

### 必要术语

- 共享视觉语言表示：让图像与指令形成多项能力共用的内部信息；本文据此连接理解和动作。
- 动作块：一次输出的一段动作目标；本文每块包含12个飞行路点。
- 闭环：根据新观测不断调整后续行动；本文需要在机载算力内持续完成这一循环。

## 证据

摘要报告在NVIDIA Jetson Orin NX上完全机载运行，以10 Hz生成动作块，每块含12个路点；这不等同于底层飞控频率。没有真实飞行训练数据，仿真训练后零样本迁移至四旋翼，在4个真实环境中的导航成功率为48%。这支持特定平台上联合理解与闭环飞行的可行性，但成功率也表明可靠性仍有限。摘要未列具体基线、成功判据、试验次数和各环境结果，无法判断相对优势或失败分布。

## 局限

48%是所报告真实环境的导航结果，不能外推为一般飞行安全能力。我的待核查问题包括碰撞如何计入失败、路点由什么底层控制器执行，以及记忆复用在快速转向时是否造成信息滞后。摘要称代码将公开，不能据此确认已经可用。

- **判断**：值得读机载推理和时序记忆的实现，尤其关注10 Hz怎样实现；真实成功率则要求继续检查失败案例后再判断部署范围。

## 研究关联

可借鉴的是共享感知表示，再用小型动作模块连接持续控制：理解能力和运行频率需要共同设计，而不是等模型训练完才考虑上机。若要复用这一做法，必须先确认目标平台的延迟与记忆更新预算。

### 下一步读哪里

核查10 Hz是否包含视觉编码、记忆更新与路点解码的全部耗时，12个路点覆盖多久，以及如何接入飞控；再看记忆与动作先验的消融、仿真数据构成和真实失败类型。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：33
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-01/OpenFlyV2 An onboard vision-language-action model for aerial perception and navi.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Human cognition flexibly draws on a shared perceptual foundation to understand environments, attend to referenced entities, reason about spatial relationships, and act. Endowing aerial robots with an analogous functional organization remains challenging, as existing systems are often specialized for individual capabilities, dependent on offboard computation, or unable to sustain closed-loop operation on resource-constrained platforms. We present OpenFlyV2, a unified onboard vision-language-action architecture that uses a shared vision-language representation to support semantic understanding, language-grounded perception, spatial reasoning, and continuous aerial control within a single model. A compact action expert converts the shared multimodal context into short-horizon flight waypoints, while motion-aware temporal memory and action priors reduce the computational cost of closed-loop execution. We construct \dataset{}, a simulation-based dataset comprising approximately 70,000 navigation trajectories and 60,000 vision-language instruction--response pairs. OpenFlyV2 generates action chunks, each comprising 12 waypoints, entirely onboard at 10 Hz using an NVIDIA Jetson Orin NX. It transfers zero-shot from simulation to physical quadrotor flight, achieving a 48\% navigation success rate across four real-world environments without real-world aerial training data. Extensive results demonstrate that broad vision-language competence and continuous closed-loop flight can coexist within a single model on a resource-constrained aerial platform. Code will be made publicly available at https://github.com/Ideal-ljl/AeroBrain.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.39287v1
- Authors: Junli Liu, Zhongrui You, Chenhui Li, Zhen Li, Yuyang Tian, Qizhen Chen, Delin Qu, Haoming Song, Dong Wang, Xuelong Li, Zhigang Wang, Bin Zhao
- Published: 2026-10-29T03:35:30Z
- Age days: 2

</details>
