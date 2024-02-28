# -*- coding: utf-8 -*-

"""
    Модуль с функциями проверки вводимых значений
"""

def checking_number(string):
    """
    Функция для проверки вводимого пользователем значения на 
    целое положительное число
    Входные параметры:
        строка
    Выходные параметры:
        True/False
    """
    return str.isdecimal(str(string))


def checking_positive(string):
    """
    Функция для проверки вводимого пользователем значения на 
    положительное число
    Входные параметры:
        строка
    Выходные параметры:
        True/False
    """
    try:
        n=int(string)
        if(n>0):
            return True
        else:
            return False
    except ValueError:
        return False

def checking_string(string):
    """
    Функция для проверки вводимого пользователем значения на строку
    только из символов
    Входные параметры:
        строка
    Выходные параметры:
        True/False
    """
    if (not string.isalpha()):
        return False
    else:
        return True

def checking_empty_string(string):
    """
    Функция для проверки вводимого пользователем значения на 
    непустую строку
    Входные параметры:
        строка
    Выходные параметры:
        True/False
    """
    if all(x.isspace() for x in string):
        return False
    else:
        return True

def checking_conditions(n,lim1=1000000,lim2=0):
    """
    Функция для проверки числа на ограничения
    Входные параметры:
        число
        число огр. сверху
        число огр. снизу
    Выходные параметры:
        True/False
    """
    if(n<=lim1 and n>=lim2):
        return True
    else:
        return False
    
    