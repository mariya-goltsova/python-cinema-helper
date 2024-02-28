# -*- coding: utf-8 -*-
# *****создание отчетов******
import numpy as np
import pandas as pd

# *****создание отчетов******

# **Простые текстовые отчеты**
def simple_family(Base,age='Нет',genre='Нет',k='Нет'):
    '''
    функция создания простого текстового отчета Семейный
    Parameters
    ----------
    Base : TYPE
        DESCRIPTION.
    age : TYPE, optional
        DESCRIPTION. The default is 'Нет'.
    genre : TYPE, optional
        DESCRIPTION. The default is 'Нет'.
    k : TYPE, optional
        DESCRIPTION. The default is 'Нет'.

    Returns
    -------
    TYPE
        DESCRIPTION.
    False - если таблица пуста
    таблицу - если есть хотя бы одна строчка с данными

    '''
    if(age != 'Нет'):
        Base=Base[Base['Возрастная категория']==age]
    if(genre != 'Нет'):
        Base=Base[(Base['Жанр 1']==genre) | (Base['Жанр 2']==genre) | (Base['Жанр 3']==genre)]
    if(k!='Нет'):
        Base=Base[Base['Категория']==k]
    Base=Base[['Название','Длительность, мин',
                                'Компания','Название платформы']]
    if(Base.shape[0]==0):
        return False
    else:
        return Base

def simple_tsen(Base,kol='Нет',fees='Нет',r='Нет'):
    '''
    функция создания простого текстового отчета Ценителям

    Parameters
    ----------
    Base : TYPE
        DESCRIPTION.
    kol : TYPE, optional
        DESCRIPTION. The default is 'Нет'.
    fees : TYPE, optional
        DESCRIPTION. The default is 'Нет'.
    r : TYPE, optional
        DESCRIPTION. The default is 'Нет'.

    Returns
    -------
    TYPE
        DESCRIPTION.
        False - если таблица пуста
        таблицу - если есть хотя бы одна строчка с данными

    '''
    if(kol != 'Нет'):
        Base=Base[Base['Количество премий']>=kol]
    if(fees != 'Нет'):
        Base=Base[Base['Сборы , млн']>=fees]
    if(r!='Нет'):
        Base=Base[Base['Рейтинг']>=r]
    Base=Base[['Название','Название платформы','Качество']]
    if(Base.shape[0]==0):
        return False
    else:
        return Base

def simple_language(Base,sub='Нет',voice='Нет',orig='Нет'):
    '''

    функция создания простого текстового отчета Изучение языков
    Parameters
    ----------
    Base : TYPE
        DESCRIPTION.
    sub : TYPE, optional
        DESCRIPTION. The default is 'Нет'.
    voice : TYPE, optional
        DESCRIPTION. The default is 'Нет'.
    orig : TYPE, optional
        DESCRIPTION. The default is 'Нет'.

    Returns
    -------
    TYPE
        DESCRIPTION.
    False - если таблица пуста
    таблицу - если есть хотя бы одна строчка с данными
    '''
    if(sub !='Нет'):
        Base=Base[Base['язык субтитров']==sub]
    if(voice !='Нет'):
        Base=Base[Base['язык иностранной озвучки']==voice]
    if(orig !='Нет'):
        Base=Base[Base['Оригинал дорожки']==orig]
    Base=Base[['Название','Категория','Жанр 1','Жанр 2','Жанр 3',
               'Название платформы']]
    if(Base.shape[0]==0):
        return False
    else:
        return Base

def simple_anyone(Base,genre='Нет',country='Нет',year1='Нет', year2='Нет'):
    '''
    функция создания простого текстового отчета Базовый(романтик/весельчак)
    Parameters
    ----------
    Base : TYPE
        DESCRIPTION.
    genre : TYPE, optional
        DESCRIPTION. The default is 'Нет'.
    country : TYPE, optional
        DESCRIPTION. The default is 'Нет'.
    year : TYPE, optional
        DESCRIPTION. The default is 'Нет'.

    Returns
    -------
    TYPE
        DESCRIPTION.
    False - если таблица пуста
    таблицу - если есть хотя бы одна строчка с данными
    '''
    if(genre != 'Нет'):
        Base=Base[(Base['Жанр 1']==genre) | (Base['Жанр 2']==genre) | (Base['Жанр 3']==genre)]
    if(country !='Нет'):
        Base=Base[Base['Страна']==country]
    if((year1 !='Нет') and (year2 !='Нет')):
        Base=Base[(Base['Год']>=year1) & (Base['Год']<=year2)]
    Base=Base[['Название','Рейтинг','Название платформы','Компания']]
    if(Base.shape[0]==0):
        return False
    else:
        return Base

