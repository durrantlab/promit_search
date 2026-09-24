
""" main function that returns the pharmacophores """

import json
from pathlib import Path
import requests
from loguru import logger

SERVER = "https://pharmit.csb.pitt.edu/fcgi-bin/pharmitserv.fcgi"


from .lib import *

class PharmitError(RuntimeError):
    pass


def main(
    sdf_path: Path,
    out_path: Path,
    timeout: float = 120.0,
    receptor_path: Path | None = None,
) -> bool:
    """Overall, takes in an SDF ligand, uploads it to the server, then returns
    the derived pharmacophore JSON.

    This is the inverse of the pharmacophore-search workflow: instead of sending
    a pharmacophore and getting back molecules, it sends a molecule and gets back
    a pharmacophore.

    Args:
        sdf_path: location of the SDF ligand to derive features from
        out_path: location where the pharmacophore JSON will be placed
                        make sure file does not already exist before running
        timeout: how long before saying the server timed out (seconds)
        receptor_path: optional receptor structure. If provided, the server
                        returns an *interaction* pharmacophore (only the ligand
                        features relevant to binding the receptor). The ligand
                        must already be posed in the receptor's frame; pharmit
                        does not dock.
        FILE_LOG: location where the log file will be placed

    Returns:
        Boolean if the server returned a pharmacophore with at least one point
    """
    if out_path.is_file():
        logger.warning("PHARMIT OUTPUT FILE ALREADY EXISTS. OVERWRITING")

    # read in the ligand structure
    ligand_text = sdf_path.read_text()
    ligand_name = sdf_path.name
    logger.info(f" loaded ligand: {ligand_name} ({len(ligand_text)} bytes)")

    success = False
    with requests.Session() as session:
        # if a receptor was supplied, stage it on the server first so that
        # getpharma can reference it by key for an interaction pharmacophore
        reckey = recname = None
        if receptor_path is not None:
            reckey, recname = upload_receptor(session, receptor_path, timeout)

        # derive the pharmacophore from the ligand
        pharma = get_pharmacophores(
            session,
            ligand_text,
            ligand_name,
            reckey=reckey,
            recname=recname,
            timeout=timeout,
        )

        n_points = len(pharma.get("points", []))
        if n_points > 0:
            save_pharmacophores(pharma, out_path)
            success = True
        else:
            logger.info(" server returned no pharmacophore points; skipping save")

    return success


