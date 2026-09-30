---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.19600v1"
published: "2026-09-17T02:27:32Z"
age_days: 0
score: 39
created: 2026-09-18
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "机器人学习", "具身智能评测与基准"]
---

# WorldContact: A Contact-Centric World Model for Scalable Robot Learning

> [!summary] 先说人话（基于摘要）
> WorldContact用少量高质量轨迹训练接触中心的世界模型，更快生成购物袋操作数据，再用这些数据改善VLA的实机表现。关键是以比原数值模拟器更大的时间步预测物体运动。

## 问题

可变形物体的新任务适配需要大量交互经验，而原模拟器为处理快速运动和避免穿透必须使用小积分步长，限制数据生成效率。

## 创新点或方法

模型作用于可变形物体动力学，从已有轨迹学习较大时间步的状态演化，扩增训练集后微调现有VLA，并直接部署到真实机器人。与继续运行原模拟器相比，它以学习到的动力学预测承担数据生成。

## 证据

在16项购物袋操作任务中评估；单张H100上的状态滚动速度为原模拟器的10倍，不含渲染和磁盘I/O。实机提袋单次成功率从仅用原仿真数据微调的65%提高到扩增数据后的95%。

## 局限

10倍不是完整数据流水线加速；95%的实机结果对应提袋任务，不能直接推广到全部16项任务或其他可变形物体。

- **判断**：值得优先精读，重点核查接触建模、数据扩增配比和实机评估规模，因其同时报告了生成效率与策略收益。

## 研究关联

直接连接世界模型、数据生成和VLA适配，为机器人学习研究者提供了以策略实机收益衡量世界模型价值的案例。

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[机器人学习]] [[具身智能评测与基准]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-18/WorldContact A Contact-Centric World Model for Scalable Robot Learning.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Adapting robots to new objects and tasks requires interaction experience that can be costly to obtain. We present WorldContact, a contact-centric world model for deformable-object manipulation, constructed from a limited set of high-quality trajectories to generate additional training data efficiently. It predicts object dynamics using larger time steps than the source numerical simulator, which requires small integration steps to resolve rapid motion and prevent interpenetration. We evaluate WorldContact across 16 shopping-bag manipulation tasks. State-rollout measurements on a single H100 GPU show a $10\times$ speedup over the source simulator, excluding rendering and disk I/O. We use the generated data to fine-tune an existing vision-language-action policy and deploy it directly on a real robot. In bag lifting, the same policy achieves 65% single-attempt success when fine-tuned on source simulation data alone, compared with 95% when fine-tuned on the dataset expanded with WorldContact. These results support efficient data generation with WorldContact for robot policy adaptation.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.19600v1
- Authors: Caoliwen Wang, Mengdi Wang, Heng Zhang, Shixun Huang, Siyuan Chen, Chao Liu, Anpei Chen, Zhendong Wang, Peter Yichen Chen, Huamin Wang
- Published: 2026-09-17T02:27:32Z
- Age days: 0

</details>
