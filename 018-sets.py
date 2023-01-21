# set = a collection which is unordered, unindexed, and contains no duplicate values.

utensils = {"fork","knife","spoon","plate"}
dishes = {"bowl","plate","cup"}

for x in utensils:
    print(x)

# add an item to the set
utensils.add("napkin")
print(utensils)

# remove an item from the list
utensils.remove("knife")
print(utensils)

# utensils.clear()
# print(utensils)

# add our dishes set to our utensils set
utensils.update(dishes)
print(utensils)
print(dishes)

# create a new set that merges two sets
dinner_table = utensils.union(dishes)
print(dinner_table)

# show what a set contains that the other does not
print(utensils.difference(dishes))

# show what two sets have in common
print(utensils.intersection(dishes))
