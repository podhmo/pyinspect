default: 00 01 02 03

00:
	$(MAKE) use target=pyinspect |& grep -v '^make' | tee $@.output.md
01:
	$(MAKE) use target=lib2to3 |& grep -v '^make' | tee $@.output.md
02:
	$(MAKE) use target=urllib |& grep -v '^make' | tee $@.output.md
# missing
03:
	$(MAKE) use target=xxx_missing |& grep -v '^make' | tee $@.output.md

use: target ?= collections
use: opts ?=
use:
	@echo '```'
	pyinspect list ${opts} ${target}
	@echo '```'

