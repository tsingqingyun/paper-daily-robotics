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
url: "https://arxiv.org/abs/2611.01215"
published: "Tue, 03 Nov 2026 00:00:00 -0500"
age_days: 0
score: 34
created: 2026-11-04
concepts: ["多模态基础模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Vision-Language Models Are Joint Denoisers in Robotic Action Generation

> [!summary] 这篇论文到底做了什么（基于摘要）
> JADE 让视觉语言模型在动作逐步去噪的过程中反复查看并修正当前动作。关键是把带噪动作变成它能读取的结构化表示，使视觉和指令的指导随着动作变化而更新。

## 问题

任务是根据图像和语言生成机器人动作。常见扩散 VLA 先由视觉语言模型提供固定条件，再交给动作专家去噪；动作已经变成什么样，前者却不再参与判断。作者认为这限制了预训练感知和推理对控制的帮助，尤其面对分布外情况。

### 用一个例子理解

理解用例（非论文实验）：输入桌面图像和“把碗放到盘子旁”；系统从带噪动作开始，视觉语言模型反复结合当前动作与场景提供指导，动作专家逐步得到可执行动作序列。这里不假设模型会输出文字形式的纠错理由。

## 创新点或方法

旧做法提供静态条件；JADE 在每个去噪步把当前带噪动作、图像和指令一起交给视觉语言模型，再通过门控交叉注意力指导动作专家。训练时还要求视觉语言模型从带噪动作潜变量恢复干净版本，让它直接学习动作。推理时双方共同迭代，作者用更少采样步数和自适应步长调节额外计算开销；具体表示结构与调度规则摘要未说明。

### 方法如何工作

1. 把当前带噪动作编码成结构化潜变量，使视觉语言模型能同时读取动作、图像和指令。
2. 每轮由视觉语言模型重新理解当前动作，再通过门控交叉注意力指导动作专家去噪。
3. 训练时额外监督干净动作潜变量恢复，让视觉语言模型获得直接动作学习信号。
4. 推理时重复联合去噪，并用采样步数与自适应步长平衡动作质量和耗时；具体规则摘要只说明到此。

### 必要术语

- 去噪：逐步把带噪变量变成动作；是本文动作生成的迭代过程。
- 动作潜变量：动作的内部编码；让视觉语言模型读取当前动作状态。
- 门控交叉注意力：有控制地引入另一组表示的信息；本文用于把视觉语言模型的指导传给动作专家。

## 证据

摘要报告：JADE 在 RoboDojo 平均成功率为 12.67%，在所评估的 π0.5 衍生方法中最高，并与近期大规模预训练 VLA、WAM 模型具有竞争力，但未列后者数值。RoboTwin 2.0 上也有改进，未给幅度；四项真机双臂任务平均成功率比 π0.5 高 20.8 个百分点。结果支持这些评测中的整体收益，尚不足以分别归因于联合去噪、直接动作监督或步长调度。

## 局限

我的待核查问题是实际端到端延迟、采样步数和训练预算。更少步数不自动等于更快，因为每步增加了视觉语言模型参与；摘要也不足以判断分布外收益具体覆盖哪些变化。

- **判断**：值得细读动作表示与联合训练损失，因为这两处决定视觉语言模型究竟怎样参与控制，以及方法能否复现。

## 研究关联

值得借鉴的是让感知模型看到“当前准备执行的动作”，而非只编码环境。若动作需要多轮生成，环境理解也可以随候选动作更新；不过是否值得采用，要结合成功率收益和逐步调用大模型的成本判断。

### 下一步读哪里

先检查结构化动作潜变量如何编码、门控连接放在哪里，再核查各项消融和成功率—延迟曲线；真机部分需确认试验次数与各任务绝对成功率。

- **概念**：多模态基础模型 视觉语言动作模型 VLA 具身智能评测与基准
- **筛选分数**：34
- **阅读状态**：摘要讲解；仍需完整精读核查证据与局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)


`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-11-04/Vision-Language Models Are Joint Denoisers in Robotic Action Generation.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

arXiv:2611.01215v1 Announce Type: new Abstract: Diffusion-based vision-language-action (VLA) models cascade pretrained vision-language models (VLMs) with diffusion action experts, but typically restrict the VLM to providing static conditioning. This separation limits how much pretrained perception and reasoning can guide action generation, especially in out-of-distribution settings. We introduce JADE, a Joint Action DEnoiser that enables the VLM and action expert to jointly refine actions. Our key insight is that structured action latents allow the VLM to read the current noisy action together with visual observations and language instructions. At every denoising step, the VLM contextualizes the noisy action and guides the action expert through gated cross-attention, so that its guidance evolves with the action being generated. We further supervise the VLM to recover clean action latents from noisy ones, which gives it a direct action-learning signal and couples perception with control. Additionally, joint denoising enables JADE to generate actions with fewer sampling steps, helping offset the additional cost of VLM participation. An adaptive step-size schedule further balances task performance and inference latency. On RoboDojo, JADE achieves an average success rate of 12.67%, the highest among the evaluated $\pi_{0.5}$-based methods, and is competitive with recent VLA and WAM foundation models pretrained at scale. It also improves performance on RoboTwin 2.0 and raises the average success rate across four real-world bimanual tasks by 20.8 percentage points compared with $\pi_{0.5}$.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2611.01215
- Authors: Xicheng Gong, Wenxuan Song, Chengze Liu, Qiwei Li, Qize Yu, Jiaolong Yang, Haoang Li, Yadong Mu
- Published: Tue, 03 Nov 2026 00:00:00 -0500
- Age days: 0

</details>
