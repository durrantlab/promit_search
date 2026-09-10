
from pathlib import Path 

from promit_search.io import text

def create_single(body: list[str], output_file: Path, settings: dict = {},
                override_base_settings: bool = False):
    """Will take in a slumr body and settings and paste a slurm script
    at that location

    Args:
        body: the code that will go underneath settings
        output_file: where the slurm will be output
        settings: batch settings. Defaults to basic settings.
        override_base_settings: remove base settings.
    """
    # setup base settings, then add in new settings
    settings_base: dict = {
        "job-name": "name",
        "cluster": "smp",
        "partition": "preempt",
        "nodes": "1",
        "ntasks": "1",
        "cpus-per-task": "32",
        "mem": "32G",
        "time": "12:00:00",
        "output": "batch.out"
    }
    if not override_base_settings:
        settings_base.update(settings)
    else:
        settings_base = settings

    # create script
    slurm_text: list[str] = ["#!/bin/bash"]
    for (key, value) in settings_base.items():
        slurm_text.append(f"#SBATCH --{key}={value}")
    slurm_text.append("")
    slurm_text.append("module purge")
    slurm_text.append("module load pixi")
    slurm_text.append("")
    slurm_text.extend(body) 
    text.write(slurm_text, output_file)

