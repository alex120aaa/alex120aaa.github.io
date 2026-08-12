---
title: "InvolutionGAN: lightweight GAN with involution for unsupervised image-to-image translation"
collection: publications
category: manuscripts
permalink: /publication/InvolutionGANlightweightGAN
excerpt: 'Published in Neural Computing and Applications (2023). Cited by 12.'
date: 2023-01-01
venue: 'Neural Computing and Applications'
paperurl: 'https://doi.org/10.1007/s00521-023-08530-z'
citation: 'Haipeng Deng, Qiuxia Wu, Han Huang, Xiaowei Yang, Zhiyong Wang (2023). "InvolutionGAN: lightweight GAN with involution for unsupervised image-to-image translation" <i>Neural Computing and Applications</i>.'
---
The unsupervised image-to-image translation aims to learn a mapping that translates images from one domain to the target domain. Current state-of-the-art generative adversarial network (GAN) models utilize time and space-costly operators to produce impressive translated images. However, further research and model deployment are under restrictions due to the high computational costs of the models. In order to resolve the problem, we enhance the GAN structure by employing a lightweight operator named involution that facilitates extracting both local features and long-range dependencies across channels. Besides, we also notice that previous works attach less importance to feature-level reconstruction discrepancy between original and reconstructed images. Nevertheless, such information is crucial in improving the quality of the synthesized images. Thus, we develop a novel loss term that evaluates the learned perceptual similarity distance to regulate the training process. The qualitative and quantitative experiment results on several prevailing benchmarks demonstrate that our model, dubbed InvolutionGAN, could produce competitive image results while saving computational costs up to 91.9%. In addition, extensive ablation studies are conducted to search for the best model structure and verify that each component we introduced is effective.
