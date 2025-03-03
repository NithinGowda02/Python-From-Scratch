"""
**Tuple Operations**:
   - Create a tuple with 5 elements.
   - Try to modify one of the elements. What happens?
   - Perform slicing on the tuple to extract the second and third elements.
   - Concatenate the tuple with another tuple.
"""
Items = ("Milk","Tea Powder","Sugar","Vegetables"," Fruits")
print(f"Accessing third item in Tuple >> {Items[2]}")
Items1 = ("Bat","Bowl","Stump")
List_Items = Items + Items1
print(f"After Concatenating the tuple with another tuple. >> \n{List_Items}")
