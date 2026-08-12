---
title: "PVLNet: Parameterized-View-Learning neural network for 3D shape recognition"
collection: publications
category: manuscripts
permalink: /publication/PVLNetParameterized-View-Learningneural
excerpt: 'Published in Computers & Graphics (2021). Cited by 4.'
date: 2021-01-01
venue: 'Computers & Graphics'
paperurl: 'https://doi.org/10.1016/j.cag.2021.04.036'
citation: 'Hongbin Xu, Lvequan Wang, Qiuxia Wu, Wenxiong Kang (2021). "PVLNet: Parameterized-View-Learning neural network for 3D shape recognition" <i>Computers & Graphics</i>.'
---
3D shape recognition has drawn much attention in recent years. Despite the amazing progress on view-based 3D feature description, previous multi-view based methods suffer from a burden in computation efficiency compared with point cloud based methods. To overcome the limitation, we propose a novel light-weight multi-view based network built on parameterized-view-learning mechanism, PVLNet, which can achieve the state-of-the-art performance with only 1/10 FLOPs compared with previous multi-view based methods. Guided by the parameterized-view-learning mechanism, the views are directly built as parameters of PVLNet which can be automatically optimized by gradient descent. A simplified differentiable depth map generator is used to ensure the gradient propagation when generating depth images from view parameters. Then multi-view features extracted by CNNs are aggregated by global max-pooling. Our experimental results on ModelNet40 and ScanObjectNN demonstrate the superior performance of the proposed method. The visualization of the networks attention further interprets the efficiency of our PVLNet.
