# slicing = create a substring by extracting elements from another string
# we can either use the indexing[] operator or the slice() function

# using the indexing[] operator
# 3 optional arguments: [start:stop:step]

name = "Fabrice Pustoc'h"

first_letter = name[0]
first_name = name[:7] # equivalent to [0:7]
last_name = name[8:] # equivalent to [8:16]
even = name[::2] # FbiePso'
odd = name[1::2] # arc utch
reversed = name[::-1]

print(first_letter)
print(first_name)
print(last_name)
print(even)
print(odd)
print(reversed)

# using the slice() function to extract "youtube" out of the URL
website = "https://www.youtube.com"
slice = slice(12,-4) # creating a slice object
print(website[slice]) # will print out "youtube"
