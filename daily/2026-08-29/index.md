---
type: daily-update
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
created: 2026-08-29
---

# 2026-08-29 AI Embodied Intelligence Update

> [!summary] 30 秒结论
> 今天最值得看的是三条线：跨本体或人类视频驱动的机器人世界—动作建模、把视频生成器变成可交互且具有空间记忆的模拟器，以及更严格地区分“画得像”与“真的学到动力学”的评测。CLAP、Zero-WAM、4DStreamCtrl、Mirage代表能力推进，R2M-Bench与PAWBench则提醒研究者：长期一致、运动丰富和概率正确是不同问题。少数医疗、通信与通用视觉论文和具身研究关联较弱，适合按具体需求选读。
> **趋势**：共同趋势是将显式几何、持久记忆和动作条件引入生成模型，并从单一平台、单条轨迹扩展到跨本体与分布级世界建模。与此同时，评测开始针对慢动作捷径、概率失配和可复现失败，而不再满足于像素质量或单次任务成功。

- **规模**：2333 个候选 → 24 篇入选；回填 0 篇
- **主题**：世界模型 14、具身智能评测与基准 13、智能体 Agent 10、多模态基础模型 5、AI 核心知识地图 3、视觉语言动作模型 VLA 3、机器人学习 2
- **源异常**：2
- **阅读方式**：先看 5 篇必读的“为什么值得读”，有用再进入 [L1 / L2 精读](../../deep-reading/README.md)

## 必读 5 篇

### 1. [CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators](items/CLAP%20Cross-Embodiment%20Video%20World%20Models%20are%20Zero-Shot%20Physical%20Simulators.md)

> CLAP把不同机器人乃至无动作标注的人类视频放进同一个动作条件视频世界模型：先用潜动作学习跨本体物理先验，再以末端执行器动作完成落地，支持零样本部署。

- **为什么值得读**：对世界模型与机器人学习研究者，价值在于把互联网人类视频转化为机器人动力学预训练资源，并提供跨本体初始化后再少样本适配的路线；对Agent研究，其零样本物理模拟能力可能支持规划。
- **证据**：摘要称其在DROID等困难环境中接近或超过先进单本体视频模型，少样本适配后优势进一步扩大；覆盖DROID、Bridge、双臂YAM和G1人形机器人，但未报告具体指标或数字。
- **判断**：值得精读方法与跨本体实验：问题关键、路线完整，但领先幅度和零样本泛化边界必须看全文才能判断。

### 2. [TrapVLA: Trapping Vision-Language-Action Models in Configured Failure Modes](items/TrapVLA%20Trapping%20Vision-Language-Action%20Models%20in%20Configured%20Failure%20Modes.md)

> TrapVLA研究一种更危险的VLA后门：隐蔽文本触发器不仅让机器人失败，还能指定它以何种方式失败。方法通过学习触发器诱导的动作残差，将策略推向预设偏移等故障行为。

- **为什么值得读**：它为VLA安全评测提供了比“是否失败”更细的威胁模型，可测试机器人是否会被语言触发器稳定操纵成特定危险动作；与世界模型的直接关系较弱。
- **证据**：摘要称两个基准覆盖四类代表性故障，并在仿真及真实机器人上有效注入指定故障，同时大体保持干净数据性能；未给出成功率、干净性能下降或检测率数字。
- **判断**：做VLA部署、安全或评测应精读基准和攻击设定；只做常规策略学习可重点阅读威胁模型与评测部分。

### 3. [SpatialCrafter: Single Image World Modeling with Generative 3D Proxies](items/SpatialCrafter%20Single%20Image%20World%20Modeling%20with%20Generative%203D%20Proxies.md)

> SpatialCrafter把单图场景生成拆成“先搭可对齐的3D骨架、再补照片级外观”：PaSS Flow生成全局3D代理，Generative Deferred Refiner沿该几何细化视频。

- **为什么值得读**：对世界模型研究者，这是用全局几何代理约束视觉想象的实用途径；对具身评测，可生成可探索场景，但摘要未证明其物理交互性或可作为机器人动力学模拟器。
- **证据**：构建了11.5万场景的混合图像到场景数据集；摘要称在合成和真实数据上超过先进方法，并改善长期漂移及极端视角一致性，但没有具体性能数字。
- **判断**：值得精读架构和数据构建；若目标是物理世界模型，则先看实验是否超出视图合成。

