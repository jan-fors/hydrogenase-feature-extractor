from pathlib import Path
from hydrogenase_feature_extractor.cofactor.extract_cofactors import extract_cofactors
from hydrogenase_feature_extractor.filter.apply_blacklist import apply_blacklist
from hydrogenase_feature_extractor.cofactor.sort import sort_into_active_site_and_fes_cluster, sort_by_distance, sort_into_pmd
from hydrogenase_feature_extractor.filter.overlap import remove_overlapping_cofactors
from hydrogenase_feature_extractor.cofactor.formula import get_formula
import numpy as np

def create_cofactor_dict(input_path : Path) -> dict:
    """
    Read the input structure and create a dictionary containing the following keys:
    - active_site
    - proximal
    - medial
    - distal
    """
    # read cofactors
    cofactors = extract_cofactors(input_path)
       
    # apply blacklist
    cofactors = apply_blacklist(cofactors)

    # classify hydrogenase specific cofactors -> proximal ...
    active_site, fes_cluster = sort_into_active_site_and_fes_cluster(cofactors)

    # check if there are overlapping fes clusters
    fes_cluster = remove_overlapping_cofactors(fes_cluster, 1.0)

    res = {
        "active_site" : {
            "center": None,
            "atoms": [],
            "formula": None
        },
        "proximal": {
            "center": None,
            "atoms": [],
            "formula": None
        },
        "medial": {
            "center": None,
            "atoms": [],
            "formula": None
        },
        "distal": {
            "center": None,
            "atoms": [],
            "formula": None
        }
    }

    active_site_center, active_site_atoms = _extract_center_and_atoms(active_site)

    res["active_site"]["center"] = active_site_center
    res["active_site"]["atoms"] = active_site_atoms
    res["active_site"]["formula"] = get_formula(active_site)

    # sort by distances
    sorted_fes_cluster = sort_by_distance(fes_cluster, active_site_center)

    if len(sorted_fes_cluster) == 3: # standard case
        proximal, medial, distal = sort_into_pmd(sorted_fes_cluster)
        
        proximal_center, proximal_atoms = _extract_center_and_atoms(proximal)
        res["proximal"]["center"] = proximal_center
        res["proximal"]["atoms"] = proximal_atoms
        res["proximal"]["formula"] = get_formula(proximal)

        medial_center, medial_atoms = _extract_center_and_atoms(medial)
        res["medial"]["center"] = medial_center
        res["medial"]["atoms"] = medial_atoms
        res["medial"]["formula"] = get_formula(medial)

        distal_center, distal_atoms = _extract_center_and_atoms(distal)
        res["distal"]["center"] = distal_center
        res["distal"]["atoms"] = distal_atoms
        res["distal"]["formula"] = get_formula(distal)

    elif len(sorted_fes_cluster) > 3: # use only 3 nearest
        sorted_fes_cluster = sorted_fes_cluster[:3]

        proximal, medial, distal = sort_into_pmd(sorted_fes_cluster)
                
        proximal_center, proximal_atoms = _extract_center_and_atoms(proximal)
        res["proximal"]["center"] = proximal_center
        res["proximal"]["atoms"] = proximal_atoms
        res["proximal"]["formula"] = get_formula(proximal)

        medial_center, medial_atoms = _extract_center_and_atoms(medial)
        res["medial"]["center"] = medial_center
        res["medial"]["atoms"] = medial_atoms
        res["medial"]["formula"] = get_formula(medial)

        distal_center, distal_atoms = _extract_center_and_atoms(distal)
        res["distal"]["center"] = distal_center
        res["distal"]["atoms"] = distal_atoms
        res["distal"]["formula"] = get_formula(distal)

    else:
        # check what positions they match
        proximal, medial, distal = sort_into_pmd(sorted_fes_cluster)

        if proximal != None:
            proximal_center, proximal_atoms = _extract_center_and_atoms(proximal)
            res["proximal"]["center"] = proximal_center
            res["proximal"]["atoms"] = proximal_atoms
            res["proximal"]["formula"] = get_formula(proximal)

        if medial != None:
            medial_center, medial_atoms = _extract_center_and_atoms(medial)
            res["medial"]["center"] = medial_center
            res["medial"]["atoms"] = medial_atoms
            res["medial"]["formula"] = get_formula(medial)

        if distal != None:
            distal_center, distal_atoms = _extract_center_and_atoms(distal)
            res["distal"]["center"] = distal_center
            res["distal"]["atoms"] = distal_atoms
            res["distal"]["formula"] = get_formula(distal)
        
    return res

def _extract_center_and_atoms(cofactor) -> tuple:
    """
    """
    atoms = []
    coords = np.array([0.0, 0.0, 0.0])
    if type(cofactor) == list:
        for residue in cofactor:
            for atom in residue["atoms"]:
                atoms.append({
                    "coordinates": atom[2],
                    "element": atom[1],
                    "name": atom[0]
                })

                coords[0] += atom[2][0]
                coords[1] += atom[2][1]
                coords[2] += atom[2][2]

        return coords / len(atoms), atoms
    elif type(cofactor) == dict:
        for atom in cofactor["atoms"]:
                atoms.append({
                    "coordinates": atom[2],
                    "element": atom[1],
                    "name": atom[0]
                })

                coords[0] += atom[2][0]
                coords[1] += atom[2][1]
                coords[2] += atom[2][2]

        return coords / len(atoms), atoms