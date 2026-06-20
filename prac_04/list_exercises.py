"""List exercise."""

def main():
    numbers = get_numbers()
    print(f"The last number is {numbers[-1]}")
    print(f"The smalles number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


def get_numbers():
    numbers = []
    for number in range(0, 5):
        numbers.append(int(input("Please enter a number:")))

    print(numbers)
    return numbers

# numbers = []              SOLUTION this is better i think
# for i in range(5):
#     number = int(input("Number: "))
#     numbers.append(number)
# main()

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Please enter username:")

if username in usernames:
    print("Access granted")
else:
    print("Access denied")