from dataclasses import dataclass

@dataclass
class Configs:
    BASE_URL = "https://api.lib.harvard.edu/v2/items.json?"
    LIMIT = 5
    ROOT_PATH = "/Users/jasonycwu/Documents/GitHub/harvardScript"
    TEST_OUTPUT_PATH = "/Users/jasonycwu/Documents/GitHub/harvardScript/testOutput.txt"
