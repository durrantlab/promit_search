
""" takes in an sdf file, runs pharmacophore generation, and returns json """

from pathlib import Path
import subprocess
from loguru import logger

def get_pharms(sdf_file: Path, out_file: Path):
    """Will take in the SDF file and output the pharm json
    in out_file.

    Args:
        sdf_file: path with SDF finding the pharmacophores for
        out_file: where the result is placed
    
    Raise:
        Exception: if running pharmit fails for any reason
    """
    logger.info(f"Running Pharmit on {sdf_file}. Writing to {out_file}")
    subprocess.run(
        ["pharmit", "pharma", "-in", str(sdf_file), "-out", str(out_file)],
        check=True
    )
