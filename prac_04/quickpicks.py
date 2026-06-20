"""Quickpicks exercise"""
from random import randint


NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

number_of_picks = int(input("Enter number of quickpicks you would like:"))

for pick in range(number_of_picks):
    quick_pick = []
    for number in range(NUMBERS_PER_LINE):
        number = randint(MIN_NUMBER, MAX_NUMBER)
        while number in quick_pick:
            number = randint(MIN_NUMBER, MAX_NUMBER)

        quick_pick.append(number)

    quick_pick.sort()
    # print(quick_pick)
    # print(type(quick_pick))
    # print(type(quick_pick[0]))


    print(" ".join(f"{number:2}" for number in quick_pick))


# print(quick_pick)
# print(type(quick_pick))
# print(type(quick_pick[0]))
# for pick in range(number_of_picks):
#     quick_pick = []
#
#     for _ in range(NUMBERS_PER_LINE):
#         number = randint(MIN_NUMBER, MAX_NUMBER)
#
#         while number in quick_pick:
#             number = randint(MIN_NUMBER, MAX_NUMBER)
#
#         quick_pick.append(number)
#
#     quick_pick.sort()
#
#     print(" ".join(f"{number:2}" for number in quick_pick))














