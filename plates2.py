def main():
    p = input("vanity plate: ")
    if is_valid(p):
        print("valid")
    else:
        print("invalid")

def is_valid(s):
    if not 2<=len(s)<=6 :
        return False
    if not s.isalnum():
        return False
    if not s[0:2].isalpha():
        return False
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i]=="0":
                return False
            elif not s[i:].isdigit():
                return False
            break
    return True

main()