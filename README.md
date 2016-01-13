This utility is meant to be a powerful python and powershell system management, monitoring, configuration management, and diagnostic tool. It will include the following features:

1) Basic Health Check - Test accessibility, resolution, services, and more of all systems added.
2) Basic Network Tools - A convenient CLI/GUI for all of the best tools - dig, nslookup, ping, tracert, Test-Connection, etc.
3) Basic Active Directory Tools - Account lockout check and unlock, AD Event Searching (failed login attempts, replication status), more!
4) Powershell Tools - PS-Remoting to one or multiple machines, File Hash comparer, WSUS management tools, Windows Defender options
5) Service checker - Check all machines to verify proper services are started, remotely start/restart services
6) More! - Things like backup report scanners to alert of failures for different backup systems (3PAR Replication, CommVault reports, and more to come!)

GETTING STARTED

--Infrastrucutre Items Folder--
These files act as a summary of your internal infrastructure. Inside of each file include a list of resolvable hostnames or IP addresses

When scans run you can target systems like "Active Directory Infrastructure" (based on the filename and contents of the file). The health check would then scan all devices in that file and output information.

You can modify the file names, add new files, or change the names of the files at any time the utility is not running and there will be no issues. The idea behind this configuration is to allow for useful breakdowns of your environment. If you have 10 ESXi hosts and want to check them and the management interfaces you could create a 'virtualenvironment.txt' file with the 20 or so IP addresses. This file can the be used in other sectors of the program, such as the VMware API or iLO/iDRAC APIs.

Another file could be all email infrasture or application infrastructure items in your environment so you can verify connectivity/status of all of those devices. A third file could be the core routers at each site so you can quickly check connectivity of all sites. Make as many as make sense with your organization