from hydrogenase_feature_extractor.utils.constants import (
    ACTIVE_SITE_ATOMS,
    FES_ATOMS,
)
from hydrogenase_feature_extractor.utils.geometric_center import calculate_geometric_center

def sort_into_active_site_and_fes_cluster(cofactors):
    """
    Sort cofactors into active site and FeS cluster based on their atoms.
    """
    fes_cluster = []
    active_site = []

    for cofactor in cofactors:
        cofactor_atoms = cofactor["atoms"]
        cofactor_atom_elements = [atom[1] for atom in cofactor_atoms]
        
        if all(elem in FES_ATOMS for elem in cofactor_atom_elements) and len(cofactor_atom_elements) > 2:
            fes_cluster.append(cofactor)
            continue
        elif all(elem in ACTIVE_SITE_ATOMS for elem in cofactor_atom_elements) or "NI" in cofactor_atom_elements:
            active_site.append(cofactor)


    return active_site, fes_cluster


def sort_into_fes_order(fes_cluster, active_site_geometric_center):
    """
    Sort FeS clusters into proximal, medial, and distal based on their distance to the active site geometric center.
    """
    distances = []
    for cofactor in fes_cluster:
        _, cofactor_center = calculate_geometric_center(cofactors=[cofactor], name=cofactor["resname"])
        distance = ((cofactor_center[0] - active_site_geometric_center[1][0]) ** 2 + 
                    (cofactor_center[1] - active_site_geometric_center[1][1]) ** 2 + 
                    (cofactor_center[2] - active_site_geometric_center[1][2]) ** 2) ** 0.5
        distances.append((cofactor, distance))

    # Sort by distance
    distances.sort(key=lambda x: x[1])

    return [d[0] for d in distances]