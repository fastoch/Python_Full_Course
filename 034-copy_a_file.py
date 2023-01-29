# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copy metadata (file's creation and modification times)

import shutil # The shutil module helps in automating the process of copying and removal of files and directories

shutil.copyfile('/home/fastoch/Documents/test.txt','/home/fastoch/Downloads/copy.txt') # 2 args: (source,destination)
