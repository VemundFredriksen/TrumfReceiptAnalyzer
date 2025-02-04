import json
from typing import List
from models.trumf_receipt import Receipt, ItemLine
from dataclasses import dataclass

@dataclass
class TrumfReceiptJsonReader:

    def read(self, path) -> List[Receipt]:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            receipts = []

            for receipt in data:
                items = [
                    ItemLine(**varelinje_data) for varelinje_data in receipt.get('varelinjer', [])
                ]
                kvittering = Receipt(
                    dato=receipt["dato"],
                    kvitteringsnummer=receipt["kvitteringsnummer"],
                    kjede=receipt.get("kjede"),
                    butikknavn=receipt["butikknavn"],
                    totaltBelop=receipt["totaltBelop"],
                    korttype=receipt["korttype"],
                    kanal=receipt.get("kanal"),
                    varelinjer=items
                )
                receipts.append(kvittering)

            return receipts
