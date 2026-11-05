---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
explanation_version: teaching-v1
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2611.04166v1"
published: "2026-11-03T01:57:41Z"
age_days: 1
score: 34
created: 2026-11-05
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Say the Same, Act Differently: Diagnosing and Steering Text-Action Divergence in Reasoning VLAs

> [!summary] 这篇论文到底做了什么（基于摘要）
> 这篇发现，推理型 VLA 可以说出逐字相同的解释，却执行明显不同甚至导致碰撞的动作。TNAS 找到一类“动作敏感、文字不敏感”的内部变化方向，再用它引导图像扰动，说明只读解释无法判断动作是否安全。

## 问题

任务是检验自然语言解释能否可靠监督驾驶和操作模型。已有攻击会破坏解释，监督者容易从文字发现异常；这里追问更隐蔽的情况：解释完全不变时，动作还能被改变多少？瓶颈在于文字和动作虽然共享内部接口，对内部变化的敏感方向可能不同。

### 用一个例子理解

理解用例（非论文实验）：输入道路图像，模型解释“前方有障碍，应避让”并输出轨迹；图像受到特定扰动后，解释仍逐字相同，轨迹却更靠近障碍。监控器若只读文字，就看不到这次变化。

## 创新点或方法

从沿着文字损失变化方向干预，改为寻找动作变化最大、同时尽量避开活跃文字损失梯度的方向。TNAS 先在共享文字／动作接口诊断这种方向，再据此引导视觉扰动，尝试从输入图像复现脱钩。这是对已有模型的诊断和干预；摘要未说明需要重新训练目标模型。实际生成时同时检查动作变化和解释是否逐字一致。

### 方法如何工作

1. 在共享接口测量文字损失和动作对内部变化的敏感性，寻找二者的差异。
2. 提取尽量不改变文字的动作敏感方向，得到干预目标。
3. 据此优化图像扰动，让输入变化也能推动动作偏移。
4. 共同统计解释一致性和动作后果，检验文字监控会漏掉什么。

### 必要术语

- VLA：把视觉和语言输入转成动作的模型；本文检查其中解释与控制的关系。
- TNAS：尽量不影响文字、却能影响动作的局部方向；用于诊断并引导扰动。
- 梯度：输出或损失对内部变化的局部敏感程度；本文用它比较文字与动作的变化方向。

## 证据

摘要在 Alpamayo 与 InstructVLA 上报告方向重叠为 1.87% 和 5.28%；等范数内部干预下，该方向造成的动作偏移是文字梯度方向的 4.64—47.8 倍。在 154 个驾驶场景中，解释逐字不变且新增碰撞的比例为全图扰动 52.6%、局部补丁 35.1%，无引导动作攻击为 4.55%。操作模型上解释完全保留率为 85.0%，动作块偏移为 1.73 单位，但单位含义未给出。

## 局限

这些受控干预支持所测模型存在文字与动作脱钩，不能推出所有 VLA 都有相同弱点。摘要未交代碰撞判定环境、扰动可见程度和真机验证；局部补丁攻击也不能直接当作现实物理攻击成功。

- **判断**：值得读到方向构造和攻击评测细节，因为它给“解释可读，所以动作可监督”这个假设提供了直接反例。

## 研究关联

具体启示是把解释检查与动作检查分开：模型说的理由没有变化，只能证明文字输出稳定。只要系统最终输出轨迹或控制量，就应直接核查这些输出与障碍物、任务约束的关系。

### 下一步读哪里

核查 TNAS 如何定义局部方向、文字梯度覆盖哪些输出，以及扰动预算如何控制；再看碰撞如何判定、解释一致是否采用自由生成，以及操作偏移对应多大实际运动。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-05/Say the Same, Act Differently Diagnosing and Steering Text-Action Divergence in.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Reasoning vision-language-action (VLA) models pair physical control with natural-language rationales that supervisors can read to monitor embodied safety. Prior attacks on VLA reasoning corrupt the rationale itself and leave visible evidence in the text. We show that visual perturbations can instead alter the physical action while keeping the generated rationale word-for-word identical. At the shared text/action interface of Alpamayo for driving and InstructVLA for manipulation, our text-neutral action-subspace (TNAS) diagnostic shows that the locally most action-sensitive direction is nearly orthogonal to the active text-loss gradients, with 1.87% and 5.28% norm overlap. At equal hidden-state perturbation norms across both models, interventions along this text-neutral residual shift actions 4.64x to 47.8x more than text-gradient perturbations, whereas text-gradient perturbations induce 21.2x to 277x more text drift. Steering visual perturbations along this direction reaches the same decoupling from the image. Across 154 obstacle-annotated driving scenes in Alpamayo, TNAS-guided attacks induce a new collision under a word-for-word identical rationale in 52.6% of scenes under full-image perturbations and 35.1% under a localized forward-camera patch, compared with 4.55% for unguided action attacks. Relative to a text-preserving baseline, TNAS guidance raises exact rationale preservation from 83.0% to 89.5% and cuts teacher-forced text drift by 68.4% at a comparable collision rate. In InstructVLA, TNAS guidance cuts text drift by 40.5% and preserves the exact response on 85.0% of examples alongside a 1.73-unit action-chunk shift. An unchanged rationale therefore cannot certify a safe action, so monitors for reasoning VLAs must verify the predicted action channel directly.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.04166v1
- Authors: Zihao Feng, Qingzhao Zhang, Chunyu Xia, Bo Yu, Z. Morley Mao, Ramesh Govindan
- Published: 2026-11-03T01:57:41Z
- Age days: 1

</details>
