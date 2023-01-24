# str.format() = optional method that gives users more control when displaying output

animal="cow"
item="moon"

print("The usual way:")
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

# another way of doing this
text = "The {} jumped over the {}."
print()