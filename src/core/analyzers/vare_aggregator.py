from dataclasses import dataclass
from typing import List, Dict
from collections import defaultdict
from models.trumf_kvittering import Kvittering
from models.vare_aggregate import VareAggregate

@dataclass
class VareAggregator:
    
    def aggregate_by_item(self, kvitteringer: List[Kvittering]) -> List[VareAggregate]:
        vare_map: Dict[str, VareAggregate] = defaultdict(lambda: VareAggregate("", 0, 0.0))

        for kvittering in kvitteringer:
            for vare in kvittering.varelinjer:
                if vare.varenavn not in vare_map:
                    vare_map[vare.varenavn] = VareAggregate(vare.varenavn, 0, 0.0)

                vare_map[vare.varenavn].total_antall += float(vare.vareAntallVekt)
                vare_map[vare.varenavn].total_belop += float(vare.vareBelop)

        return list(vare_map.values())