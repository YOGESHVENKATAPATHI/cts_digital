class StockItem:
    def __init__(self, item_id, title, amount, cost):
        self.item_id = item_id
        self.title = title
        self.amount = amount
        self.cost = cost

    def show_item(self):
        print(f"ID: {self.item_id} | Name: {self.title} | Qty: {self.amount} | Price: ${self.cost}")

stock_db = {}

# Simulated execution sequence without blocking inputs
print("\\n--- Adding Items ---")
stock_db[101] = StockItem(101, "Wireless Mouse", 50, 25.99)
stock_db[102] = StockItem(102, "Mechanical Keyboard", 30, 89.50)

print("\\n--- Updating Item 101 ---")
if 101 in stock_db:
    stock_db[101].amount = 120

print("\\n--- Current Inventory ---")
for product in stock_db.values():
    product.show_item()

print("\\n--- Deleting Item 102 ---")
stock_db.pop(102, None)

print("\\n--- Final Inventory ---")
for product in stock_db.values():
    product.show_item()