# return statement = use within functions to send values|objects back to the caller.
#                    These values|objects are known as the function's return value.

def multiply(a,b):
    return a*b

while True:
    a = input("Enter a number:")
    b = input("Enter a second number:")

    x = multiply(int(a),int(b))
    print(a+" x "+b+ " = "+str(x)+"\n")

    exit = input("Do you want to make another multiplication (y for yes, n for no)? ")
    if exit == "n":
        break
    elif exit == "y":
        continue
    else: 
        input("Do you want to make another multiplication (y for yes, n for no)? ")

