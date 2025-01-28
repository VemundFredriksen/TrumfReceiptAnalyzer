import csv
from dataclasses import dataclass
import io
from typing import List
from models.butikk_aggregate import ButikkAggregate

@dataclass
class ButikkAggregateCsvWriter:
    def butikk_aggregates_to_csv(self, butikk_aggregater: List[ButikkAggregate]) -> str:
        output = io.StringIO()
        writer = csv.writer(output, delimiter=';')
        
        writer.writerow(["Butikknavn", "Totalt Beløp", "Antall Kvitteringer"])
        
        for aggregat in butikk_aggregater:
            belop = str(aggregat.totalt_belop).replace('.', ',')
            antall = str(aggregat.antall_kvitteringer).replace('.', ',')
            writer.writerow([aggregat.butikknavn, belop, antall])
        
        return output.getvalue()