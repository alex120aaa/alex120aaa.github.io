---
title: "基于在线签名的动静态特征提取方法实现"
date: 2021-05-24
type: "RESEARCH-BASED DEGREE SUPERVISION"
student: "Yuhang Song (宋雨杭)"
degree: "Bachelor's Thesis (本科毕业设计)"
program: "Software Engineering, School of Software Engineering"
excerpt: "This bachelor's thesis proposes a novel online signature verification system that extracts both dynamic and static features. A CNN-based autoencoder extracts static features from signature images, while a GRU-based autoencoder extracts dynamic features from trajectory information. A Siamese network with early and late fusion strategies verifies signature authenticity. The method achieved a 9.24% EER on the SCUT-MMSIG in-air signature dataset, the best known result at the time."
---

This bachelor's thesis, supervised by Qiuxia Wu, proposes a novel online signature verification system to extract both dynamic and static features from online signatures. For static features, a convolutional neural network (CNN) based autoencoder is used to extract features from signature images. For dynamic features, a gated recurrent unit (GRU) based autoencoder processes the trajectory data. Finally, a Siamese network with early and late fusion strategies is employed to fuse the features and verify signature authenticity. The system was benchmarked on SCUT-MMSIG, SigWiComp2013, SVC2004, and MCYT-Signature-100 datasets, achieving a 9.24% equal error rate (EER) on the SCUT-MMSIG in-air signature subset — the best known result on this dataset at the time.