# **Статистические отчеты**

def statistics_reports(types,Basa0,Basa,var):
    """

    Parameters
    ----------
    types : TYPE
        DESCRIPTION.
    Basa0 : TYPE     - база без повторений фильмов
        DESCRIPTION.
    Basa : TYPE        - вся БД
        DESCRIPTION.
    var : TYPE        - переменная для отчета качественной переменной
        DESCRIPTION.

    Returns
    -------
    report : TYPE
        DESCRIPTION.

    """
    if(types=='kol'):
        Stat = {'Переменные':
                ['Год', 'Рейтинг', 'Возрастная категория', 'Длительность',
                'Количество премий','Сборы'],
                'Максимум': [max(Basa0['Год']),max(Basa0['Рейтинг']),
                             max(Basa0['Возрастная категория']),
                             max(Basa0['Длительность, мин']),
                             max(Basa0['Количество премий']),max(Basa0['Сборы , млн'])],
                'Минимум': [min(Basa0['Год']),min(Basa0['Рейтинг']),
                             min(Basa0['Возрастная категория']),
                             min(Basa0['Длительность, мин']),
                             min(Basa0['Количество премий']),min(Basa0['Сборы , млн'])],
                'Среднее значение': [np.mean(Basa0['Год']),np.mean(Basa0['Рейтинг']),
                             np.mean(Basa0['Возрастная категория']),
                             np.mean(Basa0['Длительность, мин']),
                             np.mean(Basa0['Количество премий']),np.mean(Basa0['Сборы , млн'])],
                'Дисперсия': [np.var(Basa0['Год']),np.var(Basa0['Рейтинг']),
                             np.var(Basa0['Возрастная категория']),
                             np.var(Basa0['Длительность, мин']),
                             np.var(Basa0['Количество премий']),np.var(Basa0['Сборы , млн'])],
                'Стандартное отклонение': [np.std(Basa0['Год']),np.std(Basa0['Рейтинг']),
                             np.std(Basa0['Возрастная категория']),
                             np.std(Basa0['Длительность, мин']),
                             np.std(Basa0['Количество премий']),np.std(Basa0['Сборы , млн'])]}
    elif((var=='Название платформы') or (var=='язык субтитров')):
        Z1=Basa[var]
        Z1=list(Z1)
        Z_no_rep=set(Z1)
        b = [Z1.count(el) for el in Z_no_rep]
        Z_no_rep = list(Z_no_rep)
        proc = [b[i]*100/sum(b) for i in range(len(b))]
        Stat={'Значения': Z_no_rep,
              'Частота': b,
              'Процент': proc}
    elif(var=='Жанр'):
        x3 = Basa0['Жанр 1']
        u3 = list(x3)
        x1=Basa0['Жанр 2']
        x2=Basa0['Жанр 3']
        u1 = list(x2)
        u2 = list(x1)
        x=list(u3+u1+u2)
        x = [z.strip(' ') for z in x]
        x_no_rep=list(set(x))
        x_no_rep = [z.strip(' ') for z in x_no_rep]
        b = [x.count(el) for el in x_no_rep]
        x_no_rep = list(x_no_rep)
        proc = [b[i]*100/sum(b) for i in range(len(b))]
        Stat={'Значения': x_no_rep,
              'Частота': b,
              'Процент': proc}
    else:
        Z1=Basa0[var]
        Z1=list(Z1)
        Z_no_rep=set(Z1)
        b = [Z1.count(el) for el in Z_no_rep]
        Z_no_rep = list(Z_no_rep)
        proc = [b[i]*100/sum(b) for i in range(len(b))]
        Stat={'Значения': Z_no_rep,
              'Частота': b,
              'Процент': proc}
    re=pd.DataFrame(Stat)
    return re
# **Сводные таблицы**

def sv_table(Base,k1,k2,k3,agg):
    '''

    Parameters
    ----------
    Base : TYPE      - БД
        DESCRIPTION.
    k1 : TYPE        - качественный атрибут
        DESCRIPTION.
    k2 : TYPE        - качественный атрибут
        DESCRIPTION.
    k3 : TYPE       - количественный атрибут
        DESCRIPTION.
    agg : TYPE     - метод агрегации
        DESCRIPTION.

    Returns
    -------
    Svvv : TYPE      - сводная таблица
        DESCRIPTION.

    '''
    Svvv=pd.pivot_table(Base,index=k1, columns=k2,values=k3,aggfunc=agg)
    return Svvv
