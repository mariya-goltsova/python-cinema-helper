# -*- coding: utf-8 -*-
"""
Модуль с функцией сохранения фигуры matplotlib
"""

import matplotlib.pyplot as plt
import files

def save(figure,path,name):
    """
    Функция сохранения графика в файл
    Входные параметры:
        Фигура
        Название файла
        Путь
        Формат
    Выходные параметры:
        -
    """
    figure.savefig(files.filename(path,name))
