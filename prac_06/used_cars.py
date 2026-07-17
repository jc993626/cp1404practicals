"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    car_name = input("Enter new car name: ")
    fuel_add = int(input("Enter fuel to add: "))

    new_car = Car(fuel_add, car_name)
    # new_car.add_fuel(fuel_add)
    print(new_car)
    new_car.drive(10)
    print(new_car)
    new_car.drive(40)
    print(new_car)


    # my_car = Car(180)
    # my_car.drive(30)
    # print(f"Car has fuel: {my_car.fuel}")
    # print(my_car)
    # new_car = Car(100, "limo")
    # new_car.add_fuel(20)
    # print(new_car.fuel)
    # new_car.drive(115)
    # print(new_car)


main()
