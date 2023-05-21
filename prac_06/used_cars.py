"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)


main()
limo = Car(fuel=100)
limo.add_fuel(20)
print(f"Limo has {limo.fuel} units of fuel.")
limo.drive(115)
def __str__(self):
    return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"
class Car:
    """Represent a Car object."""

    def __init__(self, fuel=0, name=""):
        """Initialise a Car instance.
        fuel: float, one unit of fuel drives one kilometre
        name: str, name of the car
        """
        self.fuel = fuel
        self._odometer = 0
        self.name = name

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"
my_car = Car(fuel=180, name="My Car")
limo = Car(fuel=100, name="Limo")
print(my_car)
print(limo)
