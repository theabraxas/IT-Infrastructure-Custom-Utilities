# Run this script to select a file to add systems to and then add the system.
import os

while True:
    options = []
    for config_file in os.listdir("./InfrastructureItems"):
        if config_file.endswith(".txt"):
            options.append(config_file)

    nums_and_files = zip(range(len(options)), options)
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
        file_location = "./InfrastructureItems/" + options[choice]
        selected_file = open(file_location, "a+")
        more_hosts = raw_input("\n\nWould you like to add an IP/Hostname to this file? yes/no : ")
        if more_hosts == "yes":
            hostname = raw_input("\nPlease enter IP/Hostname to add to selected file: ")
            selected_file.write("\n" + hostname)
            print "IP added Successfully"
        elif more_hosts != "no":
            print "Please enter 'yes' or 'no'"
        else:
            selected_file.close()
            break
