
from promit_search.cli.create_pharm_JSON import single_file

def test_create_pharm_JSON():
    single_file.create_pharm_JSON("files/caffeine.sdf","tests/output/create_pharm_json")
    pass



if __name__ == "__main__":
    test_create_pharm_JSON()