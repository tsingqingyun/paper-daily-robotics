---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.25636v1"
published: "2026-09-22T03:48:02Z"
age_days: 1
score: 33
created: 2026-09-24
concepts: ["多模态基础模型", "智能体 Agent", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents

> [!summary] 先说人话（基于摘要）
> RoboFollow 检查机器人是否真的听懂指令：同一场景必须允许多种不同操作，才能排除模型只看画面就猜中任务的可能。

## 问题

当一个场景只有一种合理任务时，语言变得多余，高成功率可能掩盖指令理解不足。直接看最终成功还会混淆理解错误与动作执行失败。

## 创新点或方法

训练场景包含多个运动学上不同的任务分支；L0—L3 四层协议逐步扰动布局和语义，检查同义指令的一致性及不同指令的行为区分度。通过简化物体、限制为已训练动作，并分报 Intent 和 Execution 分数来控制混淆因素。

## 证据

评估九个 VLA 和 WAM 策略；在其微调设置下，较强的 L0 表现不能可靠迁移到 L1—L3。更强 VLM、QA 联合训练、LangForce 和 Classifier-Free Guidance 均未弥合差距；摘要未给出具体分数。

## 局限

结论受该微调设置、任务分支和扰动设计约束；需核查分层评分能在多大程度上分离理解与执行。

- **判断**：建议优先精读基准构造与诊断案例，它对如何解释现有高成功率提出了直接且可测试的挑战。

## 研究关联

对多模态基础模型和 VLA 评测研究者，它直接检查语言是否对动作选择产生必要影响，有助于避免用视觉捷径误判指令遵循能力。

- **概念**：[[多模态基础模型]] [[智能体 Agent]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：33
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-24/RoboFollow Unveiling the Instruction Following Mirage in Embodied Agents.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Modern embodied agents achieve impressive success rates, yet their actual instruction-following ability is far weaker than these numbers suggest. We trace this illusion to a structural property we term low scene entropy: when a visual scene admits only one valid task, language becomes redundant and a policy can score highly while barely using it. We introduce RoboFollow, a diagnostic benchmark with three principles: (1) High Scene Entropy: each training scene supports multiple kinematically distinct task branches, making vision alone insufficient and forcing reliance on language. (2) Hierarchical Diagnostic Protocol: a four-level protocol (L0--L3) progressively perturbs visual layout and semantics, probing whether equivalent instructions yield consistent behavior and distinct ones yield discriminable behavior across spatial relations, attributes, trajectory constraints, and logic. (3) Confound-Controlled Diagnosis: we simplify interaction objects, restrict actions to the trained repertoire and report stage-wise Intent and Execution scores, isolating comprehension from motor execution. Evaluation of nine VLA and WAM policies shows that strong L0 performance, where attained, does not reliably transfer to L1--L3 under our fine-tuning setup. Representative mitigations, including stronger VLM backbones, QA co-training, LangForce, and Classifier-Free Guidance, all fail to close this gap. RoboFollow exposes genuine instruction following as a critical, overlooked bottleneck. Code and dataset are available at https://github.com/AutoLab-SAI-SJTU/RoboFollow and https://huggingface.co/datasets/AutoLab-SJTU/robofollow-data.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.25636v1
- Authors: Chang Guo, Yukun Xie, Bohan Tan, Zheng Chang, Zhaokai Yin, Qianli Ma, Yingqiao Wang, Chao Liang, Zhipeng Zhang
- Published: 2026-09-22T03:48:02Z
- Age days: 1

</details>
