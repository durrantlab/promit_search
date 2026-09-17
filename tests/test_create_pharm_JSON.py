
from promit_search.func.create_pharm_JSON import create_pharm_JSON_single

def test_create_pharm_JSON():
    create_pharm_JSON_single("files/caffeine.sdf","tests/output/create_pharm_json", create_directories=True)
    pass



if __name__ == "__main__":
    test_create_pharm_JSON()