# -*- coding: utf-8 -*-
# @Author: Jason Y. Wu
# @Date:   2023-06-23 01:18:58
# @Last Modified by:   Jason Y. Wu
# @Last Modified time: 2023-06-29 00:27:51
from dataclasses import dataclass


@dataclass
class Payload:
    ISBN: list
    TITLE: str
    AUTHOR: str
    PUBLISHER: str
    PUB_YEAR: str
