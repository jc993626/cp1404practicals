"""Enter person parameters(first name, surname, age)."""

from person import Person

def main():
    """Enter person parameters to class object and print persons in a table"""
    persons = []
    first_name = input("Enter first name: ").title()
    while first_name != "":
        last_name = input("Enter surname: ").title()
        age = int(input("Enter age: "))
        persons.append(Person(first_name, last_name, age))
        first_name = input("Enter next name: ").title()

    print(f"{'No':5}{'Name':10}{'Last Name':20}age")
    print('_-' * 19)
    for i, person in enumerate(persons, 1):
        print(f"{i}{':':4}{person.name:10}{person.surname:20}{person.age:>3}")
    print('_' * 38)

main()