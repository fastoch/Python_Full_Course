# logical operators (and,or,not)

temp = int(input("What's the temperature outside? "))
wind = input("Is there much wind today? (answer by yes or no) ")

if temp>=10 and temp<=30:
  print("The weather is pretty nice today! You should go outside!")
elif temp<10 or temp>30:
  print("The weather is not great today! You should stay inside.")

if not(wind=="yes"):
  print("You won't be able to do windsurfing today.")
else: 
  print("It's a nice day for windsurfing!")