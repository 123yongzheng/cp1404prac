import csv
class PlaceCollection:
    def __init__(self):
        self.places = []

    def load_places(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, country, priority, visited = row
                place = Place(name, country, int(priority), visited == 'True')
                self.places.append(place)

    def save_places(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for place in self.places:
                writer.writerow([place.name, place.country, place.priority, place.visited])

    def add_place(self, place):
        self.places.append(place)

    def get_number_of_unvisited_places(self):
        count = 0
        for place in self.places:
            if not place.visited:
                count += 1
        return count

    def sort(self, key):
        self.places.sort(key=key)
