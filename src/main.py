import os
from src.cofactor.extract_cofactors import extract_cofactors
from src.filter.apply_blacklist import apply_blacklist
from src.cofactor.sort import sort_into_active_site_and_fes_cluster
from src.utils.geometric_center import calculate_geometric_center
from src.cofactor.sort import sort_into_fes_order
from src.cofactor.formula import get_formula
from src.filter.overlap import remove_overlapping_cofactors
from src.fingerprint.calculate_fingerprint import create_fingerprint

def main(input_path : str, output : str, output_dir : str, results_table : bool):
    """
    """
    # read the input structure
    print(f"extracting {input_path}")

    # read cofactors
    cofactors = extract_cofactors(input_path)
   
    # apply blacklist
    cofactors = apply_blacklist(cofactors)
    
        
    # classify hydrogenase specific cofactors -> proximal ...
    active_site, fes_cluster = sort_into_active_site_and_fes_cluster(cofactors)
    
    #TODO add verbose function
    if True:
        print(f"Active site: {[cofactor['resname'] for cofactor in active_site]}")
        print(f"FeS cluster: {[cofactor['resname'] for cofactor in fes_cluster]}")


    # check if there are overlapping fes clusters
    fes_cluster = remove_overlapping_cofactors(fes_cluster, 1.0)

    active_site_geometric_center = calculate_geometric_center(active_site, activesite=True)
    
    # calculate distances to active site

    sorted_fes_cluster = sort_into_fes_order(fes_cluster, active_site_geometric_center)

    # calculate aa fingerprints
    #print(type(sorted_fes_cluster[0]), sorted_fes_cluster[0])
    for i in range(len(sorted_fes_cluster)):
        F =  create_fingerprint(input_path, sorted_fes_cluster[i]["atoms"])
        sorted_fes_cluster[i]["fingerprint"] = F

    # standard format
    proximal = sorted_fes_cluster[0]
    medial = sorted_fes_cluster[1]
    distal = sorted_fes_cluster[2]
    
    active_site_formula = get_formula(active_site)
    proximal["formula"] = get_formula(proximal)
    medial["formula"] = get_formula(medial)
    distal["formula"] = get_formula(distal)

    if True:
        print(f"Proximal: {proximal['resname'] if proximal else 'None'} {proximal['formula'] if proximal else 'None'}")
        print(f"F: {proximal['fingerprint']}")
        print(f"Medial: {medial['resname'] if medial else 'None'} {medial['formula'] if medial else 'None'}")
        print(f"F: {medial['fingerprint']}")
        print(f"Distal: {distal['resname'] if distal else 'None'} {distal['formula'] if distal else 'None'}")    
        print(f"F: {distal['fingerprint']}")

    # write output
    if results_table:
        from src.io.result_table import write_to_results_table, write_to_raw_results_table

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

    print(f"{input_path} -> {output_dir}/{output} Done.")