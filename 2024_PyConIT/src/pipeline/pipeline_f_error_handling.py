import csv
from pathlib import Path
from typing import Union

from toolz import curry, pipe


def read_csv_file(data_path: Path):
    try:
        with data_path.open() as source_file:
            data_reader = csv.reader(source_file)
            return [row for row in data_reader]
    except FileNotFoundError as ex:
        raise FileNotFoundError(f"Error reading file: {ex}")


@curry
def remove_row(row_index, rows):
    try:
        return rows[row_index:]
    except IndexError:
        return None


@curry
def extract_column(column_name, data):
    try:
        return [row[column_name] for row in data]
        # return [row.get(column_name) for row in data]
        # for row in data:
        #     yield row.get(column_name)
    except IndexError as ex:
        raise IndexError(f"Error extracting column: {ex}")


@curry
def convert_to(converter, data):
    try:
        for item in data:
            yield converter(item)
    except ValueError as ex:
        raise ValueError(f"Error converting to float: {ex}")
    except TypeError as ex:
        raise TypeError(f"Error converting to float: {ex}, {converter=} {data=}")


def is_valid_score(x: Union[float, None]) -> bool:
    """
    Check if a score is valid.
    A valid score is a number with an absolute value less than 100.

    :param x: A number representing a score.
    :return: True if the score is valid, False otherwise.
    """
    max_valid_score = 100
    return x is not None and x >= 0 and abs(x) < max_valid_score


def calculate_average_score(column_values: list[float]) -> float:
    """
    Calculate the average of a list of numbers.
    The average-score is calculated by summing all the valid scores :math:`s` and
    dividing by the number of valid scores.
    .. math::
        \\text{Average score} = \\frac{\\sum s}{\\text{number of valid scores}}

    Uses :func:`is_valid_score` to filter out invalid scores.

    :param column_values: A list of numbers representing scores.
    :return: The average score.
    :raises ValueError: If input is None.
    :raises ZeroDivisionError: If input is an empty list or a list with only invalid values.
    >>> calculate_average_score([1.0, 2.0, 3.0, float("inf")]) == 2.0
    True
    """
    if column_values is None:
        raise ValueError("Input cannot be None.")

    # filtered_values = list(column_values)
    filtered_values = [value for value in column_values if is_valid_score(value)]

    if not filtered_values:
        raise ZeroDivisionError(
            "Cannot compute average of empty list or list with only invalid values."
        )

    return sum(filtered_values) / len(filtered_values)


def compute_average_score(data_path: Path) -> float:
    try:
        return pipe(
            read_csv_file(data_path),
            extract_column(1),
            remove_row(1),
            convert_to(float),
            calculate_average_score,
        )
    except (FileNotFoundError, ValueError, IndexError, ZeroDivisionError) as e:
        print(f"Exception caught: {e}")


def main() -> None:
    print(compute_average_score(Path(__file__).parent / "data" / "example.csv"))


if __name__ == "__main__":
    main()
