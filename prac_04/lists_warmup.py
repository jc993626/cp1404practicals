"""Warmup exercise."""

numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0]            3
# numbers[-1]           2
# numbers[3]            1
# numbers[:-1]          3, 1, 4, 1, 5, 9
# numbers[3:4]          1       [3:4]  incl [3] but not [4]
# 5 in numbers          True
# 7 in numbers          False
# "3" in numbers        False
# numbers + [6, 5, 3]   3, 1, 4, 1, 5, 9, 2, 6, 5, 3    adds [6, 5, 3] to end

# 1. Change the first element of numbers to `"ten"` (the string, not the number `10`)   numbers[0] = "ten"
# 2. Change the last element of numbers to `1`                                          numbers[-1] = 1
# 3. Print all the elements from numbers except the first two (slice)                   print(numbers[2:])
# 4. Print whether `9` is an element of numbers                                         9 in numbers
#
#Remember that list indexes start at 0, but we want to print from 1. so use print[count-1] count =2, print [1] 2nd index
#
#
#
#
#
