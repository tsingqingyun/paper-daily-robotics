---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08339v1"
published: "2026-09-08T07:13:07Z"
age_days: 1
score: 25
created: 2026-09-10
concepts: ["世界模型", "机器人学习", "Sim2Real"]
---

# RoboCousin: Build Your Own Simulation Playground for Robust Bimanual Robotic Manipulation

> [!summary] 先说人话（基于摘要）
> RoboCousin 把用户给的物体图像变成可用于双臂任务的仿真资产，再生成保持任务关系的场景变体和专家轨迹，降低扩充训练数据的人工成本。

## 问题

真实双臂示范采集昂贵，而现有仿真流程受封闭资产库和预定义场景限制；加入新对象还需补齐几何、物理语义属性、交互标注和任务集成。

## 创新点或方法

基于 RoboTwin 2.0，从图像生成视觉与碰撞几何、元数据和抓取接触候选，再改变兼容物体、背景、布局和指令，保留关键可供性与空间关系，并支持桌面及房间级场景。

## 证据

发布超过 3,000 个标注物体实例和 50 个背景环境，跨 50 个任务生成超过百万条专家轨迹。仿真与实机结果报告自动交互标注接近人工整理标注，资产可支持 sim-to-real，桌面变体有助迁移；未给出增益数字。


## 局限

需核查从图像获得物理属性和接触候选的可靠性，以及自动生成流程仍需多少人工介入。

- **判断**：双臂数据团队值得细读并试用，重点审查资产质量和迁移收益，不能只看百万轨迹规模。

## 研究关联

对机器人学习和 Sim2Real 团队，核心价值是把新资产接入与任务多样化连成数据生产流程，也能扩展世界模型的交互数据来源。

- **概念**：世界模型 机器人学习 Sim2Real
- **筛选分数**：25
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-10/RoboCousin Build Your Own Simulation Playground for Robust Bimanual Robotic Mani.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Bimanual manipulation policies require large and diverse training datasets, yet collecting demonstrations on physical robots is expensive and difficult to scale. Simulation can generate data efficiently, but existing pipelines typically operate within closed asset libraries and predefined scenes: adding a newly observed object or environment still requires substantial effort to reconstruct geometry, specify physical and semantic properties, annotate interactions, and integrate the result into executable tasks. We present RoboCousin, an extensible simulation-based data-generation platform that turns user-provided observations into reusable assets, scenes, and expert trajectories for bimanual manipulation. Built on RoboTwin~2.0, RoboCousin converts object images into simulation-ready assets with visual and collision geometry, semantic and physical metadata, and automatically generated grasp-contact candidates. It further constructs digital cousins that vary compatible objects, backgrounds, layouts, and language instructions while preserving task-relevant affordances and spatial relations. The same asset system supports tabletop and room-level scene construction, with collision-aware base control for interaction beyond a fixed workspace. We release RoboCousin-OBD, containing more than 3,000 annotated object instances and 50 background environments, and use RoboCousin to generate over one million expert trajectories across 50 tasks. Simulation and real-robot experiments show that the automatically generated interaction annotations are comparable to curated annotations, generated assets provide effective sim-to-real supervision, and tabletop cousins can improve transfer beyond training on a single reconstructed scene. RoboCousin therefore provides a practical path for expanding both the scale and coverage of synthetic bimanual manipulation data.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08339v1
- Authors: Jingxuan Zhu, Jingyi Li, LiangLiang Chen, Zhiyuan Jing, Jidong Zhang, Hongming Li
- Published: 2026-09-08T07:13:07Z
- Age days: 1

</details>
