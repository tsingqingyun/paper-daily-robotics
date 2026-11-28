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
url: "https://arxiv.org/abs/2611.34509v1"
published: "2026-11-25T14:58:31Z"
age_days: 2
score: 26
created: 2026-11-28
concepts: ["智能体 Agent", "世界模型"]
---

# Long-Horizon Planning with Latent World Models via Graph Anchors

> [!summary] 这篇论文到底做了什么（基于摘要与正文节选）
> Graph Anchors 把远处的目标图片拆成沿历史轨迹可逐步追踪的近目标。它用已有画面建图找路线，再让冻结的世界模型带着控制器一段一段走。

## 问题

视觉规划器常按预测画面与目标图的编码距离给动作打分。但在迷宫里，朝目标所在方向走可能撞墙，绕出去的第一步反而让画面离目标更远。在推物体时，距离还可能偏重机械臂的位置，于是推杆到位了，物块还留在原地。两种错误都使规划器把错误的下一步排在前面。[S2](https://arxiv.org/html/2611.34509v1#S1.p1.1)[S4](https://arxiv.org/html/2611.34509v1#S1.p2.1)

### 用一个例子理解

理解用例（非论文实验）。输入迷宫当前画面和隔墙另一侧的终点图。图搜索先找到经过门洞的历史路线，控制器以门前画面为近目标并输出几步动作。新观测显示已经过门后，控制器转向走廊下一处锚点，最后抵达终点。

## 创新点或方法

作者先用记录数据检验距离排序，看距离更小的候选是否真的推进了任务。Graph Anchors 使用既有世界模型的训练帧一次性建稀疏图，保留真实相邻转移，并允许在接近的记录之间连边。推理时沿通向目标的最短路挑一个前方近节点，让原模型预测候选动作序列。规划按途中最接近锚点的时刻给序列打分，所以路径经过锚点也能得到信用。接触任务提高跨轨迹跳转的代价，降低在持续推动中间突然换到另一段录像的机会。建图和换目标无需额外训练。[S5](https://arxiv.org/html/2611.34509v1#S1.p3.1)[S6](https://arxiv.org/html/2611.34509v1#S1.I1.i2)[S12](https://arxiv.org/html/2611.34509v1#S3.SS0.SSS0.Px2.p1.2)[S13](https://arxiv.org/html/2611.34509v1#S3.SS0.SSS0.Px3.p1.2)[S27](https://arxiv.org/html/2611.34509v1#S6.p1.1)

### 方法如何工作

1. 从记录帧建立稀疏图，保留真实连贯动作对应的时间边，让路线能利用曾经走通的转移。
2. 按起点和目标找图路线，从前方取近锚点，把搜索目标放在局部控制器够得着的范围。
3. 用世界模型预演动作，按途中离锚点最近的程度评分，允许计划越过锚点。
4. 执行动作并读回新画面，重新确定进度和下一锚点，逐段完成长目标。

### 必要术语

- 潜在目标距离：两个画面编码后的差异；在本文中给预演动作后的状态打分。
- 图锚点：从记录路线前方取出的近目标帧；把远目标变成局部控制可以处理的小段。
- 跨片段边：连接不同记录轨迹的边；可拼出新路线，但接触任务会提高这类跳转的代价。

## 证据

仿真长目标表中，同一组起终点上，Graph Anchors 将 LeWM 的成功率从 13% 提至 85%（PointMaze-Medium，200 步），从 8% 提至 87%（PointMaze-Large，400 步），以及从 5% 提至 71%（Push-T，150 步，接触设置）。只给远目标加途中最近评分时，三项分别为 12%、26%、9% [S14](https://arxiv.org/html/2611.34509v1#S5.p1.1)–[S16](https://arxiv.org/html/2611.34509v1#S5.T1.10)。这支持近锚点在这些环境中的作用。同期对照也有局部强项，例如 NGC 在中型迷宫 200 步达到 100% [S23](https://arxiv.org/html/2611.34509v1#S5.T3.6.1)。

## 局限

作者明确指出，历史轨迹得覆盖可行路线，局部模型也得能完成那一小段动作。模型漏掉初次接触时，图无法补出精细抓取。Meta-World 的示范中间帧测试是理想动力学条件下的上界 [S28](https://arxiv.org/html/2611.34509v1#S6.SS0.SSS0.Px1.p1.1)。仿真中的结果对真机接触能否保持有效，仍需核查。

- **判断**：值得细读排序诊断和目标选择消融，这两处能帮助判断瓶颈出在动作预测、搜索强度，还是目标评分本身。

## 研究关联

如果世界模型能稳定做好短程控制，先用已有轨迹测目标距离会不会给候选动作排错序。若问题集中在远距离或接触阶段，可以先改目标的选法，再决定是否值得投入更多搜索或重训预测器。

### 下一步读哪里

从 [S30](https://arxiv.org/html/2611.34509v1#A1.T2) 看沿记录轨迹向前、向后各一步的排序检查。再查 [S33](https://arxiv.org/html/2611.34509v1#A3.T9) 所指的表 A9，核对只换目标与只换搜索规则分别产生多大增益，并用 [S22](https://arxiv.org/html/2611.34509v1#S5.T3)[S23](https://arxiv.org/html/2611.34509v1#S5.T3.6.1)[S28](https://arxiv.org/html/2611.34509v1#S6.SS0.SSS0.Px1.p1.1) 检查接触设置在跨片段迷宫上的代价。

- **概念**：智能体 Agent 世界模型
- **筛选分数**：26
- **阅读状态**：摘要与正文节选讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


<details>
<summary>正文依据索引（节选，非完整精读）</summary>

- 来源：https://arxiv.org/html/2611.34509v1
- 获取时间：2026-11-28T03:58:18.570922+00:00
- [S1] [Long-Horizon Planning with Latent World Models via Graph Anchors · 正文段落 1](https://arxiv.org/html/2611.34509v1#abstract1.1)
- [S2] [1 Introduction · 正文段落 2](https://arxiv.org/html/2611.34509v1#S1.p1.1)
- [S3] [1 Introduction · 正文段落 3](https://arxiv.org/html/2611.34509v1#S1.F1)
- [S4] [1 Introduction · 正文段落 4](https://arxiv.org/html/2611.34509v1#S1.p2.1)
- [S5] [1 Introduction · 正文段落 5](https://arxiv.org/html/2611.34509v1#S1.p3.1)
- [S6] [1 Introduction · 正文段落 8](https://arxiv.org/html/2611.34509v1#S1.I1.i2)
- [S7] [1 Introduction · 正文段落 9](https://arxiv.org/html/2611.34509v1#S1.I1.i3)
- [S8] [Latent world models and their goal costs. · 正文段落 10](https://arxiv.org/html/2611.34509v1#S2.SS0.SSS0.Px1.p1.1)
- [S9] [Subgoals for latent planners. · 正文段落 11](https://arxiv.org/html/2611.34509v1#S2.SS0.SSS0.Px2.p1.1)
- [S10] [Graphs of experience. · 正文段落 12](https://arxiv.org/html/2611.34509v1#S2.SS0.SSS0.Px3.p1.1)
- [S11] [Problem setting. · 正文段落 13](https://arxiv.org/html/2611.34509v1#S3.SS0.SSS0.Px1.p1.1)
- [S12] [Latent world model. · 正文段落 16](https://arxiv.org/html/2611.34509v1#S3.SS0.SSS0.Px2.p1.2)
- [S13] [Latent planning. · 正文段落 19](https://arxiv.org/html/2611.34509v1#S3.SS0.SSS0.Px3.p1.2)
- [S14] [5 Experiments · 正文段落 51](https://arxiv.org/html/2611.34509v1#S5.p1.1)
- [S15] [5 Experiments · 正文段落 52](https://arxiv.org/html/2611.34509v1#S5.T1)
- [S16] [5 Experiments · 正文段落 53](https://arxiv.org/html/2611.34509v1#S5.T1.10)
- [S17] [5 Experiments · 正文段落 54](https://arxiv.org/html/2611.34509v1#S5.F5)
- [S18] [5 Experiments · 正文段落 55](https://arxiv.org/html/2611.34509v1#S5.F6)
- [S19] [5.5 Diagnosing Training-Free World-Model Planners (AP, NGC, Metro-WM) · 正文段落 66](https://arxiv.org/html/2611.34509v1#S5.SS5.p1.1)
- [S20] [5.5 Diagnosing Training-Free World-Model Planners (AP, NGC, Metro-WM) · 正文段落 67](https://arxiv.org/html/2611.34509v1#S5.T2)
- [S21] [5.5 Diagnosing Training-Free World-Model Planners (AP, NGC, Metro-WM) · 正文段落 68](https://arxiv.org/html/2611.34509v1#S5.T2.4.1)
- [S22] [5.5 Diagnosing Training-Free World-Model Planners (AP, NGC, Metro-WM) · 正文段落 69](https://arxiv.org/html/2611.34509v1#S5.T3)
- [S23] [5.5 Diagnosing Training-Free World-Model Planners (AP, NGC, Metro-WM) · 正文段落 70](https://arxiv.org/html/2611.34509v1#S5.T3.6.1)
- [S24] [5.5 Diagnosing Training-Free World-Model Planners (AP, NGC, Metro-WM) · 正文段落 71](https://arxiv.org/html/2611.34509v1#S5.F10)
- [S25] [5.5 Diagnosing Training-Free World-Model Planners (AP, NGC, Metro-WM) · 正文段落 72](https://arxiv.org/html/2611.34509v1#S5.F11)
- [S26] [5.5 Diagnosing Training-Free World-Model Planners (AP, NGC, Metro-WM) · 正文段落 73](https://arxiv.org/html/2611.34509v1#S5.SS5.p2.1)
- [S27] [6 Conclusion · 正文段落 81](https://arxiv.org/html/2611.34509v1#S6.p1.1)
- [S28] [Limitations. · 正文段落 82](https://arxiv.org/html/2611.34509v1#S6.SS0.SSS0.Px1.p1.1)
- [S29] [Training longer does not extend range. · 正文段落 96](https://arxiv.org/html/2611.34509v1#A1.SS1.SSS0.Px3.p1.1)
- [S30] [Training longer does not extend range. · 正文段落 97](https://arxiv.org/html/2611.34509v1#A1.T2)
- [S31] [Evaluation setup and checkpoints. · 正文段落 146](https://arxiv.org/html/2611.34509v1#A2.SS2.SSS0.Px1.p1.1)
- [S32] [C.3 Ablations, Scaling, and Robustness Stress Tests · 正文段落 167](https://arxiv.org/html/2611.34509v1#A3.F13)
- [S33] [C.3 Ablations, Scaling, and Robustness Stress Tests · 正文段落 168](https://arxiv.org/html/2611.34509v1#A3.T9)
- [S34] [C.3 Ablations, Scaling, and Robustness Stress Tests · 正文段落 169](https://arxiv.org/html/2611.34509v1#A3.T9.4.1)
- [S35] [C.3 Ablations, Scaling, and Robustness Stress Tests · 正文段落 171](https://arxiv.org/html/2611.34509v1#A3.T9.5.1)
- [S36] [C.3 Ablations, Scaling, and Robustness Stress Tests · 正文段落 174](https://arxiv.org/html/2611.34509v1#A3.T10.4.1)
- [S37] [C.3 Ablations, Scaling, and Robustness Stress Tests · 正文段落 176](https://arxiv.org/html/2611.34509v1#A3.T10.5.1)
- [S38] [World-model and offline-policy baselines. · 正文段落 190](https://arxiv.org/html/2611.34509v1#A4.T13.4.1)

</details>

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-28/Long-Horizon Planning with Latent World Models via Graph Anchors.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Latent world models plan in a compact latent space by predicting the outcomes of actions. Their planners judge a plan by the latent distance between its predicted end state and the goal image. We show that this distance fails in two distinct ways. First, it loses directional signal a few steps from the goal, causing distant goals to fail. Second, it weighs the robot arm over the manipulated object, causing manipulation to fail at contact. We measure both failures directly on recorded data by asking whether a lower latent distance corresponds to true progress toward the goal. Across five environments, six visual representations (including raw pixels and V-JEPA 2), and nine Meta-World tasks, this ranking test cleanly separates the two failures, and the graph distance to a goal predicts where closed-loop planning breaks down. Both failures share a single remedy: replacing the distant goal with a nearby target that lies on a recorded trajectory. We realize this principle with Graph Anchors, a training-free planner for frozen latent world models. It builds a sparse graph once over the model's own training frames and aims each planning step at a node a few moves ahead along the shortest path to the goal, keeping paths on recorded transitions wherever contact matters. On goals up to 400 steps away, Graph Anchors raise LeWM's success from 13% to 85% on PointMaze-Medium, from 8% to 87% on PointMaze-Large, and from 5% to 71% on Push-T, where stronger search toward the goal fails and where prior training-free planners break down under missing step horizons, subsampling shortcuts, or fragmented contact.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.34509v1
- Authors: Syed Nazmus Sakib, Abdul Monaf Chowdhury, Peizhen Li, Nafiul Haque, Chandak Chakma, Md Mehedi Hasan, Zehong Cao, Shifat E. Arman
- Published: 2026-11-25T14:58:31Z
- Age days: 2

</details>
