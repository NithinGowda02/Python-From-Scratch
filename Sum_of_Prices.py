"""
**Sum of Prices**:
   - Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a `for` loop.
"""
products = {
    "Rice": 50,
    "Soap": 35,
    "Tea Powder": 65,
    "Milk": 50,
    "Curd": 26
}
Total_price = 0
for key,value in products.items():
    Total_price+=value
print(f"Total Price of all Items >> {Total_price}")
