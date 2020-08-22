# Coding: utf-8
# python 3.8

from colorama import init, Fore, Back, Style
from send2trash import send2trash
import os
import os.path
import shutil
init()

# This function lists all files and directories.


def All_info(thispath):
    Fpath = os.getcwd()
    files = os.listdir()
    print(Fore.LIGHTMAGENTA_EX)
    print(f'{thispath} {Fpath}')
    i = len(files)
    for file in range(i):
        if os.path.isdir(files[file]) == True:
            print(files[file])
    print('')
    for file in range(i):
        if os.path.isfile(files[file]) == True:
            print(files[file])

# This function lists all directories.


def All_dir(thispath):
    Fpath = os.getcwd()
    files = os.listdir()
    print(Fore.LIGHTMAGENTA_EX)
    print(f'{thispath} {Fpath}')
    i = len(files)
    for file in range(i):
        if os.path.isdir(files[file]) == True:
            print(files[file])

# This function lists all files.


def All_files(thispath):
    Fpath = os.getcwd()
    files = os.listdir()
    print(Fore.LIGHTMAGENTA_EX)
    print(f'{thispath} {Fpath}')
    i = len(files)
    for file in range(i):
        if os.path.isfile(files[file]) == True:
            print(files[file])

# This function allows switching between directories.


def Jump(thispath, Jump_func_text, Directory_text):
    print(Fore.LIGHTYELLOW_EX)
    Jump_func = int(input(Jump_func_text))
    if Jump_func == 1:
        os.chdir('..')
        Fpath = os.getcwd()
        print(Fore.LIGHTMAGENTA_EX)
        print(f'{thispath} {Fpath}')
    if Jump_func == 2:
        All_dir(thispath)
        print(Fore.LIGHTGREEN_EX)
        Directory = input(Directory_text)
        os.chdir(Directory)
        Fpath = os.getcwd()
        print(Fore.LIGHTMAGENTA_EX)
        print(f'{thispath} {Fpath}')

# Language selection.


print(Fore.LIGHTYELLOW_EX)
lang = int(input('Choose Language:\n1)English\n2)Russian Language\n'))

# English

if lang == 1:
    from Lang_en import *

# Russian language

elif lang == 2:
    from Lang_ru import *

# Error notification

else:
    print(Fore.LIGHTRED_EX)
    print('Error: This language does not exist.')

start = True

