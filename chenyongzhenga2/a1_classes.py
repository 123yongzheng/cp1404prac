from place import Place
from placecollection import PlaceCollection
import random

FILENAME = 'places.csv'

def main():
    """Main logic of the program"""
    print("Travel Tracker 2.0 - chen yongzheng")

    # Create a new PlaceCollection object
    place_collection = PlaceCollection()

    # Load data from CSV file
    place_collection.load_places(FILENAME)
    print(f"{len(place_collection.places)} places loaded from {FILENAME}")

    while True:
        show_menu()
        menu_choice = input(">>> ").upper()

        # Menu options
        if menu_choice == "L":
            list_places(place_collection)
        elif menu_choice == "R":
            recommend_place(place_collection)
        elif menu_choice == "A":
            add_place(place_collection)
        elif menu_choice == "M":
            mark_place(place_collection)
        elif menu_choice == "Q":
            place_collection.save_places(FILENAME)  # save data to file
            print(f"{len(place_collection)} places saved to {FILENAME}")
            print("Have a great day!")
            break
        else:
            print("Invalid menu choice")

def list_places(place_collection):
    """Sort and list the places in the PlaceCollection object."""
    place_collection.sort("priority")
    for i, place in enumerate(place_collection.places):
        visit_status = "Visited" if place.is_visited() else "Not Visited"
        print(f"*{i + 1}. {place.name:<8} in {place.country:<12} {place.priority:<2} ({visit_status})")

    not_visited = place_collection.get_number_of_unvisited_places()
    if len(place_collection) == 0:
        print("No places in the list. Why not add a new place?")
    elif len(not_visited) == 0:
        print(f"{len(place_collection)} places. No places left to visit. Why not add a new place?")
    else:
        print(f"{len(place_collection)} places. You still want to visit {len(not_visited)} places.")

def recommend_place(place_collection):
    """Recommend a random unvisited place from the PlaceCollection object."""
    not_visited = place_collection.get_number_of_unvisited_places()
    if len(not_visited) == 0:
        print("No places left to visit!")
    else:
        place = random.choice(not_visited)
        print("Not sure where to visit next?")
        print(f"How about... {place.name} in {place.country}?")

def add_place(place_collection):
    """Add a new place to the PlaceCollection object based on user input."""
    name = input("Name: ")
    while not name:
        print("Input cannot be blank")
        name = input("Name: ")

    country = input("Country: ")
    while not country:
        print("Input cannot be blank")
        country = input("Country: ")

    priority = input("Priority: ")
    while not priority.isdigit():
        print("Invalid input; enter a valid number")
        priority = input("Priority: ")

    place = Place(name, country, int(priority))
    place_collection.add_place(place)
    print(f"{name} in {country} ({priority}) added to Travel Tracker")

def mark_place(place_collection):
    """Mark a place in the PlaceCollection object as visited based on user input."""
    not_visited = place_collection.get_number_of_unvisited_places()
    if len(not_visited) == 0:
        print("You have visited all the places!")
        return

    list_places(place_collection)
    position = int(input("Enter the number of the place you want to mark as visited: \n>>>"))
    while position < 1 or position > len(place_collection):
        print(f"Invalid input. Please enter a number between 1 and {len(place_collection)}.")
        position = int(input("Enter the number of the place you want to mark as visited: "))

    place = place_collection.places[position - 1]
    if place.is_visited():
        print(f"You have already visited {place.name} in {place.country}.")
    else:
        place.mark_as_visited()
        print(f"{place.name} in {place.country} visited")

def show_menu():
    """Show the menu"""
    print("Menu:")
    print("L - List places")
    print("R - Recommend random place")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")

if __name__ == '__main__':
    main()
