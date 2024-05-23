import logging
import timeit
from functools import partial
from pathlib import Path
from typing import Dict, Callable, List

from rich.logging import RichHandler

from pipeline_a_ChatGPT import read_csv_and_compute_average as average_chatgpt
from pipeline_a_polars import compute_average_score as average_polars
from pipeline_f_error_handling import compute_average_score as average_error_handling
from pipeline_g_pymonad import compute_average_score as average_pymonad

# Set up the logger
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

logger = logging.getLogger("rich")


def measure_time(
    function: Callable[[Path], float], file_path: Path, n_runs: int = 10
) -> float:
    """
    Measure the time it takes to run a function on a file for n_runs times.

    :param function: The function to be timed. It should take a Path object as an argument and return a float.
    :type function: Callable[[Path], float]
    :param file_path: The path of the file on which the function will be run.
    :type file_path: Path
    :param n_runs: The number of times the function will be run. Default is 10.
    :type n_runs: int
    :return: The time it takes to run the function n_runs times.
    :rtype: float
    """
    logger.info(f"Running {function.__name__} on {file_path.name} for {n_runs} times")
    return timeit.timeit(partial(function, file_path), number=n_runs)


def print_results(times: Dict[str, List[float]]) -> None:
    """
    Print the results of the time measurements in a formatted manner.

    :param times: A dictionary where the keys are descriptions of the functions and the values are lists of floats
    representing the times it took to run the functions.
    :type times: Dict[str, List[float]]
    """
    results = "\n".join(
        f"{'time ' + desc:.<20} {time_small:.4f} | {time_large:.4f}"
        for desc, (time_small, time_large) in times.items()
    )
    print(f"{'':.<20} n=10   | n=1e6\n{results}")


def main() -> None:
    """
    Measure the time it takes to process the data in the example.csv and example_1e6.csv files.

    :return: None
    """
    file_paths = [
        Path(__file__).parent / "data" / "example.csv",
        Path(__file__).parent / "data" / "example_1e6.csv",
    ]

    functions = {
        "ChatGPT": average_chatgpt,
        "polars": average_polars,
        "pipe": average_error_handling,
        "pymonad": average_pymonad,
    }

    times = {
        description: [measure_time(func, file_path) for file_path in file_paths]
        for description, func in functions.items()
    }

    print_results(times)


if __name__ == "__main__":
    main()
