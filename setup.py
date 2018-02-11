import setuptools

setuptools.setup(
    name='lttb',
    version='0.2.0',
    url='https://github.com/javiljoen/lttb.py',

    author='Jack Viljoen',
    author_email='javiljoen@users.noreply.github.com',

    description='Largest-Triangle-Three-Buckets algorithm for downsampling time series–like data',
    long_description=open('README.rst').read(),

    packages=['lttb'],

    install_requires=[
        'numpy',
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
