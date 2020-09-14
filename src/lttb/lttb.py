import numpy as np

from .validators import (
    contains_no_nans,
    has_two_columns,
    validate,
    x_is_strictly_increasing,
)

default_validators = [has_two_columns, contains_no_nans, x_is_strictly_increasing]


def _areas_of_triangles(a, bs, c):
    """Calculate areas of triangles from duples of vertex coordinates.

    Uses implicit numpy broadcasting along first axis of ``bs``.

    Returns
    -------
    numpy.array
        Array of areas of shape (len(bs),)
    """
    bs_minus_a = bs - a
    a_minus_bs = a - bs
    return 0.5 * abs(
        (a[0] - c[0]) * (bs_minus_a[:, 1]) - (a_minus_bs[:, 0]) * (c[1] - a[1])
    )


def downsample(data, n_out, validators=default_validators):
    """Downsample ``data`` to ``n_out`` points using the LTTB algorithm.

    Reference
    ---------
    Sveinn Steinarsson. 2013. Downsampling Time Series for Visual
    Representation. MSc thesis. University of Iceland.

    Parameters
    ----------
    data : numpy.array
        A 2-dimensional array with time values in the first column
    n_out : int
        Number of data points to downsample to
    validators : sequence of callables, optional
        Validation functions that take an array as argument and
        raise ``ValueError`` if the array fails some criterion

    Constraints
    -----------
      - ncols(data) == 2
      - 3 <= n_out <= nrows(data)
      - the first column of ``data`` should be strictly monotonic.

    Returns
    -------
    numpy.array
        Array of shape (n_out, 2)

    Raises
    ------
    ValueError
        If ``data`` fails the validation checks,
        or if ``n_out`` falls outside the valid range.
    """
    # Validate input
    validate(data, validators)

    if n_out > data.shape[0]:
        raise ValueError("n_out must be <= number of rows in data")

    if n_out == data.shape[0]:
        return data

    if n_out < 3:
        raise ValueError("Can only downsample to a minimum of 3 points")

    # Split data into bins
    n_bins = n_out - 2
    data_bins = np.array_split(data[1 : len(data) - 1], n_bins)

    # Prepare output array
    # First and last points are the same as in the input.
    out = np.zeros((n_out, 2))
    out[0] = data[0]
    out[len(out) - 1] = data[len(data) - 1]

    # Largest Triangle Three Buckets (LTTB):
    # In each bin, find the point that makes the largest triangle
    # with the point saved in the previous bin
    # and the centroid of the points in the next bin.
    for i in range(len(data_bins)):
        this_bin = data_bins[i]

        if i < n_bins - 1:
            next_bin = data_bins[i + 1]
        else:
            next_bin = data[len(data) - 1 :]

        a = out[i]
        bs = this_bin
        c = next_bin.mean(axis=0)

        areas = _areas_of_triangles(a, bs, c)

        out[i + 1] = bs[np.argmax(areas)]

    return out
