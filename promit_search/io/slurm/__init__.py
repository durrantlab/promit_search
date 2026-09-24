
""" Helps write / edit slurm scripts """


from .create_single import create_single
from .create_multi import create_multi

__all__ = ["create_single", "create_multi"]