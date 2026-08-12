---
title: "SRENet: Spectral Re-Entry Network for Point Cloud Action Recognition"
collection: publications
category: manuscripts
permalink: /publication/SRENetSpectralRe-Entry
excerpt: 'Published in IEEE Transactions on Circuits and Systems for Video Technology (TCSVT) (2026).'
date: 2026-01-01
venue: 'IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)'
paperurl: 'https://doi.org/10.1109/TCSVT.2026.3695515'
citation: 'Qiuxia Wu, Jiarui Lan, Wenxiong Kang, Zhiyong Wang, Kun Hu (2026). "SRENet: Spectral Re-Entry Network for Point Cloud Action Recognition" <i>IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)</i>.'
---
Recognizing human actions from point cloud sequences is critical for 3D perception driven applications such as autonomous driving and human-computer interaction. However, the irregular structure and temporal inconsistency of point clouds pose unique challenges for spatio-temporal representation learning, especially in capturing both global motion context and fine-grained temporal dynamics. We propose SRENet, a spectral-aware framework designed to explicitly learn both global context and fine-grained temporal dynamics of motion from a frequency perspective for action recognition. SRENet introduces a Spectral Decomposition Block (SDeBlock) that performs wavelet-based analysis along temporal and spatial axes, disentangling features into low- and high-frequency components with frequency-specific attention. To recover residual dynamics and re-align temporal frequency structures distorted during semantic fusion, a Spectral Re-entry Block (SReBlock) performs secondary temporal decomposition. Furthermore, a spectral-aware learning strategy is devised to enhance discriminability in both frequency subspaces via contrastive loss and a curriculum schedule that gradually shifts focus from low- to high-frequency spaces in line with coarse to detailed motion patterns. Extensive experiments on MSR-Action3D, NTU-RGBD and NTU-RGBD120 demonstrate that SRENet achieves state-of-the-art performance, validating the effectiveness of frequency modeling in point cloud-based action understanding 1.
