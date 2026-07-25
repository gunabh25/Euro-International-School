from datetime import datetime
import math
import re

from .constants import DATE_FORMATS


def normalize_name(name: str) -> str:
    """
    Convert:
        "  ARJUN   sharma "
    into
        "Arjun Sharma"
    """

    if not name:
        return ""

    name = re.sub(r"\s+", " ", name.strip())

    return name.title()


def normalize_date(date_string: str):
    """
    Normalize all supported date formats to a Python date.
    """

    date_string = str(date_string).strip()

    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(date_string, fmt).date()
        except ValueError:
            pass

    raise ValueError(f"Unsupported date format: {date_string}")


def parse_marks(value):
    """
    Blank marks mean absent.
    """

    if value is None:
        return None

    if isinstance(value, float) and math.isnan(value):
        return None

    value = str(value).strip()

    if value == "":
        return None

    return int(float(value))