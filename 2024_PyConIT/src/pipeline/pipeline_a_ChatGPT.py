import csv
from pathlib import Path
from typing import Optional, Union


def read_csv_and_compute_average(filename: Union[str, Path]) -> Optional[float]:
    scores = []

    with open(filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                # Try converting the Score to an integer
                score = int(row["Score"])
                scores.append(score)
            except ValueError:
                # Skip the row if the conversion fails
                print(f"Invalid score '{row['Score']}' for {row['Name']}, skipping.")

    if scores:
        return sum(scores) / len(scores)
    else:
        return None


if __name__ == "__main__":
    average_score = read_csv_and_compute_average(
        Path(__file__).parent / "data" / "example.csv"
    )
    if average_score:
        print(f"The average score for the class is: {average_score:.2f}")
    else:
        print("No valid scores found.")
