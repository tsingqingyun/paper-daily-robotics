---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-09-30
---

# 2026-09-30 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今天优先看两类工作：一类检查 VLA 的收益是否经得起真实执行与评测协议检验，另一类把人类视频、交互历史和通用模型能力转成可复用的机器人技能。基准审计尤其值得先读：摘要报告修复后方法排名反转，因此加速、记忆和世界模型论文中的成功率，都应连同判定标准、延迟口径和迁移范围一起看。世界模型方向最有价值的问题也更具体了：生成结果能否忠实反映动作，以及这种忠实性能否带来策略收益。
> **趋势**：多篇工作把改进放在基础模型之外的接口上，包括成像、动作表示、记忆、执行调度和技能库，以减少重复训练或推理。另一个共同趋势是从视觉效果与单一成功率，转向动作一致性、物理可执行性、历史依赖和失败诊断。

- **规模**：2377 个候选 → 24 篇入选；回填 0 篇
- **主题**：多模态基础模型 21、具身智能评测与基准 20、视觉语言动作模型 VLA 13、智能体 Agent 12、世界模型 11、机器人学习 9、Sim2Real 4
- **源异常**：0
- **阅读方式**：先看 5 篇必读的“为什么值得读”，有用再进入 [[AI 论文深读工作流|L1 / L2 精读]]

## 必读 5 篇

### 1. [AeroManip-VLA: Scalable Vision-Language-Action Learning for Aerial Manipulation with RL-Generated Demonstrations](items/AeroManip-VLA%20Scalable%20Vision-Language-Action%20Learning%20for%20Aerial%20Manipulation%20w.md)

> AeroManip-VLA 为飞行机器人搭建可批量生成示范、测试 VLA 的仿真平台。它用强化学习技能配合专家任务规则自动完成导航和操作，并记录任务进度与安全失败。

- **为什么值得读**：对空中具身智能和 VLA 研究者，它提供了数据生成与受控评测的共同入口，尤其适合研究操作与移动强耦合时的失败。与世界模型的联系主要是潜在数据和测试环境，摘要没有报告世界模型方法。
- **证据**：摘要报告评测了多种模仿学习和 VLA 基线，覆盖不同任务设置并分析性能与失败模式；摘要未给出可核查的结果数字。
- **判断**：做空中操作或扩展 VLA 基准者值得细读平台与评测协议，其他读者重点看其事件标注和安全失败分类即可。

### 2. [Explore, Execute, Evolve: A Skill Acquisition and Reuse Loop for Embodied Agents](items/Explore%2C%20Execute%2C%20Evolve%20A%20Skill%20Acquisition%20and%20Reuse%20Loop%20for%20Embodied%20Agents.md)

> RoboSkill 让机器人把做过的任务变成下次能直接调用的技能，减少每次重新探索和推理的开销。关键是 Explore、Execute、Evolve 闭环，并用触觉和可复用代码提高执行效率。

- **为什么值得读**：对具身 Agent 研究者，价值在于把经验积累落实为可执行技能库，并同时衡量成功率与运行成本。它也提供了在 VLA 外层组织探索、触觉反馈和技能调用的思路。
- **证据**：在 LIBERO-10 的四种智能体上，首回合成功率提高 12.5–25.0 个百分点，平均运行时间减少 7.6–72.4%。真实机器人成功率提高 8.3 个百分点，成功试验的平均运行时间至少减少 14.4%。
- **判断**：值得细读技能生成、检索和更新规则，摘要同时给出跨智能体的成功率与耗时收益，具有明确复现价值。

### 3. [MotorMind: Scaffolding General Vision Language Models for Zero-Shot Robot Manipulation](items/MotorMind%20Scaffolding%20General%20Vision%20Language%20Models%20for%20Zero-Shot%20Robot%20Manipul.md)

> MotorMind 让通用 VLM 看观察、下中层动作指令，再根据执行反馈调整操作。它依靠确定性控制接口、异步监控和后台记忆更新，无需为任务专门训练策略。

- **为什么值得读**：对研究 VLM Agent 与 VLA 分工的人，提供了可检验的替代路线：通用模型负责中层决策，确定性控制负责落地。摘要还将剩余失败定位到视觉定位、具身推理和动作知识。
- **证据**：LIBERO-PRO 基础套件成功率为 66.7%，扰动下为 53.8%；所评测既有零样本方法分别最高为 13.3% 和 19.2%。真实 xArm6 在直接操作与人为扰动设置中平均成功率为 95%；更强 VLM 进一步提升表现。
- **判断**：值得精读动作接口与失败分析，它直接关系到通用 VLM 能承担多大比例的机器人控制工作。

