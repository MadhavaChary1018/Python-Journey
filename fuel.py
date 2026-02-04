def main():
    f = fraction()
    fuel(f)

def fraction():
    while True:
        try:
            x,y = input("enter fuel fraction: ").split(sep="/")
            x = int(x)
            y = int(y)
            if y>=x>=0 and y!=0 :
                return float(x/y)
        except ValueError:
            pass

def fuel(v):
    x = v*100
    if x<=1:
        print("E")
    elif x>=99:
        print("F")
    else:
        print(round(x),"%",sep="")

main()