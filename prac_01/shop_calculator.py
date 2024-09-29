total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid Number")
    number_of_items = int(input("Number of items: "))
for i in range (number_of_items):
    price = int(input("Price of item: "))
    total += price
print()
print(f"Total price for {number_of_items} items is $ {total}")