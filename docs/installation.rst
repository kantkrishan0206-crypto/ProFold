Profold Installation Guide 🛠️
Table of Contents

Prerequisites

Dependencies

Installation Instructions

Prerequisites

OS Support: Windows, Linux, macOS

Python Version: 3.6, 3.7, 3.8+

Dependencies
Name	Version Requirement
numpy	-
pandas	-
networkx	-
torch/tensorflow	>=1.10 (depends on backend)
rdkit	-
scikit-learn	-

(- means no specific version requirement)

Installation Instructions

Since some dependencies like rdkit require conda, we recommend creating a new conda environment for Profold installation.

Install Conda (if not already installed)

Download from Anaconda
 or Miniconda

Create a new environment

conda create -n profold python=3.7
conda activate profold


Install rdkit using conda

conda install -c conda-forge rdkit


Install the deep learning backend

GPU version (if you have a CUDA-enabled GPU):

python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118


CPU version:

python -m pip install torch torchvision torchaudio


Install Profold dependencies

pip install numpy pandas networkx scikit-learn
pip install pgl  # optional if using graph modules


Install Profold

pip install profold

Deactivating the environment

After using Profold, you can deactivate your conda environment:

conda deactivate
