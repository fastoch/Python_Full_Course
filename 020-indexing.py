# the index operator is represented by a set of square brackets [] 
# it gives access to a sequence's element (str,list,tuples)

name = "fastoch"

if(name[0].islower()):
    print("The first letter of your name is lower case")
else:
    print("The first letter of your name is upper case")

name = name.capitalize()
print(name)

substring = name[0:4]
print(substring)

substring = name[:4].upper()
print(substring)

nickname = name[:4]+"&Curious!"
print(nickname)

last_char = nickname[-1]
print(last_char)
