import os
import sys

options = []
for file in os.listdir("./InfrastructureItems"):
    if file.endswith(".txt"):
    	options.append(file)

nums_and_files = zip(range(len(options)),options)
print "\nAvailable lists to modify: \n"
for x in nums_and_files:
	print x
choice = int(raw_input("Please type desired number and press enter: "))

#Add Error Check
filelocation = "./InfrastructureItems/" + options[choice]
selectedfile = open(filelocation, "a+")

x = True
while x == True:
	#while True, add confirmation
	morehosts = raw_input("\n\nWould you like to add an IP/Hostname to this file? yes/no : ")
	if morehosts == "yes" or "Yes" or "y":
		hostname = raw_input("\nPlease enter IP/Hostname to add to selected file: ")
		selectedfile.write("\n"+hostname)
		print "IP added Successfully"
	elif morehosts != "no" or "No" or "n":
		print "Please enter 'yes' or 'no'"
	else:
		x = False
#add check to remove whitespace
for line in sys.stdin:
    if line[:-1]:
        sys.stdout.write(line)
selectedfile.close()