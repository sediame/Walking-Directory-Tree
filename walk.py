import os
from pathlib import Path


if __name__ == '__main__':
    home = str(Path.home())
    for folder_name, sub_folders, file_names in os.walk(home + '/delicious'):
        print('THe current folder is' + folder_name)

        for sub_folder in sub_folders:
            print('sub folder of ' + folder_name + ': ' + sub_folder)

        for file_name in file_names:
            print('file inside ' + folder_name + ': ' + file_name)
    print('')
