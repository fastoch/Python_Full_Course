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
source2 = "Python_Full_Course/empty_folder"
destination2 = "/home/fastoch/Desktop/empty_folder"

try:
    if os.path.exists(destination2):
        print("There is already a file there")
    else:
        os.replace(source2,destination2)
        print(source2+" was moved")
except FileNotFoundError:
    print("'"+source2+"' was not found")