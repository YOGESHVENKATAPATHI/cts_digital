inventory = {
    "Milk": 5,
    "Laptop": 20,
    "Bread": 3
}

low_stock = {k for k, v in inventory.items() if v < 10}
print(low_stock)
