import subprocess
from variables import *
def pinger(lines, flag):
	for item in lines:
		hostname = item.rstrip()
		ping_response = subprocess.Popen(["ping", hostname, "-n", '1', "-w", "200"], stdout=subprocess.PIPE).stdout.read()
		if exception1 in ping_response:
			print response1 % hostname
		elif exception2 in ping_response:
			print response2 % hostname
		elif exception3 in ping_response:
			print response3 % hostname
		elif exception4 in ping_response:
			print response4 % hostname
		elif exception5 in ping_response:
			print response5 % hostname
		else:
			if flag in ('v', '-v','verbose','-verbose'):
				print response6 % hostname 
			else:
				continue