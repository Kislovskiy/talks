from pathlib import Path
import polars as pl


def compute_average_score(data_path: Path) -> float:
    average_score = (
        pl.read_csv(data_path).select("Score").cast(pl.Float32, strict=False).mean()
    )
    return average_score


def main():
    csv_file_path = Path(__file__).parent / "data" / "example.csv"
    average_score = compute_average_score(csv_file_path)
    print(f"The average score for the class is: {average_score}")


if __name__ == "__main__":
    main()
