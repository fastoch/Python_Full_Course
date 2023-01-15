# variable = a container for a value.

# string
first_name = "Fabrice"
last_name = "Pustoc'h"
full_name = first_name + " " + last_name
print(type(full_name))
print("Hello! My name is " + full_name)

# integer
age = 41
print(type(age))
print("I'm " + full_name + " and I'm " + str(age) + " years old.")

# float
weight = 66.6
print(type(weight))
print("I weigh "+str(weight)+" kilograms.")

# boolean
human = True
print(type(human))
if(human==True):
  print("I'm a human being.")
else:
  print("I'm an AI.")

