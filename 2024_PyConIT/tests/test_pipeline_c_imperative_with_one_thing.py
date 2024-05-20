from pipeline.pipeline_c_imperative_with_one_thing import calculate_average


def test_calculate_average():
    assert calculate_average([1, 2, 3]) == 2
    assert calculate_average([1, 2, 3, float("inf")]) == 2
