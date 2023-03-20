num_items = -1
total_price = 0
while num_items < 0:
    try:
        num_items = int(input("Number of items: "))
        if num_items < 0:
            print("Invalid number of items!")
    except ValueError:
        print("Invalid input, please enter a positive integer.")

for i in range(num_items):
    while True:
        try:
            item_price = float(input("Price of item: $"))
            break
        except ValueError:
            print("Invalid input, please enter a number.")
    total_price += item_price

if total_price > 100:
    discount = total_price * 0.1
    total_price -= discount

print(f"Total price for {num_items} items is ${total_price:.2f}")