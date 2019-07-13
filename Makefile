examples:
	$(foreach d,$(dir $(shell find . -mindepth 2 -type f -name Makefile)), $(MAKE) -C $(d) &&) echo ok
.PHONY: examples

test:
	python setup.py test

format:
#	pip install -e .[dev]
	black pyinspect setup.py

lint:
#	pip install -e .[dev]
	flake8 pyinspect --ignore W503,E203,E501

build:
#	pip install wheel
	python setup.py bdist_wheel

upload:
#	pip install twine
	twine check dist/pyinspect-$(shell cat VERSION)*
	twine upload dist/pyinspect-$(shell cat VERSION)*

.PHONY: test format lint build upload
