from dataclasses import dataclass
from typing import List

@dataclass
class ItemCategory:
    name: str
    included_items: List[str]