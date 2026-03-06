import numpy as np

def calculate_geometric_center(cofactors, name : str = None, activesite : bool = False) -> tuple[str, tuple[float, float, float]]:
    """
    """
    coords = []
    for cof in cofactors:
        atoms = cof["atoms"]
        for atom in atoms:
            coords.append(atom[2])
    M = np.vstack(coords)
    
    if activesite:
        name = "activesite"
    elif name is None:
        name = "unknown"
    else:
        name = name
        
    return name, _calculate_center(M)

def _calculate_center(M : np.ndarray) -> tuple[float,float,float]:
    """
    """
    if M.ndim != 2 or M.shape[1] != 3:
        raise ValueError(f"Expected array of shape (N,3), got {M.shape}")

    center = np.mean(M, axis=0)

    return float(center[0]), float(center[1]), float(center[2])