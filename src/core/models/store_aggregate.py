from dataclasses import dataclass

@dataclass
class StoreAggregate:
    store_name: str
    total_sum: float
    receipt_count: int