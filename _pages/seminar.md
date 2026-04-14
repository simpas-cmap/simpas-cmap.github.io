---
layout: default
title: Seminar
permalink: /seminar/
nav: true
nav_order: 3
---

## Upcoming Seminars

#### Wednesday, April 15th, 2026 (SGS)

- **Jean-Baptiste Fermanian:** Class conditional conformal prediction for multiple inputs by p-value aggregation

  <details>
    <summary>Abstract</summary>
    
    <div class="abstract-text">
      Conformal prediction methods are statistical tools designed to quantify uncertainty and generate predictive sets with guaranteed coverage probabilities. This work introduces a refinement to these methods for classification tasks, specifically tailored for scenarios where multiple observations (multi-inputs) of a single instance are available at prediction time. Our approach is particularly motivated by applications in citizen science, where multiple images of the same plant or animal are captured by individuals. Our method integrates the information from each observation into conformal prediction, enabling a reduction in the size of the predicted label set while preserving the required class-conditional coverage guarantee. The approach is based on the aggregation of conformal p-values computed from each observation of a multi-input. By exploiting the exact distribution of these p-values, we propose a general aggregation framework using an abstract scoring function, encompassing many classical statistical tools. Knowledge of this distribution also enables refined versions of standard strategies, such as majority voting. We evaluate our method on simulated and real data, with a particular focus on Pl@ntNet, a prominent citizen science platform that facilitates the collection and identification of plant species through user-submitted images.
    </div>
  
  </details>
  

#### <span class="group-meeting-label">Group Meeting</span> Thursday, April 16, 2026 (10h-12h) (SGM)

- **Clément Bonet:** Introduction to First-order Optimization Methods in Wasserstein Space.

  <details>
    <summary>Abstract</summary>
    
    <div class="abstract-text">
      As the problem of minimizing functionals on the Wasserstein space encompasses many applications in machine learning, different optimization algorithms on Rd have received their counterpart analog on the Wasserstein space. We will first focus on lifting the mirror descent algorithm. This algorithm has been introduced to better capture the geometry of the function to minimize and is provably convergent under appropriate (namely relative) smoothness and convexity conditions. Adapting these notions to the Wasserstein space, we prove guarantees of convergence of some Wasserstein-gradient-based discrete-time schemes for new pairings of objective functionals and regularizers. Then, we will focus on lifting the Convex-Concave procedure which is tailored to deal with Difference-of-Convex functionals.
    </div>
  
  </details>
  

- **Marguerite Petit-Talamon:** Variational Inference with Mixtures of Isotropic Gaussians.

  <details>
    <summary>Abstract</summary>
    
    <div class="abstract-text">
      Variational inference (VI) is a popular approach in Bayesian inference, that looks for the best approximation of the posterior distribution within a parametric family, minimizing a loss that is typically the (reverse) Kullback-Leibler (KL) divergence. In this paper, we focus on the following parametric family: mixtures of isotropic Gaussians (i.e., with diagonal covariance matrices proportional to the identity) and uniform weights. We develop a variational framework and provide efficient algorithms suited for this family. In contrast with mixtures of Gaussian with generic covariance matrices, this choice presents a balance between accurate approximations of multimodal Bayesian posteriors, while being memory and computationally efficient. Our algorithms implement gradient descent on the location of the mixture components (the modes of the Gaussians), and either (an entropic) Mirror or Bures descent on their variance parameters. We illustrate the performance of our algorithms on numerical experiments. From https://arxiv.org/abs/2506.13613.
    </div>
  
  </details>
  
- **Anna Korba:** A Computable Measure of Suboptimality for Entropy-Regularised Variational Objectives.

  <details>
    <summary>Abstract</summary>
    
    <div class="abstract-text">
      Several emerging post-Bayesian methods target a probability distribution for which an entropy-regularised variational objective is minimised. This increased flexibility introduces a computational challenge, as one loses access to an explicit unnormalised density for the target. To mitigate this difficulty, we introduce a novel measure of suboptimality called ‘gradient discrepancy’, and in particular a ‘kernel’ gradient discrepancy (KGD) that can be explicitly computed. In the standard Bayesian context, KGD coincides with the kernel Stein discrepancy (KSD), and we obtain a novel characterisation of KSD as measuring the size of a variational gradient. Outside this familiar setting, KGD enables novel sampling algorithms to be developed and compared, even when unnormalised densities cannot be obtained. To illustrate this point several novel algorithms are proposed and studied, including a natural generalisation of Stein variational gradient descent, with applications to mean-field neural networks and predictively oriented posteriors presented. On the theoretical side, our principal contribution is to establish sufficient conditions for desirable properties of KGD, such as continuity and convergence control. From https://arxiv.org/abs/2509.10393.
    </div>
  
  </details>
  

