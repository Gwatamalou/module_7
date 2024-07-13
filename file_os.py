import os
import time

directory = os.getcwd()
for root, dirs, files in os.walk(directory):
    # для dirs нужно бы ещё один цикл, но я делаю без вложенных паппок поэтому так
    for file in files:
        filepath = os.path.join(root, file)
        filetime = time.ctime(os.path.getmtime(file))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(filepath)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {filetime},'
            f' Родительская директория: {parent_dir}')
