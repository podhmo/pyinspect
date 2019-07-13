default: 00 01 02 03

00:
	$(MAKE) use target=collections |& grep -v '^make' | tee $@.output.md
01:
	$(MAKE) use target=wsgiref.simple_server |& grep -v '^make' | tee $@.output.md
02:
	$(MAKE) use target=jupyter_console.app:ZMQTerminalIPythonApp |& grep -v '^make' | tee $@.output.md
03:
	$(MAKE) use target=enum opts="" |& grep -v '^make' | tee $@.output.md

use: target ?= collections
use: opts ?= -n
use:
	@echo '```'
	pyinspect inspect ${opts} ${target}
	@echo '```'
