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
url: "https://arxiv.org/abs/2611.33010v1"
published: "2026-11-24T17:32:00Z"
age_days: 1
score: 38
created: 2026-11-26
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> RoboDojo-Mirror 保持任务和策略固定，只改变镜面条件，再用同形状的不反光板检查实体障碍能解释多少失败。评测还观察机器人伸向哪里、碰到了什么，以定位倒影怎样干扰操作。

## 问题

镜子会把可识别的目标复制到不可抓取的位置，也可能让实物与倒影在图像中连成一块，或露出原本被遮挡的目标。常见的光照、背景与视角扰动测不出策略会怎样处理这种对应关系。插入镜子还改变了物理场景，成功率下降本身无法说明机器人是被挡住了，还是把目标位置判断错了。[S3](https://arxiv.org/html/2611.33010v1#S1.p2.1) [S4](https://arxiv.org/html/2611.33010v1#S1.p3.1) [S5](https://arxiv.org/html/2611.33010v1#S1.p5.1)[S26](https://arxiv.org/html/2611.33010v1#S4.SS1.p5.1)

### 用一个例子理解

理解用例（非论文实验）——输入抓杯指令，在匹配的桌面布局上分别放竖镜和同尺寸哑光板。保持同一策略、相机和预算，记录杯子是否被抓起、手伸向哪里、是否碰板。若镜面条件独有的失败表现为手伸向倒影附近且没有碰板，就有理由优先检查目标定位。

## 创新点或方法

作者在 RoboDojo 的同一组任务里比较无镜、单镜、双镜和镜面桌面。同一策略固定检查点和推理设置，在匹配的布局与随机种子下闭环运行，保持任务指令和成功标准。对选定策略，把竖镜换成同几何的不反光板并记录接触，用来估计直接撞板能解释多少。再单独测镜面上的抓取、目标轮廓与倒影相连时的推动，以及主视角遮挡时能否借倒影触及实物。评测沿用原策略，无镜面专项训练。[S5](https://arxiv.org/html/2611.33010v1#S1.p5.1)[S12](https://arxiv.org/html/2611.33010v1#S3.SS1.p2.1) [S13](https://arxiv.org/html/2611.33010v1#S3.SS1.p3.1) [S14](https://arxiv.org/html/2611.33010v1#S3.SS2.p2.1) [S15](https://arxiv.org/html/2611.33010v1#S3.SS2.p6.1) [S16](https://arxiv.org/html/2611.33010v1#S3.SS2.p8.1) [S17](https://arxiv.org/html/2611.33010v1#S3.SS3.p1.1) [S18](https://arxiv.org/html/2611.33010v1#S3.SS3.p2.1)[S35](https://arxiv.org/html/2611.33010v1#A1.SS2.p1.1) [S36](https://arxiv.org/html/2611.33010v1#A1.SS2.p2.1)[S45](https://arxiv.org/html/2611.33010v1#A3.SS2.p2.1) [S46](https://arxiv.org/html/2611.33010v1#A3.SS2.SSS0.Px1.p1.1) [S47](https://arxiv.org/html/2611.33010v1#A3.SS2.SSS0.Px3.p1.1) [S48](https://arxiv.org/html/2611.33010v1#A3.SS2.SSS0.Px3.p1.2)

### 方法如何工作

1. 固定任务、初始布局和策略，建立可配对的无镜基线。
2. 只改变镜面布置，跑闭环操作并收集成功率和部分完成分数。
3. 对选定的竖镜试验加入等形不反光板，同时记录接触，检验实体障碍的解释。
4. 用抓取、推动和遮挡诊断观察动作偏差，再在真机上检查总体下降是否重现。

### 必要术语

- 配对评测：在匹配的初始条件下反复测试同一策略；本文用它比较加镜前后的变化。
- 等几何板对照：保留镜子的形状与位置，去掉反光；本文用它检查实体障碍的影响。
- 倒影误瞄：动作伸向倒影所暗示的位置；本文把它当作可从轨迹检验的行为解释。

## 证据

仿真八项任务、五个策略中，每种镜面条件都使各策略的汇总成功率下降，跨三种条件平均，降幅为 10.8–56.7 个百分点。竖镜对照中，50–88% 的镜面特有失败未记录到机器人碰板。真机 Franka 四项任务每个条件各测 10 次，π₀.₅ 在无镜、竖镜和镜桌下总体为 77.5%、52.5%、27.5%，FastWAM 为 60.0%、30.0%、10.0%。真机结果支持相同的下降方向。[S6](https://arxiv.org/html/2611.33010v1#S1.p6.1)[S24](https://arxiv.org/html/2611.33010v1#S4.SS1.p2.1)[S29](https://arxiv.org/html/2611.33010v1#S4.SS4.p2.1) [S30](https://arxiv.org/html/2611.33010v1#S4.F6) [S31](https://arxiv.org/html/2611.33010v1#S4.SS4.p3.1) [S32](https://arxiv.org/html/2611.33010v1#S4.T6) [S33](https://arxiv.org/html/2611.33010v1#S4.T6.5)[S45](https://arxiv.org/html/2611.33010v1#A3.SS2.p2.1) [S46](https://arxiv.org/html/2611.33010v1#A3.SS2.SSS0.Px1.p1.1) [S47](https://arxiv.org/html/2611.33010v1#A3.SS2.SSS0.Px3.p1.1) [S48](https://arxiv.org/html/2611.33010v1#A3.SS2.SSS0.Px3.p1.2)

## 局限

作者指出各策略的执行预算不同，结果适合做同一策略内的配对比较。几何匹配的板只覆盖单、双竖镜；没测到接触可以削弱直接碰撞解释，伸错位置也只与误判目标的解释一致。我会查轨迹归类的判据，以及遮挡诊断中实际有几次触到真目标。[S22](https://arxiv.org/html/2611.33010v1#S4.p1.1)[S26](https://arxiv.org/html/2611.33010v1#S4.SS1.p5.1)[S45](https://arxiv.org/html/2611.33010v1#A3.SS2.p2.1) [S46](https://arxiv.org/html/2611.33010v1#A3.SS2.SSS0.Px1.p1.1) [S47](https://arxiv.org/html/2611.33010v1#A3.SS2.SSS0.Px3.p1.1) [S48](https://arxiv.org/html/2611.33010v1#A3.SS2.SSS0.Px3.p1.2)

- **判断**：值得读到竖镜对照和轨迹诊断，单看成功率容易错过论文怎样区分障碍和视觉干扰。

## 研究关联

测试策略能否处理视觉歧义时，可以找一种在物理上等价的场景改动做对照，再同时看成功率、末端轨迹和接触。比如同样抓空，手伸向倒影附近和手被障碍挡住，指向不同的修正方向。

### 下一步读哪里

先用 [S17](https://arxiv.org/html/2611.33010v1#S3.SS3.p1.1) [S18](https://arxiv.org/html/2611.33010v1#S3.SS3.p2.1) [S19](https://arxiv.org/html/2611.33010v1#S3.SS3.p3.1) [S20](https://arxiv.org/html/2611.33010v1#S3.SS3.p3.2) [S21](https://arxiv.org/html/2611.33010v1#S3.SS3.p3.4)[S27](https://arxiv.org/html/2611.33010v1#S4.T1) 核对配对单位、任务等权汇总和区间的计算方式。再读 [S45](https://arxiv.org/html/2611.33010v1#A3.SS2.p2.1) [S46](https://arxiv.org/html/2611.33010v1#A3.SS2.SSS0.Px1.p1.1) [S47](https://arxiv.org/html/2611.33010v1#A3.SS2.SSS0.Px3.p1.1) [S48](https://arxiv.org/html/2611.33010v1#A3.SS2.SSS0.Px3.p1.2) 的接触定义和子集说明，核查镜面特有失败的分母，并用 [S33](https://arxiv.org/html/2611.33010v1#S4.T6.5) 看真机下降集中在哪些任务。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.33010v1
- 获取时间：2026-11-26T03:57:07.966677+00:00
- [S1] [Embodied AI Fails the Mirror Test: How a Simple Mirror Breaks Robot Policies · 正文段落 1](https://arxiv.org/html/2611.33010v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2611.33010v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2611.33010v1#S1.p2.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.33010v1#S1.p3.1)
- [S5] [1 Introduction · 正文段落 6](https://arxiv.org/html/2611.33010v1#S1.p5.1)
- [S6] [1 Introduction · 正文段落 7](https://arxiv.org/html/2611.33010v1#S1.p6.1)
- [S7] [2.1 Robotic Manipulation Benchmarks and Visual Robustness · 正文段落 8](https://arxiv.org/html/2611.33010v1#S2.SS1.p1.1)
- [S8] [2.2 Mirror Perception and Spatial Reasoning · 正文段落 9](https://arxiv.org/html/2611.33010v1#S2.SS2.p1.1)
- [S9] [2.3 Mirror-Mediated Robotic Interaction · 正文段落 10](https://arxiv.org/html/2611.33010v1#S2.SS3.p1.1)
- [S10] [3 Benchmark Design and Evaluation Protocol · 正文段落 11](https://arxiv.org/html/2611.33010v1#S3.p1.1)
- [S11] [3.1 Policy and Task Selection · 正文段落 12](https://arxiv.org/html/2611.33010v1#S3.SS1.p1.1)
- [S12] [3.1 Policy and Task Selection · 正文段落 13](https://arxiv.org/html/2611.33010v1#S3.SS1.p2.1)
- [S13] [3.1 Policy and Task Selection · 正文段落 14](https://arxiv.org/html/2611.33010v1#S3.SS1.p3.1)
- [S14] [3.2 Mirror Configurations · 正文段落 17](https://arxiv.org/html/2611.33010v1#S3.SS2.p2.1)
- [S15] [3.2 Mirror Configurations · 正文段落 21](https://arxiv.org/html/2611.33010v1#S3.SS2.p6.1)
- [S16] [3.2 Mirror Configurations · 正文段落 23](https://arxiv.org/html/2611.33010v1#S3.SS2.p8.1)
- [S17] [3.3 Evaluation Protocol and Metrics · 正文段落 24](https://arxiv.org/html/2611.33010v1#S3.SS3.p1.1)
- [S18] [3.3 Evaluation Protocol and Metrics · 正文段落 25](https://arxiv.org/html/2611.33010v1#S3.SS3.p2.1)
- [S19] [3.3 Evaluation Protocol and Metrics · 正文段落 26](https://arxiv.org/html/2611.33010v1#S3.SS3.p3.1)
- [S20] [3.3 Evaluation Protocol and Metrics · 正文段落 28](https://arxiv.org/html/2611.33010v1#S3.SS3.p3.2)
- [S21] [3.3 Evaluation Protocol and Metrics · 正文段落 32](https://arxiv.org/html/2611.33010v1#S3.SS3.p3.4)
- [S22] [4 Performance under Mirror Conditions · 正文段落 35](https://arxiv.org/html/2611.33010v1#S4.p1.1)
- [S23] [4.1 Overall Performance · 正文段落 39](https://arxiv.org/html/2611.33010v1#S4.SS1.p1.1)
- [S24] [4.1 Overall Performance · 正文段落 40](https://arxiv.org/html/2611.33010v1#S4.SS1.p2.1)
- [S25] [4.1 Overall Performance · 正文段落 41](https://arxiv.org/html/2611.33010v1#S4.SS1.p3.1)
- [S26] [4.1 Overall Performance · 正文段落 43](https://arxiv.org/html/2611.33010v1#S4.SS1.p5.1)
- [S27] [4.1 Overall Performance · 正文段落 44](https://arxiv.org/html/2611.33010v1#S4.T1)
- [S28] [4.4 Real-World Validation · 正文段落 80](https://arxiv.org/html/2611.33010v1#S4.SS4.p1.1)
- [S29] [4.4 Real-World Validation · 正文段落 81](https://arxiv.org/html/2611.33010v1#S4.SS4.p2.1)
- [S30] [4.4 Real-World Validation · 正文段落 82](https://arxiv.org/html/2611.33010v1#S4.F6)
- [S31] [4.4 Real-World Validation · 正文段落 83](https://arxiv.org/html/2611.33010v1#S4.SS4.p3.1)
- [S32] [4.4 Real-World Validation · 正文段落 84](https://arxiv.org/html/2611.33010v1#S4.T6)
- [S33] [4.4 Real-World Validation · 正文段落 85](https://arxiv.org/html/2611.33010v1#S4.T6.5)
- [S34] [5 Conclusion · 正文段落 86](https://arxiv.org/html/2611.33010v1#S5.p1.1)
- [S35] [A.2 Policy Configurations · 正文段落 93](https://arxiv.org/html/2611.33010v1#A1.SS2.p1.1)
- [S36] [A.2 Policy Configurations · 正文段落 94](https://arxiv.org/html/2611.33010v1#A1.SS2.p2.1)
- [S37] [A.2 Policy Configurations · 正文段落 95](https://arxiv.org/html/2611.33010v1#A1.SS2.p3.1)
- [S38] [A.2 Policy Configurations · 正文段落 96](https://arxiv.org/html/2611.33010v1#A1.SS2.p4.1)
- [S39] [A.2 Policy Configurations · 正文段落 97](https://arxiv.org/html/2611.33010v1#A1.T7)
- [S40] [A.2 Policy Configurations · 正文段落 98](https://arxiv.org/html/2611.33010v1#A1.T7.5)
- [S41] [A.2 Policy Configurations · 正文段落 99](https://arxiv.org/html/2611.33010v1#A1.SS2.p5.1)
- [S42] [A.3 Experiment Coverage and Measurement Sources · 正文段落 105](https://arxiv.org/html/2611.33010v1#A1.SS3.p1.1)
- [S43] [A.3 Experiment Coverage and Measurement Sources · 正文段落 106](https://arxiv.org/html/2611.33010v1#A1.T8)
- [S44] [A.4 Paired Evaluation and Metrics · 正文段落 112](https://arxiv.org/html/2611.33010v1#A1.SS4.p3.2)
- [S45] [C.2 Matched Mirror–Panel Controls · 正文段落 137](https://arxiv.org/html/2611.33010v1#A3.SS2.p2.1)
- [S46] [C.2 Matched Mirror–Panel Controls · 正文段落 139](https://arxiv.org/html/2611.33010v1#A3.SS2.SSS0.Px1.p1.1)
- [S47] [C.2 Matched Mirror–Panel Controls · 正文段落 145](https://arxiv.org/html/2611.33010v1#A3.SS2.SSS0.Px3.p1.1)
- [S48] [C.2 Matched Mirror–Panel Controls · 正文段落 147](https://arxiv.org/html/2611.33010v1#A3.SS2.SSS0.Px3.p1.2)
- [S49] [G.2 Tasks and Mirror Placement · 正文段落 215](https://arxiv.org/html/2611.33010v1#A7.T23)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-26/Embodied AI Fails the Mirror Test How a Simple Mirror Breaks Robot Policies.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Can a simple mirror expose the limitations of today's robotic manipulation policies? Inspired by the mirror self-recognition test in animal cognition, we investigate whether robot policies can reliably manipulate physical objects in scenes containing their reflections. We introduce RoboDojo-Mirror, a benchmark built on RoboDojo that preserves task objectives, success criteria, and policy checkpoints while comparing a mirror-free baseline with single-mirror, dual-mirror, and mirrored-tabletop conditions. Across five policies spanning Vision-Language-Action models, World Action Models, and agentic policies, every mirror condition reduces aggregate success rates: averaged over the three conditions, the drop ranges from 10.8 to 56.7 percentage points across policies, and it reaches 62.5 points on the mirrored tabletop. Because a mirror is also a physical obstacle, we compare it against geometrically matched non-reflective panels; 50--88\% of mirror-specific failures occur without recorded robot--panel contact, so direct collisions alone do not explain the degradation. Trajectory and contact analyses instead reveal recurring behaviors consistent with phantom targeting of reflected objects and spatial mislocalization of real ones. Targeted diagnostics further characterize grasping near reflections, policy-dependent pushing progress, and physical-target interaction under main-camera occlusion. Real-robot experiments with $π_{0.5}$ and FastWAM also show lower overall success rates under the upright-mirror and mirrored-tabletop conditions. These findings reveal a shared vulnerability to reflective environments across diverse robot policies and motivate reflection-aware evaluation of embodied intelligence. Code is available at https://github.com/iPPLab/robodojo-mirror.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.33010v1
- Authors: Xuanchen Liu, Hejun Zhang, Boxuan Dong, Ying Wu, Heshuai Li, Wen Gao, Yonghong Tian, Weihao Yu
- Published: 2026-11-24T17:32:00Z
- Age days: 1

</details>
