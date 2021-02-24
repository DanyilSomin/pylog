import subprocess
import datetime

errors = open("errorlog.txt", "w")

i = 0
while(i < 765):
	logName = "log"
	logName = '%s%d' % (logName, i);
	logName += ".txt"

	log = open(logName, "r")	

	for line in log:
		if "Not ok:" in line:
			errors.write("Filenum: {} \t".format(i))
			errors.write(line)
	print(i)

	i = i + 1	