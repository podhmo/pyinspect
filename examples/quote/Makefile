default: 00 01 02 03

00:
	pyinspect quote pyinspect.code.quote:L123 | tee 00.output.md
01:
	pyinspect quote argparse:L1900 | tee 01.output.md
	pyinspect quote argparse:L1900 --show-fulldoc | tee 01.output.fulldoc.md

# missing
02:
	pyinspect quote argparses:L1900 |& tee 02.output.md

# line is empty
03:
	pyinspect quote argparse:L1900000 |& tee 03.output.md
