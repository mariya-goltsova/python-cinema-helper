# -*- coding: utf-8 -*-

import tkinter as tki
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog,StringVar,Entry
from tkinter import messagebox as mb
import os
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
import pandas as pd
import pickle
from PIL import ImageTk, Image
from setting import font, color_back,color,color_text,types_data, types_file, base_path, work, text
import text_reports
import files
import checking
#функция закрытия главного окна
def mainw_d():
    mainw.destroy()
def browse_button():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
fontExample = (font,15)
'''работа с бд'''
def created(types__data):
    '''
    Автор: Шилова С.

    Parameters
    ----------
    types__data : TYPE
        DESCRIPTION.

    Returns
    -------
    Bas : TYPE
        DESCRIPTION.

    '''
    if(types__data=='excel'):
    #открытие справочников
        files0=os.listdir(base_path)
        file1=pd.read_excel(base_path+'\\'+files0[0])
        file2=pd.read_excel(base_path+'\\'+files0[1])
        Bas=file1.merge(file2)
        for file in files0[2::]:
            table=pd.read_excel(base_path+'\\'+file)
            Bas=Bas.merge(table)
    elif(types__data=='pickle'):
        with open(base_path+'\\data.pickle', 'rb') as f:
            Bas = pickle.load(f)
    else:
        Bas=pd.read_excel(base_path+'\\base.xlsx')
    #Индексы и изначальная сортировка по номеру фильма
    Bas=Bas.sort_values('№ фильма')
    indexx=np.arange(0, len(Bas))
    Bas=Bas.set_index([pd.Index(indexx)])
    return Bas
