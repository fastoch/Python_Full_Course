# For file detection, we need the os module 
# This module is already included with the standard python library. All we need to do is import it
import os

# we want to check if a file exists somewhere on our computer
path = "/home/fastoch/Documents/test.txt"
if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else: 
    print("That location does not exist")