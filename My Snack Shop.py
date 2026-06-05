Snacks = "Chips"
quantity = 40
Avalable = True
print(f"Snack {Snacks}")
print(f"Price {price}")
print(f"Quantity {quantity}")
print(f"Avalable {Avalable}")
print(type(Snacks))
print(type(price))
print(type(quantity))
print(type(Avalable))


#YAYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY

snack_shop = {
    "chip": 20,
    "chocolate": 5,
    "ice cream": 30
}
snack = input("Enter your snack name [Options: Chips, Chocolate, Ice Cream]: ").lower()
budget = int(input("Enter your budget: "))
if snack in snack_shop:
    print("Price", snack_shop[snack])
    price = snack_shop[snack]
    if price <= budget:
        print("you can buy this snack")
    else:
        print("You need", price-budget, "more tk")
else:
    print("Snack not available")