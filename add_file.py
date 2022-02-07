from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.properties import ColorProperty

Builder.load_file("add_file.kv")


class InfoAndAddButton(FloatLayout):
    background_color_original = [1.0, 1.0, 1.0, 1.0]
    background_color_on_click = [0, 1.0, 0, 1.0]
    background_color = ColorProperty(background_color_original)

    def on_add_more_file_click(self):
        self.background_color = self.background_color_on_click
    def on_add_more_file_release(self):
        self.background_color = self.background_color_original

