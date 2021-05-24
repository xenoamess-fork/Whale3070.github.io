import os

mydir = []

path="/home/kali/Documents/Whale3070.github.io/public/2016/"

for i in range(2,13):
	for j in range(1,13):
		if i<10:
			if j <10:
				finalpath = path+"0"+str(i)
				#os.system("cd "+path+str(j))
				month = "2016-0"+str(i)
				time=month
				print(finalpath)
		if i>=10:
			finalpath = "cd "+path+str(i)
			month = "2016-"+str(i)
			time=month
			print(finalpath)
	