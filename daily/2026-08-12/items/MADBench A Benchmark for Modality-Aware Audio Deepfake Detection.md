---
type: update-item
tags: [update, ai, embodied-ai]
source: "arXiv Daily - Frontier Embodied AI Robotics Papers"
url: "https://arxiv.org/abs/2608.09593v1"
published: "2026-08-10T13:27:09Z"
age_days: 1
score: 25
created: 2026-08-12
concepts: ["多模态基础模型", "具身智能评测与基准"]
---

# MADBench: A Benchmark for Modality-Aware Audio Deepfake Detection

## 为什么重要

自动筛选分数：25

连接概念：[[多模态基础模型]], [[具身智能评测与基准]]

## 摘要

Recent advances in speech synthesis and audio generation have made high-fidelity
acoustic forgery low-cost and difficult to attribute, enabling a realistic attack
scenario in which speech and background audio are independently manipulated over
otherwise authentic video. Yet existing research either focuses on visual manipulation,
addresses speech detection in isolation, or conflates speech and non-speech audio as a
single undifferentiated audio stream, overlooking the distinct forensic challenges posed
by background audio. This conflation is consequential: the two acoustic components arise
from fundamentally different generative mechanisms, exhibit distinct artifact profiles,
and pose different challenges to detection systems. We introduce MADBench, the first
benchmark that treats speech and environmental audio as distinct acoustic components,
enabling component-aware evaluation of audio deepfake detection across independently
manipulated forgery sources. We benchmark representative state-of-the-art detectors and
multimodal large language models under a unified protocol. Our experiments reveal that
environmental audio manipulation is more detectable than synthetic speech across
general-purpose encoders, while existing pretrained detectors fail on both acoustic
components, and manipulated environmental audio asymmetrically degrades speech deepfake
detection, findings entirely invisible under the single-label paradigm of prior
benchmarks. MADBench establishes a rigorous foundation for future research into robust,
component-aware audio deepfake detection.

## 来源

- Source: arXiv Daily - Frontier Embodied AI Robotics Papers
- URL: https://arxiv.org/abs/2608.09593v1
- Authors: Yanqiu Li, Yang Xiao, Jisheng Bai, Bin Chen, Hong Jia, Ting Dang
- Published: 2026-08-10T13:27:09Z
- Age days: 1

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
