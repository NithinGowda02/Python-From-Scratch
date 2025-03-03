"""
 **Set Operations**:
   - Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
   - Find the union, intersection, and difference between the two sets.
   - Add a new fruit to your set.
   - Remove a fruit from your set using both `remove()` and `discard()`. What happens when the fruit doesn’t exist?
"""
Favourate_fruit = {"Pineapple","Banana","Orange","Apple"}
Freind_Favourate_Fruit = {"Orange","Grapes","Watermelon","Apple"}

print(f"Union of two sets {Favourate_fruit | Freind_Favourate_Fruit}")
print(f"Union of two sets {Favourate_fruit & Freind_Favourate_Fruit}")
print(f"Union of two sets {Favourate_fruit - Freind_Favourate_Fruit}")
Favourate_fruit.add("Pomegranate")
print(Favourate_fruit)
Favourate_fruit.remove("Pomegranate")
print(Favourate_fruit) 
Favourate_fruit.discard("Watermelon") #Removes a specified element without raising an error if it does not exist.
print(Favourate_fruit)