from dataclasses import dataclass

@dataclass
class KategoriAggregate:
    navn: str
    totalsum: float
    antall: int