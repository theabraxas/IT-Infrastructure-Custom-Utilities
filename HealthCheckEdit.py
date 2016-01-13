import os
import subprocess
import sys

#Variables
##Make this an included module
exception1 = "TTL expired in transit."
exception2 = "Destination net unreachable."
exception3 = "Request timed out."
exception4 = "Ping request could not find"
exception5 = "Usage:"

##Get Configuration Files
ConfigFiles = []
for file in os.listdir("./InfrastructureItems"):
    if file.endswith(".txt"):
    	ConfigFiles.append("InfrastructureItems/"+file) 

##Import this function instead of defining it here.
def pinger():
	for item in lines:
		hostname = item.rstrip()
		ping_response = subprocess.Popen(["ping", hostname, "-n", '1', "-w", "50"], stdout=subprocess.PIPE).stdout.read()
		if exception1 in ping_response:
			 print "\033[1;31m%s is unreachable, TTL expired in transit.\033[1;m" % hostname
		elif exception2 in ping_response:
			print '\033[1;31m%s is unreachable.\033[1;m' % hostname
		elif exception3 in ping_response:
			print '\033[1;31m%s timed out.\033[1;m' % hostname
		elif exception4 in ping_response:
			print '\033[1;31m%s could not be found.\033[1;m' % hostname
		elif exception5 in ping_response:
			print '\033[1;31m This entry is a blank line or space, please edit config file to fix.\033[1;m' % hostname
		else:
			print '\033[1;32m%s is online.\033[1;m' % hostname 

print "Testing All Core Systems...\n"
for i in range(len(ConfigFiles)):
	print "\n\033[1;37mTesting %s...\033[1;m\n" % ConfigFiles[i]
	devices = open(ConfigFiles[i], "r")
	lines = devices.readlines()
	pinger()
	devices.close() 