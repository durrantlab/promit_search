
from promit_search.func.create_pharm_JSON import single_file

def test_create_pharm_JSON():
    single_file("files/caffeine.sdf","tests/output/create_pharm_json", create_directories=True)
    pass



if __name__ == "__main__":
    test_create_pharm_JSON()