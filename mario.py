def main():
    h = height()
    w = width()
    print_blocks(h,w)

def height():
    while True:
        h = int(input("what's the height? "))
        if h>0:
            break
    return h

def width():
    while True:
        w = int(input("what's the width? "))
        if w>0:
            break
    return w

def print_blocks(x,y):
    for _ in range(x):
        for _ in range(y):
            print("#",end=" ")
        print()

main()