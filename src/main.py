import os
from src.cofactor.extract_cofactors import extract_cofactors
from src.filter.apply_blacklist import apply_blacklist
from src.cofactor.sort import sort_into_active_site_and_fes_cluster
from src.utils.geometric_center import calculate_geometric_center
from src.cofactor.sort import sort_into_fes_order
from src.cofactor.formula import get_formula

def main(input_path : str, output : str, output_dir : str, results_table : bool):
    """
    """
    # read the input structure

    # read cofactors
    cofactors = extract_cofactors(input_path)
    
    # apply blacklist
    cofactors = apply_blacklist(cofactors)
    
    # classify hydrogenase specific cofactors -> proximal ...
    active_site, fes_cluster = sort_into_active_site_and_fes_cluster(cofactors)
    
    #TODO add verbose function
    if False:
        print(f"Active site: {[cofactor['resname'] for cofactor in active_site]}")
        print(f"FeS cluster: {[cofactor['resname'] for cofactor in fes_cluster]}")

    active_site_geometric_center = calculate_geometric_center(active_site, activesite=True)
    
    proximal, medial, distal = sort_into_fes_order(fes_cluster, active_site_geometric_center)

    active_site_formula = get_formula(active_site)
    proximal["formula"] = get_formula(proximal)
    medial["formula"] = get_formula(medial)
    distal["formula"] = get_formula(distal)

    if False:
        print(f"Proximal: {proximal['resname'] if proximal else 'None'}")
        print(f"Medial: {medial['resname'] if medial else 'None'}")
        print(f"Distal: {distal['resname'] if distal else 'None'}")    

    # distances between cofactors

    # write output
    if results_table:
        from src.io.result_table import write_to_results_table

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
    
    print(f"{input_path} -> {output_dir}/{output} Done.")