import csv
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput


class Place:
    def __init__(self, name, country, priority):
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = False

    def __str__(self):
        return f"{self.name} in {self.country} (Priority: {self.priority})"

    def mark_visited(self):
        self.visited = True

    def mark_unvisited(self):
        self.visited = False


class PlaceApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.places = [
            Place("Place 1", "Country 1", 1),
            Place("Place 2", "Country 2", 2),
            Place("Place 3", "Country 3", 3)
        ]
        self.sort_key = 'Name'


    def build(self):
        layout = BoxLayout(orientation='horizontal')
        left_layout = BoxLayout(orientation='vertical', size_hint=(0.3, 1.0))

        # Sort by section
        sort_label = Label(text='Sort by', size_hint=(1.0, 0.1))
        spinner = Spinner(
            text='Name',
            values=('Name', 'Country', 'Priority'),
            size_hint=(1.0, 0.1)
        )
        spinner.bind(text=self.on_sort_select)
        left_layout.add_widget(sort_label)
        left_layout.add_widget(spinner)

        # Visited section
        visited_label = Label(text='Visited', size_hint=(1.0, 0.1))
        visited_button = Button(text='Mark as Visited', size_hint=(1.0, 0.1))
        visited_button.bind(on_press=self.on_visit_button_press)
        left_layout.add_widget(visited_label)
        left_layout.add_widget(visited_button)

        # Add New Place section
        new_place_label = Label(text='Add New Place', size_hint=(1.0, 0.1))
        name_input = TextInput(hint_text='Name', size_hint=(1.0, 0.1))
        country_input = TextInput(hint_text='Country', size_hint=(1.0, 0.1))
        priority_input = TextInput(hint_text='Priority', size_hint=(1.0, 0.1))
        add_place_button = Button(text='Add Place', size_hint=(1.0, 0.1))
        add_place_button.bind(on_press=self.on_add_place_button_press)
        left_layout.add_widget(new_place_label)
        left_layout.add_widget(name_input)
        left_layout.add_widget(country_input)
        left_layout.add_widget(priority_input)
        left_layout.add_widget(add_place_button)

        # Clear section
        clear_button = Button(text='Clear', size_hint=(1.0, 0.1))
        clear_button.bind(on_press=self.on_clear_button_press)
        left_layout.add_widget(clear_button)

        layout.add_widget(left_layout)

        right_layout = BoxLayout(orientation='vertical', size_hint=(0.7, 1.0))

        status_bar_top = Label(text='Number of places to visit: 0')
        right_layout.add_widget(status_bar_top)

        place_buttons = []
        for place in self.places:
            button = Button(
                text=place.name,
                background_color=(0, 0, 0, 1) if place.visited else (1, 1, 1, 1),
                color=(0.5, 0.5, 0.5, 1),
                size_hint=(1.0, 0.1)
            )
            button.bind(on_press=self.on_place_button_press)
            place_buttons.append(button)
            right_layout.add_widget(button)

        status_bar_bottom = Label(text='Program messages')
        right_layout.add_widget(status_bar_bottom)

        layout.add_widget(right_layout)

        return layout

    def on_sort_select(self, spinner, text):
        self.sort_key = text
        self.sort_places()
        self.update_place_buttons()

    def sort_places(self):
        self.places.sort(key=lambda place: getattr(place, self.sort_key.lower()))

    def update_place_buttons(self):
        for i, place in enumerate(self.places):
            button = self.root.children[0].children[1].children[i]
            button.text = place.name
            button.background_color = (0, 0, 0, 1) if place.visited else (1, 1, 1, 1)

    def on_place_button_press(self, button):
        for place in self.places:
            if place.name == button.text:
                if place.visited:
                    place.mark_unvisited()
                else:
                    place.mark_visited()
                break
        self.update_place_buttons()

    def on_visit_button_press(self, button):
        # Mark all places as visited
        for place in self.places:
            place.mark_visited()
        self.update_place_buttons()

    def on_add_place_button_press(self, button):
        name_input = self.root.children[0].children[0].children[4]
        country_input = self.root.children[0].children[0].children[5]
        priority_input = self.root.children[0].children[0].children[6]
        name = name_input.text
        country = country_input.text
        priority = int(priority_input.text) if priority_input.text.isdigit() else 0
        if name and country and priority > 0:
            new_place = Place(name, country, priority)
            self.places.append(new_place)
            self.sort_places()
            self.update_place_buttons()
            name_input.text = ''
            country_input.text = ''
            priority_input.text = ''

    def on_clear_button_press(self, button):
        for place in self.places:
            place.mark_unvisited()
        self.update_place_buttons()


if __name__ == '__main__':
    PlaceApp().run()
