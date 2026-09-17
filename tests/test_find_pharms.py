
from promit_search.func.find_pharms import single_file
from pathlib import Path
import shutil

def test_create_pharm_JSON():
    """Status: simply runs, does not validate pharm_json.single_file"""
    if Path("output/create_pharm_json").is_dir():
        shutil.rmtree(Path("output/create_pharm_json"))

    single_file("input/caffeine.sdf","output/create_pharm_json/slurm", create_directories=True, pharmit_run="slurm")
    single_file("input/caffeine.sdf","output/create_pharm_json/web", create_directories=True,  pharmit_run="web")
    single_file("input/caffeine.sdf","output/create_pharm_json/local", create_directories=True,  pharmit_run="local")

    pass



if __name__ == "__main__":
    test_create_pharm_JSON()