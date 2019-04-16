#Program to get system command output.

import subprocess

result = subprocess.check_output("dir", shell=True, universal_newlines=True)
print("To list file and directory command is 'dir' ")
print("  ")
print(result)

