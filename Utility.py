from Functions import *
import os

os.system("cls")
while True:
    print "\n"
    print "Welcome to the Abraxas.io System Management Tool"
    print "\n"
    print "Select operation."
    print "Press 1 to Manage Health Checks"
    print "Press 2 to Manage Configurations"
    print "Press 3 to Get Network tools"
    print "Press 4 to Use Powershell Tools"
    print "Press 5 to Exit"
    print "\n"

    choice = raw_input("Enter your choice: ")

    if choice == "1":
        verbose = raw_input("\nWould you like to run in verbose mode? (yes) or no: ")
        if verbose == "no":
            health_check("no")
        else:
            health_check("v")

    elif choice == "2":
        print "2"
        system_importer()

    elif choice == "3":
        network_tools()

    elif choice == "4":
        powershell_tools()

    elif choice == "5":
        os.system("cls")
        break

    else:
        os.system("cls")
        print "\nPlease enter a valid operation."
        continue
