---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26058v1"
published: "2026-08-26T17:27:36Z"
age_days: 0
score: 45
created: 2026-08-27
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# One Policy, Many Embodiments: Unified Camera-Centric Action Geometry Pre-training for Heterogeneous Embodied Manipulation

> [!summary] 先说人话（基于摘要）
> UCAG-P 不再强迫不同机器人共享同一种底层控制指令，而是让统一 VLA 预测相机可见的锚点运动，再由几何条件动作翻译器转换为各本体可执行控制。这样把“学通用操作几何”和“适配具体机器人运动学”拆开。

## 这篇到底在做什么

- **卡在哪里**：机器人臂、人形机器人和人手的形态、相机及动作空间不同，异构数据难以共同训练。显式动作重定向、人到机器人视频合成和数据集专属分支都引入额外适配，妨碍单一策略直接吸收全部数据。
- **关键解法**：输入为视觉与任务条件，统一策略输出图像坐标和相机坐标中的可观察锚点运动；几何条件翻译器再结合目标本体运动学生成控制命令。关键差异是共享目标从机器人专属动作改成跨本体的相机中心几何动作。
- **拿什么证明**：使用4.03K小时机器人与仿真数据及2.34K小时人类示范训练；单一检查点在LIBERO、RoboTwin Easy/Hard、LIBERO-Plus零样本和RoboCasa GR-1上分别达到98.3%、88.7%、89.2%、82.0%和62.0%，且无基准专属微调。

## 值不值得读

- **和你的研究有什么关系**：对扩展通用VLA很直接：它提供了一种合并人类、仿真和多种机器人数据的公共动作接口，也可能成为世界模型与控制器之间更稳定的几何层。
- **先别急着信**：摘要没有分离统一动作表示、翻译器和数据规模各自的贡献，也未说明在运动学差异极大的本体上何时会失效，需查全文消融与执行误差。
- **判断**：值得精读方法和跨本体实验；结果覆盖面与单检查点表现很强，但核心主张是否成立取决于翻译器是否真正低成本且可泛化。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：45
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-27/One Policy, Many Embodiments Unified Camera-Centric Action Geometry Pre-training.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Scaling generalist vision-language-action (VLA) policies is severely bottlenecked by the inherent heterogeneity of embodied data, which spans diverse robot morphologies, camera configurations, and low-level action spaces. Existing paradigms typically address this mismatch through explicit action retargeting, human-to-robot video synthesis, or dataset-specific adaptation branches, fundamentally hindering the joint learning of a unified policy. We introduce UCAG-P, a camera-centric unified action formulation that structurally aligns heterogeneous embodied datasets into a shared geometric action space. Rather than treating robot-specific commands as the shared policy target, UCAG-P represents manipulation through camera-observable anchor motion in image and camera-frame coordinates, treating robot arms, humanoids, and human hands as different embodiments of a common action schema. A geometry-conditioned action translator combines predicted motion with target-embodiment kinematics to produce executable controls. The resulting decoupled architecture allows a shared VLA policy to learn transferable manipulation geometry while retaining embodiment-specific controllability. UCAG-P is trained on 4.03K hours of robot and simulation data and 2.34K hours of human demonstrations. A single checkpoint reaches 98.3% on LIBERO, 88.7% and 89.2% on RoboTwin Easy and Hard, 82.0% zero-shot on LIBERO-Plus, and 62.0% on RoboCasa GR-1, without benchmark-specific fine-tuning.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26058v1
- Authors: Xiaomi Embodied Intelligence Team, University of Macau, :, Shaoqing Xu, Fang Li, Guozhi Zhan, Zhixiang Duan, Yuhan Wang, Yuechen Luo, Shengyin Jiang, Hanbing Li, Zhiying Du, Longlong Wang, Longmei Jiang, Weixiang Liang, Ying Gong, Yong Pan, Ziping Zhao, Zhiyuan Chen, Yangwei You, Kun Ma, Qinyuan Liu, Hangjun Ye, Zhi-xin Yang
- Published: 2026-08-26T17:27:36Z
- Age days: 0

</details>
