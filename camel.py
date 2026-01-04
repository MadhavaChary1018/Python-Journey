name = input("camel case variable name: ")
print("snake case: ",end="")

for i in name:
    if i.islower():
        print(i,end="")
    else:
        print("_",i.lower(),sep="",end="")
print()