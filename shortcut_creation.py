from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from plyer import filechooser

from shortcut_creation_manager import ShortcutCreationManager


class ShortcutCreation(BoxLayout):
    img_src = StringProperty("Images/link.ico")
    scm = ShortcutCreationManager()

    def on_create_shortcut_click(self, paths_list):
        if len(paths_list) > 1:
            self.scm.create_shortcut(paths_list, self.img_src)
        else:
            print("Please select at least two files")

    def on_select_icon_click(self):
        path = filechooser.open_file(title="Pick a ICO file..",
                                     filters=[("Icon", "*.ico")])
        if path:
            self.img_src = path[0]


