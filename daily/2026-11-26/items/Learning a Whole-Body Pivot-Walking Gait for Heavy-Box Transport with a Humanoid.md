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
url: "https://arxiv.org/abs/2611.33828v1"
published: "2026-11-25T05:59:20Z"
age_days: 0
score: 34
created: 2026-11-26
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# Learning a Whole-Body Pivot-Walking Gait for Heavy-Box Transport with a Humanoid

> [!summary] 这篇论文到底做了什么（基于摘要）
> 这篇 Pivot-Walking 工作让人形机器人用交替转动的方式向前挪重箱。它用一个强化学习策略同时管脚步、平衡和推箱，训练时按箱子的实际进度推进动作阶段，上真机时改用周期时钟。

## 问题

箱子重到举不起来时，可以利用它与地面的支撑交替转动，一点点往前挪。机器人得在推箱时调整脚步和身体，否则箱子的位置或受力一变，下一步就可能接不上。摘要提到，过去的人形机器人研究多把操作箱子和迈步安排成不同阶段，每次转动后先让箱子停住。这能把动作分开规划，但留下了一个问题：同一个控制器能否在搬运过程中协调这三件事？

### 用一个例子理解

理解用例（非论文实验）｜面对一个抬不动的木箱，训练时让箱子已经挪出的位移决定何时切换转动阶段，策略同步调整脚步和身体。部署时改由时钟给出阶段，策略据此连续控制全身，输出一串交替转箱和跟步的动作。

## 创新点或方法

作者用同一个强化学习策略来学迈步、维持平衡和操作箱子，让这几种动作在训练里一起适应。奖励鼓励交替转动，阶段参考则随箱子的位移推进，让动作节奏跟着实际搬运进度走。为了上真机，作者又微调出一个不直接感知物体状态的版本，用周期时钟代替位移参考。摘要没有交代策略具体读取哪些其他信号，也没有说明时钟与箱子实际进度错开时如何恢复。

### 方法如何工作

1. 用箱子位移推进训练阶段，让下一阶段的参照取决于搬运实际走了多远。
2. 用鼓励交替转动的奖励训练同一策略，让推箱、迈步和平衡控制在同一交互过程中学会配合。
3. 将阶段信号换成周期时钟并微调，让策略适应部署时无法直接测量箱子状态的输入条件。
4. 在真机上按时钟运行全身策略，用前进距离和安全停机情况观察这种配合维持了多久。

### 必要术语

- Pivot walking：轮流利用物体与地面的支撑转动物体来挪动它；本文把这种转动和人形机器人的迈步一起控制。
- 阶段参考：告诉策略当前处于循环动作哪一段的信号；训练时随箱子位移推进，部署时由周期时钟给出。

## 证据

摘要报告，仿真中机器人能转动箱子。真机以向前搬运距离和试验终止情况体现表现：5 次都超过 1 米，5 次都因机器人基座倾斜触发安全停机。这支持在所测条件下，单一策略无需直接测量物体状态也能实现一段搬运。摘要没有给出逐次距离、箱重、地面条件或与分步规划的量化对照，因此无法据此判断它运得更快，或能稳定完成更长距离。

## 局限

安全停机是摘要明确报告的真机结果。值得核查的是停机前箱子位移、步态相位和基座倾角如何变化。仅凭摘要无法判断倾斜与时钟失步、接触变化还是其他因素有关，也无法把这几次短程搬运外推到不同箱子和地面。

- **判断**：值得细读训练用位移、部署用时钟的切换，以及真机停机前的表现，来判断这种节奏替换能可靠维持多久。

## 研究关联

训练时能取得的进度信号，可以先用来教机器人把几类动作配合起来，再尝试用部署端容易获得的信号维持节奏。这条路线适合有明显重复阶段的接触任务。决定是否借鉴时，要看每一阶段耗时有多稳定，因为时钟会照常走，物体遇到阻力却可能走慢。

### 下一步读哪里

先查箱子位移如何映射到阶段，以及奖励如何定义一次交替转动。再查微调时去掉了哪些观测、真机保留哪些输入。最后找逐次搬运记录，确认停机前是否出现阶段偏差，以及有没有位移参考与时钟版本的直接对照。

- **概念**：世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-26/Learning a Whole-Body Pivot-Walking Gait for Heavy-Box Transport with a Humanoid.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Through pivot walking, humans can transport objects that are too heavy to lift. Previous humanoid studies have relied on planned sequences in which object manipulation and stepping are executed separately and the object is brought to rest between successive rotations. However, few studies have developed a single learned controller for humanoid pivot walking. In this paper, we propose a single reinforcement-learning policy that jointly coordinates stepping, balance control, and object manipulation. The policy is trained using rewards that promote alternating pivot motions and a phase reference that progresses according to the displacement of the object. In simulation, we confirmed that the humanoid can pivot a box. For deployment, we fine-tuned the policy into an object-blind version that follows a periodic clock instead of the progress reference. On the real robot, the deployed policy transported the box forward by more than 1 m in all five trials; each trial ended at a base-tilt safety stop. These results demonstrate that coordinated humanoid pivot walking can be learned with reinforcement learning and transferred to a physical humanoid robot without direct object-state sensing.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.33828v1
- Authors: Rikuto Hidaka, Tsung-Yuan Chen, Kento Kawaharazuka
- Published: 2026-11-25T05:59:20Z
- Age days: 0

</details>
