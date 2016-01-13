#Run this script to select a file to add systems to and then add the system.
import os
import sys

while True:
	options = []
	for file in os.listdir("./InfrastructureItems"):
	    if file.endswith(".txt"):
	    	options.append(file)

	nums_and_files = zip(range(len(options)),options)
	print "\nAvailable lists to modify: \n"
	for x in nums_and_files:
		print x
	choice = raw_input("Please type desired number to edit or 'exit' to quit: ")
	if choice == "exit":
		print "Thanks for keeping your files up to date!"
		break
	else:
		choice = int(choice)
	while True:
		filelocation = "./InfrastructureItems/" + options[choice]
		selectedfile = open(filelocation, "a+")
		morehosts = raw_input("\n\nWould you like to add an IP/Hostname to this file? yes/no : ")
		if morehosts == "yes":
			hostname = raw_input("\nPlease enter IP/Hostname to add to selected file: ")
			selectedfile.write("\n"+hostname)
			print "IP added Successfully"
		elif morehosts != "no":
			print "Please enter 'yes' or 'no'"
		else:
			selectedfile.close()
			break
