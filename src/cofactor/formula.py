

def get_formula(cofactor) -> str:
    """"""
    if type(cofactor) == list:
        # if it's a list of cofactors, we need to sum up the formulas
        formula_dict = {}
        for cofactor in cofactor:
            atoms = cofactor["atoms"]
            for atom in atoms:
                element = atom[1]
                if element in formula_dict:
                    formula_dict[element] += 1
                else:
                    formula_dict[element] = 1
        formula = ""    
        for element, count in formula_dict.items():
            formula += f"{count if count > 1 else ''}{element};"
        return formula[:-1]
    else:
        atoms = cofactor["atoms"]
        formula_dict = {}
        for atom in atoms:
            element = atom[1]
            if element in formula_dict:
                formula_dict[element] += 1
            else:
                formula_dict[element] = 1
        formula = ""    
        for element, count in formula_dict.items():
            formula += f"{count if count > 1 else ''}{element};"
        return formula[:-1] # remove the last ";"