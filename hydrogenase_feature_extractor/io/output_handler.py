from pathlib import Path
import json
import numpy as np

def write_output_file(specific_output_dir : Path, cof_data : dict):
    """
    """
    output_file = specific_output_dir / Path("features.json")
    with open(output_file, "w") as f:
        json.dump(cof_data, f, cls=NumpyEncoder, indent=2)

def write_to_results_table(general_output_dir : Path):
    """
    """
    pass

class NumpyEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, np.ndarray):
            return o.tolist()
        if isinstance(o, (np.integer,)):
            return int(o)
        if isinstance(o, (np.floating,)):
            return float(o)
        return super().default(o)