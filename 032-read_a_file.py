# open a file, read its content and print it
try:
    with open('/home/fastoch/Documents/test.txt') as file:
        print(file.read())

    # check that my file has been closed
    if file.closed: 
        print("Your file has been closed.") 

except FileNotFoundError:
    print("That file was not found :(")
