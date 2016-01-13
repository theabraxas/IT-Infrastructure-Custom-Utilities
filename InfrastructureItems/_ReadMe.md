These files act as a summary of your internal infrastructure. Inside of each file include a list of resolvable hostnames or IP addresses

When scans run you can target systems like "Active Directory Infrastructure" (based on the filename and contents of the file). The health check would then scan all devices in that file and output information.

You can modify the file names, add new files, or change the names of the files at any time the utility is not running and there will be no issues. The idea behind this configuration is to allow for useful breakdowns of your environment. If you have 10 ESXi hosts and want to check them and the management interfaces you could create a 'virtualenvironment.txt' file with the 20 or so IP addresses. This file can the be used in other sectors of the program, such as the VMware API or iLO/iDRAC APIs.

Another file could be all email infrasture or application infrastructure items in your environment so you can verify connectivity/status of all of those devices. A third file could be the core routers at each site so you can quickly check connectivity of all sites. Make as many as make sense with your organization