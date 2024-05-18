from pathlib import Path
import polars as pl

if __name__ == "__main__":
    current_dir_path = Path(__file__).parent
    csv_file_path = current_dir_path.joinpath("example.csv")

    print(
        pl.read_csv(csv_file_path)
        .filter(pl.col("Score") != "error")
        .select("Score")
        .cast(pl.Float32, strict=False)
        .mean()
    )
