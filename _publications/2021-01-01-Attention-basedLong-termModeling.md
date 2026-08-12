---
title: "Attention-based Long-term Modeling for Deep Visual Odometry"
collection: publications
category: conferences
permalink: /publication/Attention-basedLong-termModeling
excerpt: 'Published in DICTA 2021 (2021). Cited by 5.'
date: 2021-01-01
venue: 'DICTA 2021'
paperurl: 'https://doi.org/10.1109/DICTA52665.2021.9647140'
citation: 'Sangni Xu, Hao Xiong, Qiuxia Wu, Zhiyong Wang (2021). "Attention-based Long-term Modeling for Deep Visual Odometry" <i>DICTA 2021</i>.'
---
Visual odometry (VO) aims to determine the positions of a moving camera from an image sequence it acquired. It has been extensively utilized in many applications such as AR/VR, autonomous driving, and robotics. Conventional VO methods largely rely on hand-crafted features and data association that are in fact unreliable and suffering from fast motions. Therefore, learning-based VO utilizes neural networks mapping an image sequence to corresponding camera poses directly. Most existing learning-based methods also integrate with additional Long Short-Term Memory (LSTM) networks to model the temporal context across images, since the camera pose estimation of an image in VO is highly relevant to other images in the same sequence. However, traditional LSTM is limited to model short-term dependency rather than long-term temporal context or global information. To mitigate this issue, we propose an attention based long-term modelling approach by devising a new fusion gate into the LSTM cell. Our method consists of two modules: convolutional motion encoder and recurrent global motion refinement module. Specifically, the convolutional motion encoder extracts from images motion features which are then fused by the refinement module with more long-term temporal information. In the refinement module, the devised fusion gate generates long-term temporal information in two phases: (1) extracting correlated long-term information from previous predictions through a devised attention module; and (2) updating the current hidden state with extracted long-term information. As a result, it enables our model to gather long-term temporal information and further enhance estimation accuracy. We comprehensively evaluate our proposed method on two public datasets, KITTI and Oxford RobotCar. The experimental results demonstrate the effectiveness and superiority of our method over the baseline model.
