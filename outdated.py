def main():
    while True:
        d = input("Enter a Date: ")
        if format_1(d):
            break
        if format_2(d):
            break

def format_1(s):
    months = [
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"
    ]
    try:
        m,d,y = s.split(sep=" ")
        if not "," in d:
            return False
        m = m.title()
        d = int(d.rstrip(","))
        y = int(y)
        if m in months and 1<=d<=31 and y>=1:
            m = months.index(m)+1
            print(y,f"{m:02}",f"{d:02}",sep="-")
            return True
    except ValueError:
        return False
    
def format_2(s):
    try:
        m,d,y = s.split(sep="/")
        m,d,y = int(m),int(d),int(y)
        if 1<=m<=12 and 1<=d<=31 and y>=1:
            print(y,f"{m:02}",f"{d:02}",sep="-")
            return True 
    except ValueError:
        return False

main()