import csv
import logging
import os
from pathlib import Path
from typing import List, Union

from pymonad.either import Either
from pymonad.either import Left, Right
from pymonad.tools import curry
from rich.logging import RichHandler

logging.basicConfig(
    level=logging.INFO, format="%(message)s", datefmt="[%X]", handlers=[RichHandler()]
)

logger = logging.getLogger("rich")


def read_csv_file(file_path: Union[str, Path]) -> Either[str, List[List[str]]]:
    """
        Reads a CSV file and returns its content as a list of rows.
    §§1
        :param file_path: The path to the CSV file to read.
        :type file_path: Union[str, Path]
        :return: A Right monad containing the content of the CSV file as a list of rows if the file exists and is readable,
        or a Left monad containing an error message if the file does not exist or is not readable.
        :rtype: Either[str, List[List[str]]]
    """
    logger.info(f"Reading CSV file: {file_path}")
    return (
        Right(list(map(lambda row: row, csv.reader(open(file_path, "r")))))
        if os.path.isfile(file_path)
        else Left("Error: File does not exist")
    )


def remove_header(
    data: List[Union[str, List[str]]],
) -> Either[str, List[Union[str, List[str]]]]:
    """
    Remove the header (first row) from a list of rows.

    :param data: The list of rows from which to remove the header.
    :type data: List[Union[str, List[str]]]
    :return: A Right monad containing the list of rows without the header if the list has more than one row,
             or a Left monad containing an error message if the list has one row or less.
    :rtype: Either[str, List[Union[str, List[str]]]]
    """
    logger.info("Removing header")
    return Right(data[1:]) if len(data) > 1 else Left("Error: Unable to remove header")


@curry(2)
def extract_column(index: int, rows: List[List[str]]) -> Either[str, List[str]]:
    """
    Extracts a column from a list of rows.

    :param index: The index of the column to extract.
    :type index: int
    :param rows: The list of rows from which to extract the column.
    :type rows: List[List[str]]
    :return: A Right monad containing the extracted column if successful, or a Left monad containing an error message
     if unsuccessful.
    :rtype: Either[str, List[str]]
    """
    logger.info(f"Extracting column: {index}")

    return Right(rows).bind(lambda r: Right(list(map(lambda row: row[index], r))))


def convert_to_float(data: List[str]) -> Either[str, List[float]]:
    """
    Convert a list of numeric strings to a list of floats.

    :param data: The list of numeric strings to convert.
    :type data: List[str]
    :return: A Right monad containing the list of floats if all strings in the list can be converted to floats,
             or a Left monad containing an error message if any string in the list cannot be converted to a float.
    :rtype: Either[str, List[float]]
    """
    logger.info("Converting to float")
    return (
        Right(list(map(float, data)))
        if all([num.isnumeric() for num in data])
        else Left("Error: Unable to convert to float")
    )


def calculate_average(column_values: List[float]) -> Either[str, float]:
    """
    Calculate the average of a list of numeric values.

    :param column_values: The list of numeric values to calculate the average of.
    :type column_values: List[float]
    :return: A Right monad containing the average if the list is not empty,
             or a Left monad containing an error message if the list is empty.
    :rtype: Either[str, float]
    """
    logger.info("Calculating average")
    return (
        Right(sum(column_values) / len(column_values))
        if column_values
        else Left("Error: Division by zero")
    )


def compute_average_score(file_path: Union[str, Path]) -> Either[str, float]:
    """
    Compute the average score from a CSV file.

    :param file_path: The path to the CSV file to read.
    :type file_path: Union[str, Path]
    :return: A Right monad containing the average score if the file exists and is readable,
             or a Left monad containing an error message if the file does not exist or is not readable.
    :rtype: Either[str, float]
    """
    logger.info(f"Starting to compute average score for file: {file_path}")
    return (
        read_csv_file(file_path)
        .then(remove_header)
        .then(extract_column(1))
        .then(convert_to_float)
        .then(calculate_average)
    )


def main() -> None:
    csv_file_path = Path(__file__).parent / "data" / "example.csv"
    result = compute_average_score(csv_file_path)
    if result.is_right():
        print(f"An average score of is {result.value:.2f}")
    else:
        print(result.either(lambda x: f"Error processing data: {x}", lambda x: x))


if __name__ == "__main__":
    main()
