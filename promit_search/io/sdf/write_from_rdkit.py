
""" Take in a list of rdkit molecules and write SDFs """

from pathlib import Path
import warnings
from loguru import logger

with warnings.catch_warnings(record=True):
    from rdkit import Chem

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

from promit_search.io import gen


def write_from_rdkit(mols: Chem.SDMolSupplier | Chem.Mol, sdf_file: Path):
    """From the molecule supplier, write out all the rdkit
    molecules to an sdf

    Args:
        mols (Chem.SDMolSupplier): list of molecules to write
        sdf_file (Path): sdf file it is written out to
    
    Raise:
        Exception: if cant write to sdf_file for whatever reason
    """
    logger.info(f"Writing mol to {sdf_file}")
    # check if file exists already
    gen.file_exist_warn(sdf_file, "overwriting file")
    # writ out
    try:
        with Chem.SDWriter(sdf_file) as writer:
            if isinstance(mols, Chem.SDMolSupplier):
                for mol in mols:
                    if mol is None:      # skip records that failed to parse
                        continue
                    writer.write(mol)
            else:
                writer.write(mols)
    except:
        mess = f"Failed to write rdkit to {sdf_file}"
        logger.error(mess)
        raise Exception(mess)