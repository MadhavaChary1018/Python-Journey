def main():
    p = input("Vanity Plate: ")
    if is_valid(p):
        print("valid")
    else:
        print("invalid")

# function which checks all the constraints
def is_valid(s):
    if 2<=len(s)<=6 and num_letter(s) and s[0:2].isalpha() and digit(s):
        return 1
    else:
        return 0

# function to check whether the string is only of alphabets and numbers    
def num_letter(s):
    for i in s:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            continue
        else:
            break
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        return 1
    else:
        return 0

# function to check the digits block
def digit(s):
    for i in s:
        if i in "0123456789":
            break
        else:
            continue
    if i=="0":
        return 0
    elif i in "123456789":
        x,y = s.split(i,maxsplit=1)
        y = (i+y).isdecimal()
        return y
    else:
        return 1

main()