import csv
import math
from pathlib import Path


def read_csv_file(file_path):
    try:
        with open(file_path, "r") as csv_file:
            return [row for row in csv.reader(csv_file)]
    except FileNotFoundError:
        return None


def extract_column(column_index, rows):
    try:
        return [row[column_index] for row in rows]
    except (ValueError, IndexError):
        return None


def remove_row(row_index, rows):
    try:
        return rows[row_index:]
    except IndexError:
        return None


def convert_to(converter, rows):
    try:
        return [converter(item) for item in rows]
    except ValueError:
        return None


def is_valid_number(x):
    return x is not None and not (math.isnan(x) or math.isinf(x))


def calculate_average(column_values):
    try:
        return sum(column_values) / len(column_values)
    except ZeroDivisionError:
        return None


if __name__ == "__main__":
    csv_file_path = Path(__file__).parent / "data" / "example.csv"

    score_column_index = 1
    header_row_index = 1

    data = read_csv_file(csv_file_path)

    if data is None:
        print("Error reading CSV file")
    else:
        score_column_values = extract_column(score_column_index, data)
        removed_header_data = remove_row(header_row_index, score_column_values)
        score_column_as_float = convert_to(float, removed_header_data)

        if score_column_as_float is None:
            print("Error extracting column")
        else:
            result = calculate_average(score_column_as_float)
            if result is None:
                print("Error calculating average")
            else:
                print(f"The average is: {result}")
