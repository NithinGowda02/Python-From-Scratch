"""
**Countdown Timer**:
   - Write a program that counts down from 10 to 1 using a `while` loop and prints "Happy New Year!" after the countdown is over.
"""
import time
countdown = 10
while countdown >= 0:
    
    print(countdown)
    time.sleep(1)
    countdown -= 1
print("Happy New Year!")   
