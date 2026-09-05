from hydrogenase_feature_extractor.feature.feature_handler import calculate_fingerprint_features, calculate_geometric_features
from hydrogenase_feature_extractor.pycaver.pycaver_handler import run_pycaver, read_results, caver_successful
from hydrogenase_feature_extractor.pdb.pdb_handler import copy_without_cofactor
from pathlib import Path
from hydrogenase_feature_extractor.cofactor.cofactor_handler import create_cofactor_dict
from hydrogenase_feature_extractor.cofactor.extract_cofactors import get_active_site_ids
from hydrogenase_feature_extractor.io.output_handler import write_output_file

def main(input_path : str, output_dir : str, results_table : bool, tunnel : bool, fingerprint_radius : float, caver_params : dict):
    """
    """
    # extract relevant cofactors
    cof_data = create_cofactor_dict(input_path=input_path)

    # calculate fingerprints
    cof_data = calculate_fingerprint_features(input_structure=input_path, cof_data=cof_data, radius=fingerprint_radius)

    # calculate distances and degrees
    cof_data = calculate_geometric_features(cof_data)
     
    for key in cof_data:
        if type(cof_data[key]) != dict:
            print(key + " ::: " + str(cof_data[key]))

    # pycaver
    if tunnel:
        # create structure without active site
        caver_input_structure_path = output_dir / Path("caver.pdb")
        copy_without_cofactor(input_path, get_active_site_ids(input_path), caver_input_structure_path)

        run_pycaver(caver_input_structure_path, caver_params, cof_data["active_site"]["center"], output_dir)

        if caver_successful(output_dir):
            caver_results = read_results(output_dir)
            cof_data = cof_data | caver_results

    # write output
    if results_table:
        pass

    write_output_file(output_dir, cof_data)
    