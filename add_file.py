from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.properties import ColorProperty, StringProperty
from plyer import filechooser

from shortcut_creation_manager import ShortcutCreationManager


class AddFile(StackLayout):
    pass


class AddMoreFileButton(FloatLayout):
    background_color_original = [1.0, 1.0, 1.0, 1.0]
    background_color_on_click = [0, 1.0, 0, 1.0]
    background_color = ColorProperty(background_color_original)

    def on_add_more_file_click(self):
        self.background_color = self.background_color_on_click

    def on_add_more_file_release(self):
        self.background_color = self.background_color_original


class InfoButton(BoxLayout):
    path_str = StringProperty("Path: ")

    def on_select_file_click(self, paths_list):
        path = filechooser.open_file(title="Pick a EXE file..",
                                     filters=[("Executables", "*.exe")])
        if not path:
            return

        if path[0] in paths_list:
            print("File already selected")
            return

        if self.path_str != "Path: ":
            for i in range(len(paths_list)):
                if self.path_str.lstrip("Path: ") == paths_list[i]:
                    paths_list.pop(i)
                    break

        paths_list.append(path[0])
        self.path_str = "Path: " + str(path[0])
        print(paths_list)
