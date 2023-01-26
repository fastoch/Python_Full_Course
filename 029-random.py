import random

# generate a pseudo-random integer between 1 and 6
x = random.randint(1,6)
print(x)  

# generate a pseudo-random floating point number between 0 and 1
y = random.random()
print(y)

# random choice from a list
myList = ['rock','paper','scissors']
z = random.choice(myList)
print(z)

# to shuffle a deck of cards
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)
print(cards)

