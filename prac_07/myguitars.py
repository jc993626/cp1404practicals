"""Program to read guitar data and create list of guitar objects."""

from guitar import Guitar

def main():
    """Display guitar objects"""
    # display guitars using loop
    retrieve_guitars_data()


def retrieve_guitars_data():
    guitars = []
    in_file = open("guitars.csv", "r")
    in_file.readline()  # to exclude header from list

    for line in in_file:
        parts = line.strip().split(',')
        print(parts)
        guitar = Guitar(parts[0], parts[1], float(parts[2]))
        guitars.append(guitar)
        print(guitars)

    in_file.close()




main()

