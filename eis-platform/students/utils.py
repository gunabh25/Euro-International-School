from datetime import datetime
import re

from .constants import DATE_FORMATS


def normalize_name(name: str) -> str:

    name = name.strip()

    name = re.sub(r"\s+", " ", name)

    return name.title()


def normalize_date(date_string: str):

    date_string = date_string.strip()

    for fmt in DATE_FORMATS:

        try:
            return datetime.strptime(
                date_string,
                fmt
            ).date()

        except ValueError:
            continue

    raise ValueError(f"Invalid date format: {date_string}")


def parse_marks(value):

    if value is None:
        return None

    value = str(value).strip()

    if value == "":
        return None

    return int(value)