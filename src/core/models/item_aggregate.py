from dataclasses import dataclass

@dataclass
class ItemAggregate:
    name: str
    item_count: float
    total_sum: float