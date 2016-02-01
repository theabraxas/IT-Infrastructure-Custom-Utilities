# List of possible ping errors and responses
import os
exception1 = "TTL expired in transit."
exception2 = "Destination net unreachable."
exception3 = "Request timed out."
exception4 = "Ping request could not find"
exception5 = "Usage:"
response1 = "\033[1;31m%s is unreachable, TTL expired in transit.\033[1;m"
response2 = "\033[1;31m%s is unreachable.\033[1;m"
response3 = "\033[1;31m%s timed out.\033[1;m"
response4 = "\033[1;31m%s could not be found.\033[1;m"
response5 = "\033[1;31m This entry is a blank line or space, please edit config file to fix.\033[1;m"
response6 = "\033[1;32m%s is online.\033[1;m"
systemname = "\n\033[1;37mTesting %s...\033[1;m\n"
cls = os.system('cls')