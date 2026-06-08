"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""



try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Wrong value, cannot divide by zero, try again:"))
    fraction = numerator / denominator
    print(fraction)
except ValueError: # occurs when input is a floating point number or a string
    print("Numerator and denominator must be valid numbers!")
#except ZeroDivisionError:              Occurs when denominator is 0.
#    print("Cannot divide by zero!")    Not needed after while loop added.
print("Finished.")
