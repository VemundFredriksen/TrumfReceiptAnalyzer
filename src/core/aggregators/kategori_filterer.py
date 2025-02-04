from typing import List
from models.category_aggregate import CategoryAggregate
from models.item_aggregate import ItemAggregate
from models.category import Category


class CategoryAggregator:
    
    def filtrer(self, category: Category, item_aggregates: List[ItemAggregate]) -> CategoryAggregate:
        category_aggregates = []
        for item_category in category.categories:
            included_items = list(filter(lambda v: v.name in item_category.included_items, item_aggregates)) 
            total_category_sum = sum(map(lambda k: k.total_sum,  included_items))
            category_count = sum(map(lambda k: k.item_count, included_items))
            
            category_aggregates.append(CategoryAggregate(item_category.name, total_category_sum, category_count))
            if category.exclusive:
                item_aggregates = list(filter(lambda v: v.name not in item_category.included_items, item_aggregates))
            
        return category_aggregates