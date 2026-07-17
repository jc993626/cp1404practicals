"""Car simulator using Car class"""

from car import Car
from prac_06.car import Car


def main():
    """"""
    print("Let's drive!")
    # car = Car(100, "The Beast")
    car = Car(100, input("Enter your car name: "))

    menu_choice = display_menu(car)
    while menu_choice != "q":
        if menu_choice == "d":
            drive_car(car)
        elif menu_choice == "r":
            add_fuel(car)
        else:
            print("Invalid choice.")
        menu_choice = display_menu(car)
    print(f"Good bye {car.name}'s driver.")


def display_menu(car):
    print(car)
    print("Menu: ")
    print("d) drive")
    print("r) refuel")
    print("q) quit")
    menu_choice = input("Enter your choice: ")
    return menu_choice


def add_fuel(car: Car):
    add_fuel_input = False
    while not add_fuel_input:
        try:
            add_fuel_amount = int(input("How many units of fuel do you want to add to the car? "))
            if add_fuel_amount < 0:
                print("Distance must be >= 0.")
                add_fuel_amount = int(input("How many units of fuel do you want to add to the car? "))
            else:
                add_fuel_input = True
        except ValueError:
            print("Must be whole number!")
    print(car.add_fuel(add_fuel_amount))


def drive_car(car: Car):
    drive_input = False
    while not drive_input:
        try:
            drive_distance = int(input("How many km do you wish to drive? "))
            if drive_distance < 0:
                print("Distance must be >= 0.")
                drive_distance = int(input("How many km do you wish to drive? "))
            else:
                drive_input = True
        except ValueError:
            print("Must be whole number!")
    print(car.drive(drive_distance))

main()





