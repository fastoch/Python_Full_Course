# create a file and write some text into it
# !!!Be careful!!! if the file already exists, it will be overwritten
with open('/home/fastoch/Documents/test2.txt','w') as file:
    file.write("This file was written with Python\n")

# display our file content
with open('/home/fastoch/Documents/test2.txt') as file:
    print(file.read())

# create another file and append some text to it
with open('/home/fastoch/Documents/test3.txt','a') as file:
    file.write("This is another file\n")
with open('/home/fastoch/Documents/test3.txt','a') as file:
    file.write("This text has been appended to our file\n")

with open('/home/fastoch/Documents/test3.txt') as file:
    print(file.read())