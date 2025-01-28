import json
from typing import List
from models.trumf_kvittering import Kvittering, Varelinje
from dataclasses import dataclass

@dataclass
class TrumfReader:

    def read(self, path) -> List[Kvittering]:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            kvitteringer = []

            for kvittering_data in data:
                varelinjer = [
                    Varelinje(**varelinje_data) for varelinje_data in kvittering_data.get('varelinjer', [])
                ]
                kvittering = Kvittering(
                    dato=kvittering_data["dato"],
                    kvitteringsnummer=kvittering_data["kvitteringsnummer"],
                    kjede=kvittering_data.get("kjede"),
                    butikknavn=kvittering_data["butikknavn"],
                    totaltBelop=kvittering_data["totaltBelop"],
                    korttype=kvittering_data["korttype"],
                    kanal=kvittering_data.get("kanal"),
                    varelinjer=varelinjer
                )
                kvitteringer.append(kvittering)

            return kvitteringer
