from dataclasses import dataclass
from typing import List
from models.varekategori import Varekategori

@dataclass
class Kategori:
    navn: str
    exclusive: bool
    kategorier: List[Varekategori]

