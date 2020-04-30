"""
Name:   Hafidz Izzi Baihaqi
GitHub: https://github.com/izzitan/CP1404_practical
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.button import Label


class DynamicWidgets(App):
    def __init__(self):
        super().__init__()
        self.names = ["James", "Bob", "John"]

    def build(self):
        Window.size = (600, 300)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_button = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_button)



DynamicWidgets().run()