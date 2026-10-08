from loguru import logger
from pathlib import Path 


def get_op_path(op_dir: Path, input_parent: Path, input_path: Path, flatten: bool) -> Path:
    """Takes in an input path and the shared parent. It will then find the path
    to create that same relative path in output. If flatten is False, then it will
    just put file with same name in the root of output.

    Args:
        op_dir: the OP directory where all outputs are placed
        input_parent: the directory that holds all inputs
        input_path: the path trying to replicate in op_dir
        flatten: if placing it in root or following
            directory structure of inpiut

    Returns:
        the input files new path in op_dir
    """

    if not flatten:
        diff: Path = input_path.relative_to(input_parent)
        return (op_dir / diff).resolve()
    else:
        return (op_dir / input_path.name).resolve()