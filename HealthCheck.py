import os
from sys import argv
from modules.pinger import *

if len(argv) > 1:
	flag = argv[1]
else:
	flag =""

##Gets Configuration Files
ConfigFiles = []
for file in os.listdir("./InfrastructureItems"):
    if file.endswith(".txt"):
    	ConfigFiles.append("InfrastructureItems/"+file) 

print "Testing All Core Systems...\n"

for i in range(len(ConfigFiles)):
	print systemname % ConfigFiles[i]
	devices = open(ConfigFiles[i], "r")
	lines = devices.readlines()
	pinger(lines, flag)
	devices.close() 
	print systemname
print "\n\n\n"