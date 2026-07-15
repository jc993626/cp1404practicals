"""Car simulator using Car class"""

from car import Car
from prac_06.car import Car


def main():
    """"""
    print("Let's drive!")
    # car = Car(100, "The Beast")
    car = Car(100, input("Enter car name: "))
    print(car)
    print("Menu: ")
    print("d) drive")
    print("r) refuel")
    print("q) quit")
    menu_choice = input("Enter your choice: ")

    while menu_choice != "q":
        if menu_choice == "d":
            print("How many km do you wish to drive? ")
    try:




def add_fuel(car: Car):
    add_fuel_input = False
    while not add_fuel_input:
        try:
            add_fuel_amount = int(input("How many km do you wish to drive? "))
            if add_fuel_amount < 0:
                print("Distance must be >= 0.")
                add_fuel_amount = int(input("How many km do you wish to drive? "))
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






    # car = Car(200, "The Beast")
    # print(car)
    # car.drive(50)
    # print(car)
    # car.add_fuel(50)
    # print(car)



