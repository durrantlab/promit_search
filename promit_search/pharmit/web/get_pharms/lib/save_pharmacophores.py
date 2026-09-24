
""" takes in pharmacophore JSOn and writes it """

from pathlib import Path 
from loguru import logger 
import json



def save_pharmacophores(pharma: dict, out_path: Path) -> Path:
    """Write the pharmacophore JSON to disk.

    The transport-only "status" flag is dropped so the saved file is a clean
    pharmacophore/session JSON, matching what pharmit's "Save Session" produces
    and what the search workflow (start_query) expects as input.

    Args:
        pharma: the JSON returned by get_pharmacophore
        out_path: where the JSON will be written

    Returns:
        Path: the JSON file path
    """
    to_save = {k: v for k, v in pharma.items() if k != "status"}
    out_path.write_text(json.dumps(to_save, indent=2))
    logger.info(
        f" wrote pharmacophore ({len(to_save.get('points', []))} points) -> {out_path}"
    )
    return out_path
