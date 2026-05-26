import numpy as np

def overlapping(atoms1: list, atoms2: list, radius: float = 1.0)-> bool:
    """
    checks whether two cofactors are overlapping
    """
    cutoff = 2.0 * radius

    for atom1 in atoms1:
        pos1 = np.asarray(atom1[2], dtype=float)

        for atom2 in atoms2:
            pos2 = np.asarray(atom2[2], dtype=float)

            if np.linalg.norm(pos1 - pos2) <= cutoff:
                return True

    return False

def remove_overlapping_cofactors(cofactor_list: list, radius: float = 1.0) -> list:
    """
    Iterates through a list of cofactors and removes overlapping ones.
    If two cofactors overlap, the first one is kept.

    Parameters
    ----------
    cofactor_list : list
        List of cofactors, where each cofactor is a list of atoms.
    radius : float
        Atomic radius used for overlap checking.

    Returns
    -------
    list
        Filtered list with only the first cofactor kept from overlapping groups.
    """
    kept = []

    for cofactor in cofactor_list:
        has_overlap = False

        for existing in kept:
            if overlapping(existing["atoms"], cofactor["atoms"], radius=radius):
                has_overlap = True
                break

        if not has_overlap:
            kept.append(cofactor)

    return kept