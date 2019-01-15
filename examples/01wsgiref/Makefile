default:
	$(MAKE) readme 2>&1 | grep -v '^make' | tee readme.md

readme:
	@echo '```'
	pyinspect inspect -n wsgiref.simple_server
	@echo '```'
