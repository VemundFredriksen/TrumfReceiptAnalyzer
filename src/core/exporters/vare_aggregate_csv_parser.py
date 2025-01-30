import csv
from dataclasses import dataclass
import io
from typing import List
from models.vare_aggregate import VareAggregate

@dataclass
class VareAggregateCsvWriter:

    def vare_aggregater_til_csv(self, vare_aggregater: List[VareAggregate]) -> str:
        output = io.StringIO()
        writer = csv.writer(output)
        
        writer.writerow(["Varenavn", "Total Antall", "Total Beløp"])
        
        for aggregat in vare_aggregater:
            belop = str(aggregat.total_belop).replace('.', ',')
            antall = str(aggregat.total_antall).replace('.', ',')
            writer.writerow([aggregat.varenavn, antall, belop])
        
        return output.getvalue()
