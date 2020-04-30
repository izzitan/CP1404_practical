"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

KM_IN_MILES = 1.60934

class ConvertMiles(App):
    def build(self):
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, increment=0):
        self.root.ids.input_name.text = str(float(self.root.ids.input_name.text) + increment)

    def handle_convert(self, miles=0):
        try:
            self.root.ids.output_label.text = str(float(self.root.ids.input_name.text) * KM_IN_MILES)
        except ValueError:
            self.root.ids.input_name.text = '0.0'
        except AttributeError:
            self.root.ids.input_name.text = '0.0'


ConvertMiles().run()