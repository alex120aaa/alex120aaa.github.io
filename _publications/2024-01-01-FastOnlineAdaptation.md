---
title: "Fast Online Adaptation of Visual SLAM via Variational Information Transfer and Preservation"
collection: publications
category: conferences
permalink: /publication/FastOnlineAdaptation
excerpt: 'Published in ACM MMAsia 2024 (2024).'
date: 2024-01-01
venue: 'ACM MMAsia 2024'
paperurl: 'https://doi.org/10.1145/3696409.3700212'
citation: 'Sangni Xu, Hao Xiong, Qiuxia Wu, Zhihui Wang, Shlomo Berkovsky, et al. (2024). "Fast Online Adaptation of Visual SLAM via Variational Information Transfer and Preservation" <i>ACM MMAsia 2024</i>.'
---
Simultaneous Localisation and Mapping (SLAM) in computer vision involves estimating the camera poses and the surrounding depth information. Current deep learning based approaches achieve great success, yet most of them suffer from the domain generalisation issue. Accordingly, the online adaptation based methods have been proposed, enabling the SLAM model to continuously adapt to the changing open-world environments. However, these models are not computationally efficient while pursing accurate adaptation. In this work, we present a novel variational information transfer and preservation based visual SLAM method that aims to adapt fast while maintaining good precision. To reduce model size for faster adaptation, we introduce a lightweight network with a shared encoder for estimates of both poses and depths. To ensure adaptation precision, we exploit a large-sized network to pass our network the knowledge using a proposed information theory inspired knowledge distillation method that variationally maximizes the mutual information between the large network and ours. With pre-learned knowledge preservation, our model then learns to adapt against catastrophic forgetting by introducing the variational distribution of network weights pre-learned from knowledge distillation into the information bottleneck framework. During learning and adaptation, we keep these pre-learned weights fixed and utilise several adapters to adjust the feature representations instead. In terms of both speed and accuracy, our method surpasses several state-of-the-art baselines in evaluations of online visual SLAM adaptation.
