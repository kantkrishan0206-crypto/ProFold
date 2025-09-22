Profold Model Zoo 🧠

Welcome to the Profold Model Zoo
This module provides pre-trained and configurable models for protein sequences, graph-based learning, and sequence generative modeling.

GitHub: Profold Repository

Available Models
Pretrain GNNs Model

Module: profold.model_zoo.pretrain_gnns_model
Classes:

PretrainGNNModel

AttrmaskModel

SupervisedModel

Protein Sequence Models

Module: profold.model_zoo.protein_sequence_model
Classes:

LstmEncoderModel

ResnetEncoderModel

TransformerEncoderModel

PretrainTaskModel

SeqClassificationTaskModel

ClassificationTaskModel

RegressionTaskModel

ProteinEncoderModel

ProteinModel

ProteinCriterion

Sequence VAE Model

Module: profold.model_zoo.seq_vae_model
Class:

VAE

Quick Access

All models can be imported directly via:

from profold.model_zoo import pretrain_gnns_model, protein_sequence_model, seq_vae_model

Contribution

We welcome contributions to extend Profold models.
Open issues or pull requests in our official repo: Profold GitHub

License

This project is licensed under the MIT License.
You are free to use, modify, and distribute with attribution.
