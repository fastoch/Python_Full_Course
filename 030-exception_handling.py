# exception = event detected during execution that interrupts the normal flow of a program
# when a code is considered dangerous (user input), we surround it within a try block
# this way, we try the code and, if an exception occurs, we can catch it and handle it

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
    print(result)
# if denominator == 0, this will cause an exception called "ZeroDivisionError"
# ZeroDivisionError is a built-in exception
# we can replace this built-in exception handling with our own 
except ZeroDivisionError:
    print("You can't divide by zero, you moron!")
except Exception:
    print("Something went wrong :(")