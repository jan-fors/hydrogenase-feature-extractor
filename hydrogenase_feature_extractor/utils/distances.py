import numpy as np

def _calculate_distance(pointA : np.array, pointB : np.array) -> float:
    """
    Calculate the distance between two points in 3D space.
    
    :param
    pointA : Point
    pointB : Point  

    :return
    float : The distance between the two points.
    """
    return ((pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2 + (pointA[2] - pointB[2])**2)**0.5

def calculate_shortest_distance_between_cofactors(cofactorA : dict, cofactorB : dict) -> float:
    """
    """
    distances = []
    for atom1 in cofactorA["atoms"]:
        for atom2 in cofactorB["atoms"]:
            atom1_coords = atom1["coordinates"]
            atom2_coords = atom2["coordinates"]
            distances.append(_calculate_distance(atom1_coords, atom2_coords))

    return float(min(distances))