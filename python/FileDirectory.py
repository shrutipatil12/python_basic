#Program to list all files in a directory in Python.



import glob, os

os.chdir("/home/bridgeit")
print("txt files are as follow =")
for file in glob.glob("*.txt"):
    print(file)
    print("   ")
    print("All other files are as follow =")
for file in glob.glob("*.*"):
    print(file)