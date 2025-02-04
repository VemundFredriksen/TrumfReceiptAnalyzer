from typing import List
import csv
import io
from models.store_aggregate import StoreAggregate
from models.item_aggregate import ItemAggregate

class CsvExporter:
    def __init__(self, 
                 store_aggregates: List[StoreAggregate], 
                 item_aggregates: List[ItemAggregate],
                 result_directory: str):
        
        self.store_aggregates = store_aggregates
        self.item_aggregates = item_aggregates
        self.result_directory = result_directory
        
    def export(self):
        self.__export_store_aggregates__()
        self.__export_item_aggregates__()

    def __export_store_aggregates__(self):
        output = io.StringIO()
        writer = csv.writer(output, delimiter=';')
        
        writer.writerow(["Butikknavn", "Totalt Beløp", "Antall Kvitteringer"])
        
        for aggregate in self.store_aggregates:
            total_store_sum = str(aggregate.total_sum).replace('.', ',')
            count = str(aggregate.receipt_count).replace('.', ',')
            writer.writerow([aggregate.store_name, total_store_sum, count])
        
        self.__write_csv__(output, f"{self.result_directory}/butikker.csv")
    
    def __export_item_aggregates__(self):
        output = io.StringIO()
        writer = csv.writer(output)
        
        writer.writerow(["Varenavn", "Total Antall", "Total Beløp"])
        
        for aggregate in self.item_aggregates:
            total_item_sum = str(aggregate.total_sum).replace('.', ',')
            count = str(aggregate.item_count).replace('.', ',')
            writer.writerow([aggregate.name, count, total_item_sum])
        
        self.__write_csv__(output, f"{self.result_directory}/varer.csv")
    
    def __write_csv__(self, csv_string: io.StringIO, path: str):
        with open(path, mode='w', encoding='utf-8', newline='') as file:
            file.write(csv_string.getvalue())