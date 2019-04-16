#Program to get file creation and modification date/times.

import os.path, time

print("File Creation  %s"  % time.ctime(os.path.getctime('shruti.txt')))
print("Last Modified  %s " % time.ctime(os.path.getmtime('shruti.txt')))
