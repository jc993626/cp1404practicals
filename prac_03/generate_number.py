import random

upper_limit = int(input("Enter the upper limit for random number generation:"))
lower_limit = int(input("Now enter the lower limit for random number generation:"))

print(random.randint(lower_limit, upper_limit))
