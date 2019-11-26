import lttb
import numpy as np
from hypothesis import assume, given
from hypothesis.strategies import builds, integers


def load_test_data():
    csv = "tests/timeseries.csv"
    data = np.genfromtxt(csv, delimiter=",", names=True)
    xs = data["X"]
    ys = data["Y"]
    return np.array([xs, ys]).T


@given(integers(min_value=3, max_value=5000))
def test_downsampled_test_data_is_correct_shape(n_out):
    data = load_test_data()
    out = lttb.downsample(data, n_out)
    assert out.shape == (n_out, 2)


@given(integers(min_value=3, max_value=5000))
def test_downsampling_test_data_retains_variation(n_out):
    data = load_test_data()
    out = lttb.downsample(data, n_out)
    assert np.var(out[:, 1]) >= 29.5  # var(data) == 30.9968


def gen_valid_data(nrows):
    ys = np.random.standard_normal(nrows) * 1000
    xs = np.linspace(1, nrows, nrows)
    return np.array([xs, ys]).T


@given(
    builds(gen_valid_data, integers(min_value=3, max_value=5000)),
    integers(min_value=3, max_value=5000),
)
def test_downsampled_random_data_is_correct_shape(data, n_out):
    assume(n_out <= len(data))
    out = lttb.downsample(data, n_out)
    assert out.shape == (n_out, 2)


@given(
    builds(gen_valid_data, integers(min_value=3, max_value=5000)),
    integers(min_value=3, max_value=5000),
)
def test_downsampling_random_data_retains_variation(data, n_out):
    assume(n_out <= len(data))
    out = lttb.downsample(data, n_out)
    var_in = np.var(data[:, 1])
    var_out = np.var(out[:, 1])
    assert var_out >= 0.95 * var_in
