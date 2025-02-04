from models.item_category import ItemCategory
from models.category import Category
import json
from dataclasses import dataclass

@dataclass
class CategoryReader:
    def read(self, path) -> Category:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

            category_name = data['navn']
            exlusive = data['exclusive']
            categories = list(map(lambda k: ItemCategory(k['navn'], list(k['inkluderte_varer'])) , data['kategorier']))

            return Category(category_name, exlusive, categories)