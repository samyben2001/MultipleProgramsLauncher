from kivy.app import App
from kivy.uix.widget import Widget
from pyshortcuts import make_shortcut


class MainWidget(Widget):
    pass


class MultipleProgramsLauncherApp(App):
    pass


def fill_and_create_bat_file_for_shortcut(files_list, path_to_save, filename):
    txt = "@echo off"
    for file, file_info in files_list.items():
        txt += f'\ncd \"{file_info["path"]}\"' \
                   f'\nstart {file_info["exe"]}'

    bat_file = open(f"{path_to_save}\\{filename}.bat", "w")
    bat_file.write(txt)
    bat_file.close()


MultipleProgramsLauncherApp().run()

'''
bat_directory = "bats"

files = {}

file1_path = r"C:\Program Files (x86)\Battle.net"
file2_path = r"C:\Users\samyb\AppData\Local\HearthstoneDeckTracker"
file1_exe = "Battle.net Launcher.exe"
file2_exe = "HearthstoneDeckTracker.exe"
icon_src = r"C:\Users\samyb\Documents\.Projects\Personnels\MultipleProgramsLauncher\shortcuts.ico"

filename = file1_exe.rpartition(".")[0].replace(" ", "")

files["file1"] = {"path": file1_path, "exe": file1_exe}
files["file2"] = {"path": file2_path, "exe": file2_exe}

# Create and fill .BAT content
fill_and_create_bat_file_for_shortcut(files, bat_directory, filename)

target = rf'C:\Users\samyb\Documents\.Projects\Personnels\MultipleProgramsLauncher\{bat_directory}\{filename}.bat'

# Create shortcut
make_shortcut(target, name=filename, icon=icon_src)
'''