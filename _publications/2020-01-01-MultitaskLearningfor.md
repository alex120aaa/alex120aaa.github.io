---
title: "Multitask Learning for Video-based Surgical Skill Assessment"
collection: publications
category: conferences
permalink: /publication/MultitaskLearningfor
excerpt: 'Published in DICTA 2020 (2020). Cited by 16.'
date: 2020-01-01
venue: 'DICTA 2020'
paperurl: 'https://doi.org/10.1109/DICTA51227.2020.9363408'
citation: 'Zhiteng Jian, Wenxi Yue, Qiuxia Wu, Wei Li, Zhiyong Wang, et al. (2020). "Multitask Learning for Video-based Surgical Skill Assessment" <i>DICTA 2020</i>.'
---
Surgical skill assessment (SSA) plays a vital role in medical systems for reducing intraoperative surgical errors and improving clinical outcomes. To ensure objective and efficient SSA, many automatic video-based SSA methods have been developed. In particular, various deep learning methods have been devised recently by utilising CNN or RNN-based networks for various skill assessment tasks (e.g., skill level prediction). While predicting overall skill levels and assessing detailed attribute-based scores are highly correlated, most existing studies deal with these two tasks separately, without fully exploiting different information sources encoded in a dataset. In contrast, we propose a novel end-to-end multitask learning framework to conduct skill level classification and attribute score regression jointly. Specifically, our network incorporates two branches for the two tasks, which share earlier layers for feature extraction and hold different prediction layers for specific targets. The shared feature extractor is optimised under the supervision of both tasks simultaneously, encouraging the model to consider information from different aspects and their relatedness to learn richer and more generalised features. In addition, since not every part of a surgical video contributes to skill assessment equally, we enhance an existing feature extractor I3D with a novel Spatio-Temporal Channel Attention Module to emphasize important features. Experimental results on the public dataset JIGSAWS show that our proposed network outperforms state-of-the-art models on both skill classification and score regression tasks.
