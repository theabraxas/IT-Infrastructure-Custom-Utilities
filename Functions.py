from modules.pinger import *


def health_check(verbose):
    import os
    while True:
        os.system('cls')
        print "\n"
        print "Welcome to the Health Check Scanner"
        print "\n"
        print "Press 1 to run a full environment scan."
        print "Press 2 to run a scan against an specific environment."
        print "Press 3 to Exit."
        print "\n"

        choice = raw_input("Enter your choice: ")
        if choice == "1":
            if "v" in verbose:
                flag = "v"
            else:
                flag = ""

            config_files = []
            for config_file in os.listdir("./InfrastructureItems"):
                if config_file.endswith(".txt"):
                    config_files.append("InfrastructureItems/" + config_file)

            print "Testing All Core Systems...\n"

            for i in range(len(config_files)):
                print systemname % config_files[i]
                devices = open(config_files[i], "r")
                lines = devices.readlines()
                pinger(lines, flag)
                devices.close()
            print "\n\033[1;37mScan Completed Successfully.\033[1;m\n"
            raw_input("Press enter to continue...")
            os.system("cls")

        elif choice == "2":
            if "v" in verbose:
                flag = "v"
            else:
                flag = ""

            options = []
            for config_file in os.listdir("./InfrastructureItems"):
                if config_file.endswith(".txt"):
                    options.append(config_file)
            nums_and_files = zip(range(len(options)), options)
            os.system("cls")
            print "\nAvailable lists to modify: \n"
            for x in nums_and_files:
                print x
            choice = raw_input("Please type number of desired environment to scan or type 'exit' to quit: ")

            if not choice.isdigit():
                os.system("cls")
                break
            elif int(choice) in range(len(options)):
                file_location = "./InfrastructureItems/" + options[int(choice)]
                selected_file = open(file_location, "r")
                config_files = [0]
                print "\nTesting selected System...\n"
                for i in range(len(config_files)):
                    devices = selected_file
                    lines = devices.readlines()
                    pinger(lines, flag)
                    devices.close()
                print "\n\033[1;37mScan Completed Successfully.\033[1;m\n"
                selected_file.close()
                raw_input("Press enter to continue...")
                os.system("cls")

            else:
                os.system('cls')
                break

        elif choice == "3":
            os.system('cls')
            break


