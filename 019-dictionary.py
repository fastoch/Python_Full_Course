# dictionary =  a changeable, unordered collection of unique key:value pairs.
#               This data type is quickly accessible because it uses hashing.

capitals = {'USA':'Washington',
            'India':'New Dehli',
            'China':'Beijing',
            'France':'Paris',
            'Russia':'Moscow'}

# add an entry to the dictionary or update an existing one
capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Los Angeles'})

print(capitals['Russia']) # returns 'Moscow'
# print(capitals['Germany']) --> returns a KeyError and stops the program

# to avoid errors when keys do not exist, use the get() method
print(capitals.get('France')) # returns 'Paris'
print(capitals.get('Germany')) # returns 'None'

# to check for existing keys in a dictionary
print(capitals.keys())

# to print only the values
print(capitals.values())

# print both keys and values
print(capitals.items())

# another way to print both keys and values
for key,value in capitals.items():
    print(key,value)

