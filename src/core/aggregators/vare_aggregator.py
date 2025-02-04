from dataclasses import dataclass
from typing import List, Dict
from collections import defaultdict
from aggregators.aggregator import Aggregator
from models.trumf_receipt import Receipt
from models.item_aggregate import ItemAggregate

class ItemAggregator(Aggregator):
    
    def __init__(self, receipts: List[Receipt]):
        self.receipts = receipts
        
    def aggregate(self) -> List[Receipt]:
        item_map: Dict[str, ItemAggregate] = defaultdict(lambda: ItemAggregate("", 0, 0.0))

        for receipt in self.receipts:
            for item in receipt.varelinjer:
                if item.varenavn not in item_map:
                    item_map[item.varenavn] = ItemAggregate(item.varenavn, 0, 0.0)

                item_map[item.varenavn].item_count += float(item.vareAntallVekt)
                item_map[item.varenavn].total_sum += float(item.vareBelop)

        return list(item_map.values())