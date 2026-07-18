"""Program to read guitar data and create list of guitar objects."""
from typing import Any

from guitar import Guitar

# ADD MENU to use FUNCTIONS
def main():
    """Display guitar objects"""
    # display guitars using loop
    guitars = retrieve_guitars_data()
    guitars.sort()
    for guitar in guitars:
        print(guitar)

    add_guitars(guitars)

    save_guitars(guitars)


def save_guitars(guitars: list[Any]):
    out_file = open("guitars.csv", "w")
    for guitar in guitars:
        out_file.writelines(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    out_file.close()


def retrieve_guitars_data():
    guitars = []
    in_file = open("guitars.csv", "r")
    in_file.readline()  # to exclude header from list

    for line in in_file:
        parts = line.strip().split(',')
        #print(parts)
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
        #print(guitars)

    in_file.close()
    return guitars

def add_guitars(guitars):
    """Take a Guitar parameters until empty string is entered for guitar_name
            and store class objects in a list."""
    guitar_name = input("Enter guitar name: ")
    while guitar_name != "":
        guitar_year = int(input("Enter year of guitar manufacture: "))
        guitar_cost = float(input("Enter guitar cost: "))
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))

        guitar_name = input("Enter next guitar name: ")

    print("List of guitars to be entered into data")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name} {guitar.year}, is worth ${guitar.cost:,.2f} {guitar.is_vintage()}")





main()

