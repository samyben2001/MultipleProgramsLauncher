from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.properties import ColorProperty, StringProperty, ObjectProperty
from plyer import filechooser

from shortcut_creation_manager import ShortcutCreationManager


class RemoveFileButton(Button):
    info_btn: ObjectProperty()

    def on_remove_file_click(self, path_list):
        print(path_list)
        if self.parent.children[2].text in path_list:
            path_list.remove(self.parent.children[2].text)
        self.parent.parent.remove_widget(self.parent)
        print(path_list)


class AddFile(BoxLayout):
    stack_files = ObjectProperty()


class AddMoreFileButton(Button):
    def on_add_more_file_click(self):
        if len(self.parent.parent.stack_files.children) <= 4:
            b = InfoButton()
            b.children[0].size_hint = [.1, 1]
            rmb = RemoveFileButton()
            b.add_widget(rmb)
            self.parent.parent.stack_files.add_widget(b)
        else:
            popup = Popup(title='ERROR: Max files reached',
                          content=Label(text='You cannot add more than 5 files to execute \n simultaneously!',
                                        halign="center"),
                          size_hint=(None, None), size=(400, 150))
            popup.open()


class InfoButton(BoxLayout):
    path_str = StringProperty("")

    def on_select_file_click(self, paths_list):
        print(filechooser)
        path = filechooser.open_file(title="Pick a EXE file..",
                                     filters=[("Executables", "*.exe")])
        if not path:
            return

        if path[0] in paths_list:
            popup = Popup(title='ERROR: File already selected',
                          content=Label(text='You have already selected this file!',
                                        halign="center"),
                          size_hint=(None, None), size=(400, 150))
            popup.open()
            return

        if self.path_str != "":
            for i in range(len(paths_list)):
                if self.path_str == paths_list[i]:
                    paths_list.pop(i)
                    break

        paths_list.append(path[0])
        self.path_str = str(path[0])