### 4. [Reconstructing Humans and Objects in Interaction using Large Reconstruction Models](items/Reconstructing%20Humans%20and%20Objects%20in%20Interaction%20using%20Large%20Reconstruction%20Mode.md)

> MILO利用大重建模型生成的网格作为人—物相对几何脚手架，再分割人体与物体、拟合人体参数模型，并可选对齐物体模板，从单图恢复3D交互。

- **为什么值得读**：可为具身智能数据和评测恢复人—物空间关系、接触上下文或示范几何；它本身不是控制策略或世界模型。
- **证据**：摘要称在多个基准和交互场景中取得较强精度并超过现有基线，但未给出数据集名称、指标或数字。
- **判断**：做人—物交互感知或示范重建值得读实验与失败案例；机器人控制研究者浏览即可。

### 5. [Surgical Video Generation From Diffusion to World Models: A Survey](items/Surgical%20Video%20Generation%20From%20Diffusion%20to%20World%20Models%20A%20Survey.md)

> 这篇综述把2024—2026年手术视频生成分成无条件、条件和世界模型三类，主线是领域正从“生成像真的画面”转向“模拟手术场景的因果动态”。

- **为什么值得读**：对手术机器人和世界模型研究者，它可用于建立任务分类、识别临床合理性与像素指标之间的断层；对通用Agent研究价值有限。
- **证据**：摘要只说明覆盖2024—2026文献并汇总代表方法的公开数据结果，没有给出论文数量、数据集范围或汇总数字。
- **判断**：初入手术视频生成者值得通读；已有领域经验者重点看分类框架、量化表格与开放问题。

## 扫读 7 篇

- [Pre-training Visual Dexterity in Simulation](items/Pre-training%20Visual%20Dexterity%20in%20Simulation.md) — SPD用VR让人直接操控仿真中的多指机器人手，以全仿真的同本体轨迹预训练因果Transformer，再用少量真实示范微调到56自由度双臂灵巧系统。
- [Zero-WAM: In-Context World-Action Modeling from Human Videos for Open-Ended Task Generalization](items/Zero-WAM%20In-Context%20World-Action%20Modeling%20from%20Human%20Videos%20for%20Open-Ended%20Task.md) — Zero-WAM把人类示范视频当作机器人新任务的上下文提示，无需更新参数就执行未见任务。其IFP训练目标迫使因果视频—动作模型从视频提示取任务信息，而非靠训练任务捷径。
- [MLLM-Routed Heterogeneous Ensembles for Robust Cross-Dataset Image Classification](items/MLLM-Routed%20Heterogeneous%20Ensembles%20for%20Robust%20Cross-Dataset%20Image%20Classificatio.md) — ARMDIL让多模态大模型充当路由器，逐图选择ResNet、自监督模型或VLM等最合适的视觉骨干，以处理跨数据集分类。新增知识可通过改提示接入，而不必重新训练路由器。
- [Unified Prediction and Planning via Conflict-Aware Disjoint Parameter Training](items/Unified%20Prediction%20and%20Planning%20via%20Conflict-Aware%20Disjoint%20Parameter%20Training.md) — DPT针对拥挤导航中“预测他人”和“规划自身安全路径”争抢共享参数的问题，分别训练两种技能的关键参数区域，再稀疏合并成紧凑统一模型。
- [4DStreamCtrl: Interactive Video Generation with Online 4D Control](items/4DStreamCtrl%20Interactive%20Video%20Generation%20with%20Online%204D%20Control.md) — 4DStreamCtrl用统一3D点轨迹同时表示相机运动、物体运动和深度编辑，并把视频扩散模型蒸馏成四步去噪的因果流式生成器，实现在线4D控制。
- [DINOcular: Self-Supervised Visuospatial Representations](items/DINOcular%20Self-Supervised%20Visuospatial%20Representations.md) — DINOcular把RGB外观和深度几何先验通过跨patch与patch内融合，学习兼顾语义和三维结构的自监督RGB-D表示。
- [Egosurg: Arbitrary view synthesis for egocentric replay of operating room workflows from ambient cameras](items/Egosurg%20Arbitrary%20view%20synthesis%20for%20egocentric%20replay%20of%20operating%20room%20workflo.md) — EgoSurg用稀疏墙面双目相机重建动态手术室，再合成不同角色的第一视角回放，无需给医护人员佩戴设备。核心是尺度感知深度初始化3D Gaussian Splatting，并用条件扩散修正遮挡导致的渲染伪影。