while start == True:
    print(Fore.LIGHTGREEN_EX)
    function = int(input(function_text))

    try:
        # The part that is responsible for outputting information about what files and directories are in this directory.

        if function == 1:
            All_info(thispath)

        # This part is responsible for switching between directories.

        elif function == 2:
            Jump(thispath, Jump_func_text, Directory_text)

        # The part that is responsible for copying.
            # Selecting a function in copying.

        elif function == 3:
            print(Fore.LIGHTYELLOW_EX)
            Copy_func = int(input(Copy_func_text))

            # The part that is responsible for copying files.

            if Copy_func == 1:
                All_files(thispath)
                print(Fore.LIGHTCYAN_EX)
                file = input(file_text)
                path = os.getcwd()
                CaMO = 'n'
                while CaMO == 'n':
                    Jump(thispath, Jump_func_text, Directory_text)
                    print(Fore.LIGHTGREEN_EX)
                    CaMO = input(CaMO_text)
                    CaMO = CaMO.lower()
                    path_to = os.getcwd()
                shutil.copy(f'{path}\\{file}', f'{path_to}\\{file}')

            # The part that is responsible for copying directories.

            elif Copy_func == 2:
                All_dir(thispath)
                print(Fore.LIGHTCYAN_EX)
                file = input(Directory_text)
                path = os.getcwd()
                CaMO = 'n'
                while CaMO == 'n':
                    Jump(thispath, Jump_func_text, Directory_text)
                    print(Fore.LIGHTGREEN_EX)
                    CaMO = input(CaMO_text)
                    CaMO = CaMO.lower()
                    path_to = os.getcwd()
                shutil.copytree(f'{path}\\{file}', f'{path_to}\\{file}')

            # Error notification.

            else:
                print(Fore.LIGHTRED_EX)
                print('Error: This function is missing.')

        # This part is responsible for moving files and directories.
            # Selecting a function in moving.

        elif function == 4:
            print(Fore.LIGHTYELLOW_EX)
            Move_func = int(input(Move_func_text))

            # This part is responsible for moving files.

            if Move_func == 1:
                All_files(thispath)
                print(Fore.LIGHTCYAN_EX)
                file = input(file_text)
                path = os.getcwd()
                CaMO = 'n'
                while CaMO == 'n':
                    Jump(thispath, Jump_func_text, Directory_text)
                    print(Fore.LIGHTGREEN_EX)
                    CaMO = input(CaMO_text2)
                    CaMO = CaMO.lower()
                    path_to = os.getcwd()
                shutil.move(f'{path}\\{file}', f'{path_to}\\{file}')

            # This part is responsible for moving directories.

            elif Move_func == 2:
                All_dir(thispath)
                print(Fore.LIGHTCYAN_EX)
                file = input(Directory_text)
                path = os.getcwd()
                CaMO = 'n'
                while CaMO == 'n':
                    Jump(thispath, Jump_func_text, Directory_text)
                    print(Fore.LIGHTGREEN_EX)
                    CaMO = input(CaMO_text2)
                    CaMO = CaMO.lower()
                    path_to = os.getcwd()
                shutil.move(f'{path}\\{file}', f'{path_to}\\{file}')

            # Error notification.

            else:
                print(Fore.LIGHTRED_EX)
                print('Error: This function is missing.')

        # This part is responsible for renaming.

        elif function == 5:
            path = os.getcwd()
            All_files(thispath)
            print(Fore.LIGHTCYAN_EX)
            file = input(file_text)
            name = input(name_text)
            shutil.move(f'{path}\\{file}', f'{path}\\{name}')

        # This part is responsible for removing files and directories.

        elif function == 6:

            # Function selection: Delete file or delete directory.

            print(Fore.LIGHTYELLOW_EX)
            Remove_func = int(input(Remove_func_text))

            # Deleting a file.

            if Remove_func == 1:

                # Function selection: Delete the file permanently or send it to the trash.
                # REmoving FIle

                print(Fore.LIGHTGREEN_EX)
                REFI_func = int(input(REFI_func_text))

                # Deleting the file permanently.

                if REFI_func == 1:
                    path = os.getcwd()
                    All_files(thispath)
                    print(Fore.LIGHTCYAN_EX)
                    file = input(file_text)
                    os.remove(f'{path}\\{file}')

                # Sending a file to the trash.

                elif REFI_func == 2:
                    path = os.getcwd()
                    All_files(thispath)
                    print(Fore.LIGHTYELLOW_EX)
                    file = input(file_text)
                    send2trash(f'{path}\\{file}')

                # Error notification.

                else:
                    print(Fore.LIGHTRED_EX)
                    print('Error: This function is missing.')

            # Removing directories.

            elif Remove_func == 2:

                # Function selection: Delete the directory permanently or send it to the trash.
                # REDIR - REmove DIRectory

                print(Fore.LIGHTGREEN_EX)
                REDIR_func = int(input(REDIR_func_text))

                # Removing the directory permanently.

                if REDIR_func == 1:
                    path = os.getcwd()
                    All_files(thispath)
                    print(Fore.LIGHTCYAN_EX)
                    file = input(Directory_text)
                    shutil.rmtre(f'{path}\\{file}')

                # Sending directory to trash.

                elif REDIR_func == 2:
                    path = os.getcwd()
                    All_files(thispath)
                    print(Fore.LIGHTCYAN_EX)
                    file = input(Directory_text)
                    send2trash(f'{path}\\{file}')

                # Error notification.

                else:
                    print(Fore.LIGHTRED_EX)
                    print('Error: This function is missing.')

        # The part responsible for closing the program.

        elif function == 7:
            print(Fore.RESET)
            start = False

        # Error notification.

        else:
            print(Fore.LIGHTRED_EX)
            print('Error: This function is missing.')

    except FileNotFoundError:
        print(Fore.LIGHTRED_EX)
        print('Error: The file or directory does not exist.')
    except:
        print(Fore.LIGHTRED_EX)
        print('ERROR')
