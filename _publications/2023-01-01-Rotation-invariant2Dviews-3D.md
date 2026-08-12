---
title: "Rotation-invariant 2D views-3D point clouds auto-encoder; [旋转不变的 2D 视图-3D 点云自编码器]"
collection: publications
category: manuscripts
permalink: /publication/Rotation-invariant2Dviews-3D
excerpt: 'Published in 光学精密工程 (2023).'
date: 2023-01-01
venue: '光学精密工程'
paperurl: 'https://doi.org/10.37188/OPE.20233105.0656'
citation: 'Xianying Liu, Qiuxia Wu, Wenxiong Kang, Yuqiong Li (2023). "Rotation-invariant 2D views-3D point clouds auto-encoder; [旋转不变的 2D 视图-3D 点云自编码器]" <i>光学精密工程</i>.'
---
The unsupervised representation learning of point clouds is crucial for understanding and analyz⁃ ing point clouds，and a 3D reconstruction-based autoencoder is an important architecture in unsupervised learning. To address the rotation interference and insufficient feature learning capability of existing autoen⁃ coders，this study proposes a rotation-invariant 2D views-3D point clouds autoencoder. First，a local fu⁃ sion global rotation-invariant feature conversion strategy is designed. For the local representation，the in⁃ put point clouds are transformed into handcrafted rotation-invariant features；for the global representation，an alignment module based on PCA is proposed to align the rotating point clouds under the same pose to exclude the rotation interference while complementing the global information. Then，for the encoder，the local and non-local module are designed to fully extract the local spatial features and non-local contextual correlations of the point cloud and model the semantic consistency between different levels of features. Fi⁃ nally，a PCA alignment-based decoding method for 2D-3D reconstruction is proposed for reconstructing the aligned 3D point clouds and 2D views such that the point-cloud representation output from the encoder integrates rich learning signals from the 3D point clouds and 2D views. Experiments demonstrate that the recognition accuracies of this algorithm are 90. 84% and 89. 02% on the randomly rotated synthetic dataset ModelNet40 and real dataset ScanObjectNN，respectively. Moreover，the learned point-cloud representa⁃ tions achieve good discriminability without label supervision and have a good rotational robustness.
