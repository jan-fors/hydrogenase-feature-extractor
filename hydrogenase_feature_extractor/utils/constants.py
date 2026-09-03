

COFACTOR_BLACKLIST = [
    "FEL", "DTN", "FE2", "MPD","CL", "IMD", "CSD", "OCS", "PSW", "CA", "SE7", 
    "UOX","CO3", "SBY", "CL", "H2S", "HOH", "SO4", "MRD", "VK3", "DHI", "TRS", 
    "IMD", "CSO", "PEG", "LMT", "PO4", "NA", "LI", "MLA", "CSX", "OXY", "H2S", 
    "MQ9", "GOL", "KR", "MG", "BU3", "FAD", "ZN", "FES", "EDO", "144" # remove as well?
]

ACTIVE_SITE_ATOMS = [
    "FE", "NI", "C", "N", "O"
]

FES_ATOMS = [
    "FE", "S", "O" # O just in degraded clusters
]

RESULT_TABLE_NAME = "results_table"
RAW_RESULT_TABLE_NAME = "raw_results_table"

RESULT_TABLE_COLUMNS = [
    "input_path",
    "active_site_res_name",
    "active_site_formula",
    "proximal_res_name",
    "proximal_formula",
    "medial_res_name",
    "medial_formula",
    "distal_res_name",
    "distal_formula"
]

FINGERPRINT_RADIUS = 6.0

#### CAVER ####
SHELL_RADIUS = 3.0
SHELL_DEPTH = 4.0
PROBE_RADIUS = 0.9
DESIRED_RADIUS = 3.0
MAX_DISTANCE = 5.0
