from dataclasses import dataclass
from typing import List
from aggregators.aggregator import Aggregator
from models.trumf_receipt import Receipt
from models.store_aggregate import StoreAggregate

class StoreAggregator(Aggregator):
    
    def __init__(self, receipts: List[Receipt]):
        self.receipts = receipts
    
    def aggregate(self) -> List[StoreAggregate]:
        store_map = {}

        for receipt in self.receipts:
            store_name = receipt.butikknavn
            total_store_sum = float(receipt.totaltBelop)

            if store_name not in store_map:
                store_map[store_name] = StoreAggregate(store_name, 0.0, 0)

            store_map[store_name].total_sum += total_store_sum
            store_map[store_name].receipt_count += 1

        return list(store_map.values())