from dataclasses import dataclass
from typing import List
from aggregators.aggregator import Aggregator
from models.trumf_kvittering import Kvittering
from models.butikk_aggregate import ButikkAggregate

class ButikkAggregator(Aggregator):
    
    def __init__(self, kvitteringer: List[Kvittering]):
        self.kvitteringer = kvitteringer
    
    def aggregate(self) -> List[ButikkAggregate]:
        butikk_map = {}

        for kvittering in self.kvitteringer:
            butikknavn = kvittering.butikknavn
            belop = float(kvittering.totaltBelop)

            if butikknavn not in butikk_map:
                butikk_map[butikknavn] = ButikkAggregate(butikknavn, 0.0, 0)

            butikk_map[butikknavn].totalt_belop += belop
            butikk_map[butikknavn].antall_kvitteringer += 1

        return list(butikk_map.values())