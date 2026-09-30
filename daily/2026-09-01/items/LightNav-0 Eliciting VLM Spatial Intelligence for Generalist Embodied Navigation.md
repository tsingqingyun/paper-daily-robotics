---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.30935v1"
published: "2026-08-31T15:08:53Z"
age_days: 0
score: 37
created: 2026-09-01
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "机器人学习", "具身智能评测与基准"]
---

# LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation

> [!summary] 先说人话（基于摘要）
> LightNav-0 把多类导航统一成 token 生成：双通道 pointing 表达跨任务、场景和身体的空间意图，再由残差向量量化动作 tokenizer 转成具体机器人轨迹。

## 问题

导航需把异构目标和视觉观测映射到不同 embodiment 的动作；现有系统依赖任务或身体专用模块，割裂感知、推理与控制，限制跨任务和跨机器人泛化。

## 创新点或方法

模型输入指令、当前视觉及压缩后的时序视觉历史，输出统一空间意图 token 与 embodiment 特定轨迹。它直接激活预训练 VLM 的 grounding、空间推理和 pointing 能力，不设任务专用预测头，并结合 ER 中期训练、监督微调和强化学习；关键差异是用统一 token 接口衔接通用空间意图与具体动作。

## 证据

训练语料覆盖 2,000 多场景和 4,000 多小时。LightNav-ER 在八个具身推理基准的完整集平均分最高；LightNav-0 在十个公开导航仿真设置中取得单目成功率 SOTA，并在真实环境展示跨机器人、场景及静动态目标的零样本泛化，摘要未给具体分数。


## 局限

摘要把多种训练阶段和接口设计合并报告，尚不能判断收益来自统一 token、数据规模还是强化学习；真实评测也缺少量化结果。

- **判断**：值得精读统一接口和跨 embodiment 映射；若消融扎实，它可能是通用导航架构比单项榜单更有价值的贡献。

## 研究关联

对通用具身 Agent 和机器人学习，它提供了一条少做任务专用头、复用紧凑 VLM 空间先验的路线；世界模型研究者的直接价值较弱，因为该方法并未以环境预测为核心。

- **概念**：多模态基础模型 智能体 Agent 世界模型 机器人学习 具身智能评测与基准
- **筛选分数**：37
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-01/LightNav-0 Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Embodied navigation requires agents to translate heterogeneous goals and visual observations into actions across tasks, environments, and robot embodiments. Modern vision-language models (VLMs) already encode spatial priors for visual grounding, spatial reasoning, and pointing, but these capabilities are rarely elicited directly for robot control. Existing navigation systems instead rely on task- or embodiment-specific components, fragmenting perception, reasoning, and action while offering limited generalization. Here we present LightNav-0, a compact generalist embodied navigation model that elicits the spatial intelligence of a pretrained VLM and aligns it with navigation, without task-specific prediction heads. LightNav-0 represents diverse navigation tasks through a unified token interface: dual-channel pointing expresses task-, scene-, and embodiment-agnostic spatial intent, while a residual vector-quantized action tokenizer maps this intent to precise, embodiment-specific trajectories. Together with temporally aware visual history compression, ER mid-training, supervised fine-tuning, and reinforcement learning, this formulation supports instruction following, open-vocabulary object navigation, and visual tracking within a single model. The navigation training corpus spans 2K+ scenes and 4K+ hours of embodied navigation data. LightNav-ER, the embodied-reasoning checkpoint used to initialize LightNav-0, attains the highest complete-set average across 8 embodied-reasoning benchmarks, while LightNav-0 achieves state-of-the-art monocular success rates across all 10 public navigation simulation settings. Real-world evaluations further demonstrate zero-shot generalization across robot embodiments, diverse scenes, and static and dynamic targets. These results establish compact VLMs as a unified and transferable backbone for generalist embodied navigation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.30935v1
- Authors: Shaoan Wang, Aocheng Luo, Fei Huang, Jingyi Xu, Xiaoyang Wang, Yueyu Wang, Qianli Ma, Fan Yang, Ran Mei, Jia Wei, Jiangpeng Hu, Xuhao Liu, Hongming Chen, Yuanbin Shao, Yiyang Lin, Ziliang Li, Liang Pan, Xinhang Liu, Yuntao Ma, Tingxiang Fan
- Published: 2026-08-31T15:08:53Z
- Age days: 0

</details>
