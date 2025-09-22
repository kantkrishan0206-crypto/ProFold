Profold Featurizers ⚙️

Welcome to the Profold Featurizers Module
This module provides graph- and feature-based processing for proteins, molecules, and drug-target interactions.

GitHub: Profold Repository

Available Featurizers

HET GNN Featurizer
Module: profold.featurizers.het_gnn_featurizer
Class: DDiFeaturizer
Functions:

num_nodes_stat

nx_graph_build

Pretrain GNN Featurizer
Module: profold.featurizers.pretrain_gnn_featurizer
Classes:

AttrmaskTransformFn

AttrmaskCollateFn

SupervisedTransformFn

SupervisedCollateFn

Quick Access

All featurizers can be imported directly via:

from profold.featurizers import het_gnn_featurizer, pretrain_gnn_featurizer

Contribution

We welcome contributions to extend Profold featurizers.
Open issues or pull requests in our official repo: Profold GitHub

License

This project is licensed under the MIT License.
You are free to use, modify, and distribute with attribution.
