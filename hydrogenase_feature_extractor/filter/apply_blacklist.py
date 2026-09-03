from hydrogenase_feature_extractor.utils.constants import COFACTOR_BLACKLIST


def apply_blacklist(cofactors):
    """"""
    return [cof for cof in cofactors if cof["resname"] not in COFACTOR_BLACKLIST]