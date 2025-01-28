from models.trumf_kvittering import Kvittering
from datetime import datetime
from typing import List, Optional


def datofiltrer_kvitteringer(kvitteringer: List[Kvittering], date_from: Optional[str], date_to: Optional[str]) -> List[Kvittering]:
    if not date_from and not date_to:
        return kvitteringer

    date_from = datetime.strptime(date_from, "%Y-%m-%d") if date_from else None
    date_to = datetime.strptime(date_to, "%Y-%m-%d") if date_to else None

    filtrert = []
    for kvittering in kvitteringer:
        kvittering_dato = datetime.strptime(kvittering.dato, "%d.%m.%Y")
        if (not date_from or kvittering_dato >= date_from) and (not date_to or kvittering_dato <= date_to):
            filtrert.append(kvittering)
    return filtrert