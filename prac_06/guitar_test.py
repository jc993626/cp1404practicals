"""Program to test Guitar class methods."""

from guitar import Guitar


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    # print(f"My guitar: {name}, first made in {year}")
    gibson = Guitar(name, year, cost)
    print(gibson)
    print(f"Expected 104, got {gibson.get_age()}")
    print(f"Expected True, got {gibson.is_vintage()}")



main()