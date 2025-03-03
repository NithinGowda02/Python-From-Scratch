""" 
**Basic Dictionary Operations**:
   - Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.
   - Add a new city and its dish to the dictionary.
   - Update the dish for Bengaluru.
   - Remove one city from the dictionary.
   - Use the `keys()` method to print all city names in the dictionary.
   - Use the `values()` method to print all dishes in the dictionary.
"""

karnataka_food = {
    "Bengaluru": "Bisi Bele Bath",
    "Mysuru": "Mysore Pak",
    "Mangaluru": "Neer Dosa",
    "Coorg" : "Akki Rotti",
    "Mandya" : "Ragi Mudde"
}
karnataka_food["Davanagere"] = "Benne Dosa"
print(f"After adding new City to the dictionary \n{karnataka_food}")
karnataka_food["Bengaluru"] = "Idli"
print(f"After Updating the food of Bangalore >> \n{karnataka_food}")
karnataka_food.pop("Mandya")
print(f"After Removing one city from the dictionary is >> \n{karnataka_food}")
print(f"All the city names in Dictionary is >> \n{karnataka_food.keys()}")
print(f"All the Food names in Dictionary is >> \n{karnataka_food.values()}")