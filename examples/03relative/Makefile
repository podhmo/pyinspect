default: list resolve inspect
list:
	pyinspect list xxx | tee xxx.list
resolve:
	pyinspect resolve xxx | sed "s@$(shell pwd)@.@g" | tee xxx.resolve
inspect:
	pyinspect inspect xxx | tee xxx.inspect
