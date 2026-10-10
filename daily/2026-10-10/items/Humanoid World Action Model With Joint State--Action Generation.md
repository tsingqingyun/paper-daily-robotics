---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: body-excerpts
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2610.12026v1"
published: "2026-10-08T14:23:18Z"
age_days: 1
score: 38
created: 2026-10-10
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Humanoid World Action Model With Joint State--Action Generation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> HWAM 同时预测“让机器人怎样动”和“执行后身体实际会到哪里”。它再用正向、反向视觉预测训练这对轨迹，帮助高层策略学会低层控制造成的执行偏差。

## 问题

在人形分层控制中，高层输出运动参考，低层还要为平衡、接触和动力学调整动作，因此参考轨迹不等于实际运动。例如躯干为保持平衡改变姿态，手的接触位置也会变。只从动作预测未来画面，模型必须同时猜命令如何落实、实际运动如何改变场景，两个关系混在一起 [S3](https://arxiv.org/html/2610.12026v1#S1.p2.1) [S4](https://arxiv.org/html/2610.12026v1#S1.F1) [S5](https://arxiv.org/html/2610.12026v1#S1.p3.1) [S6](https://arxiv.org/html/2610.12026v1#S1.p4.1)。

### 用一个例子理解

理解用例（非论文实验）：输入相机画面、当前关节状态和“拿起架上的玩具”；模型联合生成伸手参考与预计执行后身体状态。低层控制为保持平衡调整运动，只执行参考动作；下一次高层查询读取新的实测状态，继续修正。

## 创新点或方法

旧目标只生成动作，HWAM 把每个参考动作与执行后的实测身体状态配对，拼接后由同一生成器联合去噪；这样动作每次修正都能接触正在形成的状态估计 [S8](https://arxiv.org/html/2610.12026v1#S1.p6.2) [S19](https://arxiv.org/html/2610.12026v1#S3.SS2.p2.1)。训练有三路：Policy 从当前图像、语言和身体状态生成联合轨迹；FDM 从示范动作及执行状态预测未来画面；IDM 从视觉变化反推联合轨迹。两个专家通过按路径设置的注意力交换信息 [S20](https://arxiv.org/html/2610.12026v1#S3.SS3.p1.1) [S21](https://arxiv.org/html/2610.12026v1#S3.SS3.p3.1) [S22](https://arxiv.org/html/2610.12026v1#S3.SS4.SSS0.Px1.p1.1)。部署只走当前观测条件下的联合生成，不生成未来视频，也只把动作交给低层控制器 [S9](https://arxiv.org/html/2610.12026v1#S1.p7.1)。

### 方法如何工作

1. 同步记录参考动作和下一采样时刻的身体状态，形成命令与执行结果的联合标签。
2. 把两种轨迹拼接后共同去噪，使动作生成持续利用状态估计。
3. 用 FDM 解释联合轨迹对应的未来画面，用 IDM 从画面变化恢复轨迹，补充双向监督。
4. 用 Policy 路径只依靠当前输入训练，匹配部署时可获得的信息。
5. 部署联合预测后仅下发动作，低层执行并反馈实测状态，闭环继续。

### 必要术语

- 运动参考：高层希望低层跟踪的姿态或运动目标；本文动作不是直接施加的力矩。
- 本体感知状态：机器人测得的自身身体状态；本文把执行后的状态作为预测标签。
- FDM／IDM：从轨迹预测视觉结果／从视觉变化反推轨迹；本文用这两个方向连接动作、身体响应与场景变化。

## 证据

LimX OLI 真机测试包括取糖果、物体收集和移动取毛绒玩具；对照含 π₀.₅、GR00T、Fast-WAM 等 [S25](https://arxiv.org/html/2610.12026v1#S4.SS2.p1.1) [S27](https://arxiv.org/html/2610.12026v1#S4.SS2.p2.1)。HWAM 成功率为70.6%、46.7%、73.3%，π₀.₅为62.5%、45.0%、60.7%；Fast-WAM 取糖果为43.3% [S31](https://arxiv.org/html/2610.12026v1#S4.T1.2)。这些是完整系统成绩。移动任务的匹配消融更关键：普通视频生成加策略训练下，加入状态目标从60.0%降至45.5%；三路径训练下则从55.0%升至73.3% [S35](https://arxiv.org/html/2610.12026v1#S4.T2.2)。证据支持状态目标与训练方式的配合，不能说加状态预测必然有益。

## 局限

作者明确说消融没有隔离各训练路径及架构选择的贡献 [S36](https://arxiv.org/html/2610.12026v1#S4.SS5.p2.1)。我的待核查问题是动作与下一采样状态是否充分对应实际响应，特别是控制存在延迟时。节选未提供真机试验次数、置信区间及执行偏差诊断数值；最高观察成功率不等于每项都可靠胜出，也不能断言收益已被证明通过缩小执行差距产生。

- **判断**：值得读到时间对齐和两因素消融：最有说服力的是联合状态目标依赖合适训练方式，而不是单纯多预测一种变量。

## 研究关联

当动作还要经过会修改命令的控制层时，可以把“命令—实际响应”作为显式学习对象，避免让图像预测独自吸收全部偏差。但状态目标要与解释物理结果的训练任务配套，不能当作随手附加的输出。

### 下一步读哪里

先核查 [S19](https://arxiv.org/html/2610.12026v1#S3.SS2.p2.1) 的采样间隔、状态字段及动作延迟对齐，再检查三路径注意力可见性，确认 Policy 不接触真实未来信息。读 [S35](https://arxiv.org/html/2610.12026v1#S4.T2.2) [S36](https://arxiv.org/html/2610.12026v1#S4.SS5.p2.1) 的试验次数与区间，并核查是否有逐路径消融和执行状态预测误差；[S29](https://arxiv.org/html/2610.12026v1#S4.SS2.p4.1) 的训练资源也需纳入复现成本。

- **概念**：多模态基础模型 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.12026v1
- 获取时间：2026-10-10T00:24:46.287138+00:00
- [S1] [HWAM: Humanoid World Action Model With Joint State–Action Generation · 正文段落 1](https://arxiv.org/html/2610.12026v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2610.12026v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.12026v1#S1.p2.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.12026v1#S1.F1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.12026v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.12026v1#S1.p4.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.12026v1#S1.p5.1)
- [S8] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.12026v1#S1.p6.2)
- [S9] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.12026v1#S1.p7.1)
- [S10] [1 Introduction · 正文段落 12](https://arxiv.org/html/2610.12026v1#S1.p8.1)
- [S11] [1 Introduction · 正文段落 14](https://arxiv.org/html/2610.12026v1#S1.I1.i2)
- [S12] [1 Introduction · 正文段落 15](https://arxiv.org/html/2610.12026v1#S1.I1.i3)
- [S13] [2.1 Vision-Language-Action Models · 正文段落 16](https://arxiv.org/html/2610.12026v1#S2.SS1.p1.1)
- [S14] [2.2 World Action Models and Joint Generative Policies · 正文段落 17](https://arxiv.org/html/2610.12026v1#S2.SS2.p1.1)
- [S15] [2.2 World Action Models and Joint Generative Policies · 正文段落 18](https://arxiv.org/html/2610.12026v1#S2.SS2.p2.1)
- [S16] [2.3 Body-State Representations for Humanoid Control · 正文段落 19](https://arxiv.org/html/2610.12026v1#S2.SS3.p1.1)
- [S17] [3.1 Hierarchical Control Interface and Overview · 正文段落 20](https://arxiv.org/html/2610.12026v1#S3.SS1.p1.1)
- [S18] [3.2 Joint Post-Execution State–Action Chunk Target · 正文段落 21](https://arxiv.org/html/2610.12026v1#S3.SS2.p1.1)
- [S19] [3.2 Joint Post-Execution State–Action Chunk Target · 正文段落 22](https://arxiv.org/html/2610.12026v1#S3.SS2.p2.1)
- [S20] [3.3 Architecture · 正文段落 30](https://arxiv.org/html/2610.12026v1#S3.SS3.p1.1)
- [S21] [3.3 Architecture · 正文段落 32](https://arxiv.org/html/2610.12026v1#S3.SS3.p3.1)
- [S22] [Training roles. · 正文段落 35](https://arxiv.org/html/2610.12026v1#S3.SS4.SSS0.Px1.p1.1)
- [S23] [Training roles. · 正文段落 36](https://arxiv.org/html/2610.12026v1#S3.SS4.SSS0.Px1.p2.1)
- [S24] [4 Experiments · 正文段落 45](https://arxiv.org/html/2610.12026v1#S4.p1.1)
- [S25] [4.2 Experimental Setup · 正文段落 47](https://arxiv.org/html/2610.12026v1#S4.SS2.p1.1)
- [S26] [4.2 Experimental Setup · 正文段落 48](https://arxiv.org/html/2610.12026v1#S4.F4)
- [S27] [4.2 Experimental Setup · 正文段落 49](https://arxiv.org/html/2610.12026v1#S4.SS2.p2.1)
- [S28] [4.2 Experimental Setup · 正文段落 50](https://arxiv.org/html/2610.12026v1#S4.SS2.p3.1)
- [S29] [4.2 Experimental Setup · 正文段落 51](https://arxiv.org/html/2610.12026v1#S4.SS2.p4.1)
- [S30] [4.3 Real-Robot Evaluation · 正文段落 52](https://arxiv.org/html/2610.12026v1#S4.SS3.p1.1)
- [S31] [4.3 Real-Robot Evaluation · 正文段落 54](https://arxiv.org/html/2610.12026v1#S4.T1.2)
- [S32] [4.3 Real-Robot Evaluation · 正文段落 55](https://arxiv.org/html/2610.12026v1#S4.SS3.p2.1)
- [S33] [4.5 Controlled Ablation on Plush-Toy Picking · 正文段落 60](https://arxiv.org/html/2610.12026v1#S4.SS5.p1.1)
- [S34] [4.5 Controlled Ablation on Plush-Toy Picking · 正文段落 61](https://arxiv.org/html/2610.12026v1#S4.T2)
- [S35] [4.5 Controlled Ablation on Plush-Toy Picking · 正文段落 62](https://arxiv.org/html/2610.12026v1#S4.T2.2)
- [S36] [4.5 Controlled Ablation on Plush-Toy Picking · 正文段落 63](https://arxiv.org/html/2610.12026v1#S4.SS5.p2.1)
- [S37] [Training data and observations. · 正文段落 72](https://arxiv.org/html/2610.12026v1#A2.SS0.SSS0.Px1.p1.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-10/Humanoid World Action Model With Joint State--Action Generation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Humanoid robots are a promising platform for general-purpose manipulation. Recent Vision-Language-Action (VLA) policies learn actions directly from multimodal observations, while World Action Models (WAMs) further incorporate future visual prediction to improve action generation. However, in hierarchical humanoid systems, VLA and WAM policies output reference actions that are subsequently realized through whole-body control, robot dynamics, balance, and contact. This hierarchy creates an action--execution gap: the reference produced by the policy can differ from the motion realized by the robot. Without explicitly modeling the realized body state, future visual prediction must jointly explain scene evolution and discrepancies between reference actions and executed motion, making it difficult to associate an action with its physical outcome. We propose HWAM, a Humanoid World Action Model with joint state--action generation, which makes the robot's post-execution proprioceptive state an explicit prediction target. By jointly generating reference actions and their realized body states, HWAM directly incorporates supervision of executed motion into action learning. HWAM is trained through three complementary conditional paths. The Policy path jointly denoises state--action trajectories conditioned only on current observations, matching deployment conditions. Forward Dynamics Modeling (FDM) predicts future visual observations conditioned on actions and post-execution states, while Inverse Dynamics Modeling (IDM) reconstructs the joint trajectory from visual transitions. Together, these paths connect policy references, realized body motion, and visual outcomes. HWAM achieves the highest success rate among evaluated baselines on three real-robot tasks on the LimX OLI humanoid. On Candy Picking, HWAM achieves a 70.6% success rate, compared with 43.3% for Fast-WAM.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.12026v1
- Authors: Yan Yang, Jikun Rong, Minzhao Zhu, Zheyi Zhao, Qirui Hu, Zihan Lan, Weixin Mao, Yinhao Li, Zhen Fu, Hua Chen
- Published: 2026-10-08T14:23:18Z
- Age days: 1

</details>
