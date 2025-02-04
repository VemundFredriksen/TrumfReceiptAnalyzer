import argparse
from pathlib import Path

from aggregators.butikk_aggregator import StoreAggregator
from aggregators.vare_aggregator import ItemAggregator
from aggregators.kategori_filterer import CategoryAggregator
from readers.category_reader import CategoryReader
from utils.datofiltrer_kvitteringer import filter_receipts_by_date_interval
from readers.trumf_receipt_json_reader import TrumfReceiptJsonReader
from exporters.excel_writer import ExcelExporter
from exporters.csv_exporter import CsvExporter

def parse_args():
    parser = argparse.ArgumentParser(description="Trumf kvitteringsanalyzer")
    parser.add_argument("-input", type=str, help="Path til JSON-filen med kvitteringer", default="./assets/kvitteringer.json")
    parser.add_argument("-output", type=str, help="Katalog for å lagre utdatafilen", default="./assets/")
    parser.add_argument("-type", type=str, choices=["csv", "excel"], help="Filtype for utdata (default: csv)", default="csv")
    parser.add_argument("-cat", nargs="+", help="Stil til kategorifil")
    parser.add_argument("-from", dest="date_from", type=str, help="Startdato (format: YYYY-MM-DD)", default=None)
    parser.add_argument("-to", dest="date_to", type=str, help="Sluttdato (format: YYYY-MM-DD)", default=None)
    return parser.parse_args()

def main():
    args = parse_args()
 
    json_reader = TrumfReceiptJsonReader()
    receipts = json_reader.read(Path(args.input))

    receipts = filter_receipts_by_date_interval(receipts, args.date_from, args.date_to)

    item_aggregates = ItemAggregator(receipts).aggregate()
    store_aggregates = StoreAggregator(receipts).aggregate()
    
    category_aggregates = []
    
    if args.cat is not None:
        category_reader = CategoryReader()
        categories = list(map(lambda c: category_reader.read(c), args.cat))
        
        parser = CategoryAggregator()
        for k in categories:
            parsed = parser.filtrer(k, item_aggregates)
            x = 0
        category_aggregates = (list(map(lambda k: parser.filtrer(k, item_aggregates), categories)))

    if args.type == "csv":
        result_directory =  Path(args.output)
        exporter = CsvExporter(store_aggregates, item_aggregates, result_directory)
        exporter.export()
        print(f"CSV exported to {result_directory}")

    if args.type == "excel":
        writer = ExcelExporter(Path(args.output) / "rapport.xls")
        writer.export(store_aggregates, item_aggregates)

if __name__ == "__main__":
    main()
