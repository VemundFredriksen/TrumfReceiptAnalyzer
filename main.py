import argparse
from pathlib import Path

from analyzers.butikk_aggregator import ButikkAggregator
from analyzers.vare_aggregator import VareAggregator
from utils.datofiltrer_kvitteringer import datofiltrer_kvitteringer
from readers.kvittering_json_reader import TrumfReader
from writers.butikk_aggregate_csv_parser import ButikkAggregateCsvWriter
from writers.csv_writer import CsvWriter
from writers.excel_writer import ExcelExporter
from writers.vare_aggregate_csv_parser import VareAggregateCsvWriter

def parse_args():
    parser = argparse.ArgumentParser(description="Trumf kvitteringsanalyzer")
    parser.add_argument("-input", type=str, help="Path til JSON-filen med kvitteringer", default="./assets/kvitteringer.json")
    parser.add_argument("-output", type=str, help="Katalog for å lagre utdatafilen", default="./")
    parser.add_argument("-type", type=str, choices=["csv", "excel"], help="Filtype for utdata (default: csv)", default="csv")
    parser.add_argument("-from", dest="date_from", type=str, help="Startdato (format: YYYY-MM-DD)", default=None)
    parser.add_argument("-to", dest="date_to", type=str, help="Sluttdato (format: YYYY-MM-DD)", default=None)
    return parser.parse_args()

def main():
    args = parse_args()
 
    trumf_reader = TrumfReader()
    kvitteringer = trumf_reader.read(Path(args.input))

    kvitteringer = datofiltrer_kvitteringer(kvitteringer, args.date_from, args.date_to)

    vare_aggregates = VareAggregator().aggregate_by_item(kvitteringer)   
    butikk_aggregates = ButikkAggregator().aggregate_by_store(kvitteringer)

    if args.type == "csv":
        butikk_aggregate_csv = ButikkAggregateCsvWriter().butikk_aggregates_to_csv(butikk_aggregates)
        vare_aggregate_csv = VareAggregateCsvWriter().vare_aggregater_til_csv(vare_aggregates)
        
        vare_output_path = Path(args.output) / "varer.csv"
        butikk_output_path = Path(args.output) / "butikker.csv"
        
        csv_writer = CsvWriter()
        
        csv_writer.lagre_csv_til_fil(vare_aggregate_csv, vare_output_path)
        print(f"CSV-fil for varer lagret til: {vare_output_path}")
            
        csv_writer.lagre_csv_til_fil(butikk_aggregate_csv, butikk_output_path)
        print(f"CSV-fil for butikker lagret til: {butikk_output_path}")
    if args.type == "excel":
        writer = ExcelExporter(Path(args.output) / "rapport.xls")
        writer.lag_rapport(butikk_aggregates, vare_aggregates)

if __name__ == "__main__":
    main()
