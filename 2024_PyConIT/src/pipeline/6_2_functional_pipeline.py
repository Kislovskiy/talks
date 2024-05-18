import csv
import os
from pathlib import Path

from pymonad.either import Left, Right
from pymonad.tools import curry


# Function to handle file reading
def read_csv_file(file_path):
    return (
        Right(list(map(lambda row: row, csv.reader(open(file_path, "r")))))
        if os.path.isfile(file_path)
        else Left("Error: File does not exist")
    )


def remove_header(data):
    return Right(data[1:]) if len(data) > 1 else Left("Error: Unable to remove header")


@curry(2)
def extract_column(index: int, rows: list[list[str]]) -> Right:
    return Right(rows).bind(
        lambda rows: Right(list(map(lambda row: row[index], rows)))
    )


def convert_to_float(data):
    return (
        Right(list(map(float, data)))
        if all([num.isnumeric() for num in data])
        else Left("Error: Unable to convert to float")
    )


def calculate_average(column_values):
    return (
        Right(sum(column_values) / len(column_values))
        if column_values
        else Left("Error: Division by zero")
    )


if __name__ == "__main__":
    extract_score_column = extract_column(1)
    extract_name_column = extract_column(0)

    current_dir_path = Path(__file__).parent
    csv_file_path = current_dir_path.joinpath("data", "example.csv")

    names = read_csv_file(csv_file_path).then(remove_header).then(extract_name_column)

    result = (
        read_csv_file(csv_file_path)
        .then(remove_header)
        .then(extract_score_column)
        .then(convert_to_float)
        .then(calculate_average)
    )

    if result.is_right() and names.is_right():
        print(
            f"An average score of {', '.join(names.value[:-1])} and {names.value[-1]} is {result.value}"
        )
    else:
        print(result.either(lambda x: f"Error processing data: {x}", lambda x: x))