- **Pierre-Cyril Aubin-Frankowski:** A gradient flow for every c(x, y) cost: EVI-inspired convexity.
 
  <details>
    <summary>Abstract</summary>
    
    <div class="abstract-text">
      How to go beyond the square distance d^2 in optimization algorithms and flows in metric spaces? Rooted in cross-differences, the convergence theory to the continuous flow is investigated is based on a (discrete) evolution variational inequality (EVI) which enjoys similar properties to the EVI with d^2 regularizer. This provides a theoretical framework for studying splitting schemes beyond the usual implicit Euler in gradient flows. This talk is based on the works https://arxiv.org/abs/2305.04917 with Flavien Léger (INRIA Paris), and https://arxiv.org/abs/2505.00559 (Journal of Functional Analysis 2026) with Giacomo Sodini and Ulisse Stefanelli (Uni Vienna).
    </div>
  
  </details>


#### Wednesday, April 22, 2026 

- **Maxime Haddouche:** *To be announced*



#### Tuesday, May 12, 2026 (11h-12h) (SGS)

- **Jason Altschuler:** Negative Stepsizes Make Gradient-Descent-Ascent Converge

  <details>
    <summary>Abstract</summary>
      Solving min-max problems is a central question in optimization, games, learning, and controls. Arguably the most natural algorithm is Gradient-Descent-Ascent (GDA), however since the 1970s, conventional wisdom has argued that it fails to converge even on simple problems. This failure spurred the extensive literature on modifying GDA with extragradients, optimism, momentum, anchoring, etc. In contrast, we show that GDA converges in its original form by simply using a judicious choice of stepsizes.   
      The key innovation is the proposal of unconventional stepsize schedules that are time-varying, asymmetric, and (most surprisingly) periodically negative. We show that all three properties are necessary for convergence, and that altogether this enables GDA to converge on the classical counterexamples (e.g., unconstrained convex-concave problems). The core intuition is that although negative stepsizes make backward progress, they de-synchronize the min/max variables (overcoming the cycling issue of GDA) and lead to a slingshot phenomenon in which the forward progress in the other iterations is overwhelmingly larger. This results in fast overall convergence. Geometrically, the slingshot dynamics leverage the non-reversibility of gradient flow: positive/negative steps cancel to first order, yielding a second-order net movement in a new direction that leads to convergence and is otherwise impossible for GDA to move in. Joint work with Henry Shugart.
  </details>

  
  
---
  
  
## Past Seminars

#### Wednesday, April 8, 2026 (13h-14h) (SGS)

- **Louis-Pierre Chaintron:** ResNets of All Shapes and Sizes: Quantitative Large-Scale Theory of Training Dynamics

  <details>
    <summary>Abstract</summary>
    We study the convergence of the training dynamics of residual neural networks (ResNets) towards their joint infinite depth–width limit. We focus on ResNets with two-layer perceptron blocks, whose shape is determined by the depth L, hidden width M, and embedding dimension D, and we adopt the residual scaling O(√D/√(LM) ) recently identified as necessary for local feature learning. We show that after a bounded number of training steps, the error between the finite ResNet and its infinite-size limit is O(1/L + √D/√(LM) + 1/√D), and numerical experiments suggest that this bound is tight in the early training phase. From a probabilistic viewpoint, the D→∞ limit amounts to a mean-field limit over the coordinates of the embedding, where some interactions scale in 1/√D contrary to the usual 1/D setting. Our analysis is a rigorous and quantitative instance of the Dynamical Mean Field Theory (DMFT) from statistical physics; it combines propagation of chaos arguments with the cavity method at a functional level.
  </details>


#### Wednesday, March 25, 2026 (14h-15h) (SGS)

- **Timothy Johnston:** Bayesian Adversarial Privacy

  
  <details>
    <summary>Abstract</summary>
    Theoretical and applied research into privacy encompasses an incredibly broad swathe of differing approaches, emphasis and aims. In this talk I shall discuss a new quantitative notion of privacy that is both contextual and specific. Our definition relies on concepts inherent to standard Bayesian decision theory, while departing from it in several important respects. In particular, the party controlling the release of sensitive information should make disclosure decisions from the prior viewpoint, rather than conditional on the data, even when the data is itself observed. I shall also discuss toy examples and computational methods, to highlight the specificities of our framework.
  </details>


#### Wednesday, March 18, 2026 (14h-15h) (SGS)

- **Marc Jourdan:** Advances in Pure Exploration in Bandits: Non-Asymptotic and Private.

  <details>
    <summary>Abstract</summary>
    In pure exploration problems for stochastic multi-armed bandits, the goal is to answer a question about a set of unknown distributions (for example, the efficacy of a treatment) by strategically sampling from them, while providing guarantees on the returned answer. The archetypal example is the best arm identification problem, where the task is to find the arm with the largest mean. Top Two algorithms, which select the next arm to sample from among a leader and a challenger, have received significant attention in recent years due to their simplicity and interpretability.

  In this talk, I will present recent advances on two complementary aspects of pure exploration: achieving non-asymptotic guarantees and ensuring differential privacy. First, we propose a Top Two algorithm which has an asymptotically optimal expected sample complexity, and also provides anytime guarantees on the probability of misidentifying a sufficiently good arm. Second, we show how the Top Two principle can be combined with differential privacy mechanisms, leading to algorithms that preserve near-optimal efficiency while ensuring privacy guarantees. These results not only deepen our theoretical understanding but also enable more practical and privacy-aware bandit algorithms.
  </details>


