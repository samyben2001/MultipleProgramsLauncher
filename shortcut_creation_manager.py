import os

from kivy.properties import StringProperty
from pyshortcuts import make_shortcut


class ShortcutCreationManager:

    def __init__(self):
        self.base_path = os.getcwd()
        self.bat_name = 0  #numbers of files already in directory
        for base, dirs, files in os.walk(self.base_path+"/bats"):
            print('Searching in : ', base)
            for Files in files:
                self.bat_name += 1
        self.bat_name = str(self.bat_name)

    def create_shortcut(self, file_paths, icon_src, shorcut_name=""):
        if icon_src == "Images\link.ico":
            icon_src = f"{self.base_path}\\{icon_src}"

        file_dict = self.create_dict_with_path_and_exe(file_paths)
        self.fill_and_create_bat_file_for_shortcut(file_dict)
        if not shorcut_name:
            shortcut_name = file_dict["file0"]["filename"].rpartition(".")[0].replace(" ", "")
        a = make_shortcut(f"{self.base_path}\\bats\\{shortcut_name}.bat", name=shortcut_name, icon=icon_src)
        print(a)
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
            txt += f'\ncd \"{file_info["path"]}\"' \
                   f'\nstart {file_info["filename"]}'

        bat_file = open(f"{self.base_path}\\bats\\{self.bat_name}.bat", "w")
        bat_file.write(txt)
        bat_file.close()


