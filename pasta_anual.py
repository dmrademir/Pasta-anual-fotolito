"""
Módulo para criação de pasta annual para a organização mensal e diária
dos arquivos de layouts e de fotolitos (arquivos de saída) para impressão.
Está localizada na pasta '!LAYOUTS'.
"""
import calendar
import os


def create_month_folder():

    for i in folders:
        try:
            os.mkdir(f'{path}{i}')
        except FileExistsError:
            continue


def create_fotolito_folder():
    for i in folder:
        os.mkdir(f'{path}{i}/ 00 - FOTOLITOS')


def create_days():
    month_days = calendar.monthcalendar(year,month)
    for i in month_days:
        week.append(i[0])
        week.append(i[1])
        week.append(i[2])
        week.append(i[3])
        week.append(i[4])


folders = ("01 - JANEIRO", "02 - FEVEREIRO", "03 - MARÇO",
           "04 - ABRIL", "05 - MAIO", "06 - JUNHO",
           "07 - JULHO", "08 - AGOSTO", "09 - SETEMBRO",
           "10 - OUTUBRO", "11 - NOVEMBRO", "12 - DEZEMBRO")
month = 1
year = 2020 #int(input('Digite o ano base: '))
path = 'E:/ARTE/ADEMIR/LAYOUTS DO DIA/ANO/'
week = list()
for x in week:
    if x == 0:
        week.remove(x)

for mes in folders:
    try:
        os.mkdir(f'{path}{mes}/')
    except FileExistsError:
        continue

    for days in week:
        try:
            if days == 0:
                os.mkdir(f'{path}{mes}/{days:02} - FOTOLITOS')
            else:
                os.mkdir(f'{path}{mes}/{days:02} - {month:02}')
        except FileExistsError:
            continue
