from pathlib import Path
from typing import List
from Bio.PDB import PDBParser, PDBIO, Select

def copy_without_cofactor(input_strucutre : Path, cofactor_res_ids : List, output_path : Path):
    """
    """
    class _RemoveCofactor(Select):
        def accept_residue(self, residue):
            het_flag, resseq, icode = residue.get_id()
            is_hetatm = het_flag != " "
            if is_hetatm and resseq in cofactor_res_ids:
                return False
            return True

    parser = PDBParser(QUIET=True)
    structure = parser.get_structure(input_strucutre.stem, str(input_strucutre))

    io = PDBIO()
    io.set_structure(structure)
    io.save(str(output_path), select=_RemoveCofactor())

    return output_path


def get_structure(structure_path : Path):
    """
    """
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("s", str(structure_path))

    return structure