from kivy import Config

Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'minimum_width', '1000')
Config.set('graphics', 'minimum_height', '600')
Config.set('graphics', 'resizable', '0')

import os, sys
from kivy.resources import resource_add_path
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

Builder.load_file("C:\\Users\\samyb\\Documents\\.Projects\\Personnels\\MPC\\MultipleProgramsLauncher\\kivy_app\\add_file.kv")
Builder.load_file("C:\\Users\\samyb\\Documents\\.Projects\\Personnels\\MPC\\MultipleProgramsLauncher\\kivy_app\\shortcut_creation.kv")


class MainWidget(BoxLayout):
    paths = ListProperty([])


class MultipleProgramsLauncherApp(MDApp):
    pass


if __name__ == '__main__':
    try:
        if hasattr(sys, '_MEIPASS'):
            resource_add_path(os.path.join(sys._MEIPASS))
        app = MultipleProgramsLauncherApp()
        app.run()
    except Exception as e:
        print(e)
        input("Press enter.")
