"""Guitar data input program. (Name, Year, Cost)."""

from guitar import Guitar

def main():
    """Take a Guitar parameters until empty string is entered for guitar_name
        and store class objects in a list."""
    guitars = []
    guitar_name = input("Enter guitar name: ")
    while guitar_name != "":
        guitar_year = int(input("Enter year of guitar manufacture: "))
        guitar_cost = float(input("Enter guitar cost: "))
        guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))

        guitar_name = input("Enter next guitar name: ")

    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name} {guitar.year}, is worth ${guitar.cost:,.2f} {guitar.is_vintage()}")

main()







