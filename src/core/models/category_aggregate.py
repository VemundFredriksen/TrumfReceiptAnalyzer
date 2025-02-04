from dataclasses import dataclass

@dataclass
class CategoryAggregate:
    name: str
    total_sum: float
    item_count: int