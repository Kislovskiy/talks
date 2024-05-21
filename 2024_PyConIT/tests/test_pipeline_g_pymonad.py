import csv
import tempfile
import pytest
from pathlib import Path

from hypothesis import given, strategies as st
from pipeline.pipeline_g_pymonad import compute_average_score
from pymonad.either import Either


def test_compute_average_score():
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Score"])  # Header
        writer.writerow(["Alice", "10"])  # Row 1
        writer.writerow(["Bob", "20"])  # Row 2
        writer.writerow(["Jenny", "30"])  # Row 3
        temp_path = f.name

    expected_average_score = (10 + 20 + 30) / 3

    result = compute_average_score(Path(temp_path))

    assert isinstance(result, Either)
    assert result.is_right()
    assert result.value == expected_average_score

    Path(temp_path).unlink()


# Define a strategy for generating valid CSV data
csv_data_strategy = st.lists(
    st.tuples(
        st.text(min_size=1),  # Name column
        st.floats(min_value=0, allow_nan=False, allow_infinity=False),  # Score column
    ),
    min_size=1,  # At least one row of data
)


@given(csv_data_strategy)
def test_compute_average_score(csv_data):
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Score"])
        for name, score in csv_data:
            writer.writerow([name, str(score)])
        temp_path = f.name

    # Calculate the expected average score
    expected_average_score = sum(score for _, score in csv_data) / len(csv_data)

    # Pass the temporary file path to the compute_average_score function
    result = compute_average_score(temp_path)

    assert isinstance(result, Either)
    if result.is_right():
        assert result.value == pytest.approx(expected_average_score)

    # Clean up the temporary file
    Path(temp_path).unlink()
