from models.varekategori import Varekategori
from models.kategori import Kategori


import json
from dataclasses import dataclass


@dataclass
class KategoriReader:
    def read(self, path) -> Kategori:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

            navn = data['navn']
            exlusive = data['exclusive']
            kategorier = list(map(lambda k: Varekategori(k['navn'], list(k['inkluderte_varer'])) , data['kategorier']))

            return Kategori(navn, exlusive, kategorier)