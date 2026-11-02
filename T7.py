##Question 7:
# (a)
import json
products = [
    {"name": "Laptop", "price": 1200.0, "category": "Electronics", "quantity": 10},
    {"name": "Phone", "price": 800.0, "category": "Electronics", "quantity": 4},
    {"name": "Charger", "price": 25.0, "category": "Electronics", "quantity": 15},
    {"name": "Desk Chair", "price": 150.0, "category": "Furniture", "quantity": 3},
    {"name": "Notebook", "price": 5.0, "category": "Stationery", "quantity": 0},
    {"name": "Backpack", "price": 45.0, "category": "Accessories", "quantity": 8}
]

# (b)
def low_stock(products, threshold=5):
    for i in products:
        if i["quantity"] < threshold:
            yield i


# (c)
def expensive_items(products, min_price=1000):
    for p in products:
        if p["price"] > min_price:
            yield p

#(d)
category = input("Enter category: ")
upper_names = [p["name"].upper() for p in products if p["category"] == category]
print(upper_names)

#(e)
updated_products = list(map(lambda p: {
    "name": p["name"],
    "price": p["price"] * 1.10,
    "category": p["category"],
    "quantity": p["quantity"]
}, products))


for p in updated_products:
    print(p)

#(f)
s = list(filter(lambda p: p["quantity"] > 0, updated_products))

print("\nIn Stock Products:")
for p in s:
    print(p)


#(h)
with open("inventory.json", "w") as f:
    json.dump(updated_products, f, indent=4)

# Read JSON
with open("inventory.json", "r") as f:
    data = f.read()
    print("\nInventory File:")
    print(data)
    print("Total Characters:", len(data))