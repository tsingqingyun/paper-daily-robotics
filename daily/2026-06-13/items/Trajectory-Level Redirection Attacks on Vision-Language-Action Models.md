---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12978v1"
published: "2026-06-11T07:12:17Z"
age_days: 1
score: 32
created: 2026-06-13
concepts: ["多模态基础模型", "智能体 Agent", "世界模型", "视觉语言动作模型 VLA"]
---

# Trajectory-Level Redirection Attacks on Vision-Language-Action Models

> [!summary] 一句话结论（基于摘要）
> To find such prompts, we introduce an on-policy prompt search method that uses rollouts to discover perturbations whose closed-loop behavior tracks a target task while satisfying the command-preserving constraints.

## 关键点

- **问题**：We identify a stronger trajectory-level failure mode: a prompt that still $\textit{appears}$ to specify the intended task but redirects the final physical outcome.
- **创新点 / 方法**：To find such prompts, we introduce an on-policy prompt search method that uses rollouts to discover perturbations whose closed-loop behavior tracks a target task while satisfying the command-preserving constraints.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[世界模型]] [[视觉语言动作模型 VLA]]
- **筛选分数**：32
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-13/Trajectory-Level Redirection Attacks on Vision-Language-Action Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) policies bring natural language into closed-loop robot
control, enabling robots to execute manipulation tasks directly from text instructions.
The same interface gives text a recurring role in control because the prompt is reused
at every replanning step, and each prompt-conditioned action changes the future
observations on which the policy acts. Existing VLA attacks study adversarial prompts
that elicit targeted low-level actions or make such actions persist across changing
images. We identify a stronger trajectory-level failure mode: a prompt that still
$\textit{appears}$ to specify the intended task but redirects the final physical
outcome. We mathematically formalize this setting as $\textit{command-preserving
trajectory redirection}$, a prompt-only threat model in which the attacker chooses one
prompt before the episode, all policy and environment components remain fixed, and the
prompt must stay close to the benign instruction while omitting target words and
correction language. To find such prompts, we introduce an on-policy prompt search
method that uses rollouts to discover perturbations whose closed-loop behavior tracks a
target task while satisfying the command-preserving constraints. Experiments in
simulation and on hardware show that near-benign prompt perturbations can redirect VLA
rollouts to attacker-specified targets. These results expose a trajectory-level
vulnerability in VLA instruction grounding: text that appears to preserve the intended
command can still give an adversary control over the robot's final physical outcome.
Project website: https://vla-redirection-attack.github.io/

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12978v1
- Authors: Gokul Puthumanaillam, Vardhan Dongre, Pranay Thangeda, Hooshang Nayyeri, Dilek Hakkani-Tür, Melkior Ornik
- Published: 2026-06-11T07:12:17Z
- Age days: 1

</details>
