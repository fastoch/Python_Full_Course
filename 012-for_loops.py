# for loop =  a statement that will execute its block of code a limited amount of times
# while loop = unlimited

# will print integers from 1 to 10
for i in range(10):
    print(i+1)

print("") # prints an empty line

# will print integers from 50 to 59
for i in range(50,60):
    print(i)

print("")

# will print all even integers from 30 to 50
for i in range(30,51,2):
    print(i)

print("")

# each letter within my alias will be printed to a new line
for i in "fastoch":
    print(i)

print("")

import time
# countdown + Happy New Year! 
# requires to import time module so that we can wait 1 sec between each iteration of the for loop
for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("Happy New Year!") 
