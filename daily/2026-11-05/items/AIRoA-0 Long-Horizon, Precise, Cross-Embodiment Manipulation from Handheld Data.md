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
url: "https://arxiv.org/abs/2611.03815v1"
published: "2026-11-02T19:00:18Z"
age_days: 2
score: 40
created: 2026-11-05
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> AIRoA-0（A-0）让人拿着带相机的夹爪示范，再把学到的策略装到使用同款夹爪的机器人上。它用夹爪相对动作统一接口，再结合视觉筛选、任务阶段预测和连续动作解码，处理只有腕部视角的长任务。

## 问题

手持示范容易扩充，但没有机器人失败与恢复数据，两只腕部相机也看不到完整工作区。相似局部画面可能对应不同任务阶段，采集地点与部署地点还不同；直接模仿动作不足以解决进度歧义、背景变化和动作段衔接。

### 用一个例子理解

理解用例（非论文实验）：输入“把文具收进盒子”和两幅腕部画面；视觉门强调文具与盒口，阶段头结合近期动作判断正在放置，动作专家输出夹爪目标；下一次观测修正缓冲中的后续动作，最终闭环完成收纳。

## 创新点或方法

沿用 π₀.₅ 骨干，但用夹爪相对轨迹取代依赖机器人关节或基座的表示。预训练用任务/子任务语言，并限制视觉门的平均权重，让动作损失教它保留有关区域。后训练增加阶段预测和近期实测状态记忆；阶段以文字条件引导动作。推理平滑阶段预测，并让动作缓冲区随新观测逐次去噪，避免每段独立重生成。预训练的子任务预测仅作辅助损失，不应混同部署阶段头。[S23](https://arxiv.org/html/2611.03815v1#S4.SS1.p1.1) [S24](https://arxiv.org/html/2611.03815v1#S4.SS1.p2.1) [S25](https://arxiv.org/html/2611.03815v1#S4.SS2.p2.1) [S26](https://arxiv.org/html/2611.03815v1#S4.SS3.p1.1) [S27](https://arxiv.org/html/2611.03815v1#S4.SS4.p1.1) [S28](https://arxiv.org/html/2611.03815v1#S4.SS4.p1.3) [S29](https://arxiv.org/html/2611.03815v1#S4.SS5.p1.1) [S35](https://arxiv.org/html/2611.03815v1#S5.p1.1) [S36](https://arxiv.org/html/2611.03815v1#S5.SS1.p1.1) [S37](https://arxiv.org/html/2611.03815v1#S5.T3) [S38](https://arxiv.org/html/2611.03815v1#S5.SS1.p2.1) [S39](https://arxiv.org/html/2611.03815v1#S5.SS2.p2.1) [S40](https://arxiv.org/html/2611.03815v1#S5.SS3.p1.1) [S41](https://arxiv.org/html/2611.03815v1#S5.E4) [S42](https://arxiv.org/html/2611.03815v1#S5.SS3.p1.2) [S43](https://arxiv.org/html/2611.03815v1#S5.SS4.p1.1) [S44](https://arxiv.org/html/2611.03815v1#S5.T4) [S45](https://arxiv.org/html/2611.03815v1#S5.T4.4) [S46](https://arxiv.org/html/2611.03815v1#S6.p1.1) [S47](https://arxiv.org/html/2611.03815v1#S6.SS2.p1.1)

### 方法如何工作

1. 用同款手持夹爪采集双腕画面、夹爪状态和分层语言，使人手与机器人共享观测动作接口。
2. 预训练视觉门及动作模型，借预算约束减少无关视觉信息，并学习子任务相关表征。
3. 后训练加入阶段头和近期状态记忆，消解局部画面的进度歧义。
4. 部署时平滑阶段并持续更新动作缓冲，让新观测参与尚未执行动作的修正。

### 必要术语

- 锚定动作：每个未来目标相对共同参照定义；避免逐步增量在动作段内累积误差。
- 视觉证据预算：限制视觉门的平均保留权重；促使模型选择任务有关信息。
- 流式解码：动作段在多次新观测中继续细化；本文用它衔接连续动作。

## 证据

作者采集16,151小时手持数据 [S3](https://arxiv.org/html/2611.03815v1#S1.p1.1)。未见采集地点的 Franka 十任务评估，每任务15次，含部分完成计分，平均78%；四个同任务后训练的 VLA 为14%—27% [S10](https://arxiv.org/html/2611.03815v1#S2.SS1.p1.1) [S11](https://arxiv.org/html/2611.03815v1#S2.SS1.p2.1) [S12](https://arxiv.org/html/2611.03815v1#S2.T1)。同任务权重还在 TX-G2、OpenArm、UR 上展示部分任务，但节选未给各平台成功率 [S14](https://arxiv.org/html/2611.03815v1#S2.SS3.p1.1) [S15](https://arxiv.org/html/2611.03815v1#S2.SS3.p2.1)。数据扩展实验支持更多手持数据降低留出动作损失 [S30](https://arxiv.org/html/2611.03815v1#S4.SS6.p1.1) [S31](https://arxiv.org/html/2611.03815v1#S4.F9) [S32](https://arxiv.org/html/2611.03815v1#S4.F10) [S33](https://arxiv.org/html/2611.03815v1#S4.SS6.p2.1) [S34](https://arxiv.org/html/2611.03815v1#S4.SS6.p3.1)，不能直接换算成机器人成功率增幅。

## 局限

“没有采集机器人数据”描述的是 A-0 自身数据流程；模型初始化于公共 π₀.₅ 权重，不能据此声称全部先验从未接触机器人数据 [S23](https://arxiv.org/html/2611.03815v1#S4.SS1.p1.1)。跨机身也以安装同款夹爪和相机为条件。尚需核查模块消融及严格全任务完成率，78%包含部分计分。

- **判断**：值得按数据接口、阶段建模、推理解码三层细读；它展示了完整手持学习路线，但不能简化成任意人类视频可直接驱动任意机器人。

## 研究关联

跨机器人迁移可以先通过统一末端、相机和动作定义，减少数据本身对机身的依赖。长任务则值得显式表达“现在做到哪一步”，避免把所有进度判断都留给动作分布隐式解决。

### 下一步读哪里

先核查 [S25](https://arxiv.org/html/2611.03815v1#S4.SS2.p2.1) 相对动作的精确定义和控制器适配条件，再看 [S38](https://arxiv.org/html/2611.03815v1#S5.SS1.p2.1) [S39](https://arxiv.org/html/2611.03815v1#S5.SS2.p2.1) [S40](https://arxiv.org/html/2611.03815v1#S5.SS3.p1.1) [S41](https://arxiv.org/html/2611.03815v1#S5.E4) [S42](https://arxiv.org/html/2611.03815v1#S5.SS3.p1.2) [S43](https://arxiv.org/html/2611.03815v1#S5.SS4.p1.1) [S44](https://arxiv.org/html/2611.03815v1#S5.T4) [S45](https://arxiv.org/html/2611.03815v1#S5.T4.4) [S46](https://arxiv.org/html/2611.03815v1#S6.p1.1) [S47](https://arxiv.org/html/2611.03815v1#S6.SS2.p1.1) 阶段误判与动作连续性的处理；非均匀噪声安排的完整规则、各模块消融和部分计分细则仍需进一步检查。

- **概念**：多模态基础模型 智能体 Agent 视觉语言动作模型 VLA 机器人学习 具身智能评测与基准
- **筛选分数**：40
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.03815v1
- 获取时间：2026-11-05T00:11:40.813132+00:00
- [S1] [正文 · 正文段落 1](https://arxiv.org/html/2611.03815v1#p1.1)
- [S2] [1. Introduction · 正文段落 2](https://arxiv.org/html/2611.03815v1#S1.F1)
- [S3] [1. Introduction · 正文段落 3](https://arxiv.org/html/2611.03815v1#S1.p1.1)
- [S4] [1. Introduction · 正文段落 4](https://arxiv.org/html/2611.03815v1#S1.p2.1)
- [S5] [1. Introduction · 正文段落 5](https://arxiv.org/html/2611.03815v1#S1.p3.1)
- [S6] [1. Introduction · 正文段落 6](https://arxiv.org/html/2611.03815v1#S1.p4.1)
- [S7] [1. Introduction · 正文段落 7](https://arxiv.org/html/2611.03815v1#S1.p5.1)
- [S8] [1. Introduction · 正文段落 10](https://arxiv.org/html/2611.03815v1#S1.I1.i2)
- [S9] [1. Introduction · 正文段落 11](https://arxiv.org/html/2611.03815v1#S1.I1.i3)
- [S10] [2.1. Ten tasks · 正文段落 13](https://arxiv.org/html/2611.03815v1#S2.SS1.p1.1)
- [S11] [2.1. Ten tasks · 正文段落 15](https://arxiv.org/html/2611.03815v1#S2.SS1.p2.1)
- [S12] [2.1. Ten tasks · 正文段落 16](https://arxiv.org/html/2611.03815v1#S2.T1)
- [S13] [2.2. A changing scene · 正文段落 20](https://arxiv.org/html/2611.03815v1#S2.SS2.p1.1)
- [S14] [2.3. Other robots · 正文段落 22](https://arxiv.org/html/2611.03815v1#S2.SS3.p1.1)
- [S15] [2.3. Other robots · 正文段落 23](https://arxiv.org/html/2611.03815v1#S2.SS3.p2.1)
- [S16] [3. Data · 正文段落 26](https://arxiv.org/html/2611.03815v1#S3.F6)
- [S17] [3.2. The corpus · 正文段落 28](https://arxiv.org/html/2611.03815v1#S3.SS2.p1.1)
- [S18] [3.2. The corpus · 正文段落 29](https://arxiv.org/html/2611.03815v1#S3.SS2.p2.1)
- [S19] [3.2. The corpus · 正文段落 30](https://arxiv.org/html/2611.03815v1#S3.SS2.p3.1)
- [S20] [3.2. The corpus · 正文段落 32](https://arxiv.org/html/2611.03815v1#S3.T2.4)
- [S21] [4. Pre-training · 正文段落 33](https://arxiv.org/html/2611.03815v1#S4.p1.1)
- [S22] [4. Pre-training · 正文段落 34](https://arxiv.org/html/2611.03815v1#S4.F7)
- [S23] [4.1. Model · 正文段落 35](https://arxiv.org/html/2611.03815v1#S4.SS1.p1.1)
- [S24] [4.1. Model · 正文段落 36](https://arxiv.org/html/2611.03815v1#S4.SS1.p2.1)
- [S25] [4.2. Anchored actions · 正文段落 40](https://arxiv.org/html/2611.03815v1#S4.SS2.p2.1)
- [S26] [4.3. Language at two levels · 正文段落 41](https://arxiv.org/html/2611.03815v1#S4.SS3.p1.1)
- [S27] [4.4. Visual evidence budget · 正文段落 42](https://arxiv.org/html/2611.03815v1#S4.SS4.p1.1)
- [S28] [4.4. Visual evidence budget · 正文段落 46](https://arxiv.org/html/2611.03815v1#S4.SS4.p1.3)
- [S29] [4.5. Subtask auxiliary loss · 正文段落 49](https://arxiv.org/html/2611.03815v1#S4.SS5.p1.1)
- [S30] [4.6. Scaling with pre-training data · 正文段落 50](https://arxiv.org/html/2611.03815v1#S4.SS6.p1.1)
- [S31] [4.6. Scaling with pre-training data · 正文段落 51](https://arxiv.org/html/2611.03815v1#S4.F9)
- [S32] [4.6. Scaling with pre-training data · 正文段落 52](https://arxiv.org/html/2611.03815v1#S4.F10)
- [S33] [4.6. Scaling with pre-training data · 正文段落 53](https://arxiv.org/html/2611.03815v1#S4.SS6.p2.1)
- [S34] [4.6. Scaling with pre-training data · 正文段落 54](https://arxiv.org/html/2611.03815v1#S4.SS6.p3.1)
- [S35] [5. Post-training · 正文段落 55](https://arxiv.org/html/2611.03815v1#S5.p1.1)
- [S36] [5.1. Stage prediction · 正文段落 56](https://arxiv.org/html/2611.03815v1#S5.SS1.p1.1)
- [S37] [5.1. Stage prediction · 正文段落 57](https://arxiv.org/html/2611.03815v1#S5.T3)
- [S38] [5.1. Stage prediction · 正文段落 59](https://arxiv.org/html/2611.03815v1#S5.SS1.p2.1)
- [S39] [5.2. Proprioceptive memory · 正文段落 61](https://arxiv.org/html/2611.03815v1#S5.SS2.p2.1)
- [S40] [5.3. Visual evidence budget in post-training · 正文段落 62](https://arxiv.org/html/2611.03815v1#S5.SS3.p1.1)
- [S41] [5.3. Visual evidence budget in post-training · 正文段落 63](https://arxiv.org/html/2611.03815v1#S5.E4)
- [S42] [5.3. Visual evidence budget in post-training · 正文段落 64](https://arxiv.org/html/2611.03815v1#S5.SS3.p1.2)
- [S43] [5.4. Objective and recipe · 正文段落 65](https://arxiv.org/html/2611.03815v1#S5.SS4.p1.1)
- [S44] [5.4. Objective and recipe · 正文段落 68](https://arxiv.org/html/2611.03815v1#S5.T4)
- [S45] [5.4. Objective and recipe · 正文段落 69](https://arxiv.org/html/2611.03815v1#S5.T4.4)
- [S46] [6. Inference Harness · 正文段落 70](https://arxiv.org/html/2611.03815v1#S6.p1.1)
- [S47] [6.2. Non-uniform streaming decoding · 正文段落 72](https://arxiv.org/html/2611.03815v1#S6.SS2.p1.1)
- [S48] [6.2. Non-uniform streaming decoding · 正文段落 76](https://arxiv.org/html/2611.03815v1#S6.SS2.p4.1)
- [S49] [8. Conclusion · 正文段落 85](https://arxiv.org/html/2611.03815v1#S8.p1.1)
- [S50] [Appendix A Post-training Loss by Task Set · 正文段落 92](https://arxiv.org/html/2611.03815v1#A1.p1.1)
- [S51] [Appendix A Post-training Loss by Task Set · 正文段落 93](https://arxiv.org/html/2611.03815v1#A1.F12)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-05/AIRoA-0 Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

AIRoA-0 (A-0) is a bimanual manipulation system learned from 16,151 hours of handheld demonstrations, with no robot data collected at any stage. The demonstrations are recorded with YUBI, our open-source handheld gripper, which lets people record manipulation data anywhere with no robot present. From a single instruction, A-0 sorts more than a dozen small parts into their numbered cells and changes the mop pads and brush of a robot vacuum; among other tasks, it unzips a pencil case and folds a towel. It performs these tasks using only a camera on each wrist, with no head or scene camera, at a site where none of its training data was recorded. Across the ten tasks of our evaluation, it averages a success rate of 78%, against 27% for the strongest of four other vision-language-action models post-trained on the same task demonstrations. We collect no teleoperation data and use no reinforcement learning or on-robot corrections, and the robot appears only at test time. The system learns which regions of each wrist view matter for the task, predicts the stage the task has reached, and decodes actions as a continuous stream. A-0 is embodiment-agnostic: it runs on robots that mount the YUBI gripper, such as a bimanual Franka, TX-G2, OpenArm and UR. We are releasing the dataset, to our knowledge the largest open dataset of handheld-gripper demonstrations with task and subtask instructions, together with the pre-trained weights and the post-training recipe. Videos of A-0 on every task are on the project page, https://a-0.airoa.io. Anyone can build the gripper, record a task of their own and post-train the model on it in under four hours on a single node of eight H200 GPUs.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.03815v1
- Authors: Yueh-Hua Wu, Kei Ota, Hanlong Li, Hayata Yuasa, Jason Wang, Kengo Ikeuchi, Kensuke Chiyoma, Makoto Sugiura, Masafumi Takahashi, Masatoshi Tateno, Naoaki Kanazawa, Nicola Scianca, Petr Khrapchenkov, Satoshi Otsubo, Takehiko Ohkawa, Takuya Okubo, Tatsuya Matsushima, Yuki Noguchi, Yuma Shin, Zixuan Zhong
- Published: 2026-11-02T19:00:18Z
- Age days: 2

</details>
