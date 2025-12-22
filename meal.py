def main():
    time = input("what is time now? ")
    
    if 7<= convert(time) <= 8:
        print("Breakfast time")
    elif 12<= convert(time) <=13:
        print("Lunch time")
    elif 18<= convert(time) <=19:
        print("Dinner time")
    
def convert(time):
    x,y = time.split(":")
    y,z = y.split(" ")
    x = int(x)
    y = int(y)/60
    if z=="am" and 1<=x<=11:
        return x+y
    elif z=="am" and x==12:
        return y
    elif z=="pm" and 1<=x<=11:
        return x+12+y
    elif z=="pm" and x==12:
        return x+y

main()