from dataclasses import dataclass

@dataclass
class Payload:
    ISBN: list
    TITLE: str
    AUTHOR: str
    PUBLISHER: str
    PUB_YEAR: str