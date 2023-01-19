# while loop =  a statement that will execute its block of code as long as its condition remains true

# the user will prompted until he enters a name
name = ""
while len(name) == 0:
  name = input("Enter your name: ")
print("Nice to meet you "+name+"!")