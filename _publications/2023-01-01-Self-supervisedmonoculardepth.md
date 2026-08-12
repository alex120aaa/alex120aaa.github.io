---
title: "Self-supervised monocular depth estimation via two mechanisms of attention-aware cost volume"
collection: publications
category: manuscripts
permalink: /publication/Self-supervisedmonoculardepth
excerpt: 'Published in The Visual Computer (2023). Cited by 3.'
date: 2023-01-01
venue: 'The Visual Computer'
paperurl: 'https://doi.org/10.1007/s00371-022-02704-x'
citation: 'Zhongcheng Hong, Qiuxia Wu (2023). "Self-supervised monocular depth estimation via two mechanisms of attention-aware cost volume" <i>The Visual Computer</i>.'
---
Self-supervised monocular depth estimation takes advantage of adjacent frame images as supervision signals for training, which has made a significant improvement in recovering holistic scene geometry. However, owing to these methods do not pay attention to the details of images, and the predicted depth maps are imprecise, where some small objects are neglected, object boundaries are blurred, as well as the predictions lack global consistency. Inspired by the excellent ability of the attention scheme to focus on details, we address these issues by using multi-frames to construct 3D cost volume and taking into account attention awareness for the cost volume so that the network is more inclined to learn important information from the cost volume. In this paper, we propose two mechanisms of attention-aware cost volume: voxel-wise attention-aware (VAA) network and recurrent attention-aware (RAA) network. For the VAA network, 3D convolution is exploited to reweight the 3D cost volume so as to enhance essential areas of the cost volume while suppressing unimportant areas. Therefore, our proposed VAA network can autonomously select the required details. For the RAA network, 3D cost volume is sequentially refined along the depth dimension with 2D convolutions, thereby expanding the receptive field in the depth range and achieving better global consistency. Experiments demonstrate that our methods outperform other self-supervised methods on the KITTI and Cityscapes datasets.
