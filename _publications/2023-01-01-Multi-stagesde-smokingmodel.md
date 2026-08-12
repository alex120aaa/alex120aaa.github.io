---
title: "Multi-stages de-smoking model based on CycleGAN for surgical de-smoking"
collection: publications
category: manuscripts
permalink: /publication/Multi-stagesde-smokingmodel
excerpt: 'Published in International Journal of Machine Learning and Cybernetics (2023). Cited by 14.'
date: 2023-01-01
venue: 'International Journal of Machine Learning and Cybernetics'
paperurl: 'https://doi.org/10.1007/s13042-023-01875-w'
citation: 'Xinpei Su, Qiuxia Wu (2023). "Multi-stages de-smoking model based on CycleGAN for surgical de-smoking" <i>International Journal of Machine Learning and Cybernetics</i>.'
---
Smoke generated during laparoscopic surgery blocks the doctor’s sight and degrades the quality of the images severely; thus, surgical de-smoking is a crucial task during laparoscopic surgery. Previous deep learning methods extract the features of smoke images to restore clear images using convolutional neural networks. However, these methods training on simulated images result in performance degradation when generalized to real smoke images. In this paper, we introduce cycle generative adversarial networks to bridge the gap between simulated and real surgical images. Therefore, we propose a multi-stages surgical de-smoking model based on cycle generative adversarial networks(MS-CycleGAN). By leveraging the convolutional neural networks-based de-smoking module in the first stage, we additionally utilize the simulated-to-real module in the second stage to pull simulated smoke-free images to the real surgical domain, generating real-like smoke-free images that even the discriminator cannot distinguish from real smoke-free images. Furthermore, to make real images and de-smoking images more consistent in image feature space instead of pixel space, the perceptual loss function is employed to calculate the loss in feature space. MS-CycleGAN outperforms state-of-the-art de-smoking methods on the evaluation metrics of both Peak Signal to Noise Ratio and Structural Similarity Index Measure. Most importantly, our MS-CycleGAN achieves qualitatively superior results on de-smoking for real surgical smoke images.
