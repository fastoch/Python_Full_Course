# Loop control statements = change a loop's execution from its normal sequence

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop
# pass =        does nothing, acts as a placeholder

# this program keeps asking for your name until you enter something
while True:
    name = input("What's your name? ")
    if name != "":
        break

phone_number = "123-456-7890"
# let's display this phone number without the dashes
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

print() # line break

# display integers from 1 to 20, except for 13
for i in range(1,21):
    if i == 13:
        pass
    else: 
        print(i)