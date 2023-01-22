# keyword arguments = arguments preceded by an identifier when we pass them to a function.
#                     The order of the arguments doesn't matter, unlike positional arguments.
#                     Python knows the name of the arguments that our function receives.

def hello(first,middle,last):
    print("Hello "+first+", "+middle+" et "+last+"!")

# For the 2 examples below, the order does matter
print("With positional arguments:")
hello("Sandro","Aurélie","Fabrice")
hello("Aurélie","Fabrice","Sandro")

# With keyword arguments, we set the order by specifying a unique id for each argument
print("\nWith keyword arguments:")
hello(middle="Aurélie",last="Fabrice",first="Sandro")
# The line above will print out "Hello Sandro, Aurélie et Fabrice!"
