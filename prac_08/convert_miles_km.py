from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty


class ConvertMilesKm(BoxLayout):
    miles = NumericProperty(0)
    km = NumericProperty(0)
    output_text = StringProperty("0.0 km")

    def calculate_conversion(self):
        self.km = round(self.miles * 1.609344, 2)
        self.output_text = str(self.km) + " km"

    def handle_increment(self, increment):
        if not self.miles:
            self.miles = 0
        self.miles += increment
        self.calculate_conversion()

    def on_miles(self, instance, value):
        self.calculate_conversion()


class ConvertMilesKmApp(App):
    def build(self):
        return ConvertMilesKm()


ConvertMilesKmApp().run()
