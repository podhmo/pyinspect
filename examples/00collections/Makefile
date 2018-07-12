default:
	$(MAKE) readme 2>&1 | grep -v '^make' | tee readme.md

readme:
	@echo '```'
	pyinspect --only-this-module collections
	@echo '```'
