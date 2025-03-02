"""
 **Character Counter**:
   Write a Python program that:
   - Asks the user for a string.
   - Prints how many characters are in the string, excluding spaces.

   **Example**:
   ```python
   Input: "Hello World"
   Output: "Number of characters (excluding spaces): 10"
   ```
"""
User_input = input("Enter a String >> ")
String_length = len(User_input.replace(" ",""))
print(f"Number of characters (excluding spaces) >> {String_length}")