global Basa
Basa=created(types_data)
def f():
    '''
    Автор: Бригада №4

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    global Basa
    Basa_no_rep = Basa.drop_duplicates('Название')
    index=np.arange(0, len(Basa_no_rep ))
    Basa_no_rep =Basa_no_rep .set_index([pd.Index(index)])
    #Отбор столбцов для главной страницы
    #жанры
    x3 = Basa['Жанр 1']
    unique_numbers = list(x3)
    x1=Basa['Жанр 2']
    x2=Basa['Жанр 3']
    unique_numbers1 = list(x2)
    unique_numbers2 = list(x1)
    global x,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17
    x=list(set(unique_numbers+unique_numbers1+unique_numbers2))
    x = [z.strip(' ') for z in x]
    x=list(set(x))
    #страны
    x4 = Basa['Страна']
    x4 = list(set(x4))
    #возраст
    x5 = Basa['Возрастная категория']
    x5 = list(set(x5))
    #год
    x6 = ['До 1970-х', '1970-е', '1980-е', '1990-е', '2000-е', '2010-е', '2020-е']
    #Платформа
    x7 = Basa['Название платформы']
    x7 = list(set(x7))
    #субтитры
    x8 = Basa['язык субтитров']
    x8 = list(set(x8))
    #рейтинг
    x9 = ['от 6 до 7', 'от 7 до 8', 'от 8 до 9', 'от 9 до 10']
    #Длительность
    x10 = ['>3 часов ', '2-3 часа ', '1.5-2 часа ','1-1.5 часа ', '0.5-1 час ', 'до 30 минут ']
    #качество
    x11 = Basa['Качество']
    x11 = list(set(x11))
    #Режиссер
    x12 = Basa['Режиссёр ']
    x12 = list(set(x12))
    #Компания
    x13 = Basa['Компания']
    x13 = list(set(x13))
    #Сборы
    x14 = ['<100 млн','100-400 млн','400-600 млн','600-900 млн','900-1000 млн',
           '1-2 млрд','>2 млрд']
    #Количество премий
    x15 = ['0-10', '10-20', '20-30','30-40', '40-50', 'более 50']
    #Категория
    x16 = Basa['Категория']
    x16 = list(set(x16))
    #Язык иностранной озвучки
    x17 = Basa['язык иностранной озвучки']
    x17 = list(set(x17))
    #Функции создания окон
    def open_main():
        '''
        Автор: Гольцова М.
        Создание главного окна

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        main=tki.Tk()
        main.title('Главная страница')
        main.geometry('1000x600+10+10')
        main.iconbitmap('application.ico')
        mainmenu = Menu(main)
        main.config(menu=mainmenu)
        main.resizable(width=False, height= False)
        mainmenu.add_command(label='Изменить БД', command=lambda:[main.destroy(), open_bd()])
        mainmenu.add_command(label='Отчеты', command=lambda:[main.destroy(), open_reports()])
        mainmenu.add_command(label='Подборки', command=lambda:[main.destroy(), open_selections()])
        mainmenu.add_command(label='Настройки', command=lambda:[main.destroy(), open_settings()])
        main["bg"] = color_back
        main.image = PhotoImage(file='hlop.png')
        bg_logo = Label(main, image=main.image)
        bg_logo.place(x=115, y=200)
        lbl = tki.Label(main, text="Жанр:", font=fontExample, fg=color_text, bg=color_back)
        lbl.place(x=85, y=47)
        lbl = tki.Label(main, text="Качество:", font=fontExample, fg=color_text, bg=color_back)
        lbl.place(x=220, y=47)
        lbl = tki.Label(main, text="Страна:", font=fontExample, fg=color_text, bg=color_back)
        lbl.place(x=365, y=47)
        lbl = tki.Label(main, text="Качество:", font=fontExample, fg=color_text, bg=color_back)
        lbl = tki.Label(main, text="Выберите критерии отбора:", borderwidth=2, relief="sunken",
                        fg=color_text, bg=color,font=(font,18,'bold', 'underline'))
        lbl.place(x=80, y=0)
        def selectedCat(Base):
            '''
            Автор: Гольцова М.

            Returns
            -------
            TYPE
                DESCRIPTION.

            '''
            if(cbGenre.get() != 'Нет'):
                Base=Base[(Base['Жанр 1']==cbGenre.get()) | (Base['Жанр 2']==cbGenre.get())
                          | (Base['Жанр 3']==cbGenre.get())]
            if (cbCountry.get() != 'Нет'):
                Base=Base[Base['Страна']==cbCountry.get()]
            if (cbQual.get()!='Нет'):
                Base=Base[Base['Качество']==cbQual.get()]
            if(Base.shape[0]==0):
                return False
            else:
                return Base
        global x,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17
        cbGenre=ttk.Combobox(values=x,state="readonly",width=17, exportselection=0)
        cbGenre.place(x=85, y=75, width=100, height=70)
        cbCountry=ttk.Combobox(values=x4,state="readonly",width=17, exportselection=0)
        cbCountry.place(x=365, y=75, width=100, height=70)
        cbQual=ttk.Combobox(values=x11,state="readonly",width=17, exportselection=0)
        cbQual.place(x=225, y=75, width=100, height=70)
        def podb(tex, op):
            '''
            Автор: Гольцова М.

            Parameters
            ----------
            tex : TYPE
                DESCRIPTION.
            op : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            n = tki.Tk()
            n.title(tex)
            n["bg"] = color_back
            n.geometry('1000x700+10+10')
            n.iconbitmap('application.ico')
            if (not (op.empty)):
                frame1 = tki.LabelFrame(n, text="Подборка")
                frame1.place(x=10,y=10,height=400, width=970)
                name=tki.StringVar()
                name1=tki.Entry(n, textvariable=name)
                name1.place(x=400, y=530, height=70, width=300)
                nnn = tki.Label(n, text="Введите название файла для сохранения", font=(font, 16),
                                fg=color_text, bg=color_back)
                nnn.place(x=380, y=520)
                def saving():
                    ''''
                    Автор: Гольцова М.

                    Returns
                    -------
                    None.

                    '''
                    if (name1.get()==("")):
                        mb.showerror("Ошибка", "Вы не ввели название файла!")
                    else:
                        path_name = files.filename(text, (name1.get()+'.xlsx'))
                        files.save_table(path_name, 'excel', op)
                    n.destroy()
                btns = tki.Button(n, text="Сохранить отчет", font=(font, 14),
                                  fg=color_text, bg=color, command=saving)
                btns.place(x=100, y=500, height=100, width=200)
                tv1 = ttk.Treeview(frame1)
                tv1.place(relheight=1, relwidth=1)
                treescrolly = tki.Scrollbar(frame1, orient="vertical", command=tv1.yview)
                treescrollx = tki.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
                tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
                treescrollx.pack(side="bottom", fill="x")
                treescrolly.pack(side="right", fill="y")
                tv1["column"] = list(op.columns)
                tv1["show"] = "headings"
                for column in tv1["columns"]:
                    tv1.heading(column, text=column)
                    df_rows = op.to_numpy().tolist()
                    for row in df_rows:
                        tv1.insert("", "end", values=row)
            elif (op==False):
                frame1 = tki.Label(n, text="Таких фильмов больше нет", font=(font, 16))
                frame1.place(x=40,y=80,height=500, width=920)
        but=tki.Button(main, text="Применить!",  fg=color_text, bg=color, padx="20",
                       pady="8", font="10", command=lambda:[podb("Подборка", selectedCat(Basa))])
        but.place(x=560, y=80)
    def open_reports():
        '''
        Автор: Жибуртович Е.

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        reports = tki.Tk()
        reports.title("Отчеты")
        reports.geometry('1420x600+0+100')
        reports.iconbitmap('application.ico')
        mainmenu = Menu(reports)
        reports.config(menu=mainmenu)

        mainmenu.add_command(label='На главную страницу', command=lambda:[reports.destroy(),
                                                                          open_main()])
        mainmenu.add_command(label='Изменить БД', command=lambda:[reports.destroy(),
                                                                  open_bd()])
        mainmenu.add_command(label='Подборки', command=lambda:[reports.destroy(),
                                                               open_selections()])
        mainmenu.add_command(label='Настройки', command=lambda:[reports.destroy(), open_settings()])
        reports["bg"] = color_back
        def reports_cach(b):
            '''
            Автор: Жибуртович Е. , Шилова С.

            Parameters
            ----------
            b : TYPE     - выбранная переменная
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            reports = tki.Tk()
            reports.title("Текстовый статистический отчет для качественных атрибутов")
            reports.geometry('1300x700+10+10')
            reports.iconbitmap('application.ico')
            reports["bg"] = color_back
            cach=text_reports.statistics_reports('s',Basa_no_rep,Basa,b)
            frame1 = tki.LabelFrame(reports, text="Статистический отчет")
            frame1.place(x=10,y=10,height=400, width=970)
            name=tki.StringVar()
            name1=tki.Entry(reports, textvariable=name)
            name1.place(x=400, y=530, height=70, width=300)
            nnn = tki.Label(reports, text="Введите название файла для сохранения", font=(font, 16),
                            fg=color_text, bg=color_back)
            nnn.place(x=380, y=520)
            def saving():
                '''
                Автор: Гольцова М.

                Returns
                -------
                None.

                '''
                if (name1.get()==("")):
                    mb.showerror("Ошибка", "Вы не ввели название файла!")
                else:
                    path_name = files.filename(text, (name1.get()+'.xlsx'))
                    files.save_table(path_name, 'excel', cach)
                reports.destroy()
            btns = tki.Button(reports, text="Сохранить отчет", font=(font, 14),
                                  fg=color_text, bg=color, command=saving)
            btns.place(x=100, y=500, height=100, width=200)
            tv1 = ttk.Treeview(frame1)
            tv1.place(relheight=1, relwidth=1)
            treescrolly = tki.Scrollbar(frame1, orient="vertical", command=tv1.yview)
            treescrollx = tki.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
            tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
            treescrollx.pack(side="bottom", fill="x")
            treescrolly.pack(side="right", fill="y")
            tv1["column"] = list(cach.columns)
            tv1["show"] = "headings"
            for column in tv1["columns"]:
                tv1.heading(column, text=column)
                df_rows = cach.to_numpy().tolist()
                for row in df_rows:
                    tv1.insert("", "end", values=row)
        def reports_col():
            '''
            Автор: Жибуртович Е. , Шилова С.

            Returns
            -------
            None.

            '''
            reports = tki.Tk()
            reports.title("Текстовый статистический отчет для количественных атрибутов")
            reports.geometry('1300x700+10+10')
            reports.iconbitmap('application.ico')
            reports["bg"] = color_back
            col=text_reports.statistics_reports('kol',Basa_no_rep,Basa,'z')
            frame1 = tki.LabelFrame(reports, text="Статистический отчет")
            frame1.place(x=10,y=10,height=400, width=970)
            name=tki.StringVar()
            name1=tki.Entry(reports, textvariable=name)
            name1.place(x=400, y=530, height=70, width=300)
            nnn = tki.Label(reports, text="Введите название файла для сохранения", font=(font, 16),
                            fg=color_text, bg=color_back)
            nnn.place(x=380, y=520)
            def saving():
                '''
                Автор: Гольцова М.

                Returns
                -------
                None.

                '''
                if (name1.get()==("")):
                    mb.showerror("Ошибка", "Вы не ввели название файла!")
                else:
                    path_name = files.filename(text, (name1.get()+'.xlsx'))
                    files.save_table(path_name, 'excel', col)
                reports.destroy()
            btns = tki.Button(reports, text="Сохранить отчет", font=(font, 14),
                                  fg=color_text, bg=color, command=saving)
            btns.place(x=100, y=500, height=100, width=200)
            tv1 = ttk.Treeview(frame1)
            tv1.place(relheight=1, relwidth=1)
            treescrolly = tki.Scrollbar(frame1, orient="vertical", command=tv1.yview)
            treescrollx = tki.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
            tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
            treescrollx.pack(side="bottom", fill="x")
            treescrolly.pack(side="right", fill="y")
            tv1["column"] = list(col.columns)
            tv1["show"] = "headings"
            for column in tv1["columns"]:
                tv1.heading(column, text=column)
                df_rows = col.to_numpy().tolist()
                for row in df_rows:
                    tv1.insert("", "end", values=row)
        def reports_sv(sv1,sv2,sv3,ag1):
            '''
            Автор: Жибуртович Е. , Шилова С.

            Parameters
            ----------
            sv1 : TYPE
                DESCRIPTION.
            sv2 : TYPE
                DESCRIPTION.
            sv3 : TYPE
                DESCRIPTION.
            ag1 : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            reports = tki.Tk()
            reports.title("Сводная таблица")
            reports.geometry('1300x600+10+10')
            reports.iconbitmap('application.ico')
            reports["bg"] = color_back
            if(ag1=='Среднее'):
                ag='mean'
            else:
                ag=np.sum
            sv=text_reports.sv_table(Basa,sv1,sv2,sv3,ag)
            sv=sv.rename_axis('index').reset_index()
            frame1 = tki.LabelFrame(reports, text="Сводная таблица")
            frame1.place(x=10,y=10,height=400, width=970)
            name=tki.StringVar()
            name1=tki.Entry(reports, textvariable=name)
            name1.place(x=400, y=530, height=70, width=300)
            nnn = tki.Label(reports, text="Введите название файла для сохранения", font=(font, 16),
                            fg=color_text, bg=color_back)
            nnn.place(x=380, y=520)
            def saving():
                '''
                Автор: Гольцова М.

                Returns
                -------
                None.

                '''
                if (name1.get()==("")):
                    mb.showerror("Ошибка", "Вы не ввели название файла!")
                else:
                    path_name = files.filename(text, (name1.get()+'.xlsx'))
                    files.save_table(path_name, 'excel', sv)
                reports.destroy()
            btns = tki.Button(reports, text="Сохранить отчет", font=(font, 14),
                                  fg=color_text, bg=color, command=saving)
            btns.place(x=100, y=500, height=100, width=200)
            tv1 = ttk.Treeview(frame1)
            tv1.place(relheight=1, relwidth=1)
            treescrolly = tki.Scrollbar(frame1, orient="vertical", command=tv1.yview)
            treescrollx = tki.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
            tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
            treescrollx.pack(side="bottom", fill="x")
            treescrolly.pack(side="right", fill="y")
            tv1["column"] = list(sv.columns)
            tv1["show"] = "headings"
            for column in tv1["columns"]:
                tv1.heading(column, text=column)
                df_rows = sv.to_numpy().tolist()
                for row in df_rows:
                    tv1.insert("", "end", values=row)
        def st_diag(event):
            '''
            Автор: Жибуртович Е., Гольцова М.
            Создание окна "Столбчатая диаграмма"

            Parameters
            ----------
            event : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            reports = tki.Tk()
            reports.title("Столбчатая диаграмма")
            reports.geometry('350x350+10+10')
            reports.iconbitmap('application.ico')
            reports["bg"] = color_back
            def open_windows():
                '''
                Автор: Жибуртович Е., Шилова С, Гольцова М.
                Наполнение окна "Столбчатая диаграмма"

                Returns
                -------
                None.

                '''
                if ((combo_x.get() != "Выберите параметр")and(combo_y.get()!= "Выберите параметр")):
                    reports1 = tki.Tk()
                    reports1.title("Гистограмма")
                    reports1.geometry('500x500+10+10')
                    reports1.iconbitmap('application.ico')
                    reports1["bg"] = color_back
                    #plot.box_vis(Basa_no_rep, combo_y.get(), combo_x.get())
                    fig = Figure(figsize = (5, 5), dpi = 100)
                    cach_gr=text_reports.statistics_reports('s',Basa_no_rep,Basa,combo_x.get())
                    if(combo_y.get()=='Количество'):
                        st_y=list(cach_gr['Частота'])
                    else:
                        st_y=list(cach_gr['Процент'])
                    st_x=list(cach_gr['Значения'])
                    plot1 = fig.add_subplot(111)
                    plot1.bar(st_x, st_y)
                    canvas = FigureCanvasTkAgg(fig,
                                               master = reports1)
                    canvas.draw()
                    canvas.get_tk_widget().pack()
                    toolbar = NavigationToolbar2Tk(canvas,
                                                   reports1)
                    toolbar.pack()
                    canvas.get_tk_widget().pack()
            lbl=tki.Label(reports,text="       ",font=(font,18), fg=color_text, bg=color_back)
            lbl.grid(column=1,row=6)
            btns = tki.Button(reports, text="Построить", font=(font, 14),
                                                  fg=color_text, bg=color, command=open_windows)
            btns.grid(column=1,row=7)
            lbl=tki.Label(reports,text="\n        ", font=(font,16), fg=color_text,
                          bg=color_back)
            lbl.grid(column=0,row=0)
            lbl=tki.Label(reports,text="Выберите параметры", font=(font,18), fg=color_text,
                          bg=color)
            lbl.grid(column=1,row=1)
            lbl=tki.Label(reports,text="\nПараметр оси Х", font=(font,16), fg=color_text,
                          bg=color_back)
            lbl.grid(column=1,row=2)
            combo_x = ttk.Combobox(reports,
                                        values=['Выберите параметр',

                                                "Жанр 1",
                                                "Жанр 2",
                                                "Жанр 3",
                                                "Категория",
                                                "Качество",

                                                "Название платформы",

                                                "Страна",
                                                "Оригинал дорожки",
                                                "язык иностранной озвучки",
                                                "язык субтитров"
                                                ],
                                        font=(font,15),state="readonly")
            print(dict(combo_x))
            combo_x.grid(column=1,row=3)
            combo_x.current(0)
            combo_x.bind("<<ComboboxSelected>>")
            lbl=tki.Label(reports,text="\nПараметр оси Y", font=(font,16), fg=color_text,
                          bg=color_back)
            lbl.grid(column=1,row=4)
            combo_y = ttk.Combobox(reports,
                                        values=['Выберите параметр',
                                                "Количество",
                                                "Процент"],
                                        font=(font,15),state="readonly")
            print(dict(combo_y))
            combo_y.grid(column=1,row=5)
            combo_y.current(0)
            combo_y.bind("<<ComboboxSelected>>")
        def rass_diag(event):
            '''
            Автор: Жибуртович Е., Гольцова М.
            Создание окна "Диаграмма рассеивания"

            Parameters
            ----------
            event : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            reports = tki.Tk()
            reports.title("Диаграмма рассеивания")
            reports.geometry('250x300+300+100')
            reports.iconbitmap('application.ico')
            reports["bg"] = color_back
            def open_windows():
                '''
                Автор: Жибуртович Е., Шилова С., Гольцова М.
                Наполнение окна "Диаграмма рассеивания"

                Returns
                -------
                None.

                '''
                if ((combo_x.get() != "Выберите параметр")and(combo_y.get()!= "Выберите параметр")):
                    reports1 = tki.Tk()
                    reports1.title("Рассеивания")
                    reports1.geometry('500x500+300+100')
                    reports1.iconbitmap('application.ico')
                    reports1["bg"] = color_back
                    fig = Figure(figsize = (5, 5),
                                 dpi = 100)
                    plot1 = fig.add_subplot(111)
                    plot1.scatter(x=Basa_no_rep[combo_x.get()], y=Basa_no_rep[combo_y.get()],
                                  color ='hotpink')
                    canvas = FigureCanvasTkAgg(fig,
                                               master = reports1)
                    canvas.draw()
                    canvas.get_tk_widget().pack()
                    toolbar = NavigationToolbar2Tk(canvas,
                                                   reports1)
                    toolbar.pack()
                    canvas.get_tk_widget().pack()
            lbl=tki.Label(reports,text="       ",font=(font,18), fg=color_text, bg=color_back)
            lbl.grid(column=1,row=6)
            btns = tki.Button(reports, text="Построить", font=(font, 14),
                                                  fg=color_text, bg=color, command=open_windows)
            btns.grid(column=1,row=7)
            lbl=tki.Label(reports,text="Выберите параметры",font=(font,18), fg=color_text, bg=color)
            lbl.grid(column=1,row=1)
            lbl=tki.Label(reports,text="\nПараметр оси Х", font=(font,16),
                          fg=color_text, bg=color_back)
            lbl.grid(column=1,row=2)
            combo_x = ttk.Combobox(reports,
                                        values=['Выберите параметр',
                                                "Год",
                                                "Рейтинг",
                                                "Возрастная категория",
                                                "Длительность, мин",
                                                "Количество премий",
                                                "количество языков субтитров",
                                                "Сборы , млн",
                                                "наличие иностранной озвучки"],
                                        font=(font,15),state="readonly")
            print(dict(combo_x))
            combo_x.grid(column=1,row=3)
            combo_x.current(0)
            combo_x.bind("<<ComboboxSelected>>")
            lbl=tki.Label(reports,text="\nПараметр оси Y", font=(font,16),
                          fg=color_text, bg=color_back)
            lbl.grid(column=1,row=4)
            combo_y = ttk.Combobox(reports,
                                        values=['Выберите параметр',
                                                "Год",
                                                "Рейтинг",
                                                "Возрастная категория",
                                                "Длительность, мин",
                                                "Количество премий",
                                                "количество языков субтитров",
                                                "Сборы , млн",
                                                "наличие иностранной озвучки"],
                                        font=(font,15),state="readonly")
            print(dict(combo_y))
            combo_y.grid(column=1,row=5)
            combo_y.current(0)
            combo_y.bind("<<ComboboxSelected>>")
        def box_diag(event):
            '''
            Автор: Жибуртович Е., Гольцова М.
            Создание окна "Диаграмма Бокса-Уискера"

            Parameters
            ----------
            event : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            reports = tki.Tk()
            reports.title("Диаграмма Бокса-Уискера")
            reports.geometry('250x300+300+100')
            reports.iconbitmap('application.ico')
            reports["bg"] = color_back
            def open_windows():
                '''
                Автор: Шилова С., Гольцова М.
                Наполнение окна "Диаграмма Бокса-Уискера"

                Returns
                -------
                None.

                '''
                if ((combo_x.get()!="Выберите параметр")and(combo_y.get() != "Выберите параметр")):
                    reports1 = tki.Tk()
                    reports1.title("Диаграмма Бокса-Уискера")
                    reports1.geometry('500x500+300+100')
                    reports1.iconbitmap('application.ico')
                    reports1["bg"] = color_back
                    fig = Figure(figsize = (5, 5),
                                 dpi = 100)
                    plot1 = fig.add_subplot(111)
                    var=combo_x.get()
                    var2=combo_y.get()
                    un_var=list(set(list(Basa_no_rep[var])))
                    yyy=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
                         [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
                    a=0
                    for i in un_var:
                        z=Basa_no_rep[Basa_no_rep[var]==i]
                        yyy[a]=z[var2]
                        a=a+1
                    yyy=yyy[:(len(set(list((Basa_no_rep[var])))))]
                    massive1=[i+1 for i in range(len(set(list((Basa_no_rep[var])))))]
                    massive2=np.array(un_var)
                    ots_x=10
                    ots_y=10
                    for i in range(len(massive1)):
                        texxxt=str(massive1[i])+' - '+str(massive2[i])
                        lbl=tki.Label(reports1,text=texxxt,font=(font,10),
                                      fg=color_text, bg=color_back)
                        lbl.place(x=ots_x,y=ots_y)
                        ots_y=ots_y+20
                    plot1.boxplot(x=yyy)
                    canvas = FigureCanvasTkAgg(fig,
                                               master = reports1)
                    canvas.draw()
                    canvas.get_tk_widget().pack()
                    toolbar = NavigationToolbar2Tk(canvas,
                                                   reports1)
                    toolbar.pack()
                    canvas.get_tk_widget().pack()
            lbl=tki.Label(reports,text="       ",font=(font,18), fg=color_text, bg=color_back)
            lbl.grid(column=1,row=6)
            btns = tki.Button(reports, text="Применить!", font=(font, 14),
                                          fg=color_text, bg=color, command=open_windows)
            btns.grid(column=1,row=7)
            lbl=tki.Label(reports,text="Выберите параметры",font=(font,18), fg=color_text, bg=color)
            lbl.grid(column=1,row=1)
            lbl=tki.Label(reports,text="\nПараметр оси Х",font=(font,16),
                          fg=color_text, bg=color_back)
            lbl.grid(column=1,row=2)
            combo_x = ttk.Combobox(reports,
                                        values=['Выберите параметр',

                                                "Жанр 1",
                                                "Жанр 2",
                                                "Жанр 3",
                                                "Категория",
                                                "Качество",

                                                "Название платформы",
                                                "Компания",
                                                "Страна",
                                                "Оригинал дорожки",
                                                "язык иностранной озвучки",
                                                "язык субтитров"],
                                        font=(font,15),state="readonly")
            print(dict(combo_x))
            combo_x.grid(column=1,row=3)
            combo_x.current(0)
            combo_x.bind("<<ComboboxSelected>>")
            lbl=tki.Label(reports,text="\nПараметр оси Y", font=(font,16),
                          fg=color_text, bg=color_back)
            lbl.grid(column=1,row=4)
            combo_y = ttk.Combobox(reports,
                                        values=['Выберите параметр',
                                                "Год",
                                                "Рейтинг",
                                                "Возрастная категория",
                                                "Длительность, мин",
                                                "Количество премий",
                                                "Сборы , млн"],
                                        font=(font,15),state="readonly")
            print(dict(combo_y))
            combo_y.grid(column=1,row=5)
            combo_y.current(0)
            combo_y.bind("<<ComboboxSelected>>")
        def gist(event):
            '''
            Автор: Жибуртович Е., Гольцова М.
            Создание окна гистограммы

            Parameters
            ----------
            event : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            reports = tki.Tk()
            reports.title("Гистограмма")
            reports.geometry('250x300+300+100')
            reports.iconbitmap('application.ico')
            reports["bg"] = color_back
            def open_windows():
                '''
                Автор: Шилова С., Гольцова М.
                Наполнение окна "Гистограмма"

                Returns
                -------
                None.

                '''
                if ((combo_x.get() != "Выберите параметр")and(combo_y.get()!= "Выберите параметр")):
                    if (combo_y.get()=='Количество'):
                        den=False
                    else:
                        den=True
                    reports1 = tki.Tk()
                    reports1.title("Гистограмма")
                    reports1.geometry('500x500+300+100')
                    reports1.iconbitmap('application.ico')
                    reports1["bg"] = color_back
                    fig = Figure(figsize = (5, 5), dpi = 100)
                    plot1 = fig.add_subplot(111)
                    plot1.hist(x=Basa_no_rep[combo_x.get()],bins='sturges', density=den)
                    canvas = FigureCanvasTkAgg(fig,
                                               master = reports1)
                    canvas.draw()
                    canvas.get_tk_widget().pack()
                    toolbar = NavigationToolbar2Tk(canvas,
                                                   reports1)
                    toolbar.pack()
                    canvas.get_tk_widget().pack()
            lbl=tki.Label(reports,text="       ",font=(font,18), fg=color_text, bg=color_back)
            lbl.grid(column=1,row=6)
            btns = tki.Button(reports, text="Построить", font=(font, 14),
                                                  fg=color_text, bg=color, command=open_windows)
            btns.grid(column=1,row=7)
            lbl=tki.Label(reports,text="Выберите параметры",font=(font,18), fg=color_text, bg=color)
            lbl.grid(column=1,row=1)
            lbl=tki.Label(reports,text="\nПараметр оси Х", font=(font,16),
                          fg=color_text, bg=color_back)
            lbl.grid(column=1,row=2)
            combo_x = ttk.Combobox(reports,
                                        values=['Выберите параметр',
                                                "Год",
                                                "Рейтинг",
                                                "Возрастная категория",
                                                "Длительность, мин",
                                                "Количество премий",
                                                "количество языков субтитров",
                                                "Сборы , млн",
                                                "наличие иностранной озвучки"],
                                        font=(font,15),state="readonly")
            print(dict(combo_x))
            combo_x.grid(column=1,row=3)
            combo_x.current(0)
            combo_x.bind("<<ComboboxSelected>>")
            lbl=tki.Label(reports,text="\nПараметр оси Y", font=(font,16),
                          fg=color_text, bg=color_back)
            lbl.grid(column=1,row=4)
            combo_y = ttk.Combobox(reports,
                                        values=['Выберите параметр',
                                                'Распространенность',
                                                'Количество'],
                                        font=(font,15),state="readonly")
            print(dict(combo_y))
            combo_y.grid(column=1,row=5)
            combo_y.current(0)
            combo_y.bind("<<ComboboxSelected>>")
        def reports_graph(event):
            '''
            Автор: Жибуртович Е.
            Открытие окон с графическими отчетами

            Parameters
            ----------
            event : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            if combo_g.get() == "Столбчатая диаграмма":
                st_diag(event)
            elif combo_g.get() == "Диаграмма рассеивания":
                rass_diag(event)
            elif combo_g.get() == "Диаграмма Бокса-Уискера":
                box_diag(event)
            elif combo_g.get() == "Гистограмма":
                gist(event)
        def open_reports_cach(event):
            '''
            Автор: Жибуртович Е.
            Открытие окна отчета для качественных атрибутов

            Parameters
            ----------
            event : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            if combo_cach.get() != "Выберите атрибут":
                reports_cach(combo_cach.get())
        def open_reports_col(event):
            '''
            Автор: Жибуртович Е.
            Открытие окна отчета для количественных атрибутов

            Parameters
            ----------
            event : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            if combo_col.get() == "Для всех атрибутов":
                reports_col()
        def open_reports_sv(event):
            '''
            Автор: Жибуртович Е.
            Открытие окна сводной таблицы

            Parameters
            ----------
            event : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            if ((combo_pk.get() != "Выберите атрибут") and (combo_vk.get() != "Выберите атрибут")
                and(combo_pk.get() != combo_vk.get()) and (combo_k.get() != "Выберите атрибут") and
                (combo_m.get() != "Выберите метод")):
                reports_sv(combo_pk.get(),combo_vk.get(),combo_k.get(),combo_m.get())
        lbl=tki.Label(reports,text="          ", font=(font,18), bg=color_back)
        lbl.grid(column=0,row=0)
        lbl=tki.Label(reports,text="Выберите отчет: ", font=(font,18), fg=color_text, bg=color)
        lbl.place(relx=0.23, rely=0.12)
        lbl=tki.Label(reports,text="Примеры графических отчетов:", font=(font,18),
                      fg=color_text, bg=color_back)
        lbl.place(relx=0.65, rely=0.03)
        reports.image1 = PhotoImage(file='4.png')
        lbl = tki.Label(reports, image=reports.image1)
        lbl.place(relx=0.53, rely=0.1, width=650, height=260)
        lbl=tki.Label(reports,text="     ", font=(font,16), bg=color_back)
        lbl.grid(column=0,row=1)
        lbl=tki.Label(reports,text="\n \n Текстовый \nстатистический\n ",
                      font=(font,18), fg=color_text, bg=color_back)
        lbl.grid(column=0,row=2, sticky="w")
        lbl=tki.Label(reports,text="Качественный атрибут", font=(font,16),
                      fg=color_text, bg=color_back)
        lbl.grid(column=1,row=3)
        combo_cach = ttk.Combobox(reports,
                                    values=[
                                            "Выберите атрибут",

                                            "Жанр 1",
                                            "Жанр 2",
                                            "Жанр 3",
                                            "Категория",
                                            "Качество",

                                            "Название платформы",
                                            "Компания",
                                            "Страна",
                                            "Оригинал дорожки",
                                            "язык иностранной озвучки",
                                            "язык субтитров"],
                                    font=(font,15),state="readonly")
        print(dict(combo_cach))
        combo_cach.grid(column=1,row=4)
        combo_cach.current(0)
        combo_cach.bind("<<ComboboxSelected>>", open_reports_cach)
        lbl=tki.Label(reports,text="Количественный атрибут", font=(font,16),
                      fg=color_text, bg=color_back)
        lbl.grid(column=3,row=3)
        combo_col = ttk.Combobox(reports,
                                    values=[
                                            "Не выбрано",
                                            "Для всех атрибутов"],
                                    font=(font,15),state="readonly")
        print(dict(combo_col))
        combo_col.grid(column=3,row=4)
        combo_col.current(0)
        combo_col.bind("<<ComboboxSelected>>", open_reports_col)
        lbl=tki.Label(reports,text="     ", font=(font,16), bg=color_back)
        lbl.grid(column=2,row=4)
        lbl=tki.Label(reports,text="\nСводная таблица\n ", font=(font,18),
                      fg=color_text, bg=color_back)
        lbl.grid(column=0,row=5)
        lbl=tki.Label(reports,text="Первый качественный", font=(font,16),
                      fg=color_text, bg=color_back)
        lbl.grid(column=1,row=6)
        combo_pk = ttk.Combobox(reports,
                                    values=[
                                            "Выберите атрибут",

                                            "Жанр 1",
                                            "Жанр 2",
                                            "Жанр 3",
                                            "Категория",
                                            "Качество",

                                            "Название платформы",
                                            "Компания",
                                            "Страна",
                                            "Оригинал дорожки",
                                            "язык иностранной озвучки",
                                            "язык субтитров"],
                                    font=(font,15),state="readonly")
        print(dict(combo_pk))
        combo_pk.grid(column=1,row=7)
        combo_pk.current(0)
        combo_pk.bind("<<ComboboxSelected>>", open_reports_sv)
        lbl=tki.Label(reports,text="Второй качественный", font=(font,16),
                      fg=color_text, bg=color_back)
        lbl.grid(column=3,row=6)
        combo_vk = ttk.Combobox(reports,
                                    values=[
                                            "Выберите атрибут",

                                            "Жанр 1",
                                            "Жанр 2",
                                            "Жанр 3",
                                            "Категория",
                                            "Качество",

                                            "Название платформы",
                                            "Компания",
                                            "Страна",
                                            "Оригинал дорожки",
                                            "язык иностранной озвучки",
                                            "язык субтитров"],
                                    font=(font,15),state="readonly")
        print(dict(combo_vk))
        combo_vk.grid(column=3,row=7)
        combo_vk.current(0)
        combo_vk.bind("<<ComboboxSelected>>", open_reports_sv)
        lbl=tki.Label(reports,text="Количественный", font=(font,16), fg=color_text, bg=color_back)
        lbl.grid(column=5,row=6)
        combo_k = ttk.Combobox(reports,
                                    values=[
                                            "Выберите атрибут",
                                            "Год",
                                            "Рейтинг",
                                            "Возрастная категория",
                                            "Длительность, мин",
                                            "Количество премий",
                                            "количество языков субтитров",
                                            "Сборы , млн",
                                            "наличие иностранной озвучки"],
                                    font=(font,15),state="readonly")
        print(dict(combo_k))
        combo_k.grid(column=5,row=7)
        combo_k.current(0)
        combo_k.bind("<<ComboboxSelected>>", open_reports_sv)
        lbl=tki.Label(reports,text="     ", font=(font,16), bg=color_back)
        lbl.grid(column=4,row=7)
        lbl=tki.Label(reports,text="     ", font=(font,16), bg=color_back)
        lbl.grid(column=6,row=7)
        lbl=tki.Label(reports,text="Метод агрегации", font=(font,16), fg=color_text, bg=color_back)
        lbl.grid(column=7,row=6)
        combo_m = ttk.Combobox(reports,
                                    values=[
                                            "Выберите метод",
                                            "Среднее",
                                            "Суммирование"],
                                    font=(font,15),state="readonly")
        print(dict(combo_m))
        combo_m.grid(column=7,row=7)
        combo_m.current(0)
        combo_m.bind("<<ComboboxSelected>>", open_reports_sv)
        lbl=tki.Label(reports,text="\nГрафические", font=(font,18), fg=color_text, bg=color_back)
        lbl.grid(column=0,row=8, sticky="w")
        lbl=tki.Label(reports,text="Тип графика", font=(font,16), fg=color_text, bg=color_back)
        lbl.grid(column=1,row=9)
        combo_g = ttk.Combobox(reports,
                                    values=[
                                            "Выберите отчет",
                                            "Столбчатая диаграмма",
                                            "Диаграмма рассеивания",
                                            "Диаграмма Бокса-Уискера",
                                            "Гистограмма"],
                                    font=(font,15),state="readonly")
        print(dict(combo_g))
        combo_g.grid(column=1,row=10)
        combo_g.current(0)
        combo_g.bind("<<ComboboxSelected>>", reports_graph)
        lbl=tki.Label(reports,text=" ", font=(font,16), bg=color_back)
        lbl.grid(column=0,row=11)
        lbl=tki.Label(reports,text=" \n \n ", font=(font,16), bg=color_back)
        lbl.grid(column=0,row=11)
    def open_bd():
        '''
        Автор: Гольцова М.
        Создание окна измения БД

        Returns
        -------
        None.

        '''
        bd=tki.Tk()
        bd.title('Изменить базу данных')
        bd.geometry('1000x600+10+10')
        bd.iconbitmap('application.ico')
        mainmenu = Menu(bd)
        bd.config(menu=mainmenu)
        mainmenu.add_command(label='На главную страницу',
                             command=lambda:[bd.destroy(), open_main()])
        mainmenu.add_command(label='Отчеты', command=lambda:[bd.destroy(), open_reports()])
        mainmenu.add_command(label='Подборки', command=lambda:[bd.destroy(), open_selections()])
        mainmenu.add_command(label='Настройки', command=lambda:[bd.destroy(), open_settings()])
        bd["bg"] = color_back
        global Basa
        def redaq():
            '''
            Автор: Шилова С.

            Returns
            -------
            None.


            обработка нажатия кнопки - редактирование'''
            try:
                selected = tv1.focus()
                temp = tv1.item(selected, 'values')
                print(temp)
                sal_up = message.get()
                sal_up2=message2.get()
                sal_up3=message3.get()
                sal_up4=message4.get()
                sal_up5=message5.get()
                sal_up6=message6.get()
                sal_up7=message7.get()
                sal_up8=message8.get()
                sal_up9=message9.get()
                sal_up10=message10.get()
                sal_up11=message11.get()
                sal_up12=message12.get()
                sal_up13=message13.get()
                sal_up14=message14.get()
                sal_up15=message15.get()
                sal_up16=message16.get()
                sal_up17=message17.get()
                sal_up18=message18.get()
                sal_up19=message19.get()
                sal_up20=message20.get()
                sal_up21=message21.get()
                sal_up22=message22.get()
                sal_up23=message23.get()
                sal_up24=message24.get()
                sal_up25=message25.get()
                massive=[sal_up, sal_up2, sal_up3,sal_up4,sal_up5,
                         sal_up6, sal_up7, sal_up8,sal_up9,sal_up10,
                         sal_up11, sal_up12, sal_up13,sal_up14,sal_up15,
                         sal_up16, sal_up17, sal_up18,sal_up19,sal_up20,
                         sal_up21, sal_up22, sal_up23,sal_up24,sal_up25]
                if((checking.checking_empty_string(sal_up)==False) or
                   checking.checking_number(sal_up)==False):
                    sal_up=temp[0]
                if(checking.checking_empty_string(sal_up2)==False):
                    sal_up2=temp[1]
                if((checking.checking_empty_string(sal_up3)==False) or
                   checking.checking_string(sal_up3)==False):
                    sal_up3=temp[2]
                if((checking.checking_empty_string(sal_up4)==False) or
                   checking.checking_string(sal_up4)==False):
                    sal_up4=temp[3]
                if((checking.checking_empty_string(sal_up5)==False) or
                   checking.checking_string(sal_up5)==False):
                    sal_up5=temp[4]
                if((checking.checking_empty_string(sal_up6)==False) or
                   checking.checking_string(sal_up6)==False):
                    sal_up6=temp[5]
                if((checking.checking_empty_string(sal_up7)==False) or
                   (checking.checking_number(sal_up7)==False) or
                   checking.checking_conditions(int(sal_up7),2022,1895)==False):
                    sal_up7=temp[6]
                if((checking.checking_empty_string(sal_up8)==False) or
                       (checking.checking_positive(sal_up8)==False) or
                       checking.checking_conditions(int(sal_up8),10,0)==False):
                    sal_up8=temp[7]
                if((checking.checking_empty_string(sal_up9)==False) or
                       (checking.checking_number(sal_up9)==False) or
                       checking.checking_conditions(int(sal_up9),18,0)==False):
                    sal_up9=temp[8]
                if((checking.checking_empty_string(sal_up10)==False) or
                       (checking.checking_number(sal_up10)==False)):
                    sal_up10=temp[9]
                if((checking.checking_empty_string(sal_up11)==False) or
                           (checking.checking_number(sal_up11)==False)):
                    sal_up11=temp[10]
                if((checking.checking_empty_string(sal_up12)==False) or
                   (checking.checking_string(sal_up12)==False)):
                    sal_up12=temp[11]
                if((checking.checking_empty_string(sal_up13)==False) or
                       (checking.checking_number(sal_up13)==False)):
                    sal_up13=temp[12]
                if((checking.checking_empty_string(sal_up14)==False) or
                   (checking.checking_string(sal_up14)==False)):
                    sal_up14=temp[13]
                if((checking.checking_empty_string(sal_up15)==False) or
                           (checking.checking_number(sal_up15)==False)):
                    sal_up15=temp[14]
                if((checking.checking_empty_string(sal_up16)==False) or
                           (checking.checking_number(sal_up16)==False)):
                    sal_up16=temp[15]
                if((checking.checking_empty_string(sal_up17)==False) or
                           (checking.checking_number(sal_up17)==False)):
                    sal_up17=temp[16]
                if((checking.checking_empty_string(sal_up18)==False) or
                           (checking.checking_number(sal_up18)==False)):
                    sal_up18=temp[17]
                if(checking.checking_empty_string(sal_up19)==False):
                    sal_up19=temp[18]
                if(checking.checking_empty_string(sal_up20)==False):
                    sal_up20=temp[19]
                if((checking.checking_empty_string(sal_up21)==False) or
                   checking.checking_string(sal_up21)==False):
                    sal_up21=temp[20]
                if((checking.checking_empty_string(sal_up22)==False) or
                   checking.checking_string(sal_up22)==False):
                    sal_up22=temp[21]
                if(checking.checking_empty_string(sal_up23)==False):
                    sal_up23=temp[22]
                if((checking.checking_empty_string(sal_up24)==False) or
                   checking.checking_string(sal_up24)==False):
                    sal_up24=temp[23]
                if((checking.checking_empty_string(sal_up25)==False) or
                   checking.checking_string(sal_up25)==False):
                    sal_up25=temp[24]
                tv1.item(selected, values=(sal_up, sal_up2, sal_up3,sal_up4,sal_up5,
                                           sal_up6, sal_up7, sal_up8,sal_up9,sal_up10,
                                           sal_up11, sal_up12, sal_up13,sal_up14,sal_up15,
                                           sal_up16, sal_up17, sal_up18,sal_up19,sal_up20,
                                           sal_up21, sal_up22, sal_up23,sal_up24,sal_up25))
                zzz={'№ фильма' : sal_up,
                     'Название' : sal_up2,
                     'Жанр 1': sal_up3,
                     'Жанр 2': sal_up4,
                     'Жанр 3': sal_up5,
                     'Категория': sal_up6,
                     'Год': sal_up7,
                     'Рейтинг': sal_up8,
                     'Возрастная категория': sal_up9,
                     'Длительность, мин': sal_up10,
                     'Количество премий': sal_up11,
                     'Качество': sal_up12,
                     'количество языков субтитров': sal_up13,
                     'Режиссёр ': sal_up14,
                     'Сборы , млн': sal_up15,
                     '№ компании': sal_up16,
                     'код платформ': sal_up17,
                     'id платформы': sal_up18,
                     'Название платформы': sal_up19,
                     'Компания': sal_up20,
                     'Страна': sal_up21,
                     'Оригинал дорожки': sal_up22,
                     'наличие иностранной озвучки': sal_up23,
                     'язык иностранной озвучки': sal_up24,
                     'язык субтитров': sal_up25}
                #selected_item = tv1.selection()[0]
                #ind=int(selected_item[1:],16)-1
                #global Basa
                #Basa=Basa.drop(ind)
                #Basa=Basa.append(zzz, ignore_index=True)
            except IndexError:
                mb.showerror(
                    "Ошибка",
                    "Строка не выбрана")
        def store():
            '''
            Автор: Шилова С.
            сохранение  БД
            Returns
            -------
            None.

            '''
            global Basa
            Basa.to_excel('new_base.xlsx')
            mb.showinfo("Информация", 'Данные сохранены в таблицу new_base')
        def del_list():
            '''
            Автор: Шилова С.

            Returns
            -------
            None.

            '''
            try:
                selected_item = tv1.selection()[0]
                tv1.delete(selected_item)
                ind=int(selected_item[1:],16)-1
                global Basa
                Basa=Basa.drop(ind)
            except IndexError:
                mb.showerror(
                 "Ошибка",
                 "Строка не выбрана")
        def dop():
            '''
            Автор: Шилова С.
            обработка нажатия кнопки добавить запись
            Returns
            -------
            None.

            '''
            selected = tv1.focus()
            temp = tv1.item(selected, 'values')
            print(temp)
            sal_up = message.get()
            sal_up2=message2.get()
            sal_up3=message3.get()
            sal_up4=message4.get()
            sal_up5=message5.get()
            sal_up6=message6.get()
            sal_up7=message7.get()
            sal_up8=message8.get()
            sal_up9=message9.get()
            sal_up10=message10.get()
            sal_up11=message11.get()
            sal_up12=message12.get()
            sal_up13=message13.get()
            sal_up14=message14.get()
            sal_up15=message15.get()
            sal_up16=message16.get()
            sal_up17=message17.get()
            sal_up18=message18.get()
            sal_up19=message19.get()
            sal_up20=message20.get()
            sal_up21=message21.get()
            sal_up22=message22.get()
            sal_up23=message23.get()
            sal_up24=message24.get()
            sal_up25=message25.get()
            a=True
            massive=[sal_up, sal_up2, sal_up3,sal_up4,sal_up5,
                     sal_up6, sal_up7, sal_up8,sal_up9,sal_up10,
                     sal_up11, sal_up12, sal_up13,sal_up14,sal_up15,
                     sal_up16, sal_up17, sal_up18,sal_up19,sal_up20,
                     sal_up21, sal_up22, sal_up23,sal_up24,sal_up25]
            if((checking.checking_empty_string(sal_up)==False) or
               checking.checking_number(sal_up)==False):
                a=False
            if(checking.checking_empty_string(sal_up2)==False):
                a=False
            if((checking.checking_empty_string(sal_up3)==False) or
               checking.checking_string(sal_up3)==False):
                a=False
            if((checking.checking_empty_string(sal_up4)==False) or
               checking.checking_string(sal_up4)==False):
                a=False
            if((checking.checking_empty_string(sal_up5)==False) or
               checking.checking_string(sal_up5)==False):
                a=False
            if((checking.checking_empty_string(sal_up6)==False) or
               checking.checking_string(sal_up6)==False):
                a=False
            if((checking.checking_empty_string(sal_up7)==False) or
               (checking.checking_number(sal_up7)==False) or
               checking.checking_conditions(int(sal_up7),2022,1895)==False):
                a=False
            if((checking.checking_empty_string(sal_up8)==False) or
                   (checking.checking_positive(sal_up8)==False) or
                   checking.checking_conditions(int(sal_up8),10,0)==False):
                a=False
            if((checking.checking_empty_string(sal_up9)==False) or
                   (checking.checking_number(sal_up9)==False) or
                   checking.checking_conditions(int(sal_up9),18,0)==False):
                a=False
            if((checking.checking_empty_string(sal_up10)==False) or
                   (checking.checking_number(sal_up10)==False)):
                a=False
            if((checking.checking_empty_string(sal_up11)==False) or
                       (checking.checking_number(sal_up11)==False)):
                a=False
            if((checking.checking_empty_string(sal_up12)==False) or
               (checking.checking_string(sal_up12)==False)):
                a=False
            if((checking.checking_empty_string(sal_up13)==False) or
                   (checking.checking_number(sal_up13)==False)):
                a=False
            if((checking.checking_empty_string(sal_up14)==False) or
               (checking.checking_string(sal_up14)==False)):
                a=False
            if((checking.checking_empty_string(sal_up15)==False) or
                       (checking.checking_number(sal_up15)==False)):
                a=False
            if((checking.checking_empty_string(sal_up16)==False) or
                       (checking.checking_number(sal_up16)==False)):
                a=False
            if((checking.checking_empty_string(sal_up17)==False) or
                       (checking.checking_number(sal_up17)==False)):
                a=False
            if((checking.checking_empty_string(sal_up18)==False) or
                       (checking.checking_number(sal_up18)==False)):
                a=False
            if(checking.checking_empty_string(sal_up19)==False):
                a=False
            if(checking.checking_empty_string(sal_up20)==False):
                a=False
            if((checking.checking_empty_string(sal_up21)==False) or
               checking.checking_string(sal_up21)==False):
                a=False
            if((checking.checking_empty_string(sal_up22)==False) or
               checking.checking_string(sal_up22)==False):
                a=False
            if(checking.checking_empty_string(sal_up23)==False):
                a=False
            if((checking.checking_empty_string(sal_up24)==False) or
               checking.checking_string(sal_up24)==False):
                a=False
            if((checking.checking_empty_string(sal_up25)==False) or
               checking.checking_string(sal_up25)==False):
                a=False
            if(a==True):
                tv1.item(selected, values=(sal_up, sal_up2, sal_up3,sal_up4,sal_up5,
                                           sal_up6, sal_up7, sal_up8,sal_up9,sal_up10,
                                           sal_up11, sal_up12, sal_up13,sal_up14,sal_up15,
                                           sal_up16, sal_up17, sal_up18,sal_up19,sal_up20,
                                           sal_up21, sal_up22, sal_up23,sal_up24,sal_up25))
                zzz={'№ фильма' : sal_up,
                     'Название' : sal_up2,
                     'Жанр 1': sal_up3,
                     'Жанр 2': sal_up4,
                     'Жанр 3': sal_up5,
                     'Категория': sal_up6,
                     'Год': sal_up7,
                     'Рейтинг': sal_up8,
                     'Возрастная категория': sal_up9,
                     'Длительность, мин': sal_up10,
                     'Количество премий': sal_up11,
                     'Качество': sal_up12,
                     'количество языков субтитров': sal_up13,
                     'Режиссёр ': sal_up14,
                     'Сборы , млн': sal_up15,
                     '№ компании': sal_up16,
                     'код платформ': sal_up17,
                     'id платформы': sal_up18,
                     'Название платформы': sal_up19,
                     'Компания': sal_up20,
                     'Страна': sal_up21,
                     'Оригинал дорожки': sal_up22,
                     'наличие иностранной озвучки': sal_up23,
                     'язык иностранной озвучки': sal_up24,
                     'язык субтитров': sal_up25}
                global Basa
                Basa=Basa.append(zzz, ignore_index=True)
            else:
                mb.showerror(
                        "Ошибка",
                        "Введены не все данные или введены некорректно")
        #кнопки управления
        bottom = tki.LabelFrame(bd,text="Управление",font=(font, 14), fg=color_text, bg=color_back)
        bottom.pack(side=tki.TOP)
        btn = tki.Button(bottom, text='Сохранить', font=(font, 14),
                         fg=color_text, bg=color, command=store)
        btn.grid(row=0, column=1)
        btn1 = tki.Button(bottom, text='Добавить запись', font=(font, 14),
                         fg=color_text, bg=color, command=dop)
        btn1.grid(row=0, column=2)
        btn1 = tki.Button(bottom, text='Редактировать запись', font=(font, 14),
                         fg=color_text, bg=color,command=redaq)
        btn1.grid(row=0, column=3)
        btn1 = tki.Button(bottom, text='Удалить запись', font=(font, 14),
                         fg=color_text, bg=color, command=del_list)
        btn1.grid(row=0, column=4)
        message = StringVar()
        message_entry = Entry(textvariable=message)
        y=10
        message_entry.place(x=10,y=y)
        y=y+25
        message2 = StringVar()
        message_entry2 = Entry(textvariable=message2)
        message_entry2.place(x=10,y=y)
        y=y+25
        message3 = StringVar()
        message_entry3= Entry(textvariable=message3)
        message_entry3.place(x=10,y=y)
        y=y+25
        message4 = StringVar()
        message_entry4 = Entry(textvariable=message4)
        message_entry4.place(x=10,y=y)
        y=y+25
        message5 = StringVar()
        message_entry5 = Entry(textvariable=message5)
        message_entry5.place(x=10,y=y)
        y=y+25
        message6 = StringVar()
        message_entry6 = Entry(textvariable=message6)
        message_entry6.place(x=10,y=y)
        y=y+25
        message7 = StringVar()
        message_entry7 = Entry(textvariable=message7)
        message_entry7.place(x=10,y=y)
        y=y+25
        message8 = StringVar()
        message_entry8 = Entry(textvariable=message8)
        message_entry8.place(x=10,y=y)
        y=y+25
        message9 = StringVar()
        message_entry9 = Entry(textvariable=message9)
        message_entry9.place(x=10,y=y)
        y=y+25
        message10 = StringVar()
        message_entry10 = Entry(textvariable=message10)
        message_entry10.place(x=10,y=y)
        y=y+25
        message11 = StringVar()
        message_entry11 = Entry(textvariable=message11)
        message_entry11.place(x=10,y=y)
        y=y+25
        message12 = StringVar()
        message_entry12 = Entry(textvariable=message12)
        message_entry12.place(x=10,y=y)
        y=y+25
        message13 = StringVar()
        message_entry13 = Entry(textvariable=message13)
        message_entry13.place(x=10,y=y)
        y=y+25
        message14 = StringVar()
        message_entry14 = Entry(textvariable=message14)
        message_entry14.place(x=10,y=y)
        y=y+25
        message15 = StringVar()
        message_entry15 = Entry(textvariable=message15)
        message_entry15.place(x=10,y=y)
        y=y+25
        message16 = StringVar()
        message_entry16 = Entry(textvariable=message16)
        message_entry16.place(x=10,y=y)
        y=y+25
        message17 = StringVar()
        message_entry17 = Entry(textvariable=message17)
        message_entry17.place(x=10,y=y)
        y=y+25
        message18 = StringVar()
        message_entry18 = Entry(textvariable=message18)
        message_entry18.place(x=10,y=y)
        y=y+25
        message19 = StringVar()
        message_entry19 = Entry(textvariable=message19)
        message_entry19.place(x=10,y=y)
        y=y+25
        message20 = StringVar()
        message_entry20 = Entry(textvariable=message20)
        message_entry20.place(x=10,y=y)
        y=y+25
        message21 = StringVar()
        message_entry21 = Entry(textvariable=message21)
        message_entry21.place(x=10,y=y)
        y=y+25
        message22 = StringVar()
        message_entry22 = Entry(textvariable=message22)
        message_entry22.place(x=10,y=y)
        y=y+25
        message23 = StringVar()
        message_entry23 = Entry(textvariable=message23)
        message_entry23.place(x=10,y=y)
        y=y+25
        message24 = StringVar()
        message_entry24 = Entry(textvariable=message24)
        message_entry24.place(x=10,y=y)
        y=y+25
        message25 = StringVar()
        message_entry25 = Entry(textvariable=message25)
        message_entry25.place(x=10,y=y)
        frame1 = tki.LabelFrame(bd, text="База Данных")
        frame1.place(x=140,y=80,height=500, width=920)
        tv1 = ttk.Treeview(frame1)
        tv1.place(relheight=1, relwidth=1)
        treescrolly = tki.Scrollbar(frame1, orient="vertical", command=tv1.yview)
        treescrollx = tki.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
        tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
        treescrollx.pack(side="bottom", fill="x")
        treescrolly.pack(side="right", fill="y")
        tv1["column"] = list(Basa.columns)
        tv1["show"] = "headings"
        for column in tv1["columns"]:
            tv1.heading(column, text=column)
            df_rows = Basa.to_numpy().tolist()
            for row in df_rows:
                tv1.insert("", "end", values=row)
    fam = text_reports.simple_family(Basa,0,'приключения','мультфильм')
    tsen= text_reports.simple_tsen(Basa, 40, 1, 8)
    lan = text_reports.simple_language(Basa, 'английские', 'английский', 'английский')
    love = text_reports.simple_anyone(Basa, 'мелодрама', 'США', 1990, 2022)
    fun = text_reports.simple_anyone(Basa, 'комедия', 'Россия', 1970, 1999)
    def open_selections():
        '''
        Автор: Гольцова М.
        Создание окна подборок

        Returns
        -------
        None.

        '''
        selec=tki.Tk()
        selec.title('Подборки')
        selec.geometry('1000x600+10+10')
        selec.iconbitmap('application.ico')
        mainmenu = Menu(selec)
        selec.config(menu=mainmenu)
        selec.resizable(width=False, height= False)
        selec.image = PhotoImage(file='family.png')
        bg_logo = Label(selec, image=selec.image)
        bg_logo.place(x=100, y=300)
        mainmenu.add_command(label='На главную страницу',
                             command=lambda:[selec.destroy(), open_main()])
        mainmenu.add_command(label='Изменить БД', command=lambda:[selec.destroy(), open_bd()])
        mainmenu.add_command(label='Отчеты', command=lambda:[selec.destroy(), open_reports()])
        mainmenu.add_command(label='Настройки', command=lambda:[selec.destroy(), open_settings()])
        lbl=tki.Label(selec,text="Не знаете, что посмотреть? Выберите, кто Вы:",
                      fg=color_text, bg=color_back, font=(font,30), height=3,
                      borderwidth=2, relief="sunken")
        lbl.place(x=50,y=65)
        lbl.place(x=50,y=65)
        def podb(tex, op):
            '''
            Автор: Гольцова М.

            Parameters
            ----------
            tex : TYPE
                DESCRIPTION.
            op : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            n = tki.Tk()
            n.title(tex)
            n["bg"] = color_back
            n.geometry('1000x700+10+10')
            if (not (op.empty)):
                frame1 = tki.LabelFrame(n, text="Подборочки")
                frame1.place(x=10,y=10,height=400, width=970)
                name=tki.StringVar()
                name1=tki.Entry(n, textvariable=name)
                name1.place(x=400, y=530, height=70, width=300)
                nnn = tki.Label(n, text="Введите название файла для сохранения", font=(font, 16),
                                fg=color_text, bg=color_back)
                nnn.place(x=380, y=520)
                def saving():
                    '''
                    Автор:Гольцова М.

                    Returns
                    -------
                    None.

                    '''
                    if (name1.get()==("")):
                        mb.showerror("Ошибка", "Вы не ввели название файла!")
                    else:
                        path_name = files.filename(text, (name1.get()+'.xlsx'))
                        files.save_table(path_name, 'excel', op)
                    n.destroy()
                btns = tki.Button(n, text="Сохранить отчет", font=(font, 14),
                                  fg=color_text, bg=color, command=saving)
                btns.place(x=100, y=500, height=100, width=200)
                tv1 = ttk.Treeview(frame1)
                tv1.place(relheight=1, relwidth=1)
                treescrolly = tki.Scrollbar(frame1, orient="vertical", command=tv1.yview)
                treescrollx = tki.Scrollbar(frame1, orient="horizontal", command=tv1.xview)
                tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
                treescrollx.pack(side="bottom", fill="x")
                treescrolly.pack(side="right", fill="y")
                tv1["column"] = list(op.columns)
                tv1["show"] = "headings"
                for column in tv1["columns"]:
                    tv1.heading(column, text=column)
                    df_rows = op.to_numpy().tolist()
                    for row in df_rows:
                        tv1.insert("", "end", values=row)
            elif (op==False):
                frame1 = tki.Label(n, text="Таких фильмов больше нет", font=(font, 16))
                frame1.place(x=40,y=80,height=500, width=920)
        btnn = tki.Button(selec, text="Семьянин",  fg=color_text, bg=color, padx="20",
                          pady="8", font="font, 16",
                          command=lambda:[podb("Подборка      семьянин", fam)])
        btnn.place(x=100, y=200, width=120, height=50)
        btn2 = tki.Button(selec, text="Романтик",  fg=color_text, bg=color, padx="20",
                          pady="8", font="font, 16",
        command=lambda:[podb("Подборка романтик: современные американские мелодрамы",
                                               love)])
        btn2.place(x=250, y=200, width=120, height=50)
        selec.image1 = PhotoImage(file='heart.png')
        bg_logo1 = Label(selec, image=selec.image1)
        bg_logo1.place(x=250, y=305)
        btn3 = tki.Button(selec, text="Весельчак", fg=color_text, bg=color, padx="20",
                          pady="8", font="font, 16",
                          command=lambda:[podb("Подборка весельчак: старые русские комедии", fun)])
        btn3.place(x=400, y=200, width=120, height=50)
        selec.image2 = PhotoImage(file='smile.png')
        bg_logo2 = Label(selec, image=selec.image2)
        bg_logo2.place(x=405, y=305)
        btn4 = tki.Button(selec, text="Учу языки", fg=color_text, bg=color, padx="20", pady="8",
                          font="font, 16",
                          command=lambda:[podb("Подборка изучение английского", lan)])
        btn4.place(x=550, y=200, width=120, height=50)
        selec.image3 = PhotoImage(file='lang.png')
        bg_logo2 = Label(selec, image=selec.image3)
        bg_logo2.place(x=560, y=305)
        btn5 = tki.Button(selec, text="Ценитель", fg=color_text, bg=color, padx="20", pady="8",
                          font="font, 16", command=lambda:[podb("Подборка ценитель", tsen)])
        btn5.place(x=700, y=200, width=120, height=50)
        selec.image4 = PhotoImage(file='medal.png')
        bg_logo2 = Label(selec, image=selec.image4)
        bg_logo2.place(x=710, y=305)
    def open_settings():
        '''
        Автор: Жибуртович Е.
        Создание окна настроек

        Returns
        -------
        None.

        '''
        sett=tki.Tk()
        sett.title('Настройки')
        sett.geometry('1420x600+0+100')
        sett.iconbitmap('application.ico')
        mainmenu = Menu(sett)
        sett.config(menu=mainmenu)
        mainmenu.add_command(label='На главную страницу',
                             command=lambda:[sett.destroy(), open_main()])
        mainmenu.add_command(label='Изменить БД', command=lambda:[sett.destroy(), open_bd()])
        mainmenu.add_command(label='Отчеты', command=lambda:[sett.destroy(), open_reports()])
        mainmenu.add_command(label='Подборки', command=lambda:[sett.destroy(), open_selections()])
        sett["bg"] = color_back
        def change_times(event):
            '''
            Автор: Жибуртович Е.
            Изменение шрифта на Times New Roman

            Parameters
            ----------
            event : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            path_setting=open('setting.py', 'r')
            lines = path_setting.readlines()
            lines[11] = 'font = "Times"' + '\n'
            path_setting.close()
            save_changes = open('setting.py', 'w')
            save_changes.writelines(lines)
            save_changes.close()
        def change_tahoma(event):
            '''
            Автор: Жибуртович Е.
            Изменение шрифта на Tahoma

            Parameters
            ----------
            event : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            path_setting=open('setting.py', 'r')
            lines = path_setting.readlines()
            lines[11] = 'font = "Tahoma"' + '\n'
            path_setting.close()
            save_changes = open('setting.py', 'w')
            save_changes.writelines(lines)
            save_changes.close()
        def change_arial(event):
            '''
            Автор: Жибуртович Е.
            Изменение шрифта на Arial

            Parameters
            ----------
            event : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            path_setting=open('setting.py', 'r')
            lines = path_setting.readlines()
            lines[11] = 'font = "Arial"' + '\n'
            path_setting.close()
            save_changes = open('setting.py', 'w')
            save_changes.writelines(lines)
            save_changes.close()
        def change_calibri(event):
            '''
            Автор: Жибуртович Е.
            Изменение шрифта на Calibri

            Parameters
            ----------
            event : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            path_setting=open('setting.py', 'r')
            lines = path_setting.readlines()
            lines[11] = 'font = "Calibri"' + '\n'
            path_setting.close()
            save_changes = open('setting.py', 'w')
            save_changes.writelines(lines)
            save_changes.close()
        def change_light():
            '''
            Автор: Жибуртович Е.
            Изменение оформления на светлое

            Returns
            -------
            None.

            '''
            path_setting=open('setting.py', 'r')
            lines = path_setting.readlines()
            lines[13] = 'color_back = "White"' + '\n'
            lines[15] = 'color = "thistle3"' + '\n'
            lines[17] = 'color_text = "Black"' + '\n'
            path_setting.close()
            save_changes = open('setting.py', 'w')
            save_changes.writelines(lines)
            save_changes.close()
        def change_dark():
            '''
            Автор: Жибуртович Е.
            Изменение оформления на темное

            Returns
            -------
            None.

            '''
            path_setting=open('setting.py', 'r')
            lines = path_setting.readlines()
            lines[13] = 'color_back = "Grey"' + '\n'
            lines[15] = 'color = "Black"' + '\n'
            lines[17] = 'color_text = "White"' + '\n'
            path_setting.close()
            save_changes = open('setting.py', 'w')
            save_changes.writelines(lines)
            save_changes.close()
        def change_pink():
            '''
            Автор: Жибуртович Е.
            Изменение оформления на розовое

            Returns
            -------
            None.

            '''
            path_setting=open('setting.py', 'r')
            lines = path_setting.readlines()
            lines[13] = 'color_back = "misty rose"' + '\n'
            lines[15] = 'color = "pink1"' + '\n'
            lines[17] = 'color_text = "VioletRed4"' + '\n'
            path_setting.close()
            save_changes = open('setting.py', 'w')
            save_changes.writelines(lines)
            save_changes.close()
        def change_blue():
            '''
            Автор: Жибуртович Е.
            Изменение оформления на синее

            Returns
            -------
            None.

            '''
            path_setting=open('setting.py', 'r')
            lines = path_setting.readlines()
            lines[13] = 'color_back = "LightBlue2"' + '\n'
            lines[15] = 'color = "SteelBlue1"' + '\n'
            lines[17] = 'color_text = "Blue4"' + '\n'
            path_setting.close()
            save_changes = open('setting.py', 'w')
            save_changes.writelines(lines)
            save_changes.close()
        def change_yellow():
            '''
            Автор: Жибуртович Е.
            Изменение оформления на желтое

            Returns
            -------
            None.

            '''
            path_setting=open('setting.py', 'r')
            lines = path_setting.readlines()
            lines[13] = 'color_back = "khaki"' + '\n'
            lines[15] = 'color = "yellow"' + '\n'
            lines[17] = 'color_text = "saddle brown"' + '\n'
            path_setting.close()
            save_changes = open('setting.py', 'w')
            save_changes.writelines(lines)
            save_changes.close()
        def change_green():
            '''
            Автор: Жибуртович Е.
            Изменение оформления на зеленое

            Returns
            -------
            None.

            '''
            path_setting=open('setting.py', 'r')
            lines = path_setting.readlines()
            lines[13] = 'color_back = "PaleGreen1"' + '\n'
            lines[15] = 'color = "OliveDrab1"' + '\n'
            lines[17] = 'color_text = "dark green"' + '\n'
            path_setting.close()
            save_changes = open('setting.py', 'w')
            save_changes.writelines(lines)
            save_changes.close()
        def change_type_to_p(event):
            '''
            Автор: Жибуртович Е.
            Изменение типа базы на двоичный

            Parameters
            ----------
            event : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            path_setting=open('setting.py', 'r')
            lines = path_setting.readlines()
            lines[7] = 'types_data = "pickle"' + '\n'
            lines[8] = 'types_file= "pickle"' + '\n'
            path_setting.close()
            save_changes = open('setting.py', 'w')
            save_changes.writelines(lines)
            save_changes.close()
        def change_type_to_e(event):
            '''
            Автор: Жибуртович Е.
            Изменение типа базы на Excel

            Parameters
            ----------
            event : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            path_setting=open('setting.py', 'r')
            lines = path_setting.readlines()
            lines[7] = 'types_data = "excel"' + '\n'
            lines[8] = 'types_file= "excel"' + '\n'
            path_setting.close()
            save_changes = open('setting.py', 'w')
            save_changes.writelines(lines)
            save_changes.close()
        #Функция сохранения настроек в файл
        def save_configurations_font(event):
            '''
            Автор: Жибуртович Е.
            Изменение шрифта

            Parameters
            ----------
            event : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            if combo.get() == "Times New Roman":
                change_times(event)
            elif combo.get() == "Tahoma":
                change_tahoma(event)
            elif combo.get() == "Arial":
                change_arial(event)
            elif combo.get() == "Calibri":
                change_calibri(event)
        def save_configurations_design(event):
            '''
            Автор: Жибуртович Е.
            Изменение оформления

            Parameters
            ----------
            event : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            if combo_d.get() == "Светлая тема":
                change_light()
            elif combo_d.get() == "Темная тема":
                change_dark()
            elif combo_d.get() == "Синяя тема":
                change_blue()
            elif combo_d.get() == "Розовая тема":
                change_pink()
            elif combo_d.get() == "Желтая тема":
                change_yellow()
            elif combo_d.get() == "Зеленая тема":
                change_green()
        def save_configurations_type(event):
            '''
            Автор: Жибуртович Е.
            Изменение типа базы

            Parameters
            ----------
            event : TYPE
                DESCRIPTION.

            Returns
            -------
            None.

            '''
            if combo_t.get() == "Excel":
                change_type_to_e(event)
            elif combo_t.get() == "Двоичный":
                change_type_to_p(event)
        lbl=tki.Label(sett,text=" ", font=('Times',20), fg=color_text, bg=color_back)
        lbl.grid(column=1,row=1)
        lbl=tki.Label(sett,text="          ", font=('Times',20), fg=color_text, bg=color_back)
        lbl.grid(column=2,row=1)
        lbl=tki.Label(sett,text="                   ", font=('Times',20), fg=color_text,
                      bg=color_back)
        lbl.grid(column=0,row=1)
        lbl=tki.Label(sett,text="Изменить оформление", font=(font,20), fg=color_text, bg=color_back)
        lbl.grid(column=0,row=2,sticky="w")
        combo_d = ttk.Combobox(sett,
                                    values=[
                                            "Светлая тема",
                                            "Темная тема",
                                            "Синяя тема",
                                            "Розовая тема",
                                            "Желтая тема",
                                            "Зеленая тема"],
                                    font=(font,18),state="readonly")
        print(dict(combo_d))
        combo_d.grid(column=2,row=2, sticky="w")
        combo_d.current(0)
        combo_d.bind("<<ComboboxSelected>>", save_configurations_design)
        lbl=tki.Label(sett,text=" ", font=(font,20), fg=color_text, bg=color_back)
        lbl.grid(column=1,row=3)

        lbl=tki.Label(sett,text="Шрифт", font=(font,20), fg=color_text, bg=color_back)
        lbl.grid(column=0,row=4, sticky="w")
        combo = ttk.Combobox(sett,
                                    values=[
                                            "Tahoma",
                                            "Times New Roman",
                                            "Arial",
                                            "Calibri"],
                                    font=(font,18),state="readonly")
        print(dict(combo))
        combo.grid(column=2,row=4, sticky="w")
        combo.current(0)
        combo.bind("<<ComboboxSelected>>", save_configurations_font)
        lbl=tki.Label(sett,text=" ", font=(font,20),fg=color_text, bg=color_back)
        lbl.grid(column=1,row=5)
        lbl=tki.Label(sett,text="Директория базы данных",font=(font,20),fg=color_text,bg=color_back)
        lbl.grid(column=0,row=6, sticky="w")
        lbl=tki.Label(sett,text=base_path, font=(font,18), fg='Black', bg='White')
        lbl.grid(column=2,row=6, sticky="ew")
        folder_path = StringVar()
        lbl1 = Label(master=sett,textvariable=folder_path, fg=color_text, bg=color_back)
        lbl1.grid(row=6, column=4)
        button2 = Button(text="Browse", command=browse_button, fg=color_text, bg=color)
        button2.grid(row=6, column=5)
        lbl=tki.Label(sett,text=" ", font=(font,20), fg=color_text, bg=color_back)
        lbl.grid(column=1,row=7)
        lbl=tki.Label(sett,text="Тип данных", font=(font,20,), fg=color_text, bg=color_back)
        lbl.grid(column=0,row=8, sticky="w")
        combo_t = ttk.Combobox(sett,
                                    values=[
                                            "Excel",
                                            "Двоичный"],
                                    font=(font,18),state="readonly")
        print(dict(combo_t))
        combo_t.grid(column=2,row=8, sticky="w")
        combo_t.current(0)
        combo_t.bind("<<ComboboxSelected>>", save_configurations_type)
        lbl=tki.Label(sett,text=" ", font=(font,20),fg=color_text, bg=color_back)
        lbl.grid(column=1,row=9)
        def info():
            '''
            Автор: Жибуртович Е.
            Создание окна-подсказки

            Returns
            -------
            None.

            '''
            mb.showinfo("Информация", "Для применения настроек \nперезапустите приложение")
        btn=tki.Button(sett,text="Сохранить",font=(font,15),fg=color_text, bg=color,
                       command=lambda:[info(), sett.destroy()])
        btn.place(x=420, y=390, width=190, height=60)
    mainw=tki.Tk()
    mainw.title('Кинопомощник')
    mainw.geometry('626x417+10+10')
    mainw.iconbitmap('application.ico')
    mainw.resizable(width=False, height= False)
    mainw.image = PhotoImage(file='fon1.png')
    bg_logo = Label(mainw, image=mainw.image)
    bg_logo.grid(row=0, column=0)
    lbl = tki.Button(mainw, text="Добро пожаловать!", font=(font,20,'bold'), borderwidth='4',
                     fg=color, bg='black', command=lambda:[mainw.destroy(), open_main()])
    lbl.place(x=320, y=120, width=300, height=130)
    mainw.mainloop()
f()
