.PHONY: help clean clean-pyc clean-build lint test test-all build upload

help:
	@echo "clean - remove Python file & build artifacts"
	@echo "lint - run linters to check the code style and formatting"
	@echo "test - run tests with the default Python"
	@echo "test-all - run tests in multiple environments"
	@echo "build - package"
	@echo "upload - release package to PyPI"

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr src/*.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name __pycache__ -type d -exec rmdir {} +
	rm -fr .cache/

lint:
	flake8 lttb tests
	black --check .

test:
	pytest -n 2

test-all:
	PYENV_VERSION="" tox -p 2

build: clean
	python setup.py sdist bdist_wheel
	ls -l dist

upload: build
	twine check dist/*
	twine upload dist/*
