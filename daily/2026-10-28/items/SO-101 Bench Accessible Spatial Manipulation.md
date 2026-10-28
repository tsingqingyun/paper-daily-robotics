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
url: "https://arxiv.org/abs/2610.36420v1"
published: "2026-10-27T00:02:28Z"
age_days: 1
score: 43
created: 2026-10-28
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# SO-101 Bench: Accessible Spatial Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> SO-101 Bench 把低成本机械臂的语言空间操作搬进可重复的仿真，并用真机检查模型排名是否可信。它既测抓取，也专门测“放在两物之间”“旋转后才能塞进去”等容易被总成功率掩盖的能力。

## 问题

任务是按语言识别目标并准确摆放。现有 SO-101 评测主要依赖真机，试验成本高，还受机械臂校准、相机和物体磨损影响；已有仿真任务又缺少语言和充分的陌生物体测试。[S5](https://arxiv.org/html/2610.36420v1#S1.p1.1) [S6](https://arxiv.org/html/2610.36420v1#S1.p2.1) [S7](https://arxiv.org/html/2610.36420v1#S1.p3.1) 真正瓶颈是：怎样便宜地比较策略，同时确保仿真没有把实际优劣排错。

### 用一个例子理解

理解用例（非论文实验）：输入“把长橡皮放到杯子和盒子之间”及桌面图像；系统识别目标、检查空隙，必要时转动橡皮再放下；输出动作轨迹，评分器检查最终空间关系。

## 创新点或方法

旧做法直接在真机上试；本文建立 Isaac Lab 数字孪生，统一场景、物体划分和自动评分，再验证仿真与真机的一致性。训练时，学习策略都用同一批已见物体示范和相同算力预算微调；推理时测试已见物体、同类新实例和新类别。另比较写代码规划、把抓取交给 Galaxea 的语言模型智能体。[S7](https://arxiv.org/html/2610.36420v1#S1.p3.1) [S33](https://arxiv.org/html/2610.36420v1#A4.T14)

### 方法如何工作

1. 把真实机械臂和桌面做成数字孪生，让不同策略面对相同执行条件。
2. 仅用已见物体示范微调学习策略，使陌生物体测试有明确边界。
3. 运行语言空间任务并按最终状态评分，再用PLAN等子集定位失败能力。
4. 把同一权重部署到真机，比较排名与成功率差距，判断仿真能替代哪部分测试。

### 必要术语

- 数字孪生：对应真实装置的仿真副本；本文用它低成本比较策略。
- PLAN：必须旋转物体才能放入狭窄空间的子集；用于区分抓得住与放得进去。
- Spearman相关：衡量排名是否一致；不保证两个环境的成功率相等。

## 证据

主评测有916回合，分数是15个任务族×物体划分单元的平均成功率；九种 VLA/WAM 中最佳约61%，PLAN均不超过17%，组合智能体为83.2%、PLAN为75%。[S8](https://arxiv.org/html/2610.36420v1#S1.p4.1) [S20](https://arxiv.org/html/2610.36420v1#S3.SS6.p1.1) 五个系统各做45组仿真/真机测试，排名完全一致，Spearman为1.00，但仿真高估成功率9–31个百分点。[S23](https://arxiv.org/html/2610.36420v1#S5.SS0.SSS0.Px2.p1.1) [S24](https://arxiv.org/html/2610.36420v1#S5.SS0.SSS0.Px4.p1.1) 这支持该设置内的相对比较，不能把仿真分数直接当真机成功率。

## 局限

作者明确提醒：五个系统的排名验证仍有较宽区间；真机箱子更轻、部分仿真物体缩小，都会影响差距。[S23](https://arxiv.org/html/2610.36420v1#S5.SS0.SSS0.Px2.p1.1) [S24](https://arxiv.org/html/2610.36420v1#S5.SS0.SSS0.Px4.p1.1) 等算力也不等于训练充分：各模型看过的样本量相差很大，低分不能解释为能力上限。[S25](https://arxiv.org/html/2610.36420v1#S6.SS0.SSS0.Px3.p1.1)

- **判断**：值得读到评测协议和配对真机结果；主要收获是学会怎样构造可信比较，而不只是记住榜首。

## 研究关联

值得借鉴的是先验证评测器，再相信排行榜；还要把抓取、空间放置和旋转规划拆开看，否则可靠抓取可能掩盖空间执行短板。

### 下一步读哪里

先看[S20](https://arxiv.org/html/2610.36420v1#S3.SS6.p1.1)的分数汇总方式，再查[S23](https://arxiv.org/html/2610.36420v1#S5.SS0.SSS0.Px2.p1.1) [S24](https://arxiv.org/html/2610.36420v1#S5.SS0.SSS0.Px4.p1.1)的配对结果；接着核查自动成功阈值、智能体感知工具，以及[S33](https://arxiv.org/html/2610.36420v1#A4.T14)中代码规划和抓取委派的具体接口。

- **概念**：智能体 Agent 世界模型 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：43
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.36420v1
- 获取时间：2026-10-28T01:41:07.208804+00:00
- [S1] [SO-101 Bench: Accessible Spatial Manipulation · 正文段落 1](https://arxiv.org/html/2610.36420v1#p1.pic1.abstract1.1)
- [S2] [SO-101 Bench: Accessible Spatial Manipulation · 正文段落 2](https://arxiv.org/html/2610.36420v1#p1.pic1.1.4)
- [S3] [SO-101 Bench: Accessible Spatial Manipulation · 正文段落 3](https://arxiv.org/html/2610.36420v1#p1.pic1.1.5)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.36420v1#S1.F1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2610.36420v1#S1.p1.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2610.36420v1#S1.p2.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2610.36420v1#S1.p3.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2610.36420v1#S1.p4.1)
- [S9] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.36420v1#S1.I1.i1)
- [S10] [1 Introduction · 正文段落 11](https://arxiv.org/html/2610.36420v1#S1.I1.i2)
- [S11] [1 Introduction · 正文段落 12](https://arxiv.org/html/2610.36420v1#S1.I1.i3)
- [S12] [1 Introduction · 正文段落 13](https://arxiv.org/html/2610.36420v1#S1.I1.i4)
- [S13] [Low-cost hardware and SO-101 benchmarks. · 正文段落 14](https://arxiv.org/html/2610.36420v1#S2.SS0.SSS0.Px1.p1.1)
- [S14] [Real2sim evaluation and sim2real transfer. · 正文段落 15](https://arxiv.org/html/2610.36420v1#S2.SS0.SSS0.Px2.p1.1)
- [S15] [Manipulation benchmarks and evaluation practice. · 正文段落 17](https://arxiv.org/html/2610.36420v1#S2.SS0.SSS0.Px4.p1.1)
- [S16] [Manipulation benchmarks and evaluation practice. · 正文段落 18](https://arxiv.org/html/2610.36420v1#S2.F2)
- [S17] [3 SO-101 Bench · 正文段落 19](https://arxiv.org/html/2610.36420v1#S3.p1.1)
- [S18] [3.5 Training Data · 正文段落 36](https://arxiv.org/html/2610.36420v1#S3.SS5.p1.1)
- [S19] [3.6 Primary Evaluation · 正文段落 37](https://arxiv.org/html/2610.36420v1#S3.F4)
- [S20] [3.6 Primary Evaluation · 正文段落 38](https://arxiv.org/html/2610.36420v1#S3.SS6.p1.1)
- [S21] [4 Real-Only vs. Sim-Only Policy Correspondence · 正文段落 40](https://arxiv.org/html/2610.36420v1#S4.F5)
- [S22] [4 Real-Only vs. Sim-Only Policy Correspondence · 正文段落 41](https://arxiv.org/html/2610.36420v1#S4.p1.1)
- [S23] [Simulation preserves the policy ranking. · 正文段落 50](https://arxiv.org/html/2610.36420v1#S5.SS0.SSS0.Px2.p1.1)
- [S24] [Simulation is optimistic, by different amounts per policy. · 正文段落 52](https://arxiv.org/html/2610.36420v1#S5.SS0.SSS0.Px4.p1.1)
- [S25] [Training scale appears to drive performance. · 正文段落 57](https://arxiv.org/html/2610.36420v1#S6.SS0.SSS0.Px3.p1.1)
- [S26] [7 LLM Agents: Harness and Model Ablations · 正文段落 62](https://arxiv.org/html/2610.36420v1#S7.p1.1)
- [S27] [8 Conclusion · 正文段落 70](https://arxiv.org/html/2610.36420v1#S8.p1.1)
- [S28] [Appendix A GR00T Sim–Real Correspondence: Additional Results · 正文段落 73](https://arxiv.org/html/2610.36420v1#A1.T2)
- [S29] [Appendix A GR00T Sim–Real Correspondence: Additional Results · 正文段落 77](https://arxiv.org/html/2610.36420v1#A1.T4)
- [S30] [Appendix A GR00T Sim–Real Correspondence: Additional Results · 正文段落 79](https://arxiv.org/html/2610.36420v1#A1.F10)
- [S31] [Appendix A GR00T Sim–Real Correspondence: Additional Results · 正文段落 82](https://arxiv.org/html/2610.36420v1#A1.F13)
- [S32] [The agent on the real robot. · 正文段落 91](https://arxiv.org/html/2610.36420v1#A2.F15)
- [S33] [Appendix D LLM Agents: Additional Results · 正文段落 113](https://arxiv.org/html/2610.36420v1#A4.T14)
- [S34] [Appendix D LLM Agents: Additional Results · 正文段落 117](https://arxiv.org/html/2610.36420v1#A4.F21)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-28/SO-101 Bench Accessible Spatial Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Low-cost arms such as the SO-101 have become the most common entry point to robot learning, yet no released policy performs spatially constrained, language-conditioned tasks on them out of the box, and existing SO-101 benchmarks run only on physical hardware with simple tasks and few held-out objects. We introduce SO-101 Bench, a simulated benchmark for language-conditioned spatial manipulation built on an Isaac Lab digital twin of a real SO-101 setup. It has four tasks scored as five families, 138 objects in seen, unseen-instance and unseen-class splits, 916 evaluation episodes with subsets for held-out appearances, rotate-to-fit planning and occlusion memory, and 3,629 simulated demonstrations on which every learned policy is fine-tuned under an equal compute budget. The twin ranks policies as the real robot does: five policies trained without real data, four VLAs and an LLM agent, keep their exact ranking when the same weights run on the physical arm in an unseen environment with unseen objects (Spearman rho = 1.00, MMRV = 0.000), although simulation overestimates success. Across nine VLAs and world-action models, the best learned policies score near 61%, with spatial placement, unseen object classes and rotate-to-fit planning remaining open. An LLM agent that writes code and hands grasping to a learned policy scores 83.2%, and an ablation shows that this lead comes from the choice of harness and the choice of language model.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.36420v1
- Authors: Truman Hickok
- Published: 2026-10-27T00:02:28Z
- Age days: 1

</details>
