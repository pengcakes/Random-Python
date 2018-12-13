# !/usr/bin/python

import os, sys

# listing directories
print("The dir is: %s"%os.listdir(os.getcwd()))

# renaming directory ''tutorialsdir"
#os.rename("Iron Man [1080p]","Iron Man")
os.rename("CC","Iron Man")

print("Successfully renamed.")

# listing directories after renaming "tutorialsdir"
print("the dir is: %s" %os.listdir(os.getcwd()))