---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.07498v1"
published: "2026-09-07T13:47:22Z"
age_days: 1
score: 28
created: 2026-09-09
concepts: ["世界模型", "机器人学习", "具身智能评测与基准"]
---

# CosmoH2G: A Hand-to-Gripper Transfer Dataset and Baseline Method for Object Manipulation with Complex Spatial Movements

> [!summary] 先说人话（基于摘要）
> CosmoH2G把带旋转、翻转等复杂动作的人手示范转成夹爪轨迹。它先预测起终关键帧，再补全连续动作，并用几何约束修正平移漂移。

## 这篇到底在做什么

- **卡在哪里**：已有手到夹爪迁移多限于简单平面任务；复杂空间动作中，直接端到端生成整段夹爪位姿会积累细小轨迹偏差，导致执行不稳定。
- **关键解法**：通过手持夹爪模仿和强调运动复杂度的协议采集手—夹爪配对示范。模型先生成稀疏起终关键帧，再条件生成完整轨迹；保持姿态由学习预测，并依据抓取启发式与运动学一致性后优化平移。
- **拿什么证明**：数据集包含6189段示范和1254个独特物体。摘要报告仿真及真实机器人中实现稳定精准迁移，显著超过传统基线；摘要未给出可核查的性能结果数字。

## 值不值得读

- **和你的研究有什么关系**：对机器人学习提供复杂三维动作的配对数据与迁移基线，有助于研究人类示范如何转成夹爪监督；摘要未展示世界模型方面的直接贡献。
- **先别急着信**：需要核查空间复杂度的度量、物体和动作划分，以及后优化所需的几何与抓取信息来源。
- **判断**：人类示范迁移方向值得精读数据协议和后优化，尤其要判断部署时能否获得相同输入。

## 研究关联

- **概念**：[[世界模型]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-09/CosmoH2G A Hand-to-Gripper Transfer Dataset and Baseline Method for Object Manip.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Transferring human hand demonstrations to robotic grippers has recently emerged as a cost-effective solution for robot learning. However, existing methods are largely confined to simple, planar tasks and fail to handle complex spatial movements (e.g., intricate trajectories involving rotations or flips) that are essential for robot manipulation. Motivated by this gap, we adopt an implicit, data-driven approach guided by fine-grained hand-pose motions. To this end, we introduce a scalable acquisition pipeline to collect hand-gripper paired demonstrations, governed by a rigorous protocol that prioritizes motion complexity and leverages a handheld gripper for seamless action mimicry. This yields a large-scale paired dataset comprising 6,189 episodes across 1,254 unique objects, exhibiting significantly higher spatial complexity than existing benchmarks. However, learning such complex mappings remains challenging. We observe that naive end-to-end generation of full gripper pose sequences is insufficient, as minor trajectory deviations compound rapidly under intricate dynamics. To address this, we propose a two-stage framework: Stage I predicts sparse gripper keyframes (initial and terminal) to simplify the mapping objective, while Stage II generates the full continuous action sequence conditioned on these keyframes. Furthermore, to mitigate cumulative drift, we keep the gripper's orientation being learned while post-optimizing its translation based on the grasping heuristic and kinematic consistency. In both simulation and real-robot experiments, our framework enables stable and precise hand-to-gripper transfer of complex spatial manipulations, significantly outperforming traditional baselines. Project page: https://cosmoh2g.github.io.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.07498v1
- Authors: Hongxiang Zhao, Mutian Xu, Zeyu Jin, Yiming Hao, Shuguang Cui, Xiaoguang Han
- Published: 2026-09-07T13:47:22Z
- Age days: 1

</details>
