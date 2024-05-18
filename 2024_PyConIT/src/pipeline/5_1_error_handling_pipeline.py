import csv
from pathlib import Path

from toolz import curry, pipe


def read_csv_file(file_path):
    try:
        with open(file_path, "r") as csv_file:
            return [row for row in csv.reader(csv_file)]
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error reading file: {e}")


@curry
def extract_column(column_index, data):
    try:
        return [row[column_index] for row in data]
    except IndexError as e:
        raise IndexError(f"Error extracting column: {e}")


@curry
def remove_row(row_index, data):
    try:
        return data[row_index:]
    except IndexError as e:
        raise IndexError(f"Error removing header: {e}")


@curry
def convert_to(converter, data):
    try:
        return [converter(item) for item in data]
    except ValueError as e:
        raise ValueError(f"Error converting to float: {e}")


# Function to calculate average
def calculate_average(column_values):
    try:
        return sum(column_values) / len(column_values)
    except ZeroDivisionError as e:
        raise ZeroDivisionError(f"Error zero division: {e}")


if __name__ == "__main__":
    current_dir_path = Path(__file__).parent
    csv_file_path = current_dir_path.joinpath("data", "example.csv")

    score_column_index = 1
    header_row_index = 1

    score_column = extract_column(score_column_index)
    remove_header = remove_row(header_row_index)
    convert_score_to_float = convert_to(float)

    try:
        average_result = pipe(
            read_csv_file(csv_file_path),
            score_column,
            remove_header,
            convert_score_to_float,
            calculate_average,
        )
        print(f"An average score is {average_result}")
    except (FileNotFoundError, ValueError, IndexError, ZeroDivisionError) as e:
        print(f"Exception caught: {e}")
