default: 00 01 02

00:
	$(MAKE) use target=requests |& grep -v '^make' | tee $@.output.md
01:
	$(MAKE) use target=notebook |& grep -v '^make' | tee $@.output.md
02:
	$(MAKE) use target=pytest |& grep -v '^make' | tee $@.output.md

use: target ?= requests
use:
	@echo '```'
	pyinspect webpage --show-only ${target}
	@echo '```'

