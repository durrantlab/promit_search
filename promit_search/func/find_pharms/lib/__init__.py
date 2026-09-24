
""" Functions to help with find_pharm functions """

from .pharm_local import pharm_local
from .pharm_slurm import pharm_slurm
from .pharm_web import pharm_web

__all__ = ["pharm_local", "pharm_slurm", "pharm_web"]