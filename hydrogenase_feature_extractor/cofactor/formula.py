

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
        formula_items = []

        for element, count in sorted(formula_dict.items(), key=lambda x: x[0]):
            if element == "O":
                continue
            formula_items.append(f"{count}{element}")

        formula = "".join(formula_items)

        return formula
    else:
        atoms = cofactor["atoms"]
        formula_dict = {}
        for atom in atoms:
            element = atom[1]
            if element in formula_dict:
                formula_dict[element] += 1
            else:
                formula_dict[element] = 1
        formula_items = []

        for element, count in sorted(formula_dict.items(), key=lambda x: x[0]):
            if element == "O":
                continue
            formula_items.append(f"{count}{element}")

        formula = "".join(formula_items)

        return formula # remove the last ";"