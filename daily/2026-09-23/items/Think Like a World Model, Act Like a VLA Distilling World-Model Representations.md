---
type: update-item
tags: [update, ai, embodied-ai]
format_version: 2
evidence_level: abstract
reading_status: skimmed
needs_fulltext: true
summary_method: codex-abstract-explanatory
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2609.24682v1"
published: "2026-09-21T14:41:08Z"
age_days: 1
score: 39
created: 2026-09-23
concepts: ["多模态基础模型", "世界模型", "视觉语言动作模型 VLA", "具身智能评测与基准"]
---

# Think Like a World Model, Act Like a VLA: Distilling World-Model Representations into Compact Robot Policies

> [!summary] 先说人话（基于摘要）
> 这项工作把世界模型学到的场景表征教给小型VLA，部署时不用再生成未来。机制是在普通策略训练中加入特征对齐，让学生吸收教师的内部表示。

## 问题

VLA训练缺少直接描述动作后果的目标，而世界模型逐次生成未来又可能耗时数秒，难以进入实时控制环。

## 创新点或方法

冻结世界模型，预先处理训练帧并缓存特征；学生训练时增加对齐损失，不在线加载教师。训练后丢弃投影器，部署策略结构与未蒸馏基线相同。

## 证据

0.8B学生在LIBERO达97.9%；RoboCasa-GR1从48.2%升至50.5%。RTX 5090上推理32毫秒、显存1.86GB；单臂和双臂硬件均验证迁移，收益在不同学生规模、骨干、对齐层和教师下仍存在。

## 局限

LIBERO未给出对应基线，真实机器人未给出量化增益；部署结构相同仍不足以单凭摘要排除训练设置等因素的影响。

- **判断**：值得精读并考虑复现，方法改动集中，适合检验世界模型表征能否稳定提升策略。

## 研究关联

为世界模型研究者提供脱离在线生成的价值验证方式，也为VLA研究者提供不增加部署结构的表征增强手段。

- **概念**：[[多模态基础模型]] [[世界模型]] [[视觉语言动作模型 VLA]] [[具身智能评测与基准]]
- **筛选分数**：39
- **阅读状态**：摘要级快读；需要全文核查证据或局限
- **精度升级**：[[AI 论文深读工作流|选择 L1 定向核查或 L2 完整精读]]

`python3 scripts/start_ai_deep_read.py --vault "." --note "30_Updates/2026-09-23/Think Like a World Model, Act Like a VLA Distilling World-Model Representations.md" --level full`

<details>
<summary>原始摘要与来源</summary>

### 原始摘要

Vision-Language-Action (VLA) models map observations to actions with no objective that accounts for how the world responds, so their robustness is bounded primarily by data coverage. World models carry precisely that missing objective and are better grounded for it, yet rolling the future forward costs seconds per decision and rules them out of the control loop. We show the two can be separated. What a world model knows about physical scenes lives in its \emph{internal features}; generating the future is merely the objective that produced them, so the grounding can be inherited while the generative machinery is left behind. We add one feature-alignment term to ordinary VLA training: a frozen world model is run over the training frames once and cached, and the student learns to agree with that cache. No teacher is loaded during training, the projector is discarded after it, and the deployed policy is identical to the undistilled baseline, running in $32$~ms and $1.86$~GB on a consumer RTX~5090, so every gain is attributable to the representation rather than to added capacity or test-time compute. A $0.8$B student reaches $97.9\%$ on LIBERO, improves from $48.2\%$ to $50.5\%$ on RoboCasa-GR1 humanoid manipulation, and the same objective carries over to real hardware, on both a single-arm and a bimanual platform. The gain survives changes of student scale, backbone, alignment layer, and teacher, indicating a broad representational prior rather than a fragile alignment between two particular networks. Project page: https://thaw-vla.trung-dt.com/.

### 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2609.24682v1
- Authors: Trung Dao, Sankalp Yamsani, Jaden Park, Joohyung Kim, Yong Jae Lee
- Published: 2026-09-21T14:41:08Z
- Age days: 1

</details>
