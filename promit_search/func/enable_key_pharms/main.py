
from pathlib import Path
from loguru import logger
import warnings

with warnings.catch_warnings(record=True):
    import prolif as plf
    from rdkit import Chem

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

from promit_search.io import gen
from promit_search.io import sdf
from promit_search.io import json

from .lib.match_sdf_json import match_sdf_json
from .lib.get_op_path import get_op_path
from .lib.enable_pharms import enable_pharms
from .lib.setup_prolif_setts import setup_prolif_setts

def main(input_dir: str, protein_file: str, output_dir: str, prolif_settings: dict[str,str]={}, 
         flatten: bool = True, create_dir: bool = True) -> None:
    """Will take in a directory with JSON and SDF pairs (should have same name). It will
    find all interactions between each molecule and protein, then enable / disable 
    pharmacophores depending on result.

    Args:
        input_dir: directory that holds all SDFs and JSONs. Can have subdirectories
        protein_file: the PDB the molecules were docked to / crystallized with
        output_dir: where the final JSONs will be placed
        prolif_settings: alternative settings for interaction finder program.
            Default is cut-offs that lined up with our chemical intuition
        flatten: if the directory structure of input is copied, or if all final
            JSONs are put into root directory
        create_dir: if the output directory will be created if it does not
            exist
    """
    # validate other inputs
    protein_file: Path = Path(protein_file).resolve()
    gen.file_verify(protein_file)
    rdkit_prot = Chem.MolFromPDBFile(str(protein_file), removeHs=False)
    protein_mol = plf.Molecule(rdkit_prot)
    output_dir: Path = Path(output_dir).resolve()
    gen.dir_verify(output_dir, create_dir)
    # set up prolif settings
    prolif_settings = setup_prolif_setts(prolif_settings)
    # get all SDFs
    input_dir: Path = Path(input_dir).resolve()
    gen.dir_verify(input_dir, False)
    sdf_files: list[Path] = gen.find_files_rec(input_dir, ["sdf"])
    temp_sdf: list[Path] = []
    for sdf_file in sdf_files:
        try:
            sdf.validate(sdf_file)
            temp_sdf.append(sdf_file)
        except:
            logger.warning("SDF molecule {} is invalid. Skipping.".format(sdf_file))
    sdf_files = temp_sdf
    # get all JSONs
    json_files: list[Path] = gen.find_files_rec(input_dir, ["json"])
    temp_json: list[Path] = []
    for json_file in json_files:
        valid_dict: dict = {"points":["x","y","z","enabled","name"]}
        try:
            json.validate(json_file, valid_dict)
            temp_json.append(json_file)
        except:
            logger.warning("pharmacophore JSON {} is invalid. Skipping.".format(json_file))
    json_files = temp_json
    # pair up JSONs and SDFs
    sdf_to_json: dict[Path, Path] = match_sdf_json(sdf_files, json_files)
    # for each pair, enable / disable pharmacophores following interaction profile
    for sdf_path, json_path in sdf_to_json.items():
        op_json_path: Path = get_op_path(output_dir, input_dir, sdf_path, flatten)
        enable_pharms(sdf_path,json_path, 
                    protein_mol, prolif_settings, op_json_path)
        
