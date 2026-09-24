
""" gets pharmacophores from web by uploading molecule """

import requests
from loguru import logger
SERVER = "https://pharmit.csb.pitt.edu/fcgi-bin/pharmitserv.fcgi"

class PharmitError(RuntimeError):
    pass


def get_pharmacophores(
    session: requests.Session,
    ligand_text: str,
    ligand_name: str,
    reckey: str | None = None,
    recname: str | None = None,
    timeout: float = 60.0,
) -> dict:
    """Submit a 'getpharma' request and return the parsed pharmacophore JSON.

    The server determines the input format from the ligand filename's extension.
    Molecular formats (sdf, pdb, mol2, xyz, ...) have their features derived;
    pharmacophore-query formats (json, ph4, pml, ...) are parsed straight through.

    Args:
        session (Session): the website querying session
        ligand_text: the full contents of the ligand file
        ligand_name: the ligand filename; its extension sets the parse format
        reckey: optional key of a receptor previously staged via upload_receptor
        recname: optional receptor filename (needed for its format extension)
        timeout: request timeout in seconds

    Returns:
        dict: the pharmacophore JSON, including the "points" list
    """
    payload = {
        "cmd": "getpharma",
        "ligand": ligand_text,
        "ligandname": ligand_name,
    }
    """data sent to the server. Tells it to derive a pharmacophore"""
    # attach the staged receptor for an interaction pharmacophore, if any
    if reckey is not None and recname is not None:
        payload["reckey"] = reckey
        payload["recname"] = recname

    resp = session.post(SERVER, data=payload, timeout=timeout)
    resp.raise_for_status()
    data = resp.json()

    # status == 0 signals a server-side error, with a message in "msg"
    if not data.get("status"):
        raise PharmitError(
            f"getpharma rejected: {data.get('msg', 'unknown error')}"
        )

    n_points = len(data.get("points", []))
    from_mol = data.get("mol")  # True if features were derived from a molecule
    logger.info(
        f" pharmacophore derived: {n_points} points"
        f" ({'from molecule' if from_mol else 'parsed from query file'})"
    )
    return data
