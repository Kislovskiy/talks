import timeit
from functools import partial
from pathlib import Path

from pipeline_a_ChatGPT import read_csv_and_compute_average as average_chatgpt
from pipeline_f_error_handling import compute_average_score as average_error_handling
from pipeline_g_pymonad import compute_average_score as average_pymonad
from pipeline_a_polars import compute_average_score as average_polars

if __name__ == "__main__":
    file_paths = [
        Path(__file__).parent / "data" / "example.csv",
        Path(__file__).parent / "data" / "example_1e6.csv",
    ]
    n_runs = 10

    time_chatgpt = []
    time_polars = []
    time_error_handling = []
    time_pymonad = []
    for file_path in file_paths:
        time_chatgpt.append(
            timeit.timeit(partial(average_chatgpt, file_path), number=n_runs)
        )
        time_polars.append(
            timeit.timeit(partial(average_polars, file_path), number=n_runs)
        )
        time_error_handling.append(
            timeit.timeit(partial(average_error_handling, file_path), number=n_runs)
        )
        time_pymonad.append(
            timeit.timeit(partial(average_pymonad, file_path), number=n_runs)
        )

    print("              n=10   | n=1e6 ")
    print(f"Time ChatGPT: {time_chatgpt[0]:.4f} | {time_chatgpt[1]:.4f}")
    print(f"Time polars:  {time_polars[0]:.4f} | {time_polars[1]:.4f}")
    print(f"Time pipe:    {time_error_handling[0]:.4f} | {time_error_handling[1]:.4f}")
    print(f"Time pymonad: {time_pymonad[0]:.4f} | {time_pymonad[1]:.4f}")
