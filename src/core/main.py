import argparse
from pathlib import Path

from aggregators.butikk_aggregator import ButikkAggregator
from aggregators.vare_aggregator import VareAggregator
from aggregators.kategori_filterer import KategoriFiltrer
from readers.kategori_reader import KategoriReader
from utils.datofiltrer_kvitteringer import datofiltrer_kvitteringer
from readers.kvittering_json_reader import TrumfReader
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
 
    trumf_reader = TrumfReader()
    kvitteringer = trumf_reader.read(Path(args.input))

    kvitteringer = datofiltrer_kvitteringer(kvitteringer, args.date_from, args.date_to)

    vare_aggregates = VareAggregator(kvitteringer).aggregate()
    butikk_aggregates = ButikkAggregator(kvitteringer).aggregate()
    
    category_aggregates = []
    
    if args.cat is not None:
        kategori_reader = KategoriReader()
        kategorier = list(map(lambda c: kategori_reader.read(c), args.cat))
        
        parser = KategoriFiltrer()
        for k in kategorier:
            parsed = parser.filtrer(k, vare_aggregates)
            x = 0
        category_aggregates = (list(map(lambda k: parser.filtrer(k, vare_aggregates), kategorier)))

    if args.type == "csv":
        result_directory =  Path(args.output)
        exporter = CsvExporter(butikk_aggregates, vare_aggregates, result_directory)
        exporter.export()
        print(f"CSV exported to {result_directory}")

    if args.type == "excel":
        writer = ExcelExporter(Path(args.output) / "rapport.xls")
        writer.lag_rapport(butikk_aggregates, vare_aggregates)

if __name__ == "__main__":
    main()
