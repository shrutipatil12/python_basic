#Program to find files and skip directories of a given directory.


import glob, os

os.chdir("/home/bridgeit")
print("txt files are as follow =")
for file in glob.glob("*.*"):
    print(file)