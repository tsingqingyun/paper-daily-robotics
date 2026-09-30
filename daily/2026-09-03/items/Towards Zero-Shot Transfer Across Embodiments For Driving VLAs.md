---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.02341v1"
published: "2026-09-02T09:17:54Z"
age_days: 0
score: 43
created: 2026-09-03
concepts: ["多模态基础模型", "视觉语言动作模型 VLA"]
---

# Towards Zero-Shot Transfer Across Embodiments For Driving VLAs

> [!summary] 先说人话（基于摘要）
> 论文研究驾驶 VLA 对未见数据集和相机布局的零样本迁移，并提出 BEV-Forcing，用共享鸟瞰空间接口把地面物体布局知识注入 VLA。该辅助目标在训练相机布局较少时有效，但随本体多样性增加而收益减弱。

## 问题

驾驶 VLA 往往按单一数据集训练，缺少对新数据集和新相机阵列的零样本测试；简单混入更多数据集还不保证已见本体性能更好，说明多源数据并不会自动形成统一空间表征。

## 创新点或方法

模型进行多数据集训练，同时以专用 BEV 模型提供地面物体布局监督，迫使 VLA 骨干通过共享 BEV 接口编码位置；区别于只扩大数据混合，它显式对齐不同相机布局下的空间结构。

## 证据

摘要报告 BEV-Forcing 在训练相机布局较少时同时改善分布内和分布外性能，并称随着训练本体增加，辅助目标收益下降；未给出可核查的结果数字。


## 局限

摘要没有给出数据集、指标、增益数值或未见相机布局的具体难度，效果大小和泛化边界需查全文。

- **判断**：值得读实验曲线和数据规模分析；BEV-Forcing 本身直观，真正有判断价值的是其收益随训练多样性衰减的证据。

## 研究关联

对驾驶 VLA 研究者，核心价值是提醒辅助几何目标必须与数据规模联合评估，不能只在小规模设置中证明有效后便宣称可扩展。

- **概念**：多模态基础模型 视觉语言动作模型 VLA
- **筛选分数**：43
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[选择 L1 定向核查或 L2 完整精读](../../../deep-reading/README.md)

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-03/Towards Zero-Shot Transfer Across Embodiments For Driving VLAs.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action models (VLAs) have shown strong potential in autonomous driving by leveraging multimodal pretraining for instruction following, visual reasoning, and scene-level generalization. In robotic manipulation, scaling VLA fine-tuning across multiple robot setups--especially when unifying representations across embodiments--has been shown to improve in-dataset performance and cross-embodiment generalization; in autonomous driving, however, VLAs remain largely trained on individual datasets and are rarely evaluated for zero-shot transfer to unseen datasets and camera rigs; furthermore naively adding more datasets to the training data does not necessarily lead to better performance within seen embodiments. To address these problems, we study multi-dataset training for the driving task and BEV-Forcing, an auxiliary objective that transfers ground-plane object-layout information from a specialized Bird's-Eye-View model into the VLA backbone. By encouraging the model to represent object position through a shared BEV spatial interface, we show that an auxiliary task such as BEV-Forcing can improve both in-distribution and out-of-distribution performance when training on a small number of camera rigs. As the number of training embodiments increases, however, the benefits of the auxiliary task are reduced; we present this as evidence that new techniques in the literature may see their benefits diminish when simply scaling up training diversity, which motivates presenting results taking into account data scaling.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.02341v1
- Authors: Caio Azevedo, Stefano Sabatini, Sascha Hornauer, Fabien Moutarde
- Published: 2026-09-02T09:17:54Z
- Age days: 0

</details>
