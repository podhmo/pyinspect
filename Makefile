test:
	python setup.py test

examples: $(dir $(shell find . -mindepth 2 -type f -name Makefile))
	for i in $^; do make -C $$i; done
.PHONY: examples
