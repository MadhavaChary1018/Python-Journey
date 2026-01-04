def main():
    print("amount due: 50")
    due()

def due():
    due = 50
    while True:
        c = coin()
        due = due-c
        if due > 0:
            print("amount due:",due)
        else:
            break
    print("change owed:",-due)
            
def coin():
    c = int(input("insert a coin: "))
    if c==5 or c==10 or c==25 :
        return c
    else:
        return 0

main()