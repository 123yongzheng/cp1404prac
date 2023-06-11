from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

class PlaceApp(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal')
        left_layout = BoxLayout(orientation='vertical', size_hint=(0.3, 1.0))

        spinner = Spinner(
            text='Sort by',
            values=('Name', 'Country', 'Priority'),
            size_hint=(1.0, 0.1)
        )
        left_layout.add_widget(spinner)


        name_input = TextInput(hint_text='Name', size_hint=(1.0, 0.1))
        country_input = TextInput(hint_text='Country', size_hint=(1.0, 0.1))
        priority_input = TextInput(hint_text='Priority', size_hint=(1.0, 0.1))
        left_layout.add_widget(name_input)
        left_layout.add_widget(country_input)
        left_layout.add_widget(priority_input)

        layout.add_widget(left_layout)

        right_layout = BoxLayout(orientation='vertical', size_hint=(0.7, 1.0))

        status_bar_top = Label(text='Number of places to visit: 0')
        right_layout.add_widget(status_bar_top)

        place_buttons = [
            Button(text='Place 1', background_color=(1, 0, 0, 1), size_hint=(1.0, 0.1)),
            Button(text='Place 2', background_color=(0, 1, 0, 1), size_hint=(1.0, 0.1)),
            Button(text='Place 3', background_color=(0, 0, 1, 1), size_hint=(1.0, 0.1)),
        ]
        for button in place_buttons:
            right_layout.add_widget(button)

        status_bar_bottom = Label(text='Program messages')
        right_layout.add_widget(status_bar_bottom)

        layout.add_widget(right_layout)

        return layout

if __name__ == '__main__':
    PlaceApp().run()
