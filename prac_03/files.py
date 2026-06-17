""" Program to read number on each line and add them up"""

sum_of_numbers = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        sum_of_numbers += int(line)

    print(sum_of_numbers)



