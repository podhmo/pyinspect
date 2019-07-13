test:
	python setup.py test

examples:
	$(foreach d,$(dir $(shell find . -mindepth 2 -type f -name Makefile)), $(MAKE) -C $(d) &&) echo ok

.PHONY: examples
