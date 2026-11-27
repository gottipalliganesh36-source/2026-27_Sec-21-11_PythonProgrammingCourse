def shopping_cart(**products):
    total = 0
    print("Items Purchased:")
    for item, price in products.items():
        print(f"{item}: ₹{price}")
        total = total + price
    print(f"Total: ₹{total}")

# multiple keyword arguments
shopping_cart(apple=15, orange=12, mango=10)