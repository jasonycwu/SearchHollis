# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:25:35
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-06-29 02:17:22
from dataclasses import dataclass
import os


@dataclass
class Configs:
    BASE_URL = "https://api.lib.harvard.edu/v2/items.json?"
    LIMIT = 5
    ROOT_PATH = "/Users/jasonycwu/Documents/GitHub/harvardScript"
    TEST_ROOT = os.path.join(ROOT_PATH, "tests")
    INPUT_PATH = os.path.join(TEST_ROOT, "input")
    OUTPUT_PATH = os.path.join(TEST_ROOT, "output")
    TEST_IUTPUT_TXT_PATH = os.path.join(INPUT_PATH, "testInput.txt")
    TEST_OUTPUT_TXT_PATH = os.path.join(OUTPUT_PATH, "testOutput.txt")
