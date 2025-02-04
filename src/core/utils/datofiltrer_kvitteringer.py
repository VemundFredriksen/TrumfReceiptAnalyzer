from models.trumf_receipt import Receipt
from datetime import datetime
from typing import List, Optional


def filter_receipts_by_date_interval(receipts: List[Receipt], date_from: Optional[str], date_to: Optional[str]) -> List[Receipt]:
    if not date_from and not date_to:
        return receipts

    date_from = datetime.strptime(date_from, "%Y-%m-%d") if date_from else None
    date_to = datetime.strptime(date_to, "%Y-%m-%d") if date_to else None

    filtered = []
    for receipt in receipts:
        receipt_date = datetime.strptime(receipt.dato, "%d.%m.%Y")
        if (not date_from or receipt_date >= date_from) and (not date_to or receipt_date <= date_to):
            filtered.append(receipt)
    return filtered