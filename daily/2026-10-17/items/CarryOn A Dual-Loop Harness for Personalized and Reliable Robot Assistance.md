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
url: "https://arxiv.org/abs/2610.21453v1"
published: "2026-10-15T07:54:39Z"
age_days: 1
score: 42
created: 2026-10-17
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> CarryOn 给冻结的 VLA 加了两层管理：一层记住用户偏好和场景变化，决定该做什么；另一层在动作落地前避碰、失败后修复，让原任务继续。

## 问题

“做个三明治”既要符合这个人的饮食习惯，也要在碰到障碍或抓取失败后继续。普通指令执行缺少跨对话的用户信息；仅靠安全微调也不能阻止危险接触。已有外围系统多关注陌生场景下的执行表现，本文要把用户条件下的任务选择和物理执行接起来。

### 用一个例子理解

理解用例（非论文实验）：用户说“帮我收好杯子”→系统取回“不放高处”的偏好并观察空架位→派发低层放置任务，绕开障碍；杯子滑落后先重新抓取，再继续原来的低层放置目标。

## 创新点或方法

旧做法让策略接指令后直接操作；本文先用用户记忆约束任务选择，再用可更新的场景记忆定位物体。运行时，几何过滤器预测夹爪和所持物体的运动，只放行可执行的动作前缀，首步受阻则短暂退让。视觉判断器决定继续、完成或恢复。跨次改进发生在离线恢复技能修订中，VLA 和几何过滤器保持固定；这不是在线重训策略。[S9](https://arxiv.org/html/2610.21453v1#S2.p3.1) [S13](https://arxiv.org/html/2610.21453v1#S3.SS1.p1.1) [S16](https://arxiv.org/html/2610.21453v1#S3.SS3.SSS1.p1.1)

### 方法如何工作

1. 把请求、用户记忆和场景记忆合起来，得到带依赖的子任务，避免选择违背偏好的通用方案。
2. 让冻结 VLA 生成动作块，再预测夹爪与所持物体的接触风险，过滤后才交给控制器。
3. 比较子任务开始时和近期图像，成功则推进计划，失败则调用恢复，保留同一个用户目标。
4. 回合结束后用失败记录修订恢复参数与策略，经格式和数值范围检查后保存新版本，供后续尝试使用。[S17](https://arxiv.org/html/2610.21453v1#S3.SS3.SSS3.p2.1)

### 必要术语

- Harness：围绕基础策略的运行管理系统；本文负责记忆、派发、检查和恢复。
- 几何过滤器：按空间距离约束拦截动作；本文同时检查夹爪和所持物体。
- 恢复技能：修复物理状态的控制程序；本文用它把任务交还给原 VLA。

## 证据

真机三明治实验中，直接指定偏好和跨对话记忆均派发正确子任务24/24，更新偏好后为20/24；这是规划准确性，不是整餐完成率。[S25](https://arxiv.org/html/2610.21453v1#S4.SS1.p2.1) LIBERO-Safety 共900回合，安全微调策略加过滤器后，违规率52.6%→6.1%，但无违规任务成功率仅25.3%→25.6%；主要收益是减少违规。[S29](https://arxiv.org/html/2610.21453v1#S4.SS2.p1.1) [S30](https://arxiv.org/html/2610.21453v1#S4.T3) [S31](https://arxiv.org/html/2610.21453v1#S4.T3.7) 真机避障无接触完成0/20→20/20。[S32](https://arxiv.org/html/2610.21453v1#S4.SS2.p4.1) 摘要另报恢复13%→80%，节选未给完整对应协议；不能与真机恢复3/20→18/20混为一组。[S24](https://arxiv.org/html/2610.21453v1#S4.T1.6.2)

## 局限

作者把长期适应、恢复经验跨任务迁移及保护与完成的平衡列为后续方向。[S34](https://arxiv.org/html/2610.21453v1#S5.p1.1) 我的待核查问题是恢复提升有多少来自技能修订、多少来自增加重试：真机 FULL 同时改变了高度参数和尝试次数，不能单独归因于反思。[S24](https://arxiv.org/html/2610.21453v1#S4.T1.6.2)

- **判断**：值得读到记忆修订、动作过滤和恢复协议细节；它最有说服力的是职责分工，数字则显示安全改善远大于任务完成改善。

## 研究关联

值得借鉴的是把两种经验分开保存：用户与场景知识改变下一次任务决策，失败经验改变恢复控制。这样可以改善辅助行为，而不必把所有记忆和纠错都塞进 VLA 权重。

### 下一步读哪里

先读[S13](https://arxiv.org/html/2610.21453v1#S3.SS1.p1.1) [S16](https://arxiv.org/html/2610.21453v1#S3.SS3.SSS1.p1.1)核查动作如何截断、障碍如何构造；再查恢复实验的失败筛选、重试预算和版本比较。部署条件还要看[S37](https://arxiv.org/html/2610.21453v1#A5.T8.5)：规划、判断和反思调用 API，不能把执行过滤器的速度视为整个系统延迟。

- **概念**：多模态基础模型 智能体 Agent 世界模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：42
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2610.21453v1
- 获取时间：2026-10-17T00:17:16.998207+00:00
- [S1] [CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance · 正文段落 1](https://arxiv.org/html/2610.21453v1#abstract1.1)
- [S2] [CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance · 正文段落 2](https://arxiv.org/html/2610.21453v1#S0.F1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2610.21453v1#S1.p1.1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2610.21453v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 9](https://arxiv.org/html/2610.21453v1#S1.p7.1)
- [S6] [1 Introduction · 正文段落 10](https://arxiv.org/html/2610.21453v1#S1.p8.1)
- [S7] [2 Related Work · 正文段落 11](https://arxiv.org/html/2610.21453v1#S2.p1.1)
- [S8] [2 Related Work · 正文段落 12](https://arxiv.org/html/2610.21453v1#S2.p2.1)
- [S9] [2 Related Work · 正文段落 13](https://arxiv.org/html/2610.21453v1#S2.p3.1)
- [S10] [2 Related Work · 正文段落 14](https://arxiv.org/html/2610.21453v1#S2.p4.1)
- [S11] [3 Method · 正文段落 15](https://arxiv.org/html/2610.21453v1#S3.p1.1)
- [S12] [3 Method · 正文段落 16](https://arxiv.org/html/2610.21453v1#S3.F2)
- [S13] [3.1 Overview of CarryOn · 正文段落 17](https://arxiv.org/html/2610.21453v1#S3.SS1.p1.1)
- [S14] [3.3 The Execution Loop: Proactive Protection and Reactive Recovery · 正文段落 22](https://arxiv.org/html/2610.21453v1#S3.SS3.p1.1)
- [S15] [3.3 The Execution Loop: Proactive Protection and Reactive Recovery · 正文段落 23](https://arxiv.org/html/2610.21453v1#S3.F3)
- [S16] [3.3.1 Proactive shielding within an episode · 正文段落 25](https://arxiv.org/html/2610.21453v1#S3.SS3.SSS1.p1.1)
- [S17] [3.3.3 Refining recovery skills across attempts · 正文段落 36](https://arxiv.org/html/2610.21453v1#S3.SS3.SSS3.p2.1)
- [S18] [4 Experiments · 正文段落 37](https://arxiv.org/html/2610.21453v1#S4.p1.1)
- [S19] [4 Experiments · 正文段落 38](https://arxiv.org/html/2610.21453v1#S4.F4)
- [S20] [4 Experiments · 正文段落 39](https://arxiv.org/html/2610.21453v1#S4.T1)
- [S21] [4 Experiments · 正文段落 40](https://arxiv.org/html/2610.21453v1#S4.T1.5.1)
- [S22] [4 Experiments · 正文段落 41](https://arxiv.org/html/2610.21453v1#S4.T1.5.2)
- [S23] [4 Experiments · 正文段落 42](https://arxiv.org/html/2610.21453v1#S4.T1.6.1)
- [S24] [4 Experiments · 正文段落 43](https://arxiv.org/html/2610.21453v1#S4.T1.6.2)
- [S25] [4.1 Personalization across Interactions and Scenes · 正文段落 45](https://arxiv.org/html/2610.21453v1#S4.SS1.p2.1)
- [S26] [4.1 Personalization across Interactions and Scenes · 正文段落 47](https://arxiv.org/html/2610.21453v1#S4.SS1.p3.1)
- [S27] [4.1 Personalization across Interactions and Scenes · 正文段落 48](https://arxiv.org/html/2610.21453v1#S4.SS1.p4.1)
- [S28] [4.1 Personalization across Interactions and Scenes · 正文段落 55](https://arxiv.org/html/2610.21453v1#S4.SS1.p6.1)
- [S29] [4.2 Safety during Execution · 正文段落 57](https://arxiv.org/html/2610.21453v1#S4.SS2.p1.1)
- [S30] [4.2 Safety during Execution · 正文段落 58](https://arxiv.org/html/2610.21453v1#S4.T3)
- [S31] [4.2 Safety during Execution · 正文段落 59](https://arxiv.org/html/2610.21453v1#S4.T3.7)
- [S32] [4.2 Safety during Execution · 正文段落 62](https://arxiv.org/html/2610.21453v1#S4.SS2.p4.1)
- [S33] [4.3 Recovery and Improvement from Failure Experience · 正文段落 64](https://arxiv.org/html/2610.21453v1#S4.SS3.p1.1)
- [S34] [5 Conclusion · 正文段落 79](https://arxiv.org/html/2610.21453v1#S5.p1.1)
- [S35] [Appendix E Experimental Configuration · 正文段落 110](https://arxiv.org/html/2610.21453v1#A5.p1.1)
- [S36] [Appendix E Experimental Configuration · 正文段落 111](https://arxiv.org/html/2610.21453v1#A5.T8)
- [S37] [Appendix E Experimental Configuration · 正文段落 112](https://arxiv.org/html/2610.21453v1#A5.T8.5)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-10-17/CarryOn A Dual-Loop Harness for Personalized and Reliable Robot Assistance.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

While generalist vision-language-action (VLA) models have enabled diverse open-world manipulation, real-world robotic assistance requires two critical capabilities they currently lack: personalization and reliable execution. First, executing an instruction like "make me a sandwich" requires grounding subtask decomposition in persistent user preferences rather than relying on a single generic solution. Second, reliable deployment demands explainable safety assurance that proactively prevents hazards and gracefully recovers from occasional physical failures. To address these gaps, we present CarryOn, a dual-loop harness designed to augment a frozen VLA policy. The planning loop maintains persistent user-level and scene-level context that is continually grounded against new observations and revised through interaction, enabling personalized task selection and execution grounding across conversations and changing scenes. The execution loop actively supervises policy rollouts, shielding actions from predicted hazardous contact. When execution fails, the system invokes reusable control-based recovery skills that restore task progress and are refined through reflection on earlier failures. On a real robot and in simulation, CarryOn dispatches preference-consistent subtasks across users and scenes, reduces the violation rate of an already safety-finetuned VLA from 52.6% to 6.1%, and increases recovery success from 13% to 80% when refined skills are reused.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2610.21453v1
- Authors: Zixuan Wang, Yuqi Liu, Yuxin Chen, Sengqiao Yang, Jinhui Ye, Pengguang Chen, Changsheng Lu, Shu Liu, Bei Yu, Jiaya Jia
- Published: 2026-10-15T07:54:39Z
- Age days: 1

</details>
