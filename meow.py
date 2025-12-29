def main():

    while True:
        n = int(input("what's n? "))
        if n>0:
            break

    meow(n)


def meow(x):
    print("meow\n"*x,end="")
    
main()