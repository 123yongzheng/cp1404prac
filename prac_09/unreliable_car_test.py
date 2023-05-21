from prac_09.unreliable_car import UnreliableCar


my_car = UnreliableCar("Ford", 100, 50)
distance_driven = my_car.drive(90)
if distance_driven > 0:
    print(f"The car drove {distance_driven} km.")
else:
    print("The car did not drive.")

print(my_car)