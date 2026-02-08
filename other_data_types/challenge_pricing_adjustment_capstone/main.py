#1 Create the Dictionary Define grocery_inventory with the following items and details:
grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}
#2 Check and Update Price 
egg_price = grocery_inventory.get ("Eggs")[1] 
if egg_price > 5.00:
    print("Eggs are too expensive, reducing the price by $1.") 
    grocery_inventory["Eggs"] = (
        grocery_inventory.get ("Eggs")[0], 
        egg_price-1, 
        grocery_inventory.get ("Eggs")[2]
    ) 
else:
    print("The price of Eggs is reasonable.")

#3 Add a New Item
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes: ", grocery_inventory)

#4 Manage Stock
milk_stock = grocery_inventory.get("Milk")[2]
if milk_stock < 10:
    print ("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (
        grocery_inventory.get ("Milk")[0],
        grocery_inventory.get ("Milk")[1],
        milk_stock+20
    )
else:
    print ("Milk has sufficient stock.")

#5 Remove Item Based on Price
apple_price = grocery_inventory.get ("Apples")[1]
if apple_price > 2.00:
    grocery_inventory.pop ("Apples")
    print ("Apples removed from inventory due to high price.")

#6 Final Print
print ("Updated inventory: ",grocery_inventory)

