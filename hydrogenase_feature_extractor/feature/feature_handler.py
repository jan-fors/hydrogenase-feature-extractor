from pathlib import Path
from hydrogenase_feature_extractor.fingerprint.calculate_fingerprint import count_aminoacids
from hydrogenase_feature_extractor.utils.distances import calculate_shortest_distance_between_cofactors
from hydrogenase_feature_extractor.utils.degree import calculate_degree_at_point

def calculate_fingerprint_features(input_structure : Path, cof_data : dict, radius : float) -> dict:
    """
    """
    for cof in cof_data:
        # caclulcate fingerprint
        cof_data[cof]["fingerprint"] = count_aminoacids(input_structure, cof_data[cof]["center"], radius)
    return cof_data

def calculate_geometric_features(cof_data : dict) -> dict:
    """
    """
    # calculate distances
    cof_data["active_site_proximal_min_distance"] = calculate_shortest_distance_between_cofactors(cofactorA=cof_data["active_site"], cofactorB=cof_data["proximal"])
    cof_data["active_site_medial_min_distance"] = calculate_shortest_distance_between_cofactors(cofactorA=cof_data["active_site"], cofactorB=cof_data["medial"])
    cof_data["active_site_distal_min_distance"] = calculate_shortest_distance_between_cofactors(cofactorA=cof_data["active_site"], cofactorB=cof_data["distal"])

    cof_data["proximal_medial_min_distance"] = calculate_shortest_distance_between_cofactors(cofactorA=cof_data["proximal"], cofactorB=cof_data["medial"])
    cof_data["proximal_distal_min_distance"] = calculate_shortest_distance_between_cofactors(cofactorA=cof_data["proximal"], cofactorB=cof_data["distal"])

    cof_data["medial_distal_min_distance"] = calculate_shortest_distance_between_cofactors(cofactorA=cof_data["medial"], cofactorB=cof_data["distal"])

    # cacluclate degrees
    cof_data["degree_proximal"] = calculate_degree_at_point(cof_data["active_site"]["center"], cof_data["medial"]["center"], cof_data["proximal"]["center"])
    cof_data["degree_medial"] = calculate_degree_at_point(cof_data["proximal"]["center"], cof_data["distal"]["center"], cof_data["medial"]["center"])

    return cof_data