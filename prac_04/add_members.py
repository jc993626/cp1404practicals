"""Add elements of lists of integers with same index together"""

numbers = [1, 2, 3, 4]
more_numbers = [2, 3, 4, 5]

def main():
    numbers_total = member_wise(numbers, more_numbers)
    print(numbers_total)


def member_wise(list1, list2):
    totals = []
    for i in range(len(list1)):
        totals.append(list1[i] + list2[i])
    return totals

main()







