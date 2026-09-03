import os
from hydrogenase_feature_extractor.cofactor.extract_cofactors import extract_cofactors
from hydrogenase_feature_extractor.filter.apply_blacklist import apply_blacklist
from hydrogenase_feature_extractor.cofactor.sort import sort_into_active_site_and_fes_cluster
from hydrogenase_feature_extractor.utils.geometric_center import calculate_geometric_center
from hydrogenase_feature_extractor.cofactor.sort import sort_into_fes_order
from hydrogenase_feature_extractor.cofactor.formula import get_formula
from hydrogenase_feature_extractor.filter.overlap import remove_overlapping_cofactors
from hydrogenase_feature_extractor.fingerprint.calculate_fingerprint import create_fingerprint
from hydrogenase_feature_extractor.io.result_table import write_to_results_table, write_to_raw_results_table
from hydrogenase_feature_extractor.pycaver.pycaver_handler import run_pycaver
from hydrogenase_feature_extractor.pdb.pdb_handler import copy_without_cofactor
from pathlib import Path

def main(input_path : str, output_dir : str, results_table : bool, tunnel : bool, fingerprint_radius : float, caver_params : dict):
    """
    """
    # read cofactors
    cofactors = extract_cofactors(input_path)
   
    # apply blacklist
    cofactors = apply_blacklist(cofactors)
            
    # classify hydrogenase specific cofactors -> proximal ...
    active_site, fes_cluster = sort_into_active_site_and_fes_cluster(cofactors)
    
    # check if there are overlapping fes clusters
    fes_cluster = remove_overlapping_cofactors(fes_cluster, 1.0)

    # calculate geometric centers
    active_site_geometric_center = calculate_geometric_center(active_site, activesite=True)

    # calculate distances to active site
    sorted_fes_cluster = sort_into_fes_order(fes_cluster, active_site_geometric_center)

    # calculate aa fingerprints
    for i in range(len(sorted_fes_cluster)):
        F =  create_fingerprint(input_path, sorted_fes_cluster[i]["atoms"], fingerprint_radius)
        sorted_fes_cluster[i]["fingerprint"] = F

    # standard format
    proximal = sorted_fes_cluster[0]
    medial = sorted_fes_cluster[1]
    distal = sorted_fes_cluster[2]
    
    active_site_formula = get_formula(active_site)
    proximal["formula"] = get_formula(proximal)
    medial["formula"] = get_formula(medial)
    distal["formula"] = get_formula(distal)   

    # calculate geometric centers
    proximal_center = calculate_geometric_center([proximal], "proximal")
    medial_center = calculate_geometric_center([medial], "medial")
    distal_center = calculate_geometric_center([distal], "distal")

    # pycaver
    if tunnel:
        # create structure without active site
        active_site_res_ids = []
        for i in active_site:
            active_site_res_ids.append(i["id"])
        caver_input_structure_path = output_dir / Path("caver.pdb")
        copy_without_cofactor(input_path, active_site_res_ids, caver_input_structure_path)

        run_pycaver(caver_input_structure_path, caver_params, active_site_geometric_center[1], output_dir)

    # write output
    if results_table:
        raw_results = {
            "active_site_res_name": ";".join([cofactor["resname"] for cofactor in active_site]),
            "active_site_formula": active_site_formula,
        }

        for cl in sorted_fes_cluster:
            fingerprint = ""
            for i in cl["fingerprint"]:
                fingerprint += str(i) +","
            fingerprint = fingerprint[:-1]
            raw_results[f"{sorted_fes_cluster.index(cl)}_cl_res_name"] = cl["resname"]
            raw_results[f"{sorted_fes_cluster.index(cl)}_cl_formula"] = get_formula(cl)
            raw_results[f"{sorted_fes_cluster.index(cl)}_cl_fingerprint"] = fingerprint

        write_to_raw_results_table(output_dir, os.path.basename(input_path), raw_results)

        # standard hyd format
        results = {
            "active_site_res_name": ";".join([cofactor["resname"] for cofactor in active_site]),
            "active_site_formula": active_site_formula,
            "proximal_res_name": proximal["resname"] if proximal else "None",
            "proximal_formula": proximal["formula"] if proximal else "None",
            "medial_res_name": medial["resname"] if medial else "None",
            "medial_formula": medial["formula"] if medial else "None",
            "distal_res_name": distal["resname"] if distal else "None",
            "distal_formula": distal["formula"] if distal else "None"
        }

        write_to_results_table(output_dir, os.path.basename(input_path), results)
    
    # TODO write output 

    #print(f"{input_path} -> {output_dir}/{output} Done.")