"""Module containing the feature names used in the TFRecords of this repo."""

# Overall Tasks
LIBRARY_MATCHING = 'library_matching'
SPECTRUM_PREDICTION = 'spectrum_prediction'

# Feature names
ATOM_WEIGHTS = 'atom_weights'
MOLECULE_WEIGHT = 'molecule_weight'
CIRCULAR_FP_BASENAME = 'circular_fp'
COUNTING_CIRCULAR_FP_BASENAME = 'counting_circular_fp'
INDEX_TO_GROUND_TRUTH_ARRAY = 'index_in_library'

FP_TYPE_LIST = [
    CIRCULAR_FP_BASENAME, COUNTING_CIRCULAR_FP_BASENAME
]

DENSE_MASS_SPEC = 'dense_mass_spec'
INCHIKEY = 'inchikey'
NAME = 'name'
SMILES = 'smiles'
MOLECULAR_FORMULA = 'molecular_formula'
ADJACENCY_MATRIX = 'adjacency_matrix'
ATOM_IDS = 'atom_id'
SMILES_TOKEN_LIST_LENGTH = 'smiles_sequence_len'