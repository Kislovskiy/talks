import csv
from pathlib import Path

from toolz import curry, pipe


def read_csv_file(file_path):
    try:
        with open(file_path, "r") as csv_file:
            return [row for row in csv.reader(csv_file)]
    except FileNotFoundError:
        return None


@curry
def extract_column(column_index, rows):
    try:
        return [row[column_index] for row in rows]
    except (ValueError, IndexError):
        return None


@curry
def remove_row(row_index, rows):
    try:
        return rows[row_index:]
    except IndexError:
        return None


@curry
def convert_to(converter, rows):
    try:
        return [converter(item) for item in rows]
    except ValueError:
        return None


def calculate_average(column_values):
    try:
        return sum(column_values) / len(column_values)
    except ZeroDivisionError:
        return None


if __name__ == "__main__":
    csv_file_path = Path(__file__).parent / "data" / "example.csv"

    score_column_index = 1
    header_row_index = 1

    score_column = extract_column(score_column_index)
    removed_header = remove_row(header_row_index)
    score_as_float = convert_to(float)

    average_result = pipe(
        read_csv_file(csv_file_path),
        score_column,
        removed_header,
        score_as_float,
        calculate_average,
    )

    print(f"An average score is {average_result}")
