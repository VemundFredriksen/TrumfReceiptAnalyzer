from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ItemLine:
    varenavn: str
    vareAntallVekt: str
    vareBelop: str

@dataclass
class Receipt:
    dato: str
    kvitteringsnummer: str
    kjede: Optional[str]
    butikknavn: str
    totaltBelop: str
    korttype: str
    kanal: Optional[str]
    varelinjer: List[ItemLine]
