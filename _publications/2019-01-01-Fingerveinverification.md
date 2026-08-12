---
title: "Finger vein verification using a Siamese CNN"
collection: publications
category: manuscripts
permalink: /publication/Fingerveinverification
excerpt: 'Published in IET Biometrics (2019). Cited by 65.'
date: 2019-01-01
venue: 'IET Biometrics'
paperurl: 'https://doi.org/10.1049/iet-bmt.2018.5245'
citation: 'Su Tang, Shan Zhou, Wenxiong Kang, Qiuxia Wu, Feiqi Deng (2019). "Finger vein verification using a Siamese CNN" <i>IET Biometrics</i>.'
---
Finger vein verification has received more attention recently due to its unique advantages. However, most existing algorithms rely on handcrafted features, making them less robust to finger rotation and offsets. To alleviate these problems, the authors propose a novel method to extract more discriminative features from finger vein images. First, facing the issue of insufficient training data, they adopt a heavy image augmentation strategy and develop a pretrained-weights based convolutional neural network (CNN). Second, focusing on the characteristics of finger vein verification, they construct a Siamese structure combining with a modified contrastive loss function for training the above CNN, which effectively improves the network's performance. Finally, considering the feasibility of deploying the above CNN on embedded devices, they construct a lightweight CNN with depthwise separable convolution and adopt a knowledge distillation method to learn the knowledge from the pretrained-weights based CNN, which makes it small but effective. The experimental results show that the size of the lightweight CNN shrinks to 1/6th of the pretrained-weights based CNN, while its equal error rates achieved in the MMCBNU_6000, FV-USM and SDUMLA-HMT datasets are 0.08, 0.11 and 0.75% respectively, which nearly stays the same with the pretrained-weights based CNN and surpasses state-of-the-art methods. .,, . ., .
