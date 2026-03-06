import os
from src.cofactor.extract_cofactors import extract_cofactors
from src.filter.apply_blacklist import apply_blacklist
from src.cofactor.sort import sort_into_active_site_and_fes_cluster
from src.utils.geometric_center import calculate_geometric_center
from src.cofactor.sort import sort_into_fes_order

def main(input_path : str, output : str, output_dir : str):
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

    if False:
        print(f"Proximal: {proximal['resname'] if proximal else 'None'}")
        print(f"Medial: {medial['resname'] if medial else 'None'}")
        print(f"Distal: {distal['resname'] if distal else 'None'}")    

    # distances between cofactors

    # write output
    pass