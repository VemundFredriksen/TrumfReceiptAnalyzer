from dataclasses import dataclass
from typing import List, Dict
from collections import defaultdict
from aggregators.aggregator import Aggregator
from models.trumf_kvittering import Kvittering
from models.vare_aggregate import VareAggregate

class VareAggregator(Aggregator):
    
    def __init__(self, kvitteringer: List[Kvittering]):
        self.kvitteringer = kvitteringer
        
    def aggregate(self) -> List[Kvittering]:
        vare_map: Dict[str, VareAggregate] = defaultdict(lambda: VareAggregate("", 0, 0.0))

        for kvittering in self.kvitteringer:
            for vare in kvittering.varelinjer:
                if vare.varenavn not in vare_map:
                    vare_map[vare.varenavn] = VareAggregate(vare.varenavn, 0, 0.0)

                vare_map[vare.varenavn].total_antall += float(vare.vareAntallVekt)
                vare_map[vare.varenavn].total_belop += float(vare.vareBelop)

        return list(vare_map.values())