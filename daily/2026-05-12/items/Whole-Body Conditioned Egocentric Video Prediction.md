---
type: update-item
tags: [update, ai, embodied-ai]
source: "Berkeley BAIR Blog"
url: "http://bair.berkeley.edu/blog/2025/07/01/peva/"
published: "Tue, 01 Jul 2025 02:00:00 -0700"
score: 24
created: 2026-05-12
concepts: ["智能体 Agent", "世界模型", "具身智能评测与基准"]
---

# Whole-Body Conditioned Egocentric Video Prediction

## 为什么重要

自动筛选分数：24

连接概念：[[智能体 Agent]], [[世界模型]], [[具身智能评测与基准]]

## 摘要

.modal { display: none; position: fixed; z-index: 9999; padding-top: 50px; left: 0; top:
0; width: 100%; height: 100%; overflow: auto; background-color: rgba(0,0,0,0.9); }
.modal-content { margin: auto; display: block; max-width: 90%; max-height: 90%; } .close
{ position: absolute; top: 15px; right: 35px; color: #f1f1f1; font-size: 40px; font-
weight: bold; transition: 0.3s; cursor: pointer; } .close:hover, .close:focus { color:
#bbb; text-decoration: none; cursor: pointer; } .clickable-img { cursor: zoom-in;
transition: opacity 0.3s; } .clickable-img:hover { opacity: 0.9; } @media only screen
and (max-width: 700px){ .modal-content { width: 100%; } } ×
document.addEventListener('DOMContentLoaded', function() { var modal =
document.getElementById('imageModal'); var modalImg =
document.getElementById('modalImg'); var span =
document.getElementsByClassName('close')[0]; // Add click handler to all images in the
post var images = document.querySelectorAll('.post-content img, article img');
images.forEach(function(img) { // Make all images clickable
img.classList.add('clickable-img'); img.title = 'Click to enlarge'; img.onclick =
function() { modal.style.display = 'block'; // Use the original high-res version if it
exists var highResSrc = this.src.replace('_web.png', '.png'); modalImg.src = highResSrc;
modalImg.onerror = function() { // Fall back to the web version if high-res doesn't
exist modalImg.src = img.src; }; } }); // Close modal when clicking the X span.onclick =
function() { modal.style.display = 'none'; } // Close modal when clicking outside the
image modal.onclick = function(event) { if (event.target == modal) { modal.style.display
= 'none'; } } // Close modal with ESC key document.addEventListener('keydown',
function(event) { if (event.key === 'Escape') { modal.style.display = 'none'; } }); });
Predicting Ego-centric Video from human Actions (PEVA) . Given past video frames and an
action specifying a desired change in 3D pose, PEVA predicts the next video frame. Our
results show that, given the first frame and a sequence of actions, our model can
generate videos of atomic actions (a), simulate counterfactuals (b), and support long
video generation (c). Recent years have brought significant advances in world models
that learn to simulate future outcomes for planning and control. From intuitive physics
to multi-step video prediction, these models have grown increasingly powerful and
expressive. But few are designed for truly embodied agents. In order to create a World
Model for Embodied Agents, we need a real embodied agent that acts in the real world. A
real embodied agent has a physically grounded complex action space as opposed to
abstract control signals. They also must act in diverse real-life scenarios and feature
an egocentric view as opposed to aesthetic scenes and stationary cameras. 💡 Tip: Click
on any image to view it in full resolution. Why It’s Hard Action and vision are heavily
context-dependent. The same view can lead to different movements and vice versa. This is
because humans act in complex, embodied, goal-directed environments. Human control is
high-dimensional and structured. Full-body motion spans 48+ degrees of freedom with
hierarchical, time-dependent dynamics. Egocentric view reveals intention but hides the
body. First-person vision reflects goals, but not motion execution, models must infer
consequences from invisible physical actions. Perception lags behind action. Visual
feedback often comes seconds later, requiring long-horizon prediction and temporal
reasoning. To develop a World Model for Embodied Agents, we must ground our approach in
agents that meet these criteria. Humans routinely look first and act second—our eyes
lock onto a goal, the brain runs a brief visual “simulation” of the outcome, and only
then does the body move. At every moment, our egocentric view both serves as input from
the environment and reflects the intention/goal behind the next movement. When we
consider our body movements, we should consider both actions of the feet (locomotion and
navigation) and the actions of the hand (manipulation), or more generally, whole-body
control. What Did We Do? We trained a model to P redict E go-centric V ideo from human A
ctions ( PEVA ) for Whole-Body-Conditioned Egocentric Video Prediction. PEVA conditions
on kinematic pose trajectories structured by the body’s joint hierarchy, learning to
simulate how physical human actions shape the environment from a first-person view. We
train an autoregressive conditional diffusion transformer on Nymeria, a large-scale
dataset pairing real-world egocentric video with body pose capture. Our hierarchical
evaluation protocol tests increasingly challenging tasks, providing comprehensive
analysis of the model’s embodied prediction and control abilities. This work represents
an initial attempt to model complex real-world environments and embodied agent behaviors
through human-perspective video prediction. Method Structured Action Representation from
Motion To bridge human motion and egocentric vision, we represent each action as a rich,
high-dimensional vector capturing both full-body dynamics and detailed joint movements.
Instead of using simplified controls, we encode global translation and relative joint
rotations based on the body’s kinematic tree. Motion is represented in 3D space with 3
degrees of freedom for root translation and 15 upper-body joints. Using Euler angles for
relative joint rotations yields a 48-dimensional action space (3 + 15 × 3 = 48). Motion
capture data is aligned with video using timestamps, then converted from global
coordinates to a pelvis-centered local frame for position and orientation invariance.
All positions and rotations are normalized to ensure stable learning. Each action
captures inter-frame motion changes, enabling the model to connect physical movement
with visual consequences over time. Design of PEVA: Autoregressive Conditional Diffusion
Transformer While the Conditional Diffusion Transformer (CDiT) from Navigation World
Models uses simple control signals like velocity and rotation, modeling whole-body human
motion presents greater challenges. Human actions are high-dimensional, temporally
extended, and physically constrained. To address these challenges, we extend the CDiT
method in three ways: Random Timeskips : Allows the model to learn both short-term
motion dynamics and longer-term activity patterns. Sequence-Level Training : Models
entire motion sequences by applying loss over each frame prefix. Action Embeddings :
Concatenates all actions at time t into a 1D tensor to condition each AdaLN layer for
high-dimensional whole-body motion. Sampling and Rollout Strategy At test time, we
generate future frames by conditioning on a set of past context frames. We encode these
frames into latent states and add noise to the target frame, which is then progressively
denoised using our diffusion model. To speed up inference, we restrict attention, where
within image attention is applied only to the target frame and context cross attention
is only applied for the last frame. For action-conditioned prediction, we use an
autoregressive rollout strategy. Starting with context frames, we encode them using a
VAE encoder and append the current action. The model then predicts the next frame, which
is added to the context while dropping the oldest frame, and the process repeats for
each action in the sequence. Finally, we decode the predicted latents into pixel-space
using a VAE decoder. Atomic Actions We decompose complex human movements into atomic
actions—such as hand movements (up, down, left, right) and whole-body movements
(forward, rotation)—to test the model’s understanding of how specific joint-level
movements affect the egocentric view. We include some samples here: Body Movement
Actions Move Forward Rotate Left Rotate Right Left Hand Actions Move Left Hand Up Move
Left Hand Down Move Left Hand Left Move Left Hand Right Right Hand Actions Move Right
Hand Up Move Right Hand Down Move Right Hand Left Move Right Hand Right Long Rollout
Here you can see the model’s ability to maintain visual and semantic consistency over
extended prediction horizons. We demonstrate some samples of PEVA generating coherent
16-second rollouts conditioned on full-body motion. We include some video samples and
image samples for closer viewing here: Sequence 1 Sequence 2 Sequence 3 Planning PEVA
can be used for planning by simulating multiple action candidates and scoring them based
on their perceptual similarity to the goal, as measured by LPIPS. In this example, it
rules out paths that lead to the sink or outdoors finding the correct path to open the
fridge. In this example, it rules out paths that lead to grabbing nearby plants and
going to the kitchen while finding reasonable sequence of actions that lead to the
shelf. Enables Visual Planning Ability We formulate planning as an energy minimization
problem and perform action optimization using the Cross-Entropy Method (CEM), following
the approach introduced in Navigation World Models [ arXiv:2412.03572 ]. Specifically,
we optimize action sequences for either the left or right arm while holding other body
parts fixed. Representative examples of the resulting plans are shown below: In this
case, we are able to predict a sequence of actions that raises our right arm to the
mixing stick. We see a limitation with our method as we only predict the right arm so we
do not predict to move the left arm down accordingly. In this case, we are able to
predict a sequence of actions that reaches toward the kettle but does not quite grab it
as in the goal. In this case, we are able to predict a sequence of actions that pulls
our left arm in, similar to the goal. Quantitative Results We evaluate PEVA across
multiple metrics to demonstrate its effectiveness in generating high-quality egocentric
videos from whole-body actions. Our model consistently outperforms baselines in
perceptual quality, maintains coherence over long time horizons, and shows strong
scaling properties with model size. Baseline Perceptual Metrics Baseline perceptual
metrics comparison across different models. Atomic Action Performance Comparison of
models in generating videos of atomic actions. Video Quality Video Quality Across Time
(FID). --> FID Comparison FID comparison across different models and time horizons.
Scaling PEVA has good scaling ability. Larger models lead to better performance. Future
Directions Our model demonstrates promising results in predicting egocentric video from
whole-body motion, but it remains an early step toward embodied planning. Planning is
limited to simulating candidate arm actions and lacks long-horizon planning and full
trajectory optimization. Extending PEVA to closed-loop control or interactive
environments is a key next step. The model currently lacks explicit conditioning on task
intent or semantic goals. Our evaluation uses image similarity as a proxy objective.
Future work could leverage combining PEVA with high-level goal conditioning and the
integration of object-centric representations. Acknowledgements The authors thank
Rithwik Nukala for his help in annotating atomic actions. We thank Katerina Fragkiadaki
, Philipp Krähenbühl , Bharath Hariharan , Guanya Shi , Shubham Tulsiani and Deva
Ramanan for the useful suggestions and feedbacks for improving the paper; Jianbo Shi for
the discussion regarding control theory; Yilun Du for the support on Diffusion Forcing;
Brent Yi for his help in human motion related works and Alexei Efros for the discussion
and debates regarding world models. This work is partially supported by the ONR MURI
N00014-21-1-2801. For more details, read the full paper or visit the project website .

## 来源

- Source: Berkeley BAIR Blog
- URL: http://bair.berkeley.edu/blog/2025/07/01/peva/

- Published: Tue, 01 Jul 2025 02:00:00 -0700

## 我的判断

- [ ] 是否值得沉淀为核心笔记？
- [ ] 是否需要加入 [[具身智能评测与基准]] 或 [[视觉语言动作模型 VLA]]？

## 后续追踪

- 复现实验/代码：
- 相关论文：
- 影响的知识节点：
