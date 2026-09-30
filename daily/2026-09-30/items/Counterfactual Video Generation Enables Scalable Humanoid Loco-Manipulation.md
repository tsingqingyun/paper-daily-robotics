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
url: "https://arxiv.org/abs/2609.38172v1"
published: "2026-09-29T17:59:45Z"
age_days: 0
score: 38
created: 2026-09-30
concepts: ["Sim2Real", "具身智能评测与基准"]
---

# Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> PRISM 把少量真人搬运视频生成不同物体的版本，再按手和物体的接触关系修正动作，拿去训练人形机器人。它证明生成视频可以帮助扩充搬运训练数据，最终在真机上搬起并运输了未见过的物体，但仍由人用摇杆给方向和放下指令。

## 问题

人形机器人要学搬东西，光看见一个人怎么动还不够，还得看清手碰在哪里、物体如何跟着移动。网上视频往往有遮挡、视角不合适，拿来还原可执行动作很困难；逐个拍摄不同形状物体的高质量示范，又很费人力。[S5](https://arxiv.org/html/2609.38172v1#S1.p2.1)

### 用一个例子理解

理解用例（非论文实验）：你只有一段人搬方箱子的视频，想让机器人也学会搬圆桶。先生成搬圆桶的版本，再检查双手接触点和桶的运动是否一致，把修正后的轨迹转到机器人身体上，最后在仿真里训练抓起与行走，不能把生成画面直接当作机器人控制命令。

## 创新点或方法

作者先拍少量清楚的真人示范，再让视频生成模型替换物体，同时调整人的动作。真正关键的是后半段：生成视频不一定符合物理，所以用接触关系把人与物体的运动约束在一起，修正三维重建，再转换成机器人身体能做的动作。训练时，仿真中的教师策略同时跟踪身体和物体，并奖励正确接触；之后把能力教给只依赖机载感知和摇杆指令的学生策略，上真机时无需重演参考动作或动作捕捉系统。[S7](https://arxiv.org/html/2609.38172v1#S1.p4.1)[S19](https://arxiv.org/html/2609.38172v1#S4.p1.1)[S25](https://arxiv.org/html/2609.38172v1#S4.SS2.p1.1)

### 方法如何工作

1. 从拍清楚的真实示范出发，生成物体形状、位置和搬法不同的视频，扩充行为变化，而不只是换贴图。[S13](https://arxiv.org/html/2609.38172v1#S3.SS1.p2.1)[S15](https://arxiv.org/html/2609.38172v1#S3.SS1.p3.1)
2. 恢复人和物体的三维运动，用手与物体保持接触这条约束相互纠错，减少遮挡导致的错误。[S16](https://arxiv.org/html/2609.38172v1#S3.SS2.SSS0.Px1.p1.1) [S17](https://arxiv.org/html/2609.38172v1#S3.SS2.SSS0.Px1.p2.1) [S18](https://arxiv.org/html/2609.38172v1#S3.SS2.SSS0.Px1.p2.2)
3. 把人体动作转换为机器人能执行的轨迹，保留接触位置和交互阶段，适应两种身体的差异。[S7](https://arxiv.org/html/2609.38172v1#S1.p4.1)[S14](https://arxiv.org/html/2609.38172v1#S3.F2)
4. 先训练能读到仿真完整状态的教师，再训练依靠机载感知和摇杆的学生，把示范变成能实际执行的策略。[S19](https://arxiv.org/html/2609.38172v1#S4.p1.1)[S25](https://arxiv.org/html/2609.38172v1#S4.SS2.p1.1)

### 必要术语

- 反事实视频：原来没发生、换一个物体后可能发生的互动；这里用它扩充搬法，而非预测真实未来。
- 接触锚点：手应该碰到物体的哪个位置；它把视频重建、动作转换和策略训练连起来。
- 动作重定向：把人的运动转换成另一副身体能完成的动作；不是照抄人的关节角度。
- 教师—学生训练：教师先借助仿真的完整信息学会，再把能力转给部署时信息更少的学生。

## 证据

数据扩充有一个需要看清的漏斗：4 条真实视频生成了 256 条视频，但最后得到的是 137 条可行轨迹和 129 条成功教师执行，不是所有生成视频都能直接变成训练数据。[S41](https://arxiv.org/html/2609.38172v1#S7.p3.1) 真机用 Unitree G1，每个物体试 5 次，抓起并稳定搬运至少 3 米才算成功；箱子是 15/15，球是 12/15，未见类别的物体也有成功记录。[S30](https://arxiv.org/html/2609.38172v1#S5.SS2.p1.1)[S34](https://arxiv.org/html/2609.38172v1#S5.T2.4.1) 仿真消融中，逐步加入接触相关修正后，域内成功率从 22.50% 到 96.25%，域外从 12.50% 到 72.92%。这些数据支持接触处理对这套系统有用；不能把仿真数字当作真机成绩。[S36](https://arxiv.org/html/2609.38172v1#S5.T3.4.1)

## 局限

目前仍需要视角稳定、遮挡较少的种子视频，重建与动作转换也是实际瓶颈；现有数据规模还不足以说明再生成十倍视频能换来多少收益。[S37](https://arxiv.org/html/2609.38172v1#S5.SS3.p2.1)[S41](https://arxiv.org/html/2609.38172v1#S7.p3.1) 真机由人操作摇杆，深度估计使用外接计算机，所以这不是全自主、全部计算都在机载端的搬运系统。[S30](https://arxiv.org/html/2609.38172v1#S5.SS2.p1.1) 仿真把物体当刚体，对折叠椅、软物体这类接触形状会变的对象可能失效。[S42](https://arxiv.org/html/2609.38172v1#S7.p5.1)

- **判断**：缺搬运数据时值得读，重点看接触约束如何修正生成错误。其效果依赖较清楚的种子视频，对柔性物体仍有明显限制。

## 研究关联

想用生成视频补机器人数据，关键要检查手接触哪里、物体怎样跟着动，不能只看视频是否逼真。这篇把接触约束一路用于重建、动作转换和训练，提供了一个把“看着合理”变成“可以学着做”的具体办法。

### 下一步读哪里

先看图 2，沿着接触信息如何贯穿整个流程读方法。[S14](https://arxiv.org/html/2609.38172v1#S3.F2) 再看表 3 的消融，确认收益来自哪里，而不是只看演示视频。[S35](https://arxiv.org/html/2609.38172v1#S5.T3) [S36](https://arxiv.org/html/2609.38172v1#S5.T3.4.1) 最后核查真机的成功定义、摇杆与外接计算机条件，以及从生成视频到成功示范的损耗。[S30](https://arxiv.org/html/2609.38172v1#S5.SS2.p1.1)[S41](https://arxiv.org/html/2609.38172v1#S7.p3.1)

- **概念**：Sim2Real 具身智能评测与基准
- **筛选分数**：38
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2609.38172v1
- 获取时间：2026-09-30T16:28:16.311318+00:00
- [S1] [Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation · 正文段落 1](https://arxiv.org/html/2609.38172v1#abstract1.1)
- [S2] [Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation · 正文段落 2](https://arxiv.org/html/2609.38172v1#S0.F1)
- [S3] [Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation · 正文段落 3](https://arxiv.org/html/2609.38172v1#p2.1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2609.38172v1#S1.p1.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2609.38172v1#S1.p2.1)
- [S6] [1 Introduction · 正文段落 6](https://arxiv.org/html/2609.38172v1#S1.p3.1)
- [S7] [1 Introduction · 正文段落 7](https://arxiv.org/html/2609.38172v1#S1.p4.1)
- [S8] [1 Introduction · 正文段落 8](https://arxiv.org/html/2609.38172v1#S1.p5.1)
- [S9] [2 Related Work · 正文段落 9](https://arxiv.org/html/2609.38172v1#S2.SS0.SSS0.Px1.p1.1)
- [S10] [2 Related Work · 正文段落 10](https://arxiv.org/html/2609.38172v1#S2.SS0.SSS0.Px2.p1.1)
- [S11] [2 Related Work · 正文段落 11](https://arxiv.org/html/2609.38172v1#S2.SS0.SSS0.Px3.p1.1)
- [S12] [3 Real-to-Sim Data Acquisition · 正文段落 12](https://arxiv.org/html/2609.38172v1#S3.p1.1)
- [S13] [3.1 Counterfactual Interaction Video Generation · 正文段落 14](https://arxiv.org/html/2609.38172v1#S3.SS1.p2.1)
- [S14] [3.1 Counterfactual Interaction Video Generation · 正文段落 15](https://arxiv.org/html/2609.38172v1#S3.F2)
- [S15] [3.1 Counterfactual Interaction Video Generation · 正文段落 16](https://arxiv.org/html/2609.38172v1#S3.SS1.p3.1)
- [S16] [3.2 Contact-Anchored Real-to-Sim · 正文段落 18](https://arxiv.org/html/2609.38172v1#S3.SS2.SSS0.Px1.p1.1)
- [S17] [3.2 Contact-Anchored Real-to-Sim · 正文段落 19](https://arxiv.org/html/2609.38172v1#S3.SS2.SSS0.Px1.p2.1)
- [S18] [3.2 Contact-Anchored Real-to-Sim · 正文段落 21](https://arxiv.org/html/2609.38172v1#S3.SS2.SSS0.Px1.p2.2)
- [S19] [4 Learning a Unified Visuomotor Interaction Policy · 正文段落 28](https://arxiv.org/html/2609.38172v1#S4.p1.1)
- [S20] [4.1 Training a Co-Tracking Teacher Policy · 正文段落 29](https://arxiv.org/html/2609.38172v1#S4.SS1.p1.1)
- [S21] [4.1 Training a Co-Tracking Teacher Policy · 正文段落 30](https://arxiv.org/html/2609.38172v1#S4.SS1.p2.1)
- [S22] [4.1 Training a Co-Tracking Teacher Policy · 正文段落 31](https://arxiv.org/html/2609.38172v1#S4.SS1.p3.1)
- [S23] [4.1 Training a Co-Tracking Teacher Policy · 正文段落 32](https://arxiv.org/html/2609.38172v1#S4.E2)
- [S24] [4.1 Training a Co-Tracking Teacher Policy · 正文段落 33](https://arxiv.org/html/2609.38172v1#S4.SS1.p3.2)
- [S25] [4.2 Distilling a Unified Depth-Based Student Policy · 正文段落 34](https://arxiv.org/html/2609.38172v1#S4.SS2.p1.1)
- [S26] [4.2 Distilling a Unified Depth-Based Student Policy · 正文段落 35](https://arxiv.org/html/2609.38172v1#S4.SS2.p2.1)
- [S27] [4.2 Distilling a Unified Depth-Based Student Policy · 正文段落 36](https://arxiv.org/html/2609.38172v1#S4.E3)
- [S28] [4.2 Distilling a Unified Depth-Based Student Policy · 正文段落 37](https://arxiv.org/html/2609.38172v1#S4.SS2.p2.2)
- [S29] [5 Results · 正文段落 43](https://arxiv.org/html/2609.38172v1#S5.p1.1)
- [S30] [5.2 Real-World Deployment · 正文段落 47](https://arxiv.org/html/2609.38172v1#S5.SS2.p1.1)
- [S31] [5.2 Real-World Deployment · 正文段落 48](https://arxiv.org/html/2609.38172v1#S5.SS2.p2.1)
- [S32] [5.3 Ablation Study · 正文段落 49](https://arxiv.org/html/2609.38172v1#S5.SS3.p1.1)
- [S33] [5.3 Ablation Study · 正文段落 50](https://arxiv.org/html/2609.38172v1#S5.T2)
- [S34] [5.3 Ablation Study · 正文段落 51](https://arxiv.org/html/2609.38172v1#S5.T2.4.1)
- [S35] [5.3 Ablation Study · 正文段落 52](https://arxiv.org/html/2609.38172v1#S5.T3)
- [S36] [5.3 Ablation Study · 正文段落 53](https://arxiv.org/html/2609.38172v1#S5.T3.4.1)
- [S37] [5.3 Ablation Study · 正文段落 54](https://arxiv.org/html/2609.38172v1#S5.SS3.p2.1)
- [S38] [5.3 Ablation Study · 正文段落 55](https://arxiv.org/html/2609.38172v1#S5.F4)
- [S39] [5.3 Ablation Study · 正文段落 56](https://arxiv.org/html/2609.38172v1#S5.F5)
- [S40] [6 Conclusion · 正文段落 57](https://arxiv.org/html/2609.38172v1#S6.p1.1)
- [S41] [7 Limitations and Future Work · 正文段落 60](https://arxiv.org/html/2609.38172v1#S7.p3.1)
- [S42] [7 Limitations and Future Work · 正文段落 62](https://arxiv.org/html/2609.38172v1#S7.p5.1)
- [S43] [Appendix B Real-World Test Objects · 正文段落 69](https://arxiv.org/html/2609.38172v1#A2.p1.1)
- [S44] [Appendix B Real-World Test Objects · 正文段落 70](https://arxiv.org/html/2609.38172v1#A2.F7.2)
- [S45] [Appendix B Real-World Test Objects · 正文段落 71](https://arxiv.org/html/2609.38172v1#A2.F7.3)
- [S46] [Appendix E Object Physics and Payload Sensitivity · 正文段落 92](https://arxiv.org/html/2609.38172v1#A5.T8)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-30/Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Teaching humanoids loco-manipulation skills, such as carrying diverse objects, via visual imitation is a promising path toward generalist robots. However, collecting diverse, high-quality interaction videos, such as clips that clearly show a person's full body and unoccluded interactions with objects, poses a practical barrier to scaling this approach. We propose PRISM, a real-to-sim-to-real framework that overcomes this limitation by amplifying a handful of real videos into a large, diverse training set. PRISM first generates hundreds of diverse "counterfactual" human-object interaction videos via video-to-video (V2V) generation from a few exemplar real videos. Our contact-anchored real-to-sim pipeline then reconstructs both human and object motions, retargeting this imperfect video data into physically plausible trajectories. The intra-class variability across these counterfactual videos lets us train a single policy that generalizes to unseen objects within each category. We demonstrate the full pipeline by deploying this policy on a real robot without any real-world fine-tuning. Using only onboard depth observations, our humanoid picks up, carries, and drops objects, including boxes, barrels, bins, and balls, across novel instances, sizes, and initial configurations.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.38172v1
- Authors: Zihan Wang, Zhen Wu, Pieter Abbeel, Rocky Duan, Jitendra Malik, Carmelo Sferrazza, C. Karen Liu, Guanya Shi, Angjoo Kanazawa
- Published: 2026-09-29T17:59:45Z
- Age days: 0

</details>
