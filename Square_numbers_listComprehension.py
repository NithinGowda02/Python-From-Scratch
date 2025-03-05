"""
**List of Squares**:
   - Create a list of numbers from 1 to 10. Use list comprehension to generate a list of their squares.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Square_numbers = [num**2 for num in numbers]
print(f"List of Square Numbers using List Comprehension >>{Square_numbers}")