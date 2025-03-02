""" **String Manipulation Exercise**:
   Write a Python program that:
   - Takes a sentence as input from the user.
   - Prints the sentence in all uppercase and lowercase.
   - Replaces all spaces with underscores.
   - Removes leading and trailing whitespace.

   **Example**:
   ```python
   Input: "   Python is awesome!   "
   Output:
   Uppercase: "PYTHON IS AWESOME!"
   Lowercase: "python is awesome!"
   Replaced: "___Python_is_awesome!___"
   Stripped: "Python is awesome!"
   ```
"""

Sentence = input("Enter a Sentence >> \n")
upper_case = Sentence.upper()
lower_case = Sentence.lower()
replaced = Sentence.replace(" ","_")
stripped= Sentence.strip()
print(f"Upper case >> {upper_case}")
print(f"Lower case >> {lower_case}")
print(f"Replaced  >> {replaced}")    
print(f"Stripped >> {stripped}")