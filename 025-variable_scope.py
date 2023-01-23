# scope = The region that a variable is recognized # scope = the region that a variable is recognized 
#         A variable is only available from inside the region it is created
#         A global and locally scoped versions of a variable can be created

name = "fastoch" # global scope (available inside & outside of any functions)

def display_name():
    name = "Code" # local scope (available only inside this function)
    print(name)

# will print "fastoch"
print(name)

# will print "Code" 
display_name()

# a program will first try to use the local version of a variable
# if no local version is found, it will look for a global version
# This is known as the "LEGB" rule = Local Enclosing Global Built-in
