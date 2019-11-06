lttb.py |pypi|
==============

Numpy implementation of Steinarsson’s *Largest-Triangle-Three-Buckets*
algorithm for downsampling time series–like data

Based on the original JavaScript code:

https://github.com/sveinn-steinarsson/flot-downsample

and:

Sveinn Steinarsson. 2013.  *Downsampling Time Series for Visual
Representation.* MSc thesis. University of Iceland.

A test data set is provided in ``tests/timeseries.csv``.
It was downloaded from http://flot.base.is/ and converted from JSON to CSV.


Usage
-----

.. code:: python

   import numpy as np
   import lttb
   data = np.array([range(100), np.random.random(100)]).T
   small_data = lttb.downsample(data, n_out=20)
   assert small_data.shape == (20, 2)

For example, here is the data set provided in ``tests`` downsampled to 100
points:

.. image:: http://github.com/javiljoen/lttb.py/raw/master/tests/timeseries.png


Installation
------------

To install the ``lttb`` package into your (virtual) environment::

   pip install lttb


Requirements
^^^^^^^^^^^^

* Python 3
* Numpy


Licence: MIT


Contributors
------------

- Jack Viljoen (@javiljoen) – original Numpy implementation
- Guillaume Bethouart (@guillaumeB) – performance improvements



.. |pypi| image:: https://img.shields.io/pypi/v/lttb?color=blue
   :target: https://pypi.org/project/lttb/
