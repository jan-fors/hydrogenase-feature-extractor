from Bio.PDB import PDBParser

def extract_cofactors(pdb_file):
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure('protein', pdb_file)
    
    TWO_CHAR_ELEMENTS = {"FE", "NI", "CU", "ZN", "MG", "MN", "CO", "MO", "SE", "CA"}

    for atom in structure.get_atoms():
        raw_name = atom.get_name().strip()
        if raw_name in TWO_CHAR_ELEMENTS and atom.element != raw_name:
            atom.element = raw_name

    for atom in structure.get_atoms():
        if atom.element == "X" or atom.element == "":
            # Derive from atom name, stripping numbers
            name = atom.get_name().strip().lstrip("0123456789")
            atom.element = name.upper()[:-1] # remove number from FE1

    cofactors = []

    for model in structure:
        for chain in model:
            for residue in chain:
                # 'H_' indicates a HETATM (Hetero-atom)
                # 'W' would be water, which we usually want to skip
                res_id = residue.get_id()

                            
                if res_id[0].startswith('H_'):

                    res_name = residue.get_resname()
                    # Extract atom information as a tuple (name, element, coord)
                    atoms = tuple(
                        (atom.get_name(), atom.element, atom.get_coord()) 
                        for atom in residue
                    )

                    cofactors.append({
                        "resname": res_name,
                        "chain": chain.id,
                        "id": res_id[1],
                        "atoms": atoms
                    })
                    
    return cofactors
