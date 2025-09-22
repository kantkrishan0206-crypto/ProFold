Profold Datasets 📚

Welcome to the Profold Datasets Module
This repository contains datasets for protein, molecular, and drug-target modeling. All datasets are preprocessed and ready for use in Profold pipelines.

GitHub: Profold Repository

Available Datasets

BACE Dataset
Functions: get_default_bace_task_names, load_bace_dataset

BBBP Dataset
Functions: get_default_bbbp_task_names, load_bbbp_dataset

ChEMBL Filtered Dataset
Functions: get_chembl_filtered_task_num, load_chembl_filtered_dataset, _load_chembl_filtered_dataset

ClinTox Dataset
Functions: get_default_clintox_task_names, load_clintox_dataset

Davis Dataset
Functions: load_davis_dataset

DDI Dataset
Functions: get_default_ddi_task_names, load_ddi_dataset

DTI Dataset
Functions: get_default_dti_task_names, load_dti_dataset

ESOL Dataset
Functions: get_default_esol_task_names, get_default_esol_range, load_esol_dataset

FreeSolv Dataset
Functions: get_default_freesolv_task_names, get_default_freesolv_range, load_freesolv_dataset

HIV Dataset
Functions: get_default_hiv_task_names, load_hiv_dataset

InMemory Dataset
Class: InMemoryDataset

KIBA Dataset
Functions: load_kiba_dataset

Lipophilicity Dataset
Functions: get_default_lipophilicity_task_names, get_default_lipophilicity_range, load_lipophilicity_dataset

MUV Dataset
Functions: get_default_muv_task_names, load_muv_dataset

PPI Dataset
Functions: get_default_ppi_task_names, load_ppi_dataset

SIDER Dataset
Functions: get_default_sider_task_names, load_sider_dataset

TOX21 Dataset
Functions: get_default_tox21_task_names, load_tox21_dataset

TOXCAST Dataset
Functions: get_default_toxcast_task_names, load_toxcast_dataset

ZINC Dataset
Functions: load_zinc_dataset, _load_zinc_dataset

Quick Access

All datasets can be imported directly via:

from profold.datasets import bace_dataset, bbbp_dataset, clintox_dataset, ...

Contribution

We welcome contributions to extend Profold datasets.
Open issues or pull requests in our official repo: Profold GitHub

License

This project is licensed under the MIT License.
You are free to use, modify, and distribute with attribution.
