from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty
import csv


NEW_COLOUR = (0, 0, 0, 1)
ALTERNATIVE_COLOUR = (0, 255, 0, 1)


class Place:
    def __init__(self, name, country, priority, is_visited=False):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        return f"{self.name}, {self.country}, {self.priority}"


class PlaceCollection:
    def __init__(self):
        self.places = []

    def __str__(self):
        result = ""
        for place in self.places:
            result += str(place) + '\n'
        return result

    def load_places(self, filename):
        with open(filename, 'r') as csvfile:
            places_reader = csv.reader(csvfile)
            for row in places_reader:
                name, country, priority, is_visited = row
                place = Place(name, country, int(priority), is_visited == "True")
                self.places.append(place)

    def save_places(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            places_writer = csv.writer(csvfile)
            for place in self.places:
                places_writer.writerow([place.name, place.country, place.priority, 'v' if place.is_visited else 'n'])

    def add_place(self, place):
        self.places.append(place)

    def get_number_of_unvisited_places(self):
        return len([place for place in self.places if not place.is_visited])

    def sort(self, key, reverse=False):
        self.places.sort(key=lambda place: (getattr(place, key), place.priority), reverse=reverse)


class TravelTrackerApp(App):
    top_status_bar = StringProperty()
    bottom_status_bar = StringProperty()
    sort_spinner_values = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.places_data = PlaceCollection()
        self.places_data.load_places('places.csv')

    def build(self):
        self.title = "Travel Tracker"
        self.root = Builder.load_file('app.kv')
        self.create_entry_buttons()
        self.sort_spinner_values = ["Name", "Country", "Priority", "Visited"]
        return self.root

    def create_entry_buttons(self):
        self.top_status_bar = f"Places to visit: {self.places_data.get_number_of_unvisited_places()}"
        for place in self.places_data.places:
            button_text = f"{place.name}, {place.country}, {place.priority}"
            temp_button = Button(text=button_text)
            if place.is_visited:
                temp_button.background_color = ALTERNATIVE_COLOUR
            else:
                temp_button.background_color = NEW_COLOUR

            temp_button.bind(on_release=self.press_entry)
            temp_button.place = place
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):
        instance.place.is_visited = not instance.place.is_visited
        if instance.place.is_visited:
            instance.background_color = ALTERNATIVE_COLOUR
            self.bottom_status_bar = f"You visited {instance.place.name}! Great travelling!"
        else:
            instance.background_color = NEW_COLOUR
            self.bottom_status_bar = f"You need to visit {instance.place.name}. Get going!"
        self.top_status_bar = f"Places to visit: {self.places_data.get_number_of_unvisited_places()}"

    def press_clear(self):
        self.clear_fields()
        self.bottom_status_bar = ""

    def press_add(self):
        self.bottom_status_bar = "Enter details for new place"

    def press_save(self, added_name, added_country, added_priority):
        if added_name == "" or added_country == "" or added_priority == "":
            self.bottom_status_bar = "All fields must be completed"
            return
        try:
            added_priority = int(added_priority)
        except ValueError:
            self.bottom_status_bar = "Please enter a valid number"
            return

        if added_priority < 1:
            self.bottom_status_bar = "Priority must be > 0"
            return

        new_place = Place(added_name, added_country, added_priority)
        self.places_data.add_place(new_place)
        self.bottom_status_bar = "Saved"
        self.root.ids.entries_box.cols = len(self.places_data.places) // 5 + 1
        temp_button = Button(text=str(new_place))
        temp_button.bind(on_release=self.press_entry)
        self.root.ids.entries_box.add_widget(temp_button)
        self.clear_fields()
        self.top_status_bar = f"Places to visit: {self.places_data.get_number_of_unvisited_places()}"

    def clear_fields(self):
        self.root.ids.added_name.text = ""
        self.root.ids.added_country.text = ""
        self.root.ids.added_priority.text = ""

    def sort_spinner(self, sort_option):
        """Sort spinner"""
        reverse = False
        if sort_option == "Country" or sort_option == "Priority":
            reverse = True
        self.places_data.sort(sort_option.lower(), reverse)
        self.root.ids.entries_box.clear_widgets()
        self.top_status_bar = f"Places to visit: {self.places_data.get_number_of_unvisited_places()}"

        for place in self.places_data.places:
            button_text = f"{place.name}, {place.country}, {place.priority}"
            temp_button = Button(text=button_text)

            temp_button.bind(on_release=self.press_entry)
            temp_button.place = place
            self.root.ids.entries_box.add_widget(temp_button)

    def on_stop(self):
        self.places_data.save_places('places.csv')


if __name__ == '__main__':
    TravelTrackerApp().run()
