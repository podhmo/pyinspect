default: 00 01 02 03

00:
	$(MAKE) use target=pyinspect |& grep -v '^make' | sed 's@$(HOME)@.@g' | tee $@.output.md
01:
	$(MAKE) use target=argparse |& grep -v '^make' | sed 's@$(HOME)@.@g' | tee $@.output.md

02:
	$(MAKE) use target=jupyter_console |& grep -v '^make' | sed 's@$(HOME)@.@g' | tee $@.output.md

# missing
03:
	$(MAKE) use target=xxxxxxxxxx |& grep -v '^make' | sed 's@$(HOME)@.@g' | tee $@.output.md

use: target ?= collections
use:
	@echo '```'
	pyinspect resolve ${target}
	@echo '```'

