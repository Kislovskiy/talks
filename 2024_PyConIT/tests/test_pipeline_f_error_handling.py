from pipeline.pipeline_f_error_handling import (
    calculate_average_score,
    is_valid_score,
    remove_row,
)
import pytest
from hypothesis import given, example, strategies as st


@given(st.lists(st.one_of(st.floats(), st.none(), st.integers())))
@example([])
@example([None, float("inf"), float("-inf"), float("nan")])
def test_calculate_average_general_properties(column_values):
    filtered_values = list(filter(is_valid_score, column_values))
    if filtered_values:
        result = calculate_average_score(filtered_values)
        assert is_valid_score(result), "Result should be a valid number"
        assert (
            min(filtered_values) <= result <= max(filtered_values)
        ), "Result should be between min and max of filtered values"
    else:
        with pytest.raises(
            ZeroDivisionError,
            match="Cannot compute average of empty list or list with only invalid values",
        ):
            calculate_average_score(column_values)


@given(st.data())
def test_remove_row(data):
    rows = data.draw(
        st.lists(st.integers(min_value=0), min_size=1)
    )  # At least one row index
    row_index = data.draw(
        st.integers(min_value=0, max_value=len(rows) - 1)
    )  # Row index within bounds
    data_list = list(range(len(rows)))  # Example data list

    # Apply remove_row function to example data
    try:
        result = remove_row(row_index, data_list)
        if row_index >= len(data_list) or row_index < 0:
            # Check if IndexError is raised for out of bounds index
            with pytest.raises(IndexError):
                remove_row(row_index, data_list)
        else:
            # Check if row is removed correctly
            assert len(result) == len(data_list) - row_index
            assert result == data_list[row_index:]
    except IndexError as e:
        # Check if IndexError is raised correctly
        assert str(e) == f"Error removing header: list index out of range"
