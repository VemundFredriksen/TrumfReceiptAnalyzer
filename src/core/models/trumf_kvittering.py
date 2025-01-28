from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Varelinje:
    varenavn: str
    vareAntallVekt: str
    vareBelop: str

@dataclass
class Kvittering:
    dato: str
    kvitteringsnummer: str
    kjede: Optional[str]
    butikknavn: str
    totaltBelop: str
    korttype: str
    kanal: Optional[str]
    varelinjer: List[Varelinje]
