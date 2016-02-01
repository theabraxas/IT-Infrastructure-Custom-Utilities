from sys import argv
from modules.pinger import *

if len(argv) > 1:
    flag = argv[1]
else:
    flag = ""

# Gets Configuration Files
ConfigFiles = []
for config_file in os.listdir("./InfrastructureItems"):
    if config_file.endswith(".txt"):
        ConfigFiles.append("InfrastructureItems/" + config_file)

print "Testing All Core Systems...\n"

for i in range(len(ConfigFiles)):
    print systemname % ConfigFiles[i]
    devices = open(ConfigFiles[i], "r")
    lines = devices.readlines()
    pinger(lines, flag)
    devices.close()
