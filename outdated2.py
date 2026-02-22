months = [
    "January","February","March","April",
    "May","June","July","August",
    "September","October","November","December"
]
while True:
    date = input("Date: ").strip().title()
    if "," in date:
        try:
            m,d,y = date.split(sep=" ")
            d = int(d.removesuffix(","))
            y = int(y)
            if m in months and 1<=d<=31 and y>0 :
                m = months.index(m)+1
                print(f"{y}-{m:02}-{d:02}")
                break
        except ValueError:
            pass
    
    elif "/" in date:
        try:
            m,d,y = date.split(sep="/")
            m,d,y = int(m),int(d),int(y)
            if 1<=m<=12 and 1<=d<=31 and y>0 :
               print(f"{y}-{m:02}-{d:02}")
               break
        except ValueError:
            pass
