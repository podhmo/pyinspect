# TODO: replace it
default: list resolve inspect

TARGET := xxx

list:
	pyinspect list ${TARGET} | tee ${TARGET}.list
resolve:
	pyinspect resolve ${TARGET} | sed "s@$(shell pwd)@.@g" | tee ${TARGET}.resolve
inspect:
	pyinspect inspect ${TARGET} | tee ${TARGET}.inspect
