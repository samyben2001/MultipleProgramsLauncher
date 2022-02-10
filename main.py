from kivy import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '600')
Config.set('graphics', 'minimum_width', '1000')
Config.set('graphics', 'minimum_height', '600')
Config.set('graphics', 'resizable', '0')
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget

Builder.load_file("add_file.kv")
Builder.load_file("shortcut_creation.kv")


class MainWidget(BoxLayout):
    paths = ListProperty([])


class MultipleProgramsLauncherApp(MDApp):
    pass


MultipleProgramsLauncherApp().run()