## 其余存档 12 篇

- [Think3D: Thinking with Space for Spatial Reasoning](items/Think3D%20Thinking%20with%20Space%20for%20Spatial%20Reasoning.md) · 多模态基础模型 智能体 Agent
- [4DSynth: Controllable Procedural World Synthesis for Dynamic Embodied Simulation](items/4DSynth%20Controllable%20Procedural%20World%20Synthesis%20for%20Dynamic%20Embodied%20Simulation.md) · 多模态基础模型 智能体 Agent 世界模型 具身智能评测与基准
- [Parameter Efficient Continual Learning for Sparse Event-Based Transformers](items/Parameter%20Efficient%20Continual%20Learning%20for%20Sparse%20Event-Based%20Transformers.md) · AI 核心知识地图
- [R2M-Bench: Evaluating Revisit Memory via Relative Consistency in Interactive Video World Models](items/R2M-Bench%20Evaluating%20Revisit%20Memory%20via%20Relative%20Consistency%20in%20Interactive%20Vide.md) · 世界模型 具身智能评测与基准
- [PAWBench: How Far Are We from Probabilistically Aligned World Modeling?](items/PAWBench%20How%20Far%20Are%20We%20from%20Probabilistically%20Aligned%20World%20Modeling.md) · 世界模型 具身智能评测与基准
- [GameWAM: A World Action Model for Video Games](items/GameWAM%20A%20World%20Action%20Model%20for%20Video%20Games.md) · 智能体 Agent 世界模型 视觉语言动作模型 VLA
- [I spent a day at a robot “carnival” in Shanghai. Here’s what I saw.](items/I%20spent%20a%20day%20at%20a%20robot%20%E2%80%9Ccarnival%E2%80%9D%20in%20Shanghai.%20Here%E2%80%99s%20what%20I%20saw..md) · AI 核心知识地图
- [Successive Capacity Growth: Task-Complexity-Driven Width and Depth Expansion for Vision Transformer Encoders in JEPA World Models](items/Successive%20Capacity%20Growth%20Task-Complexity-Driven%20Width%20and%20Depth%20Expansion%20for.md) · 世界模型
- [High-Fidelity Face Content Recovery via Tamper-Resilient Versatile Watermarking](items/High-Fidelity%20Face%20Content%20Recovery%20via%20Tamper-Resilient%20Versatile%20Watermarking.md) · 具身智能评测与基准
- [DALE-CT: Depth-Aware 2D Slice Encoders Learn an Anatomical World Model of Chest CT](items/DALE-CT%20Depth-Aware%202D%20Slice%20Encoders%20Learn%20an%20Anatomical%20World%20Model%20of%20Chest%20C.md) · 世界模型 具身智能评测与基准
- [Knowledge Distillation Driven Semantic NOMA with GAN Refinement for 6G Robotic Vehicle Networks](items/Knowledge%20Distillation%20Driven%20Semantic%20NOMA%20with%20GAN%20Refinement%20for%206G%20Robotic%20V.md) · AI 核心知识地图
- [Latent Spatial Memory for Video World Models](items/Latent%20Spatial%20Memory%20for%20Video%20World%20Models.md) · 世界模型

<details>
<summary>运行信息与信息源状态</summary>

- 候选数量：2333
- 入选条目：24
- 回填已见条目：0
- 最高分论文：CLAP: Cross-Embodiment Video World Models are Zero-Shot Physical Simulators
- 最高分论文发布时间：Sat, 29 Aug 2026 00:00:00 -0400
- 主要技术对象分类：世界模型 14、具身智能评测与基准 13、智能体 Agent 10、多模态基础模型 5、AI 核心知识地图 3、视觉语言动作模型 VLA 3、机器人学习 2
- 信息源错误：1
- 自动恢复信息源：1

### 自动恢复信息源

- arXiv Daily - Frontier Embodied AI Robotics Papers: primary failed: The read operation timed out (after 1 attempts); recovered via 4/4 configured fallback feeds

### 信息源错误

- Berkeley BAIR Blog: <urlopen error _ssl.c:1112: The handshake operation timed out> (after 3 attempts)

</details>
