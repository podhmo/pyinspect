default:
	$(MAKE) readme 2>&1 | grep -v '^make' | tee readme.md

readme:
	@echo '```console'
	pyinspect jupyter_console.app:ZMQTerminalIPythonApp
	@echo '```'
