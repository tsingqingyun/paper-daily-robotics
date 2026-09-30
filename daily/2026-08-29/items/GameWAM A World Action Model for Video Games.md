---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.26200"
published: "Sat, 29 Aug 2026 00:00:00 -0400"
age_days: 0
score: 21
created: 2026-08-29
concepts: ["智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# GameWAM: A World Action Model for Video Games

> [!summary] 先说人话（基于摘要）
> GameWAM在游戏中联合生成未来画面和可执行键鼠动作，把世界模型与任务策略合为闭环系统。它用分块因果条件、flow matching和滚动式block-cycle控制处理长时交互。

## 问题

游戏Agent通常直接从视觉与任务映射到动作，缺少显式动力学；交互世界模型虽能按动作预测未来，却不会自主完成任务。原生键鼠控制异构、视觉变化快且状态需长期保持，使联合建模困难。

## 创新点或方法

同步游戏与GUI轨迹用于联合训练，视觉与动作通过并行生成过程输出。每步先判断游戏或GUI模式，再用对应分布预测归一化动作；block-cycle生成较长计划但只执行短前缀，随后基于新观察重规划，并保留周期内和跨周期历史。

## 证据

摘要称其以更少的实际原生动作取得有竞争力的任务成功率，但未给出数字。还发现LASI：固定条件下，动作采样源的低频成分会系统性改变生成相机的粗粒度运动。


## 局限

需要核查联合视频预测是否真正提高任务成功，以及LASI会在多大程度上破坏可控性、安全性和跨游戏泛化。

- **判断**：世界—动作联合建模研究者值得精读，尤其看滚动控制和LASI分析；摘要不足以证明其总体优于专用游戏Agent。

## 研究关联

对Agent、VLA和世界模型，这是原生闭环环境中联合预测与行动的完整案例；LASI还暴露了生成式控制中特定于采样源的可靠性问题。

- **概念**：智能体 Agent 世界模型 视觉语言动作模型 VLA
- **筛选分数**：21
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-08-29/GameWAM A World Action Model for Video Games.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2608.26200v1 Announce Type: cross Abstract: Modern video games combine first-person perception, rapid visual changes, persistent world state, and heterogeneous native controls. Existing game agents map visual and task context directly to actions but lack explicit world dynamics modeling, whereas interactive game world models predict visual futures from supplied actions but do not serve as task policies. World-Action Models (WAMs) unify these objectives, but remain largely unexplored under the dynamics and open-ended interaction of video games. We introduce GameWAM, to our knowledge the first WAM for native closed-loop gameplay and GUI control. GameWAM jointly generates future visual observations and executable keyboard-mouse trajectories through parallel visual and action generative processes with block-causal conditioning and flow matching. To support joint world-action learning, we construct synchronized gameplay and GUI trajectories. To handle heterogeneous native control, GameWAM predicts a gameplay/GUI mode at each action step and generates actions with mode-specific prediction distributions and continuous-action normalization. For long-horizon interaction, block-cycle control predicts beyond the committed horizon, executes only a short action prefix, and replans from new observations, while fine-grained within-cycle context and hierarchical cross-cycle history preserve temporal continuity. Experiments demonstrate competitive task success with fewer executed native actions than the compared agents. We further uncover Low-Frequency Action Source Imprinting (LASI), in which low-frequency components of the sampled action source systematically steer coarse generated camera motion under fixed conditioning, revealing a source-sensitivity failure mode in generative control. Project page is available at https://yunncheng.github.io/GameWAM/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.26200
- Authors: Yuncheng Guo, Zhanqiu Zhang, Yiwen Guo, Weijia Li
- Published: Sat, 29 Aug 2026 00:00:00 -0400
- Age days: 0

</details>
