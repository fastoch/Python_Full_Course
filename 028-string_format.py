# str.format() = optional method that gives users more control when displaying output

animal="cow"
item="moon"

print("Without the format method:")
print("The "+animal+" jumped over the "+item)
print()

# There's a more elegant way of writing the above line of code,
# and that is by using the format method available to strings
print("With format fields:")
print("The {} jumped over the {}.".format(animal,item))
print()

# {} is a format field, it's a placeholder for a value or a variable
# we can use the index of the values|variables to modify their order
print("With format fields + positional arguments:")
print("The {1} jumped over the {0}.".format(animal,item)) # output = The moon jumped over the cow.
# we can also select the same value twice
print("The {1} jumped over the {1}.".format(animal,item))
print()

# another way of writing this 
print("With format fields + keyword arguments:")
print("The {animal} jumped over the {item}.".format(animal="cow",item="moon"))
print("The {item} jumped over the {animal}.".format(animal="cow",item="moon"))
print("The {animal} jumped over the {animal}.".format(animal="cow",item="moon"))
print()
# we no longer need to declare our two variables at the beginning

# How to add some padding to a string
text = "The {} jumped over the {}."
print(text.format(animal,item))

# How to add some padding to a string
name = "fastoch"
print("Without padding:\n Hello, my name is {}. Nice to meet you!".format(name))
print("With padding + left aligned:\n Hello, my name is {:16}. Nice to meet you!".format(name))
print("With padding + right aligned:\n Hello, my name is {:>16}. Nice to meet you!".format(name))
print("With padding + centered:\n Hello, my name is {:^16}. Nice to meet you!".format(name))
# we still can add a positional|keyword argument to the format field by preceeding the colon with our argument

# How to format numbers?
number = 3.14159
print("The number pi, rounded to the thousandth, is {:.3f}".format(number)) # f is for floating point number (float type)
num = 1000
print("The number 1000 with a comma: {:,}".format(num)) 
print("The number 1000 in binary is {:b}".format(num)) 
print("The number 1000 in octal is {:o}".format(num)) 
print("The number 1000 in hexadecimal is {:X}".format(num)) 
print("The number 1000 in scientific notation is {:E}".format(num)) 
