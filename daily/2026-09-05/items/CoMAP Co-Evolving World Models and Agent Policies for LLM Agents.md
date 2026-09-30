---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.02372"
published: "Fri, 04 Sep 2026 00:00:00 -0400"
age_days: 0
score: 29
created: 2026-09-05
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# CoMAP: Co-Evolving World Models and Agent Policies for LLM Agents

> [!summary] 先说人话（基于摘要）
> CoMAP 让文本世界模型和 Agent 策略在闭环交互中共同演化：模型先预测候选动作后果，Agent 评估预测可信度并反思改动作，再用新产生的在策略轨迹自蒸馏更新世界模型。

## 这篇到底在做什么

- **卡在哪里**：固定文本世界模型无法适应不断变化的 Agent 所访问的状态—动作分布；现有 Agent 改进方法又常依赖外部奖励或验证器，在真实交互环境中不一定可得。
- **关键解法**：每步由世界模型为候选动作预测未来反馈，Agent 做面向未来且考虑预测可靠性的反思；执行所得在策略轨迹随后用于世界模型自蒸馏，使预测器跟随策略分布变化。与旧做法的关键差异是策略与模型互相更新，而非固定其中一方。
- **拿什么证明**：在具身任务规划、网页导航和工具使用基准上持续优于竞争基线；摘要举例 Qwen3-4B 相对提升16.75%。分析还显示世界模型预测准确率随训练提高并改善长程决策，但无更多数字。

## 值不值得读

- **和你的研究有什么关系**：对 Agent 与世界模型研究者，它针对模型偏差随策略分布漂移这一核心问题，并减少对外部验证器的依赖，可用于长程交互式任务。
- **先别急着信**：自蒸馏可能强化自身错误；需核查可靠性估计如何防止错误闭环，以及16.75%对应的指标、基准和统计稳定性。
- **判断**：值得精读闭环更新和防漂移机制；思想重要，但成败取决于自生成监督是否具备可靠的纠错来源。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-05/CoMAP Co-Evolving World Models and Agent Policies for LLM Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2606.02372v2 Announce Type: replace Abstract: Equipping language agents with world models enables them to anticipate environment dynamics and evaluate candidate actions before execution. However, existing textual world models are typically fixed after training, preventing them from adapting to the on-policy state-action distributions induced by an evolving agent. Meanwhile, agent-improvement methods often rely on external rewards or verifiers, limiting their applicability in realistic interactive environments. In this paper, we propose COMAP, a novel framework that co-evolves textual world models and agent policies through closed-loop interaction. At each decision step, the world model predicts future state feedback for candidate actions, and the agent performs future-aware reflection by estimating the reliability of this feedback and refining its action accordingly. The resulting on-policy trajectories are then used to update the world model via self-distillation, allowing it to better match the agent's evolving interaction distribution. Across embodied task planning, Web navigation, and tool-use benchmarks, COMAP consistently outperforms competitive baselines, e.g., +16.75% relative improvement with Qwen3-4B. Further analyses show that the co-evolutionary loop improves the world model's prediction accuracy over time and leads to more effective long-horizon decision-making. Our code is available at: https://github.com/loyiv/CoMAP.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.02372
- Authors: Youwei Liu, Jian Wang, Hanlin Wang, Wenjie Li
- Published: Fri, 04 Sep 2026 00:00:00 -0400
- Age days: 0

</details>
