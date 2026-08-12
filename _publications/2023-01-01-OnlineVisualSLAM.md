---
title: "Online Visual SLAM Adaptation against Catastrophic Forgetting with Cycle-Consistent Contrastive Learning"
collection: publications
category: conferences
permalink: /publication/OnlineVisualSLAM
excerpt: 'Published in IEEE ICRA 2023 (2023). Cited by 3.'
date: 2023-01-01
venue: 'IEEE ICRA 2023'
paperurl: 'https://doi.org/10.1109/ICRA48891.2023.10161464'
citation: 'Sangni Xu, Hao Xiong, Qiuxia Wu, Tingting Yao, Zhihui Wang, et al. (2023). "Online Visual SLAM Adaptation against Catastrophic Forgetting with Cycle-Consistent Contrastive Learning" <i>IEEE ICRA 2023</i>.'
---
Visual SLAM (Simultaneous Localisation and Mapping) aims to simultaneously estimate camera poses and depth maps from navigation videos captured. While recent deep learning based methods have achieved great success on this task, they tend to work well on source domain data and suffer from performance degradation on the unseen data of target domain. Hence, we propose an online adaptation approach to continuously adapt a pre-trained visual SLAM model to changing environments in a self-supervised manner. To preserve pre-learned knowledge against catastrophic forgetting, we perform updating on a novel adapter proposed rather than fine-tuning the whole model for adaptation. The adapter includes a cross-domain feature translation module that translates pre-learned features into translated features suitable for adaptation. Ideally, the translated new features should not only contain pre-learned knowledge but also substantially distinct from pre-learned features since these two features represent different domains. We thus introduce cycle-consistent contrastive learning to maximize the dissimilarity between these two features by enlarging the distance between them in the feature space. Besides, our contrastive learning method exploiting cycle-consistency contraint enables the translated features to be transferred back to the pre-learned ones, which helps the translated features better preserve pre-learned knowledge. Comprehensive experiments on both synthetic and real-world datasets demonstrate superior adaptation performance of our proposed method over several state-of-the-art baselines.
