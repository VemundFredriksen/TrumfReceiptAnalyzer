
from dataclasses import dataclass

@dataclass
class CsvWriter:
    def lagre_csv_til_fil(self, csv_streng: str, filbane: str):
        with open(filbane, mode='w', encoding='utf-8', newline='') as file:
            file.write(csv_streng)