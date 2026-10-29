
from pathlib import Path
from promit_search.io import gen
from loguru import logger

def get_validate_recursive(input_dir: Path, file_type: str, validate, valid_kwarg = {}) -> list[Path]:
    """Takes in a directory to recursively search. Will then 
    validate each result and only return ones that pass

    Args:
        input_dir: directory searched for file type
        file_type: the file type searched for
        validate: function to validate file typ

    Returns:
        list of validated file types
    """
    gen.dir_verify(input_dir, False)
    files: list[Path] = gen.find_files_rec(input_dir, [file_type])
    validate_files: list[Path] = []
    for file in files:
        try:
            validate(file, **valid_kwarg)
            validate_files.append(file)
        except:
            logger.warning("{} file {} is invalid. Skipping.".format(file_type, file))
    return validate_files