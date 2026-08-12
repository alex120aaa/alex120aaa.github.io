---
title: "MoTeNet: Motion-Temporal Network for Dynamic Hand Gesture Recognition on Point Clouds"
collection: publications
category: conferences
permalink: /publication/MoTeNetMotion-TemporalNetwork
excerpt: 'Published in IJCB 2025 (2025).'
date: 2025-01-01
venue: 'IJCB 2025'
paperurl: 'https://doi.org/10.1109/IJCB65343.2025.11411209'
citation: 'Qiuxia Wu, Xinran Xie, Sangni Xu, Wenxiong Kang (2025). "MoTeNet: Motion-Temporal Network for Dynamic Hand Gesture Recognition on Point Clouds" <i>IJCB 2025</i>.'
---
As deep learning techniques are increasingly applied to gesture recognition, point cloud-based dynamic gesture recognition methods have attracted significant attention. However, many existing approaches overlook per-point motion features and the overall temporal dynamics of gestures, thereby failing to fully exploit motion and temporal cues embedded in point cloud sequences. To address this issue, we propose Motion-Temporal Network (MoTeNet), a novel framework for dynamic gesture recognition on point clouds, which preserves spatial structural information while modeling both global frame-level temporal changes and per-point motion. MoTeNet extracts spatial geometric features through a Hierarchical Graph Convolution (HGC) module, and incorporates a Motion Feature Encoding Module (MFEM) to encode point-level motion features across adjacent frames. This approach provides fine-grained dynamic information for subsequent temporal modeling. Furthermore, an Adaptive Temporal Feature Fusion (ATFF) module integrates convolutional neural networks (CNNs) and transformers to adaptively fuse short-term and long-term temporal dependencies, enabling comprehensive modeling of the dynamic evolution of gestures. Experimental results demonstrate that MoTeNet achieves state-of-the-art performance on point cloud gesture recognition benchmarks, including SHREC'17, DHG, and NVGesture, with ablation studies further validating the effectiveness of the proposed framework.
