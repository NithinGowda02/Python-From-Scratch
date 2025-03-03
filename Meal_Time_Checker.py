"""
**Meal Time Checker**:
   - Create a program that checks the time of day (24-hour format) and prints whether it's time for breakfast, lunch, or dinner.
     - Breakfast: 8 AM
     - Lunch: 1 PM
     - Dinner: 8 PM
     - If none of these times, print "It's not meal time."

"""
Current_time = input("Enter the Current Time (Including AM or PM (ex: 8 AM)) >> ")
if Current_time == "8 AM":
    print("Its time for Breakfast ")
elif Current_time == "1 PM":
    print("Its time for Lunch ")  
elif Current_time == "8 PM":
    print("Its time for Dinner ") 
else:
    print("It's not meal time.")
