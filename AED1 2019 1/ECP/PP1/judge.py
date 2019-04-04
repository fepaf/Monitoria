import os
import sys

for filename in os.listdir("."):
	if (filename[-3:]==".in"):
		if (os.system(" ".join(["python3",sys.argv[1],"<",filename,">",filename[:-3]+".out"]))==0):
			print("OK",filename[:-3])
		else :
			print("ERRO",filename[:-3])
		
