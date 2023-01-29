import os

source = "/home/fastoch/Documents/test2.txt"
destination = "/home/fastoch/Desktop/moved_test2.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print("'"+source+"' was not found")

# This program can also be used to move folders