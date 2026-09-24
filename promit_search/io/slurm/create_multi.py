
""" Create a slurm file that will split commands over many jobs """

from pathlib import Path 

from .create_single import create_single
from promit_search.io import text

def create_multi(body: list[str], output_file: Path, settings: dict = {},
                override_base_settings: bool = False):
    """Creates files required to do parallel batch jobs. Each line
    in body will be a seperate run. Creates 3 files in directory of output:
    output_file, job_list.txt, [name of output_file].sh. If they are already
    present, will override them

    Args:
        body: all commands to be run. Each will be seperate
        output_file: where the .slurm file is placed
            All other files will be put in this directory as well
        settings: batch settings. Defaults to basic settings.
        override_base_settings: remove base settings.
    """
    # setup settings
    if not override_base_settings:
        settings["output"] = "logs/%A_%a.out"
        settings["error"] = "logs/%x_%A_%a.err"

    # create slurm
    slurm_body: list[str] = []
    slurm_body.append("""ARGS=$(awk -v line=$((SLURM_ARRAY_TASK_ID + 1)) 'NR == line {print $0}' "job_list.txt")""")
    slurm_body.append("""LOG="${OUT%.sdf}.log" """)

    slurm_body.append(f"""$ARGS | tee "$LOG" """)
    slurm_body.append("""echo "Done!" """)
    create_single(slurm_body, output_file, settings, override_base_settings)

    # create job list
    job_list_path: Path = (output_file.parent / "job_list.txt").resolve()
    text.write(body, job_list_path)

    # create 
    bash_path: Path = (output_file.parent / f"{output_file.stem}.sh").resolve()
    text.write(f"sbatch --array=0-{len(body)-1} --export=ALL {output_file.name}", bash_path)
