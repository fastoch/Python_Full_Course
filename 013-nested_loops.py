# nested loops =    The "inner loop" will finish all of its iterations before 
#                   finishing one iteration of the "outer loop".

# this program will draw a rectangle made of a specified symbol
rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") # end="" prevents the line break inherent to the print function
    print() # new line
# each iteration of the inner loop draws a line made of as many symbols as the number of columns
# each iteration of the outer loop simply moves the cursor to the beginning of the next line

