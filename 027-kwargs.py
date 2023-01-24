# **kwargs = parameter that will pack all arguments into a dictionary
#          useful so that a function can accept a varying amount of keyword arguments

# reminder: args will accept a varying amount of positional arguments and pack them into a tuple

def hello(first,last):
    print("Hello "+first+" "+last)

hello(first="Fabrice",last="Pustoc'h")

# What if I want to add a middle name?
def hello(**kwargs):
    print("Hello "+kwargs['first']+", "+kwargs['middle']+", "+kwargs['last'])

hello(first="Fabrice",middle="aka fastoch",last="Pustoc'h")

# How to add more arguments?
def hello(**kwargs):
    print("Hello",end=" ") # replace the new line character with a space
    for key,value in kwargs.items():
        print(value,end=" ")
    print()

hello(first="Fabrice",second="fastoch",third="fast&curious",last="Pustoc'h")

# as with *args, we could use any other word instead of kwargs
# we could use **names, for example
def hello(**names):
    print("Hello",end=" ") # replace the new line character with a space
    for key,value in names.items():
        print(value,end=" ")
    print()

hello(first="Fabrice",second="fastoch",third="fast&curious",last="Pustoc'h")