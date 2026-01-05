def main():
    text = input("enter a string: ")
    for i in text:
        if is_vowel(i):
            print(end="")
    
        else:
            print(i,end="")
    print()

def is_vowel(c):
    if c in "AEIOUaeiou":
        return 1
    else:
        return 0

main()