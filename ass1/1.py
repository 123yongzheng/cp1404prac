import csv
import random

FILENAME = "places.csv"
MENU = "Menu:\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit\n"
COUNTRY_LENGTH = 10
NAME_LENGTH = 20


def main():
    print("Travel Tracker 1.0 - by YOUR NAME")
    places = read_places_from_file()
    print("{} places loaded from {}".format(len(places), FILENAME))

    while True:
        print(MENU)
        choice = input(">>> ").upper()
        if choice == "L":
            list_places(places)
        elif choice == "A":
            add_place(places)
        elif choice == "M":
            mark_place_visited(places)
        elif choice == "Q":
            save_places_to_file(places)
            print("{} places saved to {}".format(len(places), FILENAME))
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


def read_places_from_file():
    places = []
    with open(FILENAME, "r", newline="") as file:
        reader = csv.reader(file)
        for line in reader:
            name, country, priority, visited = line
            places.append([name, country, int(priority), visited == "v"])
    return places


def save_places_to_file(places):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        for place in places:
            name, country, priority, visited = place
            writer.writerow([name, country, priority, "v" if visited else "n"])


def list_places(places):
    places.sort(key=lambda x: (not x[3], -x[2]))
    unvisited_count = sum(1 for place in places if not place[3])
    print("{:<{}s}  {:<{}}  {:>4s}  {}".format("Name", NAME_LENGTH, "Country", COUNTRY_LENGTH, "Priority", "Visited"))
    print("-" * (NAME_LENGTH + COUNTRY_LENGTH + 14))
    for i, place in enumerate(places):
        name, country, priority, visited = place
        mark = "*" if not visited else " "
        print(
            "{:<{}s}  {:<{}}  {:>4d}  {} {}".format(name, NAME_LENGTH, country, COUNTRY_LENGTH, priority, mark, i + 1))
    print("{} places. You still want to visit {} places.".format(len(places), unvisited_count))


def add_place(places):
    name = input("Name: ")
    while not name.strip():
        print("Input can not be blank")
        name = input("Name: ")

    country = input("Country: ")
    while not country.strip():
        print("Input can not be blank")
        country = input("Country: ")

    priority = input("Priority: ")
    while not priority.isdigit() or int(priority) <= 0:
        print("Priority must be >= 1")
        priority = input("Priority: ")

    places.append([name, country, int(priority), False])
    print("{} in {} (priority {}) added to Travel Tracker".format(name, country, priority))



