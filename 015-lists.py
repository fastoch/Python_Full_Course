# list = used to store multiple items in a single variable

food = ["pizza","hamburger","prosciutto","spaghetti"]

print("Here is my food list: "+str(food))
print("food is a variable which type is: "+str(type(food)))
print("This food list contains "+str(len(food))+" items.")
print("The first item in the list is: "+food[0])
print("The second item in this list is: "+food[1])

food[0] = "sushi"
print("I replaced the first item by: "+food[0])

print("Here are the items of my new list:")
for x in food:
    print(x)

# add an item to the list
food.append("paëlla")
print(food)

food.remove("hamburger")
print(food)

# remove the last element
food.pop()
print(food)

# insert an item at a given index
food.insert(1,"shrimps")
print(food)

# sort list items alphabetically
food.sort()
print(food)

# clear list
food.clear()
print(food)
