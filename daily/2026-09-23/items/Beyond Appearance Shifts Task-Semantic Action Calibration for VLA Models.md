---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.23650v1"
published: "2026-09-20T13:54:45Z"
age_days: 2
score: 35
created: 2026-09-23
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models

> [!summary] 先说人话（基于摘要）
> BAS-VLA要求机器人分清两件事：场景换了样子时保持行为，任务换了目标时及时改变行为。它在冻结VLA上添加动作校准，并只在证据支持“任务没变”时启用稳定行为的辅助机制。

## 问题

现有策略可能对光照、风格等无关变化过度反应，却在目标或约束真正改变时继续执行旧轨迹，缺乏稳定性与任务敏感性的明确平衡。

## 创新点或方法

以语义改变条件下的校准为默认核心，再通过证据门控，选择性启用针对语义保持扰动的辅助机制，作用于冻结基础VLA。

## 证据

π₀.₅/LIBERO-Object Milk-Swap上，干净和语义保持条件成功率为98.0%与97.5%；目标交换后按旧任务标准计的成功率降至0.0%。经过验证的风格保持变化下，成功率从42%升至70%，干净性能未下降。

## 局限

旧任务标准成功率降为0，只能支持旧行为受到抑制，不能证明模型成功完成了交换目标后的新任务。

- **判断**：值得读指标定义和目标交换实验；新任务完成情况是判断方法价值的关键。

## 研究关联

为VLA评测提出有用区分：抵抗无关变化和响应任务变化是不同能力，应分别测量。

- **概念**：[[多模态基础模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：35
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/Beyond Appearance Shifts Task-Semantic Action Calibration for VLA Models.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-language-action (VLA) models have achieved strong performance in embodied manipulation, but still lack a clear mechanism to balance behavioral stability with task-semantic sensitivity. We identify two complementary failure modes. Under task-preserving changes, where task semantics remain unchanged but scene appearance varies (e.g., style, illumination, clutter, or paraphrasing), policies often exhibit unnecessary action drift. Conversely, under semantic-breaking changes, where key task semantics such as the target object or constraint are altered, policies frequently fail to produce sufficiently distinct behaviors and instead follow the original trajectory. To address this gap, we propose BAS-VLA, a task-semantic action calibration framework built on top of a frozen base VLA. BAS-VLA adopts a breaking-centered calibration core as the default path, and introduces a selective evidence-gated preserving auxiliary that activates only when nuisance variation is detected while task semantics remain consistent. On the OpenPI-pi0.5 / LIBERO-Object Milk-Swap benchmark, BAS-VLA maintains high success on clean (98.0%) and semantics-preserving conditions (97.5%), while reducing clean-criterion success to 0.0% under deliberate target-object swaps, demonstrating strong stale-task suppression and task-semantic separation. On validated style-preserving shifts, it improves success from 42% to 70% without degrading clean performance. These results highlight that reliable VLA behavior requires moving beyond appearance robustness toward explicit task-semantic action calibration.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.23650v1
- Authors: Shuaijun Liu, Feiyang You, Chengyu Wu, Shuyang Hao, Chenglong Zhang, Jingyao Cai, Xingwei Chen, Ningxin Su
- Published: 2026-09-20T13:54:45Z
- Age days: 2

</details>
