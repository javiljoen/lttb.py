import numpy as np
import pytest

from lttb.validators import (
    contains_no_nans,
    has_two_columns,
    validate,
    x_is_regular,
    x_is_sorted,
    x_is_strictly_increasing,
)


@pytest.fixture(scope="module")
def valid_data():
    nrows = 10
    ys = np.random.standard_normal(nrows)
    xs = np.linspace(1, nrows, nrows)
    return np.array([xs, ys]).T


def test_has_two_columns_passes_for_2d_array_with_2_columns(valid_data):
    assert has_two_columns(valid_data) is None


def test_has_two_columns_fails_for_1d_array():
    array1d = np.random.standard_normal(10)

    with pytest.raises(ValueError):
        has_two_columns(array1d)


def test_has_two_columns_fails_for_3d_array():
    array3d = np.random.standard_normal((3, 10, 2))

    with pytest.raises(ValueError):
        has_two_columns(array3d)


def test_has_two_columns_fails_for_2d_array_with_1_column():
    matrix1c = np.random.standard_normal((10, 1))

    with pytest.raises(ValueError):
        has_two_columns(matrix1c)


def test_has_two_columns_fails_for_2d_array_with_3_columns():
    matrix3c = np.random.standard_normal((10, 3))

    with pytest.raises(ValueError):
        has_two_columns(matrix3c)


def test_x_is_strictly_increasing_passes_for_valid_data(valid_data):
    assert x_is_strictly_increasing(valid_data) is None


def test_x_is_strictly_increasing_fails_with_repeated_xs():
    data = np.array([[1, 1, 2, 2], np.random.standard_normal(4)]).T

    with pytest.raises(ValueError):
        x_is_strictly_increasing(data)


def test_x_is_sorted_passes_for_valid_data(valid_data):
    assert x_is_sorted(valid_data) is None


def test_x_is_sorted_passes_with_repeated_xs():
    data = np.array([[1, 1, 2, 2], np.random.standard_normal(4)]).T
    assert x_is_sorted(data) is None


def test_x_is_sorted_fails_if_xs_not_sorted():
    data = np.array([[1, 4, 3, 2], np.random.standard_normal(4)]).T

    with pytest.raises(ValueError):
        x_is_sorted(data)


def test_x_is_regular_passes_with_valid_data(valid_data):
    assert x_is_regular(valid_data) is None


def test_x_is_regular_fails_if_x_intervals_are_not_constant():
    data = np.array([[1, 2, 4, 9], np.random.standard_normal(4)]).T

    with pytest.raises(ValueError):
        x_is_regular(data)


def test_contains_no_nans_passes_with_valid_data(valid_data):
    assert contains_no_nans(valid_data) is None


def test_contains_no_nans_fails_if_nan_in_xs():
    data = np.array([[0, 1, 2, np.nan], [0.0, 1.0, 2.0, 3.0]]).T

    with pytest.raises(ValueError):
        contains_no_nans(data)


def test_contains_no_nans_fails_if_nan_in_ys():
    data = np.array([[0, 1, 2, 3], [1.0, np.nan, 2.6, np.nan]]).T

    with pytest.raises(ValueError):
        contains_no_nans(data)


def test_validate_multiple_criteria_passes_for_valid_data(valid_data):
    validate(valid_data, [has_two_columns, x_is_regular])


def test_validate_raises_with_multiple_messages():
    data = np.random.standard_normal((4, 3))  # 3 columns
    data[:, 0] = [1, 4, 2, 9]  # unsorted x values
    data[2, 1] = np.nan  # missing y value
    validators = [has_two_columns, x_is_sorted, x_is_regular, contains_no_nans]

    with pytest.raises(ValueError) as exc:
        validate(data, validators)

    assert exc.match(
        "data does not have 2 columns; "
        "data is not sorted on the first column; "
        "first column is not regularly spaced; "
        "data contains NaN values"
    )
