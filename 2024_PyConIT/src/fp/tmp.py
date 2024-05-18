import re
from typing import Optional


def extract_year_start(show: str) -> Optional[int]:
    match = re.search(r"\((\d{4})", show)
    if match:
        return int(match.group(1))
    return None


def extract_year_end(show: str) -> Optional[int]:
    match = re.search(r"\((\d{4})-(\d{4})\)", show)
    if match:
        return int(match.group(2))
    return None


def extract_single_year(show: str) -> Optional[int]:
    match = re.search(r"\((\d{4})\)", show)
    if match:
        return int(match.group(1))
    return None


tv_show = "The Wire (2002-2008)"
year = extract_year_start(tv_show) or extract_single_year(tv_show)


# Function to extract a colum
def extract_column(data):
    try:
        column_values = [float(row[1]) for row in data[1:]]
        return column_values
    except (ValueError, IndexError) as e:
        return None


# Function to extract a colum
def extract_column(column_index, data):
    data.pop(0)
    return [float(row[column_index]) for row in data]


import re


def extract_year_end(show: str) -> int:
    match = re.search(r"\((\d{4})-(\d{4})\)", show)
    if match:
        return int(match.group(2))
    else:
        raise ValueError("End year not found in the string")


tv_show = "The Wire (2002-2008)"
start = extract_year_start(tv_show)
end = extract_year_end(tv_show)

# Testing another show
chernobyl_show = "Chernobyl (2019)"

# >>> import pymonad
# >>> help(pymonad)
