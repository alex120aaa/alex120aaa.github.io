---
title: "WaveLoss: An Adaptive Dynamic Loss for Deep Gait Recognition"
collection: publications
category: conferences
permalink: /publication/WaveLossAnAdaptive
excerpt: 'Published in AAAI 2025 (2025). Cited by 4.'
date: 2025-01-01
venue: 'AAAI 2025'
paperurl: 'https://doi.org/10.1609/aaai.v39i8.32891'
citation: 'Zicheng Wang, Qiuxia Wu (2025). "WaveLoss: An Adaptive Dynamic Loss for Deep Gait Recognition" <i>AAAI 2025</i>.'
---
Designing an appropriate loss function can enhance the discriminative power on gait recognition. However, previous research focuses on improving network structure and enriching input modalities but overlooks the loss functions. Although transferring loss functions from face recognition can address sample-level loss, additional design is needed for part-level loss. Therefore, we have designed a new loss function called Waveloss, aimed at adaptively and dynamically changing the preference for parts of different difficulties. First, the previous method treats the loss of different parts equally, which brings the problems of difficult convergence or susceptibility to noise interference, so we propose norm-fusion to adaptively learn samples of different difficulties. Additionally, since we find the exponential value represents preference for learning different samples, we introduce the Dynamic Learning Process, which dynamically adjusts the exponential value during iteration to focus on samples of varying difficulties at different training stages. Finally, as the changes of the exponential value leads to significant fluctuations in the gradient, we introduce the gradient truncation and normalization to avoid getting trapped in local optima and gradient vanishing or exploding by adaptively adjusting the gradient. Experimental results demonstrate that our proposed Waveloss achieves state-of-the-art performance on various gait recognition datasets and can improve the performance of different backbones as well.
