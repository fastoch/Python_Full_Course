# tuple =   a collection which, unlike a list, is ordered and unchangeable
#           used to group together related data

student = ("fastoch",40,"male")

print(student.count("fastoch"))
print(student.index("male"))

for x in student:
    print(x)

if "fastoch" in student:
    print("fastoch is here!")