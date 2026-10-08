import csv
import json
from loguru import logger
from pathlib import Path
from rdkit import Chem

from .log_pharms import log_pharms
from .update_pharm import update_pharm
from .get_valid_pharms import get_valid_pharms

from promit_search.io import json as pms_json



def main(sdf_path: Path, inter_dict: dict[str, list[int]],
    pharm_json_path: Path) -> dict:
    """Takes in list of atoms interacting on the ligand and
    the pharmacophore list for the ligand. It will then check
    each pharmacophore, see if it is actually interaction, then disable
    or enable it.

    Args:
        sdf_path: path of the SDF being checking
        inter_dict: dictionary matching interactions to atoms involved
        pharm_json_path: where the pharmacophore list for SDF is stored
    """
    # read in the pharmacophores concat json
    pharms: dict = pms_json.load(pharm_json_path)
    # modify pharmacophores
    supplier = Chem.SDMolSupplier(
        str(sdf_path), sanitize=True, removeHs=False, strictParsing=True
    )
    new_pharm: dict = {}
    valid_pharms: list[bool] = get_valid_pharms(
        pharms, supplier[0], inter_dict
    )
    log_pharms(sdf_path, valid_pharms)
    return update_pharm(pharms, valid_pharms)


