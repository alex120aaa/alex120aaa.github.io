---
title: "Distinguishing and Matching-Aware Unsupervised Point Cloud Completion"
collection: publications
category: manuscripts
permalink: /publication/DistinguishingandMatching-Aware
excerpt: 'Published in IEEE Transactions on Circuits and Systems for Video Technology (TCSVT) (2023). Cited by 18.'
date: 2023-01-01
venue: 'IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)'
paperurl: 'https://doi.org/10.1109/TCSVT.2023.3250970'
citation: 'Haihong Xiao, Yuqiong Li, Wenxiong Kang, Qiuxia Wu (2023). "Distinguishing and Matching-Aware Unsupervised Point Cloud Completion" <i>IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)</i>.'
---
Real-scanned point clouds are often incomplete due to occlusion, light reflection and limitations of sensor resolution, which impedes the related progress of downstream tasks, e.g., shape classification and object detection. Although there has been impressive research progress on the point cloud completion topic, they rely on the premise of extensive paired training data. However, collecting complete point clouds in some specified scenarios is labor-intensive and even impractical. To mitigate this problem, we propose DMNet, a distinguishing and matching-aware unsupervised point cloud completion network. Our work belongs to the group of unsupervised completion methods but goes beyond previous studies. Firstly, we propose a distinguishing-aware feature extractor to learn discriminable semantic information for different instances, simultaneously enhancing the robust invariant representation under noise disturbances. Secondly, we design a hierarchy-aware hyperbolic decoder to recover the complete geometry of point clouds, which not only can capture the implicit hierarchical relationships in data but also has an explicit extended nature. Finally, we develop a matching-aware refiner to eliminate noise points via aligning the topology structure of the input and predicted partial point clouds. Extensive experiments on MVP, Completion3D and KITTI datasets prove the effectiveness of our method, which performs favorably over state-of-the-art methods both quantitatively and qualitatively.
