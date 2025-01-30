from typing import List
import csv
import io
from models.butikk_aggregate import ButikkAggregate
from models.vare_aggregate import VareAggregate

class CsvExporter:
    def __init__(self, 
                 butikk_aggregates: List[ButikkAggregate], 
                 vare_aggregates: List[VareAggregate],
                 result_directory: str):
        
        self.butikk_aggregates = butikk_aggregates
        self.vare_aggregates = vare_aggregates
        self.result_directory = result_directory
        
    def export(self):
        self.__export_butikk_aggregates__()
        self.__export_vare_aggregates__()

    def __export_butikk_aggregates__(self):
        output = io.StringIO()
        writer = csv.writer(output, delimiter=';')
        
        writer.writerow(["Butikknavn", "Totalt Beløp", "Antall Kvitteringer"])
        
        for aggregat in self.butikk_aggregates:
            belop = str(aggregat.totalt_belop).replace('.', ',')
            antall = str(aggregat.antall_kvitteringer).replace('.', ',')
            writer.writerow([aggregat.butikknavn, belop, antall])
        
        self.__write_csv__(output, f"{self.result_directory}/butikker.csv")
    
    def __export_vare_aggregates__(self):
        output = io.StringIO()
        writer = csv.writer(output)
        
        writer.writerow(["Varenavn", "Total Antall", "Total Beløp"])
        
        for aggregat in self.vare_aggregates:
            belop = str(aggregat.total_belop).replace('.', ',')
            antall = str(aggregat.total_antall).replace('.', ',')
            writer.writerow([aggregat.varenavn, antall, belop])
        
        self.__write_csv__(output, f"{self.result_directory}/varer.csv")
    
    def __write_csv__(self, csv_string: io.StringIO, path: str):
        with open(path, mode='w', encoding='utf-8', newline='') as file:
            file.write(csv_string.getvalue())