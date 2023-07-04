# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:18:58
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-07-04 11:36:29
from dataclasses import dataclass
from typing import List


@dataclass
class Payload:
    ISBN: list
    FULL_TITLE: str
    AUTHOR: str
    PUBLISHER: str
    PUB_YEAR: str
    TITLES: List[str]
