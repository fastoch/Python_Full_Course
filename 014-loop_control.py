# Loop control statements = change a loop's execution from its normal sequence

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop
# pass =        does nothing, acts as a placeholder

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

