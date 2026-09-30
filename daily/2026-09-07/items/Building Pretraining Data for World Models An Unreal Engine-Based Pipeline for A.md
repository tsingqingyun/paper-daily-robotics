---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.03557v1"
published: "2026-09-03T08:58:04Z"
age_days: 3
score: 24
created: 2026-09-07
concepts: ["世界模型"]
---

# Building Pretraining Data for World Models: An Unreal Engine-Based Pipeline for Action-Conditioned Video Generation

> [!summary] 先说人话（基于摘要）
> 这套Unreal Engine管线把实时物理轨迹生成与高质量离线渲染拆成两阶段，在大规模集群上生产动作、状态、相机严格对齐的多视角视频，供世界模型预训练。

## 问题

动作条件视频模型需要控制信号与视觉变化逐帧对齐，但普通真实视频通常不知道变化由什么动作造成；实时物理和高质量离线渲染又有不同执行要求，难以直接规模化。

## 创新点或方法

阶段I在PIE中运行真实物理并记录角色状态、控制输入和相机状态到中间轨迹；阶段II在新进程重放轨迹并用MRQ离线渲染。外围系统负责缓存感知分片、节点槽位调度、场景筛选、质量过滤、断点恢复、异步上传和集群监控。

## 证据

集群含25台服务器、每台8张RTX 5090；从2,384个资产包筛出429个关卡，并使用40个人形角色。已生成2,691小时1080p视频和6,076小时720p视频；该管线是EchoWM的合成数据组件。


## 局限

合成到真实的迁移效果摘要未报告；作者也明确指出依靠感知质量代理进行数据筛选存在局限，需核查其偏差如何影响模型。

- **判断**：建设世界模型数据管线者值得精读工程章节；关注算法创新者浏览架构和数据统计即可。

## 研究关联

对世界模型团队，这是少见的生产级动作条件视频数据工程说明，尤其有助于解决物理执行与电影级渲染解耦、故障恢复和集群吞吐问题。

- **概念**：世界模型
- **筛选分数**：24
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-07/Building Pretraining Data for World Models An Unreal Engine-Based Pipeline for A.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Action-conditioned video models require large-scale visual data paired with control signals that are temporally aligned with the resulting scene transitions. Such supervision is difficult to obtain from ordinary real-world video because the actions that caused each visual change are typically unknown. We present a large-scale synthetic data production pipeline built on Unreal Engine for generating action-conditioned, multi-view video. To accommodate the different execution requirements of real-time physics and high-quality offline rendering, the pipeline executes trajectory generation and final rendering in two stages: Stage I runs real physics in PIE and records per-frame character states, control inputs, and camera states into an intermediate trajectory representation; Stage II replays those trajectories in a new engine process and renders them offline with Movie Render Queue (MRQ). Around this core, we develop a distributed production system with cache-aware task partitioning, node-local slot scheduling, automated scene screening, aesthetic and luminance filtering, partial-output recovery, asynchronous upload, and continuous cluster health monitoring. The production cluster contains 25 servers with eight NVIDIA RTX 5090 GPUs per server. From 2,384 asset packs, 429 levels were retained for production together with a pool of 40 humanoid characters. The pipeline has produced 2,691 hours of 1080p video and 6,076 hours of 720p video. We describe the system architecture, the implementation decisions that emerged from production failures, and the limitations of using perceptual quality proxies for world-model data curation. The pipeline described in this report constitutes the Unreal Engine synthetic-data production component used in EchoWM.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.03557v1
- Authors: Haoyu Wang, Songchun Zhang, Haoran Li, Haoyang Huang, Zeyue Xue, Nan Duan
- Published: 2026-09-03T08:58:04Z
- Age days: 3

</details>
