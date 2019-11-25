import numpy as np

import lttb


def test_downsampling():
    csv = "tests/timeseries.csv"
    data = np.genfromtxt(csv, delimiter=",", names=True)
    xs = data["X"]
    ys = data["Y"]
    data = np.array([xs, ys]).T
    out = lttb.downsample(data, 100)
    assert out.shape == (100, 2)
