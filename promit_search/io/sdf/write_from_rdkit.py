
""" Take in a list of rdkit molecules and write SDFs """

from pathlib import Path
import warnings

with warnings.catch_warnings(record=True):
    from rdkit import Chem

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)



def write_from_rdkit(mols: Chem.SDMolSupplier | Chem.Mol, sdf_file: Path):
    """From the molecule supplier, write out all the rdkit
    molecules to an sdf

    Args:
        mols (Chem.SDMolSupplier): list of molecules to write
        sdf_file (Path): sdf file it is written out to
    """

    with Chem.SDWriter(sdf_file) as writer:
        if isinstance(mols, Chem.SDMolSupplier):
            for mol in mols:
                if mol is None:      # skip records that failed to parse
                    continue
                writer.write(mol)
        else:
            writer.write(mols)