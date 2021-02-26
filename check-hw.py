import subprocess
import datetime
import time

errors = open("errorlog.txt", "w")

files = 1000 
callsForEachFile = 100 

i = 0
while(i < files):
	logName = "log"
	logName = '%s%d' % (logName, i);
	logName += ".txt"

	log = open(logName, "w")	

	for x in range(callsForEachFile):
		code, otp = subprocess.getstatusoutput('openamp-connector -de /usr/bin/hw.mpy -f')	
		norm = True 

		#time.sleep(0.5)

		for j in range(1000):
			strToFind = "%s\n%d\n" % ("Hello world! Hello world! Demo.", j)
			if strToFind not in otp:
				norm = False
				break
	
		if norm:
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
