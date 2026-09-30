---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.08159v1"
published: "2026-09-08T02:43:48Z"
age_days: 1
score: 28
created: 2026-09-09
concepts: ["智能体 Agent", "具身智能评测与基准"]
---

# OmniNav: Robust Long-Horizon Target Navigation in Dynamic Environments

> [!summary] 先说人话（基于摘要）
> OmniNav持续检查地图是否过时、目标可能在哪里，以及到达位置是否方便实际操作。它把找不到目标和执行失败也作为证据，用来修正下一步搜索与导航。

## 这篇到底在做什么

- **卡在哪里**：长任务中物体会移动或消失，搜索失败会改变目标位置概率，而几何上可达的终点未必支持抓取；这些状态若不更新，错误会向后续决策传播。
- **关键解法**：联合推断场景有效性、目标信念和交互可行性：维护可更新三维对象记忆，以贝叶斯信念修正吸收语义先验及负搜索证据，并按操作可达性和碰撞约束选终点，通过分层闭环处理执行反馈。
- **拿什么证明**：摘要称语义ObjectNav及细粒度实例导航成功率在比较方法中最高，对目标重定位保持鲁棒；真实抓放成功率由适配后的开环基线53.3%提升至71.7%。

## 值不值得读

- **和你的研究有什么关系**：对具身Agent最直接的价值是把导航终点与后续操作联系起来，并给记忆失效和负证据提供明确处理机制。
- **先别急着信**：真实抓放提升来自整套闭环系统对开环基线的比较，各状态模块分别贡献多少，需要核查消融。
- **判断**：移动操作与长期Agent方向值得精读，18.4个百分点的真实任务提升值得追查具体来源。

## 研究关联

- **概念**：[[智能体 Agent]] [[具身智能评测与基准]]
- **筛选分数**：28
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-09/OmniNav Robust Long-Horizon Target Navigation in Dynamic Environments.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Long-horizon target navigation requires a robot to sustain task execution across evolving observations, decisions, and physical interactions. This requires three coupled capabilities: maintaining valid scene memory, revising target beliefs under partial observability, and selecting interaction-feasible navigation endpoints. However, the state underlying each capability is only conditionally valid: scene representations become stale when objects move or disappear, unsuccessful searches alter beliefs over target locations, and geometrically convenient endpoints may still be infeasible for manipulation. To address these challenges, we present OmniNav, which formulates long-horizon navigation as continual inference over a factorized task state posterior coupling scene validity, target belief, and interaction feasibility. For representation, OmniNav incrementally constructs an updatable 3D object scene memory, preventing stale scene evidence from propagating to subsequent decisions. For exploration, it introduces an evidence-aware Bayesian belief-revision mechanism that derives dependency-aware region priors from semantic context, incorporates unsuccessful searches as negative evidence, and updates them for posterior-guided frontier selection. For interaction, OmniNav incorporates manipulation reachability and collision constraints into navigation-endpoint selection and propagates execution feedback through hierarchical closed-loop recovery. Extensive experiments demonstrate that OmniNav achieves the highest success rates among the compared methods on semantic ObjectNav and fine-grained instance navigation benchmarks, remains robust to target relocation, and improves real-world pick-and-place success from 53.3% to 71.7% over an adapted open-loop baseline. The project page of OmniNav is available at https://omni-nav.github.io/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.08159v1
- Authors: Yujie Tang, Meiling Wang, Jinhao Jiang, Sibo Zuo, Yinan Deng, Xinyu Zhang, Yufeng Yue
- Published: 2026-09-08T02:43:48Z
- Age days: 1

</details>
