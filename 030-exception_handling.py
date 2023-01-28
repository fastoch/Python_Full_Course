# exception = event detected during execution that interrupts the normal flow of a program
# when a code is considered dangerous (user input), we surround it within a try block
# this way, we try the code and, if an exception occurs, we can catch it and handle it

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
# if denominator == 0, this will cause an exception called "ZeroDivisionError"
# ZeroDivisionError is a built-in exception
# we can customize the handling of this built-in exception 
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero, you moron!")
except ValueError as e:
    print(e)
    print("Enter only numbers, please.")
# It's considered good practice to first catch specific exceptions, and let the user know exactly what went wrong.

except Exception as e: # just in case there are exceptions we didn't anticipate
    print(e)
    print("Something went wrong :(")

# in case we don't catch any exception, we execute what's in the else block
else: 
    print("Congratulations! We didn't catch any exception.")
    print("The result is: " + str(result))

# whether or not we catch an exception, we will always execute what's in the finally block
finally:
    print("Whether we catch an exception or not, this will always execute.")
