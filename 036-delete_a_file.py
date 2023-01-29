import os

# to delete a file
path = '/home/fastoch/Documents/test2.txt'

try:
    os.remove(path)
except FileNotFoundError:
    print("This file does not exist")
except PermissionError:
    print("You do not have permission to delete that!")

# to delete an empty folder
path2 = '/home/fastoch/Git/Python_Full_Course/empty_folder'

try:
    os.rmdir(path2)
except FileNotFoundError:
    print("This folder does not exist")
except OSError:
    print("You cannot delete a folder wich contains files using that function")
except PermissionError:
    print("You do not have permission to delete that!")
else:
    print(path2+" was deleted")

# to delete a folder which contains files
path3 = '/home/fastoch/Git/Python_Full_Course/not_empty_folder'

try:
    os.rmdir(path3)
except FileNotFoundError:
    print("This folder does not exist")
except PermissionError:
    print("You do not have permission to delete that!")
else:
    print(path3+" was deleted")