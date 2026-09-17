
from promit_search.func.create_pharm_JSON import single_file

def test_create_pharm_JSON():
    """Status: simply runs, does not validate pharm_json.single_file"""
    single_file("input/caffeine.sdf","output/create_pharm_json", create_directories=True, pharmit_run="slurm")
    single_file("input/caffeine.sdf","output/create_pharm_json", create_directories=True,  pharmit_run="web")
    single_file("input/caffeine.sdf","output/create_pharm_json", create_directories=True,  pharmit_run="local")

    pass



if __name__ == "__main__":
    test_create_pharm_JSON()