#### Tuesday, March 17, 2026 (10h30-12h30) (SGS)

- **Ye Zhu:** Dynamic and Structural Sampling for Interpretable and Versatile Control in Multimodal Generation
  
  <details>
    <summary>Abstract</summary>
      Generative models are revolutionizing daily life through applications such as image and audio synthesis, while also enabling breakthroughs in scientific discovery. Despite their huge practical successes, the interpretability of modern generative models remains relatively underexplored. In this talk, I will present one line of my recent work that investigates the intrinsic dynamics and latent geometric structures of generative models. By drawing on both probabilistic and physical perspectives, we aim to demonstrate how these insights can be harnessed during the sampling stage to guide and control pre-trained multimodal models in fine-grained scenarios. This enables versatile downstream multimodal applications, including image semantic editing, text-image guided data customization, controllable enhancement of low-level visual attributes, text-guided acoustic masking, and text-to-image diversity enhancement. Through a series of real-world applications, we hope to bridge the gap between theoretical insights and the reliable deployment of multimodal generative models in complex, real-world environments.
  </details>
  
- **Elise Bayraktar:** Efficient estimation of jump parameters for stochastic differential equations driven by Lévy processes

  <details>
    <summary>Abstract</summary>
      In this talk, we consider the high-frequency estimation of the jump parameters of a stochastic differential equation driven by a Lévy process. More precisely, we are interested in the efficient estimation of scaling and jump activity parameters in the presence of a Brownian motion and a jump component.

      We first study efficiency for the prototype Lévy process. By studying the behavior of the density of the process in small time,  we prove that the LAN property holds for the joint estimation of the diffusion, scaling and jump activity  parameters. We next consider a stochastic differential equation driven both by a Brownian Motion and a locally stable pure-jump Lévy process. Using a quasi-likelihood estimation method, we exhibit an estimator that attains the optimal rate of convergence previously identified.
  </details>

#### <span class="group-meeting-label">Group Meeting</span> Wednesday, February 24, 2026 (10h-12h) (SGM)
- **Badr Moufad:** When Test-Time Guidance Is Enough: Training-Free Posterior Sampling with Diffusion Priors
- **Benjamin Dupuis:** Score matching gap and generalization properties of diffusion models
- **Aymeric Capitaine:** From Prediction to Decision in Dynamic Strategic Environments


#### Monday, February 16, 2026 (11h-12h) (SGS)
- **Eloi Tanguy:** Computing Barycentres of Measures for Generic Transport Costs

  <details>
    <summary>Abstract</summary>
      Wasserstein barycentres represent average distributions between multiple probability measures for the Wasserstein distance. The numerical computation of Wasserstein barycentres is notoriously challenging. A common approach is to use Sinkhorn iterations, where an entropic regularisation term is introduced to make the problem more manageable. Another approach involves using fixed-point methods, akin to those employed for computing Fréchet means on manifolds. The convergence of such methods for 2-Wasserstein barycentres, specifically with a quadratic cost function and absolutely continuous measures, was studied by Alvarez-Esteban et al.. In this paper, we delve into the main ideas behind this fixed-point method and explore how it can be generalised to accommodate more diverse transport costs and generic probability measures, thereby extending its applicability to a broader range of problems. We show convergence results for this approach and illustrate its numerical behaviour on several barycentre problems.
  </details>

#### <span class="group-meeting-label">Group Meeting</span> Wednesday, January 22, 2026 (10h-12h) (SGM)
- **Rémi Flamary:** Introduction to Optimal Transport and Gromov-Wasserstein
- **Paul Krzakala:** The quest for the GRAph Level autoEncoder (GRALE)
- **Sonia Mazelet:** Unsupervised Learning for Optimal Transport plan prediction between unbalanced graphs
- **Thibaut Germain:** A Spectral-Grassmann Wasserstein metric for operator representations of dynamical systems 


#### <span class="group-meeting-label">Group Meeting</span> Wednesday, November 12, 2025 (10h-12h) (SGM)
- **Paul Mangold:** Federated Learning: a Tale of Heterogeneity
- **Lucas Versini:** Analysis of Decentralized SGD: a Markov Chain Perspective
- **Safwan Labbi:** Federated Model-Based Reinforcement Learning
- **Lorenzo Mancini:** Personalized Federated Reinforcement Learning
