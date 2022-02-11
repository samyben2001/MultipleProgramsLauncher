from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ObjectProperty
from plyer import filechooser


class RoundedButton(Button):
    pass


class RemoveFileButton(RoundedButton):
    info_btn: ObjectProperty()

    def on_remove_file_click(self, path_list):
        info_layout = self.parent.parent
        path_txt = info_layout.children[1].text

        if path_txt in path_list:
            path_list.remove(path_txt)
        info_layout.parent.remove_widget(info_layout)


class AddFile(BoxLayout):
    stack_files = ObjectProperty()


class AddMoreFileButton(Button):
    def on_add_more_file_click(self):
        if len(self.parent.parent.stack_files.children) <= 4:
            b = InfoButton()
            rmb = RemoveFileButton()
            b.children[0].add_widget(rmb)
            self.parent.parent.stack_files.add_widget(b)
        else:
            popup = Popup(title='ERROR: Max files reached',
                          content=Label(text='You cannot add more than 5 files to execute \n simultaneously!',
                                        halign="center"),
                          size_hint=(None, None), size=(400, 150),
                          separator_color=(1, 1, 1, 1))
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
                          size_hint=(None, None), size=(400, 150),
                          separator_color=(1, 1, 1, 1))
            popup.open()
            return

        if self.path_str != "":
            for i in range(len(paths_list)):
                if self.path_str == paths_list[i]:
                    paths_list.pop(i)
                    break

        paths_list.append(path[0])
        self.path_str = str(path[0])
