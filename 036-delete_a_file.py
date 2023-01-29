import os
import shutil # we need this module to delete a folder that contains files

# delete a file
path = '/home/fastoch/Documents/test2.txt'

try:
    os.remove(path)
except FileNotFoundError:
    print("This file does not exist")
except PermissionError:
    print("You do not have permission to delete that!")

# delete an empty folder
path2 = '/home/fastoch/Git/Python_Full_Course/empty_folder'

try:
    os.rmdir(path2)
except FileNotFoundError:
    print("This folder does not exist")
except OSError:
    print("You cannot delete a folder that contains files using that function")
except PermissionError:
    print("You do not have permission to delete that!")
else:
    print(path2+" was deleted")

# delete a folder containing files
path3 = '/home/fastoch/Git/Python_Full_Course/not_empty_folder'

try:
    shutil.rmtree(path3)
except FileNotFoundError:
    print("This folder does not exist")
except PermissionError:
    print("You do not have permission to delete that!")
else:
    print(path3+" was deleted")