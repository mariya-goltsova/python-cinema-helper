# -*- coding: utf-8 -*-

"""
Модуль с функциями для работы с файлами
"""
import pickle

def filename(path,name):
    """
    Функция для создания названия файла с полным путем
    Входные параметры:
        строка - название файла
        строка - путь
    Выходные параметры:
        строка - путь + название файла
    """
    path_name=path+'\\'+name
    return path_name

def save_table(path_name,typ,table):
    """
    Функция для сохранения файла
    Входные параметры:
        строка - путь + название файла
        тип файла - excel/pickle
        таблица
    Выходные параметры:
        True/False
    """
    try:
        if(typ=='excel' or typ=='base'):
            table.to_excel(path_name, index=False)
        elif(typ=='pickle') :
            with open(path_name, 'wb') as f:
                pickle.dump(table, f)
        return True
    except PermissionError:
        return False
                    

