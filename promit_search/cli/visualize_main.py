from argparse import _SubParsersAction
import argparse

def add_subparsers(subparsers: _SubParsersAction) -> None:
    visualize_parser = subparsers.add_parser("visualize", help="Visualization tools.")
    visualize_subparsers = visualize_parser.add_subparsers(dest="tool")

    sdf_parser = visualize_subparsers.add_parser(
        "sdf", help="Generate 2D SVG figures from SDF files."
    )
    sdf_add_arguments(sdf_parser)
    sdf_parser.set_defaults(func=sdf_main)

    umap_parser = visualize_subparsers.add_parser(
        "umap", help="UMAP chemical space visualization with clustering."
    )
    umap_add_arguments(umap_parser)
    umap_parser.set_defaults(func=umap_main)