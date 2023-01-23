# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

def add(num1,num2):
    sum = num1 + num2
    return sum

print(add(1,2))
# print(add(1,2,3)) will return an error, because add() takes 2 positional arguments, not 3

# What if I wanna add a third argument, or a fourth?
def add2(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add2(1,2,3))
print(add2(1,2,3,4,5))

# args is an arbitrary name (a common convention), we could use any other word
def add3(*stuff):
    sum = 0
    for i in stuff:
        sum += i
    return sum
print(add3(1,2,3))
print(add3(1,2,3,4,5))