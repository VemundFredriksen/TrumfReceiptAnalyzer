from dataclasses import dataclass
from typing import List
from models.item_category import ItemCategory

@dataclass
class Category:
    name: str
    exclusive: bool
    categories: List[ItemCategory]

