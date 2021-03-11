import calendar
import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog


# Funções para criação da Interface
def CreateWidget():
    labelyear = Label(root, text='ANO DA PASTA:')
    labelyear.grid(row=0, column=0, padx=3, pady=3)
    root_sourceYear = Entry(root, width=50, textvariable=AnodaPasta)
    root_sourceYear.grid(row=0, column=2, padx=5, pady=5, columnspan=2)

    label_Destination = Label(root, text='LOCAL DA PASTA:')
    label_Destination.grid(row=1, column=0, padx=5, pady=5)
    root_Destination = Entry(root, width=50, textvariable=LocaldaPasta)
    root_Destination.grid(row=1, column=2, padx=5, pady=5, columnspan=2)
    button_browse = Button(root, text='Localizar', width=15)
    button_browse.grid(row=1, column=4, padx=3, pady=3, columnspan=2)


root = tk.Tk()

root.title('Pasta Anual')
root.geometry('720x100')
LocaldaPasta = StringVar()  # Local onde a Pasta Anual será criada
AnodaPasta = StringVar()  # Nome da Pasta Anual. O ano a ser criado

CreateWidget()

root.mainloop()


# Funções para criação das Pastas
def create_year_folder():
    directory = [year]
    for i in directory:
        try:
            os.mkdir(f'{os_path}/!{i}')
        except FileExistsError:
            continue


def create_month_folder():
    for i in folders:
        try:
            os.mkdir(f'{path}{i}')
        except FileExistsError:
            continue


def create_fotolito_folder():
    for i in folders:
        try:
            os.mkdir(f'{path}{i}/ 00 - FOTOLITOS')
        except FileExistsError:
            continue


def create_days():
    months = 1
    index = 0
    while months <= 12:
        month_days = calendar.monthcalendar(year, months)
        for i in month_days:
            weeks.append(i[0])
            weeks.append(i[1])
            weeks.append(i[2])
            weeks.append(i[3])
            weeks.append(i[4])
        week_days = list(set(weeks.copy()))
        weeks.clear()
        if week_days[0] == 0:
            week_days.remove(0)
        for days in week_days:
            try:
                os.mkdir(f'{path}{folders[index]}/{days:02} - {months:02}')
            except FileExistsError:
                continue
        week_days.clear()
        months += 1
        index += 1


# Interface

# Program
folders = ("01 - JANEIRO", "02 - FEVEREIRO", "03 - MARÇO",
           "04 - ABRIL", "05 - MAIO", "06 - JUNHO",
           "07 - JULHO", "08 - AGOSTO", "09 - SETEMBRO",
           "10 - OUTUBRO", "11 - NOVEMBRO", "12 - DEZEMBRO")
year = int(input("Informe o ANO:  "))
os_path = '/home/ademir'  # Local onde a pasta do "ano" será criada
path = f'{os_path}/!{year}/'
weeks = list()

create_year_folder()
create_month_folder()
create_fotolito_folder()
create_days()
