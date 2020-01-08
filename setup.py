import setuptools

setuptools.setup(
    name="lttb",
    use_scm_version=True,
    url="https://github.com/javiljoen/lttb.py",
    author="Jack Viljoen",
    author_email="javiljoen@users.noreply.github.com",
    description="Largest-Triangle-Three-Buckets algorithm for downsampling time series-like data",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    packages=["lttb"],
    package_dir={"": "src"},
    install_requires=["numpy"],
    setup_requires=["setuptools_scm"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
