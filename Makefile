.PHONY: help clean clean-pyc clean-build list test build

help:
	@echo "clean - remove Python file & build artifacts"
	@echo "test - run tests with the default Python"
	@echo "build - package"

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name __pycache__ -type d -exec rmdir {} +
	rm -fr .cache/

test:
	pytest

build: clean
	python setup.py bdist_wheel
	ls -l dist
