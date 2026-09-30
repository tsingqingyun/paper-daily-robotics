---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.31112v1"
published: "2026-09-25T10:57:02Z"
age_days: 2
score: 31
created: 2026-09-28
concepts: ["多模态基础模型", "智能体 Agent", "具身智能评测与基准"]
---

# DualManip: Agentic Dynamic Manipulation via Dual-Path Semantic Reasoning and Geometric Adaptation

> [!summary] 先说人话（基于摘要）
> DualManip 把慢速语义推理和快速几何更新分开：任务意图未变时，机器人直接跟着物体运动或变形调整抓取。几何更新失败后才重新调用语义规划。

## 问题

VLM 支持开放词汇操作推理，但推理延迟使动态场景中的响应变慢。许多变化只改变物体几何、没有改变任务意图，反复完整重规划会增加不必要的等待。

## 创新点或方法

语义路径分解任务、定位交互并求解位姿约束；几何路径从实时 RGB-D 更新模板与观测的对应关系，将抓取接触点迁移到新几何上。交互模块负责初始化、验证更新，并在失败时触发语义重规划。

## 证据

真机评估覆盖六项任务，包含非刚性形变、关节重构、刚体运动和精密装配，测试静态、单次变化及持续动态三种设置。摘要报告持续变化下鲁棒性更强，几何适应约比智能体验证与语义重规划快 46 倍，未给出成功率数字。

## 局限

46 倍比较的是几何适应与验证重规划两个过程，并非整套系统提速；需核查何种变化会使对应关系失效及触发机制的可靠性。

- **判断**：值得读双路径接口与失败触发实验，尤其适合动态操作系统设计。

## 研究关联

对机器人智能体研究者，它提供了按变化类型分配计算的具体架构，适合研究语义规划与实时感知控制之间的职责划分。

- **概念**：多模态基础模型 智能体 Agent 具身智能评测与基准
- **筛选分数**：31
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-28/DualManip Agentic Dynamic Manipulation via Dual-Path Semantic Reasoning and Geom.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language models (VLMs) enable open-vocabulary reasoning for robot manipulation, but their high inference latency limits responsiveness in dynamic scenes. Many scene changes, however, alter object geometry without invalidating task intent. We present DualManip, a dual-path framework that decouples infrequent semantic reasoning from responsive geometric adaptation. The semantic path decomposes the task and grounds task-relevant interactions, followed by a constraint-solving module for pose optimization. During execution, the geometric path continuously updates template-to-observation correspondences from live RGB-D observations via a shape-adaptive network. These correspondences transfer task-relevant grasp contacts across observations, enabling online grasp reconstruction under object motion and non-rigid deformation. The Information Interaction Module bridges the two paths by initializing task-relevant grasps from semantic grounding, validating geometric updates, and triggering semantic replanning upon update failures. Real-world evaluation spans six manipulation tasks covering non-rigid deformation, articulated reconfiguration, rigid motion, and high-precision assembly across three settings: static, single-change, and continuous dynamic. DualManip demonstrates superior manipulation robustness, particularly under continuous scene changes, while achieving geometric adaptation approximately 46$\times$ faster than agentic verification and semantic replanning. Our project page: https://lichengxi1.github.io/Dualmanip.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.31112v1
- Authors: Chengxi Li, Yan Di, Yingyue Li, Ruida Zhang, Mingyang Li, Xiangyang Ji
- Published: 2026-09-25T10:57:02Z
- Age days: 2

</details>
