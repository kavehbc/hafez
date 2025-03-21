build:
	python -m pip install --upgrade build
	python -m build

push:
	python -m pip install --upgrade twine
	python -m pip install -U packaging
	python -m twine upload dist/*

install:
	pip install -e . --upgrade --upgrade-strategy only-if-needed

install-whl:
    pip install dist/hafez-0.2.6-py3-none-any.whl

module:
	pip install dist/hafez-0.2.6.tar.gz
