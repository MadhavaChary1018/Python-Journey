price = {
    "Baja Taco":4.25,
    "Burrito":7.50,
    "Bowl":8.50,
    "Nachos":11.00,
    "Quesadilla":8.50,
    "Super Burrito":8.50,
    "Super Quesadilla":9.50,
    "Taco":3.00,
    "Tortilla Salad":8.00
}

total = 0
while True:
    try:
        i = input("Item: ").title()
        if i in price:
            total = total + price[i]
            print(f"Total: ${total:.2f}")
        
    except EOFError:
        print("Thank you for ordering!")
        break
