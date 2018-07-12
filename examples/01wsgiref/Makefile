default:
	$(MAKE) readme 2>&1 | grep -v '^make' | tee readme.md

readme:
	@echo '```'
	pyinspect -n wsgiref.simple_server
	@echo '```'
