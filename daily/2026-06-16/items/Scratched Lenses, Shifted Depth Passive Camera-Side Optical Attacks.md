---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: abstract-extractive
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2606.14504v1"
published: "2026-06-12T14:34:53Z"
age_days: 3
score: 21
created: 2026-06-16
concepts: ["具身智能评测与基准"]
---

# Scratched Lenses, Shifted Depth: Passive Camera-Side Optical Attacks

> [!summary] 一句话结论（基于摘要）
> Camera-side attacks using stickers or auxiliary optics have also been explored, but they treat attacks as image-space perturbations from designed patterns.

## 关键点

- **问题**：Physical adversarial attacks on vision systems are typically studied through scene manipulation, such as adversarial patches or projections, where the adversary controls what the camera observes.
- **创新点 / 方法**：Camera-side attacks using stickers or auxiliary optics have also been explored, but they treat attacks as image-space perturbations from designed patterns.
- **证据**：摘要未报告明确实验结论；需阅读全文核查。
- **局限**：摘要未明确说明；需阅读全文核查。

## 研究关联

- **概念**：[[具身智能评测与基准]]
- **筛选分数**：21
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-06-16/Scratched Lenses, Shifted Depth Passive Camera-Side Optical Attacks.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Physical adversarial attacks on vision systems are typically studied through scene
manipulation, such as adversarial patches or projections, where the adversary controls
what the camera observes. Camera-side attacks using stickers or auxiliary optics have
also been explored, but they treat attacks as image-space perturbations from designed
patterns. This misses how physical imperfections interact with scene-dependent lighting
and optics. We identify a threat: passive lens-side damage that is persistent yet
trigger-conditioned, producing optical artifacts that bias geometric inference under
particular visual conditions. We instantiate this threat through Scratch-induced Lens
Adversarial Streak Hijacking SLASH, a physical-world attack caused by small scratches on
a camera lens or protective cover. Scratches interact with bright light sources and
specular reflections to create structured streak artifacts that distort depth cues.
Since the perturbation is fixed in the optical path but triggered by the scene, it is
both persistent and selective. We formulate the attack in optical space, model the
scratch pattern as a trigger-conditioned optical channel, and optimize one fixed
configuration across diverse viewing conditions. We evaluate SLASH on monocular depth
estimation and monocular 3D object detection in digital and real-world settings. Under
the fixed-scratch constraint, directional depth shifts reach up to 32% relative error
for monocular depth estimation, with consistent effects on monocular 3D object
detection. Physical experiments confirm transfer to real camera recordings, inducing
depth shifts above the model's natural prediction baseline. These findings reveal an
attack surface where benign-looking hardware imperfections act as latent, scene-
triggered adversarial mechanisms, challenging assumptions about physical robustness and
motivating defenses for secure vision systems.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2606.14504v1
- Authors: Qinlin He, Zeming Zhuang, Yongji Wu, Lan Zhang, Xiaoyong, Yuan
- Published: 2026-06-12T14:34:53Z
- Age days: 3

</details>
