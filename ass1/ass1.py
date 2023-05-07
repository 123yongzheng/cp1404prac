"""
CP1404 2023 Assignment 1
Travel Tracker 1.0
Student Name: CHEN YONGZHENG
Date started: 28/4/2023
"""
import csv
import random
FILENAME = "places.csv"


def main():
    print("Travel Tracker 1.0 - by CHEN YONGZHENG")
    places_list = load_places(FILENAME)
    print(f"{len(places_list)} places loaded from {FILENAME}\n")

    while True:
        print("Menu:")
        print("L - List places")
        print("A - Add new place")
        print("M - Mark a place as visited")
        print("R - Recommend an unvisited place to travel")
        print("Q - Quit")
        choice = input(">>> ").upper()

        if choice == "L":
            list_places(places_list)
        elif choice == "A":
            add_place(places_list)
        elif choice == "M":
            mark_place(places_list)
        elif choice == "R":
            recommend_place(places_list)
        elif choice == "Q":
            save_places(FILENAME, places_list)
            print(f"{len(places_list)} places saved to {FILENAME}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid choice, please try again.\n")

def recommend_place(places_list):
    unvisited_places = [place for place in places_list if place[3] == "n"]
    if not unvisited_places:
        print("You have visited all places!")
        return
    unvisited_places.sort(key=lambda place: -place[2])
    highest_priority = unvisited_places[0][2]
    highest_priority_places = [place for place in unvisited_places if place[2] == highest_priority]
    if len(highest_priority_places) == 1:
        place = highest_priority_places[0]
        print(f"You should visit {place[0]} in {place[1]} with priority {place[2]}!")
    else:
        place = random.choice(highest_priority_places)
        print(f"You should consider visiting {place[0]} in {place[1]} with priority {place[2]}!")

def load_places(filename):
    places_list = []
    try:
        with open(filename, "r") as file:
            for line in file:
                name, country, priority, visited = line.strip().split(",")
                places_list.append([name, country, int(priority), visited])
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except ValueError:
        print(f"Error: Invalid data in {filename}.")
    else:
        print("File loaded successfully.")
    return places_list

def save_places(filename, places_list):
    try:
        with open(filename, "w") as file:
            for place in places_list:
                file.write(f"{place[0]},{place[1]},{place[2]},{place[3]}\n")
    except IOError:
        print(f"Error: Failed to save data to {filename}.")

def list_places(places_list):
    places_list.sort(key=lambda place: (place[3], -place[2]))
    longest_name = max(len(place[0]) for place in places_list)
    longest_country = max(len(place[1]) for place in places_list)
    count = 0
    for i, place in enumerate(places_list):
        mark = "*" if place[3] == "n" else " "
        print(f"{i + 1}. {place[0]:<{longest_name}} from {place[1]:<{longest_country}} "
              f"{'Priority: ' + str(place[2]):<10} {mark}")
        if place[3] == "n":
            count += 1
    print(f"{len(places_list)} places. You still want to visit {count} places.")

def get_priority():
    while True:
        try:
            priority = int(input("Priority: "))
            if priority <= 0:
                print("Priority must be > 0")
            else:
                return priority
        except ValueError:
            print("Invalid input; enter a valid number")

def add_place(places_list):
    name = input("Name: ")
    while not name:
        print("Input can not be blank.")
        name = input("Name: ")
    country = input("Country: ")
    while not country:
        print("Input can not be blank.")
        country = input("Country: ")
    priority = get_priority()
    places_list.append([name, country, priority, "n"])
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker.")

def mark_place(places_list):
    unvisited_places = [place for place in places_list if place[3] == "n"]
    if not unvisited_places:
        print("No unvisited places.")

main()