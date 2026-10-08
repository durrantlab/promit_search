from pathlib import Path 
from loguru import logger


def match_sdf_json(sdf_list: list[Path], json_list: list[Path]) -> dict[Path, Path]:
    """Takes in a list of SDFs and JSONs (validated), and finds the JSON
    that corresponds with each SDF. Linked if they have same file name. Returns
    dictionary where SDF path is key, JSON path is value.
 
    Args:
        sdf_list: list of SDF paths
        json_list: list of JSON paths
 
    Warns:
        If an SDF does not have a respective JSON, logs a warning
        If a JSON does not have a respective SDF, logs a warning
 
    Returns:
        Dictionary matching SDF Paths to respective JSON Paths
    """
    # index JSONs by file name without extension
    json_by_stem: dict[str, Path] = {}
    for json_file in json_list:
        stem = json_file.stem
        json_by_stem[stem] = json_file
 
    matched: dict[Path, Path] = {}
    matched_stems: set[str] = set()
    for sdf_file in sdf_list:
        stem = sdf_file.stem
        if stem not in json_by_stem:
            logger.warning(f"No matching JSON for SDF: {sdf_file}")
            continue
        matched[sdf_file] = json_by_stem[stem]
        matched_stems.add(stem)
 
    for stem, json_file in json_by_stem.items():
        if stem not in matched_stems:
            logger.warning(f"No matching SDF for JSON: {json_file}")
 
    return matched

