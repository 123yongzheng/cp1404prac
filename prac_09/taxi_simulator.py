from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_cost = 0

    print("Let's drive!")
    user_choice = get_menu_choice()

    while user_choice != 'q':
        if user_choice == 'c':
            print_taxis(taxis)
            taxi_choice = get_valid_taxi_choice(taxis)
            current_taxi = taxis[taxi_choice]
        elif user_choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive.")
            else:
                distance = get_valid_distance()
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_cost += trip_cost
                current_taxi.start_fare()

        print(f"Bill to date: ${total_cost:.2f}")
        user_choice = get_menu_choice()

    print(f"Total trip cost: ${total_cost:.2f}")
    print("Taxis are now:")
    print_taxis(taxis)


def get_valid_taxi_choice(taxis):
    taxi_choice = input("Choose taxi: ")
    while not taxi_choice.isdigit() or int(taxi_choice) not in range(len(taxis)):
        print("Invalid taxi choice")
        taxi_choice = input("Choose taxi: ")
    return int(taxi_choice)


def print_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_menu_choice():
    print("q)uit, c)hoose taxi, d)rive")
    user_choice = input(">>> ").lower()
    while user_choice not in ['q', 'c', 'd']:
        print("Invalid option")
        user_choice = input(">>> ").lower()
    return user_choice


def get_valid_distance():
    distance = input("Drive how far? ")
    while not distance.isdigit():
        print("Invalid input. Please enter a number.")
        distance = input("Drive how far? ")
    return int(distance)


main()
