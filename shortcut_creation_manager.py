import os

from kivy.graphics import Color, RoundedRectangle, Callback
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from pyshortcuts import make_shortcut


class ShortcutCreationManager:
    def __init__(self):
        self.desktop_location = desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        self.base_path = os.getcwd()
        self.bat_name = 0  # numbers of files already in directory
        self.shortcut_name = ""
        self.icon_src = ""
        self.create_button = Button()
        self.rect_btn = RoundedRectangle()
        for base, dirs, files in os.walk(self.base_path + "/bats"):
            for Files in files:
                self.bat_name += 1

    def popup_dismiss_callback(self, instance):
        self.__create_shortcut()

    def set_shortcut_name(self, instance, text):
        self.shortcut_name = text

    def call_popup_shortcut_name(self, default_name):
        content = BoxLayout(orientation='vertical',
                            spacing=dp(15),
                            padding=10,
                            size_hint=(1, 1))

        b = BoxLayout(pos_hint={'center_x': .5, 'center_y': .5})
        b.add_widget(Label(text="Shortcut name:",
                           font_size=dp(15),
                           size_hint=(.3, None),
                           height=40,
                           pos_hint={'center_x': .5, 'center_y': .5}))

        text_input = TextInput(text=default_name,
                               font_size=dp(15),
                               size_hint=(.7, None),
                               height=40,
                               pos_hint={'center_x': .5, 'center_y': .5},
                               multiline=False)
        text_input.padding = [10, text_input.height / 2.0 - (text_input.line_height / 2.0), 0, 0]
        text_input.bind(text=self.set_shortcut_name)
        b.add_widget(text_input)
        content.add_widget(b)

        self.create_button = Button(text="Create Shortcut",
                                    bold=True,
                                    size_hint=(None, None),
                                    size=(150, 50),
                                    pos_hint={'center_x': .5},
                                    color=(0, 0, 0, 1),
                                    background_color=(0, 0, 0, 0),
                                    background_normal="")
        with self.create_button.canvas.before:
            Color(1, 1, 1)
            self.rect_btn = RoundedRectangle(pos=self.create_button.pos, size=self.create_button.size, radius=[25])
            Callback(self.btn_callback)
        content.add_widget(self.create_button)

        popup = Popup(title='Shortcut Name',
                      auto_dismiss=False,
                      content=content,
                      size_hint=(None, None),
                      size=(400, 230))

        self.create_button.bind(on_press=popup.dismiss)
        popup.bind(on_dismiss=self.popup_dismiss_callback)
        popup.open()

    def btn_callback(self, instr):
        self.rect_btn.pos = self.create_button.pos
        self.rect_btn.size = self.create_button.size

    def __create_shortcut(self):
        if os.path.exists(self.desktop_location + f"\\{self.shortcut_name}.lnk"):
            os.remove(f"{self.base_path}\\bats\\{self.bat_name}.bat")
            popup = Popup(title='ERROR: Shortcut Name',
                          content=Label(text='Shortcut name already exist on Desktop!\n'
                                             'Please change shortcut\'s name.',
                                        halign="center"),
                          size_hint=(None, None), size=(400, 150))
            popup.open()
        else:
            make_shortcut(f"{self.base_path}\\bats\\{self.bat_name}.bat", name=self.shortcut_name,
                          icon=self.icon_src, startmenu=False)
            self.bat_name += 1
            popup = Popup(title='Shortcut Created',
                          content=Label(text='Shortcut successfully created on Desktop!',
                                        halign="center"),
                          size_hint=(None, None), size=(400, 150))
            popup.open()

    def create_shortcut(self, file_paths, icon_src):
        self.icon_src = icon_src
        if self.icon_src == "Images/link.ico":
            self.icon_src = f"{self.base_path}\\{icon_src}"

        file_dict = self.create_dict_with_path_and_exe(file_paths)
        self.fill_and_create_bat_file_for_shortcut(file_dict)

        self.shortcut_name = file_dict["file0"]["filename"].rpartition(".")[0].replace(" ", "")

        self.call_popup_shortcut_name(self.shortcut_name)

    @staticmethod
    def create_dict_with_path_and_exe(file_paths):
        file_dict = {}
        for i in range(len(file_paths)):
            directory_path = file_paths[i].rpartition("\\")[0]
            filename = file_paths[i].rpartition("\\")[-1]
            file_dict[f"file{str(i)}"] = {"path": directory_path, "filename": filename}
        return file_dict

    def fill_and_create_bat_file_for_shortcut(self, files_list):
        txt = "@echo off"
        for file, file_info in files_list.items():
            txt += f'\nstart \"\" \"{file_info["path"]}\\{file_info["filename"]}\"'

        bat_file = open(f"{self.base_path}\\bats\\{self.bat_name}.bat", "w")
        bat_file.write(txt)
        bat_file.close()