def system_importer():
    import os
    import glob
    os.system('cls')
    while True:
        os.chdir("C:/users/stewart.olson/desktop/stuff/code/python/HealthCheck")
        print "\n"
        print "Welcome to the HealthCheck Configuration Manager"
        print "\n"
        print "Press 1 to add addresses to config files."
        print "Press 2 to search for addresses in config files."
        print "Press 3 to view config files."
        print "Press 4 to remove an entry from a config file."
        print "Press 5 to remove an entry from all config files."
        print "Press 6 to create a new config file."
        print "Press 7 to remove a configuration file."
        print "Press 8 to exit the configuration manager."
        print "\n"
        choice = raw_input("Enter your selection: ")
        os.system("cls")

        if choice == "1":
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
                os.system('cls')
                print "\n\nThanks for keeping your files up to date!"
                break
            elif not choice.isdigit():
                os.system('cls')
                print "\n\nThanks for keeping your files up to date!"
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
                    print "IP added Successfully"
                    selected_file.close()
                    os.system("cls")
                    break

        elif choice == "2":
            searchresult = []
            os.system("cls")
            search = raw_input("Please enter IP/Hostname to search: ")
            os.chdir("C:/users/stewart.olson/desktop/stuff/code/Python/HealthCheck/InfrastructureItems")
            print "\n"
            print "Searching files..."
            for config_file in glob.glob('*.txt'):
                with open(config_file) as f:
                    contents = f.read()
                if search in contents:
                    searchresult += contents
                    print "IP or hostname has been found in " + config_file
            print "\n"
            clean = raw_input("Press (1) to keep contents visible or 2 to clear the screen: ")
            if clean == "1":
                continue
            elif clean == "2":
                os.system("cls")
            else:
                continue

        elif choice == "3":
            os.system("cls")
            print "Configuration Viewer"
            options = []
            for config_file in os.listdir("./InfrastructureItems"):
                if config_file.endswith(".txt"):
                    options.append(config_file)
            nums_and_files = zip(range(len(options)), options)
            for x in nums_and_files:
                print x
            print "\nAvailable lists to modify: \n"
            choice = raw_input("Please type desired number to edit or 'exit' to quit: ")
            if choice == "exit":
                os.system('cls')
                print "\n\nThanks for keeping your files up to date!"
            else:
                choice = int(choice)
            file_location = "./InfrastructureItems/" + options[choice]
            selected_file = open(file_location, "r")
            close_file = selected_file
            selected_file = selected_file.readlines()
            stuff = []
            for things in selected_file:
                stuff.append(things)
            nums_and_lines = zip(range(len(stuff)), stuff)
            for x in nums_and_lines:
                print x
            print "\nEnd of File.\n"
            clean = raw_input("Press (1) to keep contents visible or 2 to clear the screen: ")
            if clean == "1":
                continue
            elif clean == "2":
                os.system("cls")
            else:
                continue
            close_file.close()

        elif choice == "4":
            os.system("cls")
            print "Configuration Line Editor"
            options = []
            for config_file in os.listdir("./InfrastructureItems"):
                if config_file.endswith(".txt"):
                    options.append(config_file)
            nums_and_files = zip(range(len(options)), options)
            for x in nums_and_files:
                print x
            print "\nAvailable lists to modify: \n"
            choice = raw_input("Please type desired number to edit or 'exit' to quit: ")
            if choice == "exit":
                os.system('cls')
                print "\n\nThanks for keeping your files up to date!"
            else:
                choice = int(choice)
            file_location = "./InfrastructureItems/" + options[choice]
            selected_file = open(file_location, "r")
            close_file = selected_file
            selected_file = selected_file.readlines()
            stuff = []
            for things in selected_file:
                stuff.append(things)
            nums_and_lines = zip(range(len(stuff)), stuff)
            for x in nums_and_lines:
                print x
            print "\nEnd of File.\n"
            close_file.close()

            delete_it = raw_input("Enter number of line to be removed: ")
            modify_file = open(file_location, "w")
            count = 0
            for line in selected_file:
                if str(count) != delete_it:
                    count += 1
                    modify_file.write(line)
                else:
                    count += 1
            clean = raw_input("Press (1) to keep contents visible or 2 to clear the screen: ")
            if clean == "1":
                continue
            elif clean == "2":
                os.system("cls")
            else:
                continue
            modify_file.close()

        elif choice == "8":
            os.system("cls")
            break
        else:
            continue


def network_tools():
    import os
    os.system("cls")
    while True:
        print "\n"
        print "Welcome to the Network Tools menu."
        print "\n"
        print "Press 1 to run the ping utility."
        print "Press 2 to run nslookup."
        print "Press 3 to run tracert."
        print "Press 4 to run pathping."
        print "Press 5 to Exit"
        print "\n"

        choice = raw_input("Please make a selection: ")

        if choice == "1":
            target = raw_input("Enter IP or hostname to ping: ")
            os.system("ping " + target)
            clean = raw_input("Press 1 to keep contents visible or 2 to clear the screen: ")
            if clean == "1":
                continue
            elif clean == "2":
                os.system("cls")
            else:
                continue

        elif choice == "2":
            os.system("nslookup")
            clean = raw_input("Press 1 to keep contents visible or 2 to clear the screen: ")
            if clean == "1":
                continue
            elif clean == "2":
                os.system("cls")
            else:
                continue

        elif choice == "3":
            target = raw_input("Enter IP or hostname to trace: ")
            os.system("tracert " + target)
            clean = raw_input("Press 1 to keep contents visible or 2 to clear the screen: ")
            if clean == "1":
                continue
            elif clean == "2":
                os.system("cls")

        elif choice == "4":
            target = raw_input("Enter IP or hostname to pathping: ")
            os.system("pathping " + target)
            clean = raw_input("Press 1 to keep contents visible or 2 to clear the screen: ")
            if clean == "1":
                continue
            elif clean == "2":
                os.system("cls")
            else:
                continue

        elif choice == "5":
            os.system("cls")
            break

        else:
            continue


