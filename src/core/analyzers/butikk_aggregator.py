from dataclasses import dataclass
from typing import List
from models.trumf_kvittering import Kvittering
from models.butikk_aggregate import ButikkAggregate

@dataclass
class ButikkAggregator:
    
    def aggregate_by_store(self, kvitteringer: List[Kvittering]) -> List[ButikkAggregate]:
        butikk_map = {}

        for kvittering in kvitteringer:
            butikknavn = kvittering.butikknavn
            belop = float(kvittering.totaltBelop)

            if butikknavn not in butikk_map:
                butikk_map[butikknavn] = ButikkAggregate(butikknavn, 0.0, 0)

            butikk_map[butikknavn].totalt_belop += belop
            butikk_map[butikknavn].antall_kvitteringer += 1

        return list(butikk_map.values())