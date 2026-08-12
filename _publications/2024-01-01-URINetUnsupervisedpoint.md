---
title: "URINet: Unsupervised point cloud rotation invariant representation learning via semantic and structural reasoning"
collection: publications
category: manuscripts
permalink: /publication/URINetUnsupervisedpoint
excerpt: 'Published in ICCV Workshops 2024 (2024).'
date: 2024-01-01
venue: 'ICCV Workshops 2024'
paperurl: 'https://doi.org/10.1016/j.cviu.2024.104136'
citation: 'Qiuxia Wu, Kunming Su (2024). "URINet: Unsupervised point cloud rotation invariant representation learning via semantic and structural reasoning" <i>ICCV Workshops 2024</i>.'
---
In recent years, many rotation-invariant networks have been proposed to alleviate the interference caused by point cloud arbitrary rotations. These networks have demonstrated powerful representation learning capabilities. However, most of those methods rely on costly manually annotated supervision for model training. Moreover, they fail to reason the structural relations and lose global information. To address these issues, we present an unsupervised method for achieving comprehensive rotation invariant representations without human annotation. Specifically, we propose a novel encoder–decoder architecture named URINet, which learns a point cloud representation by combining local semantic and global structural information, and then reconstructs the input without rotation perturbation. In detail, the encoder is a two-branch network where the graph convolution based structural branch models the relationships among local regions to learn global structural knowledge and the semantic branch learns rotation invariant local semantic features. The two branches derive complementary information and explore the point clouds comprehensively. Furthermore, to avoid the self-reconstruction ambiguity brought by uncertain poses, a bidirectional alignment is proposed to measure the quality of reconstruction results without orientation knowledge. Extensive experiments on downstream tasks show that the proposed method significantly surpasses existing state-of-the-art methods on both synthetic and real-world datasets.
