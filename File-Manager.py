# Coding: utf-8
# python 3.8.3

from colorama import init, Fore, Back, Style
from send2trash import send2trash
import os
import os.path as osp
import shutil
init()


def All_DIR():
    print(Fore.LIGHTCYAN_EX)
    files = os.listdir()
    num = len(files)
    for file in range(num):
        if osp.isdir(files[file]) == True:
            print(files[file])


def ALL_FILE():
    print(Fore.LIGHTCYAN_EX)
    files = os.listdir()
    num = len(files)
    for file in range(num):
        if osp.isfile(files[file]) == True:
            print(files[file])


def walking(walkChoose, dirNAME):
    print(Fore.LIGHTGREEN_EX)
    walk = int(input(walkChoose))
    if walk == 1:
        os.chdir('..')
        path = os.getcwdb()
    elif walk == 2:
        All_DIR()
        print(Fore.LIGHTMAGENTA_EX)
        directory = input(dirNAME)
        os.chdir(directory)
        path = os.getcwdb()


start = True

print(Fore.LIGHTYELLOW_EX)
lang = int(input(
    'Welcome to File-Manager.\nVersion 0.1.0\nChoose language:\n1)English\n2)Russian Language\n'))

if lang == 1:
    func = '1) Browse directory \n2) Move to another directory \n3) Copy file \n4) Move file \n5) Delete file \n6) Close \n'
    view = '1) Show all files \n2) Show only directories \n3) Show only files \n'
    replacer = 'Which file to copy: '
    replacers = 'Which file to transfer: '
    dirYN = 'Do you want to transfer the file to this directory? (Y / n)'
    delF = 'Which file to delete: '
    delfilt = '1) Delete file permanently \n2) Send file to trash \n'
    walkChoose = '1) Move to previous directory \n2) Move to next directory \n'
    dirNAME = 'Enter directory name: '
    copyOK = 'Copying was successful'
    moveOK = 'The move went well'
elif lang == 2:
    func = '1)Просмотр директории\n2)Перемещение в другую директорию\n3)Копирование файла\n4)Перемещение файла\n5)Удаление файла\n6)Закрыть\n'
    view = '1)Показать все файлы\n2)Показать только директории\n3)Показать только файлы\n'
    replacer = 'Какой файл нужно скопировать: '
    replacers = 'Какой файл нужно перенести: '
    dirYN = 'В эту директорию надо перенести файл?(y/n) '
    delF = 'Какой файл удалить: '
    delfilt = '1)Файл удалить навсегда\n2)Файл отправить в корзину\n'
    walkChoose = '1)Перемещение в предыдущую директорию\n2)Перемещение в следующую директорию\n'
    dirNAME = 'Введите название директории: '
    copyOK = 'Копирование прошло удачно'
    moveOK = 'Перемещение прошло удачно'
else:
    print(Fore.LIGHTRED_EX)
    print('ERROR')

path = os.getcwdb()

while start == True:

    print(Fore.LIGHTGREEN_EX)
    function = int(input(func))
    if function == 1:
        view_filters = int(input(view))
        if view_filters == 1:
            All_DIR()
            ALL_FILE()
        elif view_filters == 2:
            All_DIR()
        elif view_filters == 3:
            ALL_FILE()
        else:
            print(Fore.LIGHTRED_EX)
            print('ERROR')
    elif function == 2:
        walking(walkChoose, dirNAME)
    elif function == 3:
        ALL_FILE()
        replace = 'n'
        replace_file = input(replacer)
        replace_path = osp.abspath(replace_file)
        while replace == 'n':
            walking(walkChoose, dirNAME)
            replace = input(dirYN)
        temp_path = os.getcwd()
        shutil.copy(replace_path, temp_path)
        print(Fore.LIGHTMAGENTA_EX)
        print(copyOK)
    elif function == 4:
        ALL_FILE()
        replace = 'n'
        replace_file = input(replacers)
        replace_path = osp.abspath(replace_file)
        while replace == 'n':
            walking(walkChoose, dirNAME)
            replace = input(dirYN)
        temp_path = os.getcwd()
        shutil.move(replace_path, temp_path)
        print(moveOK)
    elif function == 5:
        ALL_FILE()
        print(Fore.LIGHTGREEN_EX)
        del_file = input(delF)
        print(Fore.LIGHTCYAN_EX)
        del_filters = int(input(delfilt))
        if del_filters == 1:
            os.remove(del_file)
        elif del_filters == 2:
            send2trash(del_file)
    elif function == 6:
        start = False
    else:
        print(Fore.LIGHTRED_EX)
        print('ERROR')
