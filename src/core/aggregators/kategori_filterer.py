from typing import List
from aggregators.aggregator import Aggregator
from models.category_aggregate import CategoryAggregate
from models.item_aggregate import ItemAggregate
from models.category import Category


class CategoryAggregator(Aggregator):
    
    def __init__(self, category: Category, item_aggregates: List[ItemAggregate]):
        self.category = category
        self.item_aggregates = item_aggregates.copy()
    
    def aggregate(self) -> List[CategoryAggregate]:
        category_aggregates = []
        for item_category in self.category.categories:
            included_items = list(filter(lambda v: v.name in item_category.included_items, self.item_aggregates)) 
            total_category_sum = sum(map(lambda k: k.total_sum, included_items))
            category_count = sum(map(lambda k: k.item_count, included_items))
            
            category_aggregates.append(CategoryAggregate(item_category.name, total_category_sum, category_count))
            if self.category.exclusive:
                item_aggregates = list(filter(lambda v: v.name not in item_category.included_items, self.item_aggregates))
            
        return category_aggregates