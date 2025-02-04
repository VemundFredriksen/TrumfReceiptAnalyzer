from dataclasses import dataclass
from typing import List

@dataclass
class Varekategori:
    navn: str
    inkluderte_varer: List[str]