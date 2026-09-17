from pathlib import Path
import requests
import hashlib
from loguru import logger

SERVER = "https://pharmit.csb.pitt.edu/fcgi-bin/pharmitserv.fcgi"


def upload_receptor(
    session: requests.Session, receptor_path: Path, timeout: float
) -> tuple[str, str]:
    """Stage a receptor on the server so an interaction pharmacophore can be built.

    The server stores the receptor under a client-chosen key and later retrieves
    it when getpharma is called with a matching 'reckey'. Any stable key works as
    long as the same one is used for both calls, so we hash the receptor contents.

    Args:
        session (Session): the website querying session
        receptor_path: location of the receptor structure file
        timeout: request timeout in seconds

    Returns:
        tuple: (reckey, recname) to pass along to get_pharmacophore
    """
    receptor_text = receptor_path.read_text()
    recname = receptor_path.name
    # deterministic key derived from the receptor contents
    reckey = hashlib.md5(receptor_text.encode()).hexdigest()

    payload = {"cmd": "setreceptor", "key": reckey, "receptor": receptor_text}
    resp = session.post(SERVER, data=payload, timeout=timeout)
    resp.raise_for_status()

    # server replies with plain text "saved" or "exists"
    logger.info(
        f" uploaded receptor {recname} (key={reckey}): {resp.text.strip() or 'ok'}"
    )
    return reckey, recname

