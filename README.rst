===================
lttb.py |pypi| |ci|
===================

Numpy implementation of Steinarsson’s *Largest-Triangle-Three-Buckets* algorithm
for downsampling time series–like data

It is based on the original JavaScript code at
https://github.com/sveinn-steinarsson/flot-downsample
and Sveinn Steinarsson’s 2013 MSc thesis
*Downsampling Time Series for Visual Representation.*


Usage
=====

.. code:: python

   import numpy as np
   import lttb

   data = np.array([range(100), np.random.random(100)]).T
   small_data = lttb.downsample(data, n_out=20)
   assert small_data.shape == (20, 2)

A test data set is provided in the source repo in ``tests/timeseries.csv``.
It was downloaded from http://flot.base.is/ and converted from JSON to CSV.

This is what it looks like, downsampled to 100 points:

.. image:: https://github.com/javiljoen/lttb.py/raw/master/tests/timeseries.png


Installation
============

To install the ``lttb`` package into your (virtual) environment::

   pip install lttb


Development
===========

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

In a virtual environment, install the dependencies and development tools::

   pip install -r requirements.txt
   pip install -e .
   pip install -r requirements-dev.txt

The linters and tests can then be run with the commands in the ``Makefile``::

   make lint
   make test
   make test-all

Note that the ``test-all`` task requires the versions of Python used by ``tox``
to have already been installed with ``pyenv``.


History
=======

0.2.2 / 2020-01-08
------------------

- ``setup.py`` was fixed so that this package can be installed in Python 2 again.

0.2.1 / 2019-11-25
------------------

- Versions are now managed with ``setuptools_scm`` rather than ``bumpversion``.
- The code is formatted with Black.

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
