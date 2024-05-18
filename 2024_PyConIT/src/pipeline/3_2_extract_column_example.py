import csv


def read_csv_file(file_path):
    try:
        with open(file_path, "r") as csv_file:
            return [row for row in csv.reader(csv_file)]
    except FileNotFoundError:
        return None


def extract_column_currying(index):
    """
    Curried function to extract column from a list of rows
    f(x, y) = f(x)(y)
    ```
    def extract_column(column_index, rows):
    try:
        return [row[column_index] for row in rows]
    except (ValueError, IndexError):
        return None
    ```
    :param index: index of the column to extract
    :return: curried function to extract column
    """

    def curried(rows):
        try:
            score_column_values = [row[index] for row in rows]
            return score_column_values
        except (ValueError, IndexError):
            return None

    return curried


if __name__ == "__main__":
    data = read_csv_file("data/example.csv")

    name_column_index = 0
    score_column_index = 1

    name_list = extract_column_currying(name_column_index)
    score_list = extract_column_currying(score_column_index)

    print(f"Extracted Column: {score_list(data)}")
    print(f"Extracted Column: {name_list(data)}")
