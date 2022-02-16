from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from plyer import filechooser

from shortcut_creation_manager import ShortcutCreationManager


class ShortcutCreation(BoxLayout):
    img_src = StringProperty("Images/neural.ico")
    scm = ShortcutCreationManager()

    def on_create_shortcut_click(self, paths_list):
        if len(paths_list) > 1:
            self.scm.create_shortcut(paths_list, self.img_src)
        else:
            popup = Popup(title='ERROR:  Not enough files',
                          content=Label(text='Please select at least two files.',
                                        halign="center"),
                          size_hint=(None, None), size=(400, 150),
                          separator_color=(1, 1, 1, 1))
            popup.open()

    def on_select_icon_click(self):
        path = filechooser.open_file(title="Pick a ICO file..",
                                     filters=[("Icon (.ico)", "*.ico")])
        if path:
            self.img_src = path[0]
