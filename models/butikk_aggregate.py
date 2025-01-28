from dataclasses import dataclass

@dataclass
class ButikkAggregate:
    butikknavn: str
    totalt_belop: float
    antall_kvitteringer: int