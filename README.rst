===================
lttb.py |pypi| |ci|
===================

Numpy implementation of Steinarsson’s *Largest-Triangle-Three-Buckets* algorithm
for downsampling time series–like data
while retaining the overall shape and variability in the data

LTTB is well suited to filtering time series data for visual representation,
since it reduces the number of *visually redundant* data points,
resulting in smaller file sizes and faster rendering of plots.

Note that it is not a technique for statistical aggregation,
cf. regression models or non-parametric curve fitting / smoothing.

This implementation is based on the original JavaScript code at
https://github.com/sveinn-steinarsson/flot-downsample
and Sveinn Steinarsson’s 2013 MSc thesis
*Downsampling Time Series for Visual Representation.*

Licence: MIT


Usage
=====

Install the ``lttb`` package into your (virtual) environment::

   $ pip install lttb


The function ``lttb.downsample()`` can then be used in your Python code:

.. code:: python

   import numpy as np
   import lttb

   # Generate an example data set of 100 random points:
   #  - column 0 represents time values (strictly increasing)
   #  - column 1 represents the metric of interest: CPU usage, stock price, etc.
   data = np.array([range(100), np.random.random(100)]).T

   # Downsample it to 20 points:
   small_data = lttb.downsample(data, n_out=20)
   assert small_data.shape == (20, 2)

A test data set is provided in the source repo in ``tests/timeseries.csv``.
It was downloaded from http://flot.base.is/ and converted from JSON to CSV.

This is what it looks like, downsampled to 100 points:

.. image:: https://github.com/javiljoen/lttb.py/raw/master/tests/timeseries.png


Input validation
----------------

By default, ``downsample()`` checks that the input data satisfies the following constraints:

- it is a two-dimensional array of two columns;
- the values in the first column are strictly increasing; and
- there are no missing (NaN) values in the data.

These checks can be skipped (e.g. if you know that your data will always meet these conditions),
or additional checks can be added (e.g. that the time values must be evenly spaced),
by passing in a different list of validation functions, e.g.:

.. code:: python

   # No input validation:
   small_data = lttb.downsample(data, n_out=20, validators=[])

   # Stricter check on x values:
   from lttb.validators import *
   small_data = lttb.downsample(data, n_out=20, validators=[has_two_columns, x_is_regular])


Contributing
============

If you find a bug or have an idea for improving this package,
please describe it in an *issue* on GitHub.

Patches are welcome and may be submitted as *pull requests* on GitHub.
They should pass the tests and linting checks listed in the ``Makefile``,
and any new features should be covered by tests.


Development setup
-----------------

Create a Python virtual environment, e.g. using ``pyenv`` and/or ``direnv``.
In that venv, install the dependencies and development tools::

   pip install -r requirements.txt -r requirements-dev.txt
   pip install -e .

The linters and tests can then be run with the commands in the ``Makefile``::

   make lint
   make test

If you are using ``pyenv``, you can run the tests on multiple versions of Python.
Use ``pyenv`` to install pythons from the 2.7, 3.5, and 3.8 series;
then activate them in the project folder and run the tests with, e.g.::

   pyenv local 3.8.2 3.5.9 2.7.17
   make test-all


History
=======

0.3.0 / 2020-09-15
------------------

- Validation of input data is now configurable.
- New default: ``downsample()`` raises ``ValueError`` if input data contains NaN values.
  This can be disabled by removing ``contains_no_nans()`` from the list of validators.
- [dev] Imports are now sorted with isort.

0.2.2 / 2020-01-08
------------------

- ``setup.py`` was fixed so that this package can be installed in Python 2 again.

0.2.1 / 2019-11-25
------------------

- [dev] Versions are now managed with ``setuptools_scm`` rather than ``bumpversion``.
- [dev] The code is formatted with Black.

0.2.0 / 2018-02-11
------------------

- Performance improvements
- Released on PyPI (on 2019-11-06)

0.1.0 / 2017-03-18
------------------

- Initial implementation


Contributors
============

- Jack Viljoen (@javiljoen) – original Numpy implementation
- Guillaume Bethouart (@guillaumeB) – performance improvements


.. |pypi| image:: https://img.shields.io/pypi/v/lttb?color=blue
   :target: https://pypi.org/project/lttb/

.. |ci| image:: https://travis-ci.com/javiljoen/lttb.py.svg?branch=master
   :target: https://travis-ci.com/javiljoen/lttb.py
