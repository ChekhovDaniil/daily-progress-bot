import dateparser
from datetime import date

def parse_human_date(raw: str) -> date:
    parsed = dateparser.parse(
        raw,
        languages=["ru", "en"]
    )
    if not parsed:
        raise ValueError(f"Не удалось распознать дату: {raw}")

    return parsed.date()
