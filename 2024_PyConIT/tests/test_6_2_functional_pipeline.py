from pipeline.tmp import get_hello
from pipeline.functional_pipeline import remove_header
from pymonad.either import Left, Right
from hypothesis import given, strategies as st


def test_get_hello():
    val = get_hello()
    assert val == "Hello, World!"


@given(st.lists(st.lists(st.text())))
def test_remove_header(test_data):
    # test_data = [
    #     ["Name", "Score"],
    #     ["Alice", "90"],
    #     ["Bob", "85"],
    #     ["Charlie", "95"],
    # ]

    assert (
        remove_header(test_data) == len(test_data) - 1
        if len(test_data) > 1
        else Left("Error: Unable to remove header")
    )
