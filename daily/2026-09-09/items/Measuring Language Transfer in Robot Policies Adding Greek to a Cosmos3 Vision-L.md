---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 3
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.07470v1"
published: "2026-09-07T13:24:23Z"
age_days: 1
score: 38
created: 2026-09-09
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# Measuring Language Transfer in Robot Policies: Adding Greek to a Cosmos3 Vision-Language-Action Policy

> [!summary] 先说人话（基于摘要）
> 给 Cosmos3 VLA 加上希腊语，难点首先是证明机器人真的听懂了。论文通过错误指令对照、多随机种子和有区分力的任务集，发现双语训练有效，但离英语水平仍有明显距离。

## 这篇到底在做什么

- **卡在哪里**：任务是在缺少希腊语机器人示范的条件下实现语言迁移。现有测量可能把不依赖指令的成功误判为理解语言：颜色直方图奖励噪声，单目标测试无法区分正确与错误指令，训练损失和单次运行也不可靠。
- **关键解法**：不改架构，仅用机器改写指令比较希腊语单语、双语训练等方案；在90项任务上为每组运行3个种子，并设置故意错误指令的对照。每任务使用多种措辞，检验策略是否只适应翻译器表达。
- **拿什么证明**：单目标测试中，正确与错误希腊语指令得分分别为84.6%和82.6%。90任务评测中，希腊语单语训练最多超过对照2.7个百分点，双语训练稳定超过6.7—7.1个百分点，达到约四成英语性能；每任务7种措辞约减半措辞过拟合惩罚。语言适配世界模型热启动及解冻文本塔均使性能下降。

## 值不值得读

- **和你的研究有什么关系**：对VLA本地化和具身评测最直接的价值，是提供检验策略是否真正利用语言的对照思路；世界模型研究者也应注意，语言适配的收益未必能迁移到动作策略。
- **先别急着信**：需要全文核查90任务如何保证指令具有区分力，以及错误指令对照的构造；对希腊语和该策略栈的结果不能直接推广到其他语言。
- **判断**：优先精读评测设计与负结果，它比单纯报告多语言成功率更能帮助排除虚假进展。

## 研究关联

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：38
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-09/Measuring Language Transfer in Robot Policies Adding Greek to a Cosmos3 Vision-L.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Robot foundation models are trained and evaluated predominantly in English, and robot demonstration corpora do not exist for most languages. We study the addition of Greek to an open vision-language-action stack using only machine-rephrased instructions and no architecture changes. The main challenge is measurement rather than translation. Several plausible instruments produce false conclusions: a color-histogram metric rewards noise, a single-goal benchmark scores 84.6% under correct Greek and 82.6% under deliberately wrong instructions, training loss fails to predict Greek success, and single-run comparisons are dominated by seed variation. On a discriminative ninety-task suite with three seeds per arm, a multilingual text tower without Greek demonstrations remains at its wrong-instruction floor, while Greek-only training exceeds its control by at most 2.7 points. Bilingual training yields a consistent 6.7-7.1 point margin over its control and reaches about two fifths of English performance. The policy also overfits the translator's phrasing; training on seven phrasings per task approximately halves this penalty. Warm-starting from a language-adapted world model and unfreezing the text tower both degrade performance. The results support two practical requirements for low-resource robot-policy localization: build a guaranteed null before trusting a metric, and replicate low-resource-language results across seeds.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.07470v1
- Authors: Ayoub Kirouane, Georgios Giaples, Christos Petrocheilos
- Published: 2026-09-07T13:24:23Z
- Age days: 1

</details>
