.PHONY: clean lint build deploy virtual-env activate-virtual-env

virtual-env:
	virtualenv -p python3 venv

clean:
	rm -r build

build:
	pip install .