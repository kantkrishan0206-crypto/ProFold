Profold Utilities 🛠️

Welcome to the Profold Utilities Module
This module provides helper functions and tools for handling molecular data, proteins, language models, and dataset splitting.

GitHub: Profold Repository

Available Utility Modules
Basic Utilities

Module: profold.utils.basic_utils
Functions:

mp_pool_map

load_json_config

Compound Tools

Module: profold.utils.compound_tools
Functions/Classes:

get_gasteiger_partial_charges

create_standardized_mol_id

check_smiles_validity

split_rdkit_mol_obj

get_largest_mol

rdchem_enum_to_list

CompoundKit

Compound3DKit

mol_to_graph_data

mol_to_md_graph_data

mol_to_polar_graph_data

mol_to_superedge_graph_data

Data Utilities

Module: profold.utils.data_utils
Functions:

save_data_list_to_npz

load_npz_to_data_list

get_part_files

Language Model Tools

Module: profold.utils.language_model_tools
Functions:

apply_bert_mask

Protein Tools

Module: profold.utils.protein_tools
Class:

ProteinTokenizer

Dataset Splitters

Module: profold.utils.splitters
Classes/Functions:

RandomSplitter

IndexSplitter

ScaffoldSplitter

RandomScaffoldSplitter

generate_scaffold

Quick Access

All utility modules can be imported directly via:

from profold.utils import basic_utils, compound_tools, data_utils, language_model_tools, protein_tools, splitters

Contribution

We welcome contributions to extend Profold utilities.
Open issues or pull requests in our official repo: Profold GitHub

License

This project is licensed under the MIT License.
You are free to use, modify, and distribute with attribution.