### 4. [RawVLA: Embodied Neural Image Signal Processor For Robotic Manipulation](items/RawVLA%20Embodied%20Neural%20Image%20Signal%20Processor%20For%20Robotic%20Manipulation.md)

> RawVLA 把相机 RAW 数据到 RGB 图像的处理变成可学习环节，让输入图像适配冻结的 VLA。它针对会影响动作的成像因素调整渲染，改善恶劣成像条件下的操作表现。

- **为什么值得读**：对 VLA 部署与评测研究者，它指出视觉鲁棒性的一部分可能来自成像接口，提供了无需改动策略权重的干预位置，也提示基准应明确相机处理条件。
- **证据**：摘要报告 RawVLA 在 RawVLA-Bench 正常条件下保持性能，在退化成像下显著改善鲁棒性；摘要未给出可核查的结果数字。
- **判断**：值得读方法和成像因素实验，选题直接触及部署接口，但收益幅度需看全文数字再判断。

### 5. [Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation](items/Counterfactual%20Video%20Generation%20Enables%20Scalable%20Humanoid%20Loco-Manipulation.md)

> PRISM 用少量真人视频生成大量交互变体，再把这些不完美的视频转成物理合理的训练轨迹。最终人形机器人仅凭机载深度观察，就能对新物体实例执行拿起、搬运和放下。

- **为什么值得读**：对 Sim2Real 和人形机器人学习，价值在于连接生成式数据扩增、接触重建和真实控制，使少量视频有机会覆盖更多交互条件。
- **证据**：摘要报告生成数百段视频，并在无真实世界微调条件下完成实机部署。机器人使用机载深度观察，对箱子、桶、收纳容器和球的新实例、尺寸及初始配置执行拿取、搬运和放下；未给出成功率。
- **判断**：值得精读接触锚定与物理轨迹生成部分，这是从视频多样性走向可执行技能的关键环节。

## 扫读 7 篇

- [Urgent Actions Go First: Urgency-Aware Denoising for Real-Time VLA Control](items/Urgent%20Actions%20Go%20First%20Urgency-Aware%20Denoising%20for%20Real-Time%20VLA%20Control.md) — Urgency-Aware Denoising（UAD）让马上要执行的动作先完成去噪并交给机器人，后面的动作在后台继续细化。它利用动作按顺序执行的特点降低等待时间，再修复提前释放带来的误差与轨迹不一致。
- [EgoHumanoid-V2: Human-to-Humanoid Transfer of Coordinated Whole-Body Skills for Loco-Manipulation](items/EgoHumanoid-V2%20Human-to-Humanoid%20Transfer%20of%20Coordinated%20Whole-Body%20Skills%20for%20L.md) — EgoHumanoid-V2 把第一视角人类示范转成人形机器人的全身协同技能。它先修正运动学参考，再按动力学细化动作，同时处理人和机器人外观、视角的差异。
- [Real2Gym: Building Gyms from Videos, Bringing Skills to Robots](items/Real2Gym%20Building%20Gyms%20from%20Videos%2C%20Bringing%20Skills%20to%20Robots.md) — Real2Gym 把示范视频变成机器人能反复试错的交互式仿真环境，再把成功和失败整理成可复用技能。它通过代码执行、物理检查和共享控制接口，将仿真经验带到真实机器人，且不更新底层模型权重。
- [Remember What You Did: Action-History Memory with Dual-Expert Denoising for Long-Horizon Vision-Language-Action Policies](items/Remember%20What%20You%20Did%20Action-History%20Memory%20with%20Dual-Expert%20Denoising%20for%20Long-.md) — ActMem-VLA 让机器人记住自己执行过哪些动作，避免相似画面下分不清任务阶段。记忆专家先在去噪早期引导任务进度，冻结的原策略随后细化动作。
- [CrossBFM: Distilling a Shared Latent Behavior Space Across Humanoid Embodiments](items/CrossBFM%20Distilling%20a%20Shared%20Latent%20Behavior%20Space%20Across%20Humanoid%20Embodiments.md) — CrossBFM 尝试让不同人形机器人共享同一个行为潜空间，使相同潜向量能跨机器人表达运动、目标姿态或奖励偏好。它先蒸馏共享编码器，再训练各自的潜变量条件控制器。
- [Faster and Better? Benchmark Bugs and Design Limitations Distort the Evaluation of Vision-Language-Action Acceleration](items/Faster%20and%20Better%20Benchmark%20Bugs%20and%20Design%20Limitations%20Distort%20the%20Evaluation%20o.md) — 这篇论文检查了为什么近似原策略计算的 VLA 加速方法，有时反而拿到更高成功率。作者发现部分收益来自基准漏洞或过宽判定，修复后甚至会逆转方法排名。
- [When to Adapt: Multi-Signal Domain Shift Detection for Efficient Training-Free Adaptation in Open-Vocabulary Segmentation](items/When%20to%20Adapt%20Multi-Signal%20Domain%20Shift%20Detection%20for%20Efficient%20Training-Free%20Ad.md) — 这项方法让开放词汇分割系统在环境确实变化时才启动适配，减少逐帧调整的成本。它联合监测画面变化、适配器失配和语义漂移，判断何时需要更新。