def powershell_tools():
    import os
    import subprocess
    import Tkinter as Tk
    import tkFileDialog as fileDialog

    while True:
        os.system("cls")
        print "\n"
        print "Welcome to the PowerShell Tools menu."
        print "\n"
        print "Press 1 to run a Powershell CLI."
        print "Press 2 to start a New-PSSession with a remote machine."
        print "Press 3 to get MD5 hash of object."
        print "Press 4 to unlock an AD account."
        print "Press 5 to get Remote System Uptime"
        print "Press 6 to find local users on remote machine"
        print "Press 7 to flush DNS of remote machine"
        print "Press 8 to exit"
        print "\n"

        choice = raw_input("Enter your choice: ")

        if choice == "1":
            os.system("powershell -NoProfile")

        elif choice == "2":
            target = raw_input("Enter your target hostname: ")
            print "Creating target.ps1 file to establish connection"
            pstarget = open("pstarget.ps1", "w")
            pstarget.write("$target = New-Pssession " + target + "\n")
            pstarget.write("Enter-PSSession $target" + "\n")
            pstarget.close()
            print "File created. Initiating Connection to remote host..."
            os.system("powershell -noexit -ExecutionPolicy Unrestricted " +
                      "C:\Users\stewart.olson\Desktop\Stuff\Code\Python\HealthCheck\pstarget.ps1")

        elif choice == "3":
            raw_input("Press enter to select a file...")
            root = Tk.Tk()
            root.focus_force()
            hash_path = fileDialog.askopenfilename()
            hash_target = open("hashtarget.ps1", "w")
            root.destroy()
            hash_target.write('$target = "' + hash_path + '"\n')
            hash_target.write("Get-FileHash -Algorithm MD5 $target | fl" + "\n")
            hash_target.close()

            os.system("powershell -noexit -ExecutionPolicy Unrestricted " +
                      "C:\Users\stewart.olson\Desktop\Stuff\Code\Python\HealthCheck\hashtarget.ps1")

        elif choice == "4":
            username = raw_input("Unlock AD User (Input username): ")
            print "Creating target.ps1 file to unlock AD account"
            psunlock = open("unlocktarget.ps1", "w")
            psunlock.write("$unlock = Unlock-ADAccount " + username + "\n")
            psunlock.close()
            print "File created. Unlocking User Account."
            os.system("powershell -ExecutionPolicy Unrestricted " +
                      "C:\Users\stewart.olson\Desktop\Stuff\Code\Python\HealthCheck\unlocktarget.ps1")
            print "%s's account has been unlocked. Press enter to continue." % username
            raw_input("Press enter to continue...")
            os.system("cls")

        elif choice == "5":
            remote_target = raw_input("Which system do you want the uptime for?: ")
            psfunction = """
function Get-SystemUptime($RemoteSystem) {
    $Target = $RemoteSystem
    $operatingSystem = Get-WmiObject Win32_OperatingSystem -ComputerName $Target
    "$((Get-Date) - ([Management.ManagementDateTimeConverter]::ToDateTime($operatingSystem.LastBootUpTime)))"
}
"""
            psuptime = open("psuptime.ps1", "w")
            psuptime.write(psfunction)
            psuptime.write("Get-SystemUptime -RemoteSystem " + remote_target)
            psuptime.close()
            print "File Created, checking system"
            thing = subprocess.Popen("powershell -ExecutionPolicy Unrestricted -File " +
                                     "C:\Users\stewart.olson\Desktop\Stuff\Code\Python\HealthCheck\psuptime.ps1",
                                     shell=True, stdout=subprocess.PIPE).stdout.read()
            days = thing.split('.')
            hours = days[1].split(':')
            print "\nThe system %s has been up for %s days %s hours and %s minutes\n" % \
                  (remote_target, days[0], hours[0], hours[1])
            os.system('pause')

        elif choice == "6":
            remote_target = raw_input("For which system do you want to discover local users?: ")
            pslocalusers = """
Param
(
    [Parameter(Position=0,Mandatory=$false)]
    [ValidateNotNullorEmpty()]
    [Alias('cn')][String[]]$ComputerName=$Env:COMPUTERNAME,
    [Parameter(Position=1,Mandatory=$false)]
    [Alias('un')][String[]]$AccountName,
    [Parameter(Position=2,Mandatory=$false)]
    [Alias('cred')][System.Management.Automation.PsCredential]$Credential
)
    
$Obj = @()

Foreach($Computer in $ComputerName)
{
    If($Credential)
    {
        $AllLocalAccounts = Get-WmiObject -Class Win32_UserAccount -Namespace "root\cimv2" `
        -Filter "LocalAccount='$True'" -ComputerName $Computer -Credential $Credential -ErrorAction Stop
    }
    else
    {
        $AllLocalAccounts = Get-WmiObject -Class Win32_UserAccount -Namespace "root\cimv2" `
        -Filter "LocalAccount='$True'" -ComputerName $Computer -ErrorAction Stop
    }
    
    Foreach($LocalAccount in $AllLocalAccounts)
    {
        $Object = New-Object -TypeName PSObject
        
        $Object|Add-Member -MemberType NoteProperty -Name "Name" -Value $LocalAccount.Name
        $Object|Add-Member -MemberType NoteProperty -Name "Full Name" -Value $LocalAccount.FullName
        $Object|Add-Member -MemberType NoteProperty -Name "Caption" -Value $LocalAccount.Caption
          $Object|Add-Member -MemberType NoteProperty -Name "Disabled" -Value $LocalAccount.Disabled
          $Object|Add-Member -MemberType NoteProperty -Name "Status" -Value $LocalAccount.Status
          $Object|Add-Member -MemberType NoteProperty -Name "LockOut" -Value $LocalAccount.LockOut
        $Object|Add-Member -MemberType NoteProperty -Name "Password Changeable" -Value $LocalAccount.PasswordChangeable
        $Object|Add-Member -MemberType NoteProperty -Name "Password Expires" -Value $LocalAccount.PasswordExpires
        $Object|Add-Member -MemberType NoteProperty -Name "Password Required" -Value $LocalAccount.PasswordRequired
        $Object|Add-Member -MemberType NoteProperty -Name "SID" -Value $LocalAccount.SID
        $Object|Add-Member -MemberType NoteProperty -Name "SID Type" -Value $LocalAccount.SIDType
        $Object|Add-Member -MemberType NoteProperty -Name "Account Type" -Value $LocalAccount.AccountType
        $Object|Add-Member -MemberType NoteProperty -Name "Domain" -Value $LocalAccount.Domain
        $Object|Add-Member -MemberType NoteProperty -Name "Description" -Value $LocalAccount.Description
        
        $Obj+=$Object
    }
    
    If($AccountName)
    {
        Foreach($Account in $AccountName)
        {
            $Obj|Where-Object{$_.Name -like "$Account"}
        }
    }
    else
    {
        $Obj
    }
}
"""
            theoutput = subprocess.Popen("powershell -ExecutionPolicy Unrestricted -File " +
                                         "C:\Users\stewart.olson\Desktop\Stuff\Code\Python\HealthCheck\pslusr.ps1 " +
                                         remote_target, shell=True, stdout=subprocess.PIPE).stdout.readlines()
            for line in theoutput:
                if "Get-LocalAccount : The term 'Get-LocalAccount' is not recognized as the name of a cmdlet" not in line:
                    print line,
                else:
                    break
            os.system('pause')

        elif choice == "7":
            target = raw_input("Enter name of computer to clear cache on: ")
            print "Creating target.ps1 file to flush DNS"
            flushdns = open("flushdns.ps1", "w")
            flushdns.write("Invoke-Command -script {Clear-DnsClientCache } -ComputerName " + target)
            flushdns.close()
            os.system("powershell -ExecutionPolicy Unrestricted " +
                      "C:\Users\stewart.olson\Desktop\Stuff\Code\Python\HealthCheck\flushdns.ps1")
            print "\nSystem %s has had it's DNS Cache flushed.\n" % target
            raw_input("Press enter to continue...")
            os.system("cls")

        elif choice == "8":
            os.system("cls")
            break

        else:
            continue
