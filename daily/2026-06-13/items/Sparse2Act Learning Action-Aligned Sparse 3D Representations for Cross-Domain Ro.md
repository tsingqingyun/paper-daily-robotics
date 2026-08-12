---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.12759v1"
published: "2026-06-10T23:56:01Z"
age_days: 2
score: 29
created: 2026-06-13
concepts: ["世界模型", "Sim2Real", "具身智能评测与基准"]
---

# Sparse2Act: Learning Action-Aligned Sparse 3D Representations for Cross-Domain Robot Manipulation

> [!summary] 一句话结论（基于摘要）
> On the LIBERO-10 benchmark, our method achieves 86.9% average success after 500 fine-tuning steps.

## 关键点

- **问题**：However, sparse 3D encoders are often learned through downstream task objectives, tying the representation to a particular data distribution, policy architecture, and action parameterization.
- **创新点 / 方法**：We introduce Sparse2Act, an observation-action alignment framework for pretraining sparse point-cloud encoders.
- **证据**：On the LIBERO-10 benchmark, our method achieves 86.9% average success after 500 fine-tuning steps.
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[世界模型]] [[Sim2Real]] [[具身智能评测与基准]]
- **筛选分数**：29
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-13/Sparse2Act Learning Action-Aligned Sparse 3D Representations for Cross-Domain Ro.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Explicit 3D representations are attractive for manipulation because they expose object
shape, workspace geometry, and robot-object relations in metric coordinates. However,
sparse 3D encoders are often learned through downstream task objectives, tying the
representation to a particular data distribution, policy architecture, and action
parameterization. We introduce Sparse2Act, an observation-action alignment framework for
pretraining sparse point-cloud encoders. The key idea is to use task-space end-effector
actions as geometric supervision: masked sparse 3D tokens are trained to organize scene
features around the workspace motion paired with the observation. After pretraining,
only the encoder initialization is reused by downstream policies, allowing them to
retain their own architectures and action spaces, including joint-space commands. On the
LIBERO-10 benchmark, our method achieves 86.9% average success after 500 fine-tuning
steps. The same pretrained encoder supports LIBERO-to-Meta-World cross-domain transfer,
achieving 73.4% average success on the Meta-World-5 benchmark. Ablations on the
objective and decoder capacity show that the gains come from the masked action-alignment
signal and remain useful across downstream action decoders. In real-world experiments,
simulation pretraining followed by limited real-data fine-tuning achieves an average
success rate of 72.5% across four tasks, demonstrating effective sim-to-real transfer.
These results suggest that robot actions can provide compact geometric supervision for
reusable sparse 3D representations.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.12759v1
- Authors: Yu Guo, Chang Yu, Siyu Ma, Yunuo Chen, Yin Yang, Ying Nian Wu, Chenfanfu Jiang
- Published: 2026-06-10T23:56:01Z
- Age days: 2

</details>
