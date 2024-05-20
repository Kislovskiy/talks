import csv
from pathlib import Path


def read_csv_file(file_path):
    try:
        with open(file_path, "r") as csv_file:
            reader = csv.reader(csv_file)
            return [row for row in reader]
    except FileNotFoundError:
        return None


def extract_column(index, rows):
    try:
        column_values = [float(row[index]) for row in rows[1:]]
        return column_values
    except (ValueError, IndexError):
        return None


def calculate_average(column_values):
    if column_values is None or not column_values:
        return None, "Cannot calculate average due to empty or missing column"
    try:
        average = sum(column_values) / len(column_values)
        return average
    except ZeroDivisionError:
        return None


if __name__ == "__main__":
    csv_file_path = Path(__file__).parent / "data" / "example.csv"
    column_index = 1
    data = read_csv_file(csv_file_path)

    if data is None:
        print("Error reading CSV file")
    else:
        score_column_values = extract_column(column_index, data)
        if score_column_values is None:
            print("Error extracting column")
        else:
            result = calculate_average(score_column_values)
            if result is None:
                print("Error calculating average")
            else:
                print(f"The average is: {result}")
