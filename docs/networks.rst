Profold Networks 🏗️

Welcome to the Profold Networks Module
This module provides building blocks for neural networks in protein, molecular, and drug-target modeling pipelines.

GitHub: Profold Repository

Available Network Blocks
Basic Block

Module: profold.networks.basic_block
Classes:

Activation

MLP

Compound Encoder

Module: profold.networks.compound_encoder
Classes:

AtomEmbedding

BondEmbedding

GNN Block

Module: profold.networks.gnn_block
Classes/Functions:

GraphNorm

MeanPool

GIN

Involution Block

Module: profold.networks.involution_block
Class:

Involution2D

LSTM Block

Module: profold.networks.lstm_block
Functions/Classes:

lstm_encoder

Optimizer

Module: profold.networks.optimizer
Class:

AdamW

Pre/Post Processing

Module: profold.networks.pre_post_process
Function:

pre_post_process_layer

ResNet Block

Module: profold.networks.resnet_block
Functions/Classes:

resnet_encoder

Transformer Block

Module: profold.networks.transformer_block
Functions/Classes:

multi_head_attention

positionwise_feed_forward

transformer_encoder_layer

transformer_encoder

Quick Access

All networks can be imported directly via:

from profold.networks import basic_block, compound_encoder, gnn_block, involution_block, lstm_block, optimizer, pre_post_process, resnet_block, transformer_block

Contribution

We welcome contributions to extend Profold networks.
Open issues or pull requests in our official repo: Profold GitHub

License

This project is licensed under the MIT License.
You are free to use, modify, and distribute with attribution.
