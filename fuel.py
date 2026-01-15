def main():
    f = fraction()
    fuel(f)

def fraction():
    while True:
        f = input("enter fuel fraction: ")
        x,y = f.split(sep="/")
        if x.isdigit() and y.isdigit() and int(y)>=int(x)>=0 and int(y)!=0 :
            break
    f = float(x)/float(y)
    return f

def fuel(v):
    x = v*100
    if x<=1:
        print("E")
    elif x>=99:
        print("F")
    else:
        print(round(x),"%",sep="")

main()