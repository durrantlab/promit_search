
import argparse
from pathlib import Path

from .main import run



def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Upload an SDF ligand to the Pharmit server and download the "
        "derived pharmacophore JSON."
    )
    parser.add_argument("sdf", type=Path, help="input SDF ligand file")
    parser.add_argument("out", type=Path, help="output pharmacophore JSON path")
    parser.add_argument(
        "--receptor",
        type=Path,
        default=None,
        help="optional posed receptor file for an interaction pharmacophore",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=120.0,
        help="request timeout in seconds (default: 120)",
    )
    parser.add_argument(
        "--log",
        type=Path,
        default=Path("pharmit_sdf_to_pharmacophore.log"),
        help="log file path",
    )
    args = parser.parse_args(argv)

    ok = run(
        sdf_path=args.sdf,
        out_path=args.out,
        timeout=args.timeout,
        receptor_path=args.receptor,
    )
    return 0 if ok else 1