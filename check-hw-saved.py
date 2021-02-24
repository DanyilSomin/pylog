import subprocess
import datetime

strToFind = "Hello world!"




errors = open("errorlog.txt", "w")

i = 0
while(i < 5):

	logName = "log"
	logName = '%s%d' % (logName, i);
	logName += ".txt"

	log = open(logName, "w")	

	for x in range(5):



		code, otp = subprocess.getstatusoutput('openamp-connector -de /usr/bin/hw.mpy -f')	
		if strToFind in otp:
			str = "Ok: "
			str += datetime.datetime.now().strftime("%d %m, %H:%M:%S.")

			log.write(str)
			log.write("\n")
		else:
			str = "Not ok: "
			str += datetime.datetime.now().strftime("%d %m, %H:%M:%S.")

			log.write(str)
			log.write("\n")

			errors.write("%d" % i)
			errors.write(" ")
			errors.write(str)
			errors.write("\n")
			print(str)


	log.close()

	print(i)
	i = i + 1
