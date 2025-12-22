expression = input("enter a math expression ")

x,y,z = expression.split(" ")
x=int(x)
z=int(z)

if y=="+":
    print(f"{x+z:.1f}")
elif y=="-":
    print(f"{x-z:.1f}")
elif y=="*":
    print(f"{x*z:.1f}")
elif y=="/":
    print(f"{x/z:.1f}")
else:
    print("Invalid")