## 其余存档 12 篇

- [VLALight: A Vision-Language-Action Model for Traffic Signal Control](items/VLALight%20A%20Vision-Language-Action%20Model%20for%20Traffic%20Signal%20Control.md) · [[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[机器人学习]]
- [DROM: A Language-Guided Diffusion Framework for Multi-Skill Robotic Manipulation](items/DROM%20A%20Language-Guided%20Diffusion%20Framework%20for%20Multi-Skill%20Robotic%20Manipulation.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]]
- [RoXDrive: Closed-Loop Reinforcement Learning for End-to-End Autonomous Driving via Action-Faithful Rollouts](items/RoXDrive%20Closed-Loop%20Reinforcement%20Learning%20for%20End-to-End%20Autonomous%20Driving%20vi.md) · [[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[Sim2Real]] [[具身智能评测与基准]]
- [UniAfford: Token-Routed Multitask Learning for Generalizable 2D-3D Affordance Perception](items/UniAfford%20Token-Routed%20Multitask%20Learning%20for%20Generalizable%202D-3D%20Affordance%20Per.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [Disentangling Spurious Correlations in Vision-Language-Action Models via Predicting Domain-Invariant Latent Lookahead](items/Disentangling%20Spurious%20Correlations%20in%20Vision-Language-Action%20Models%20via%20Predict.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [Beyond Token Importance: Preserving Spatial Scaffolds for Efficient Vision-Language-Action Inference](items/Beyond%20Token%20Importance%20Preserving%20Spatial%20Scaffolds%20for%20Efficient%20Vision-Langua.md) · [[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- [Exemplar2VQA: A Scalable Exemplar-Driven Visual Question Answering Generation Framework via Multi-Agent Coding](items/Exemplar2VQA%20A%20Scalable%20Exemplar-Driven%20Visual%20Question%20Answering%20Generation%20Fra.md) · [[多模态基础模型]] [[智能体 Agent]] [[Sim2Real]] [[具身智能评测与基准]]
- [Video2STL: Grounding VLM-Generated Temporal Specifications for Robot Learning](items/Video2STL%20Grounding%20VLM-Generated%20Temporal%20Specifications%20for%20Robot%20Learning.md) · [[多模态基础模型]] [[智能体 Agent]] [[机器人学习]] [[具身智能评测与基准]]
- [Taming VLAs under Robot Execution Errors: Self-Compensation and Stress Testing](items/Taming%20VLAs%20under%20Robot%20Execution%20Errors%20Self-Compensation%20and%20Stress%20Testing.md) · [[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- [MultiTalk: Scaling Full-Duplex Speech Models to Long, Multi-Party, Bilingual Conversation](items/MultiTalk%20Scaling%20Full-Duplex%20Speech%20Models%20to%20Long%2C%20Multi-Party%2C%20Bilingual%20Conv.md) · [[多模态基础模型]] [[智能体 Agent]] [[具身智能评测与基准]]
- [LongLive-Plug: Once-for-All Distillation for Video Generation](items/LongLive-Plug%20Once-for-All%20Distillation%20for%20Video%20Generation.md) · [[多模态基础模型]] [[世界模型]]
- [WorldLine: Action-Driven Visual Simulation for Robotic Manipulation](items/WorldLine%20Action-Driven%20Visual%20Simulation%20for%20Robotic%20Manipulation.md) · [[智能体 Agent]] [[世界模型]] [[机器人学习]] [[具身智能评测与基准]]

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2377
- 入选条目：24
- 回填已见条目：0
- 最高分论文：AeroManip-VLA: Scalable Vision-Language-Action Learning for Aerial Manipulation with RL-Generated Demonstrations
- 最高分论文发布时间：2026-09-29T07:34:54Z
- 主要技术对象分类：多模态基础模型 21、具身智能评测与基准 20、视觉语言动作模型 VLA 13、智能体 Agent 12、世界模型 11、机器人学习 9、Sim2Real 4
- 信息源错误：0
- 自动恢复信息源：0

</details>
