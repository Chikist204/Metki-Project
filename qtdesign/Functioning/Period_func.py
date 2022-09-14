from PyQt5.QtWidgets import QMainWindow
from Functioning import Start_func
from Designs import Period_Window
from PyQt5 import QtCore
from constants import HOST, FILE, MONTHS, URL1
import os
from bs4 import BeautifulSoup
import requests as rq
import csv


class Period(QMainWindow, Period_Window.Ui_Period_WIndow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_back.clicked.connect(self.back)
        self.btn_compile.clicked.connect(self.compile)
        self.pushButton.clicked.connect(self.get_date_from)
        self.pushButton_2.clicked.connect(self.get_date_til)

    def back(self):
        self.close()
        self.win = Start_func.Main()
        self.win.show()

    def compile(self):
        self.metka = self.chosen_metka.toPlainText()
        try:
            self.date_period()
        except Exception as ex:
            print(ex)

    def get_date_from(self):
        self.date1 = list(reversed((str(self.calendarWidget.selectedDate())[19::])[:-1].split(', ')))
        self.date_from.setGeometry(QtCore.QRect(30, 170, 150, 21))
        self.date_from.setText(f"Выбрана дата: {'.'.join(self.date1)}")

    def get_date_til(self):
        self.date2 = list(reversed((str(self.calendarWidget.selectedDate())[19::])[:-1].split(', ')))
        self.date_til.setGeometry(QtCore.QRect(30, 260, 150, 21))
        self.date_til.setText(f"Выбрана дата: {'.'.join(self.date2)}")

    def date_period(self):
        day = self.date1[0]
        month = self.date1[1]
        year = self.date1[2]
        day2 = self.date2[0]
        month2 = self.date2[1]
        year2 = self.date2[2]
        metka = self.metka
        s = rq.Session()
        r = s.post(URL1, data={'login-email': '89052796658', 'login-password': '89052796658'})

        table = []
        if int(month2) - int(month) == 0:
            for i in range(int(day), int(day2) + 1):
                url4 = HOST + '/demo6/devices.php?date=' + str(year) + '-' + str(month) + '-' + str(
                    i) + '&minor=' + str(
                    metka)
                soup = BeautifulSoup(s.post(url4).text, "lxml")
                items = soup.find('table', id='example-datatables').find_all('tr')
                for i in range(1, len(items)):
                    table.append({
                        'metka': str(items[i])[8:20],
                        'date': str(items[i])[29:39],
                        'from': str(items[i])[48:56],
                        'till': str(items[i])[65:73],
                        'zone': str(items[i])[82:(len(items[i]) - 15)],
                    })
            self.save_file(table, FILE)
            os.startfile(FILE)
        else:
            for i in range(int(day), int(MONTHS[month]) + 1):
                url4 = HOST + '/demo6/devices.php?date=' + str(year) + '-' + str(month) + '-' + str(
                    i) + '&minor=' + str(
                    metka)
                soup = BeautifulSoup(s.post(url4).text, "lxml")
                items = soup.find('table', id='example-datatables').find_all('tr')
                for i in range(1, len(items)):
                    table.append({
                        'metka': str(items[i])[8:20],
                        'date': str(items[i])[29:39],
                        'from': str(items[i])[48:56],
                        'till': str(items[i])[65:73],
                        'zone': str(items[i])[82:(len(items[i]) - 15)],
                    })

            for i in range(1, int(day2) + 1):
                url4 = HOST + '/demo6/devices.php?date=' + str(year) + '-' + str(month2) + '-' + str(
                    i) + '&minor=' + str(
                    metka)
                soup = BeautifulSoup(s.post(url4).text, "lxml")
                items = soup.find('table', id='example-datatables').find_all('tr')
                for i in range(1, len(items)):
                    table.append({
                        'metka': str(items[i])[8:20],
                        'date': str(items[i])[29:39],
                        'from': str(items[i])[48:56],
                        'till': str(items[i])[65:73],
                        'zone': str(items[i])[82:(len(items[i]) - 15)],
                    })
            self.save_file(table, FILE)
            os.startfile(FILE)

    def save_file(self, table, path):
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Метка', 'Дата', 'Время от', 'Время до', 'Зона'])
            for i in table:
                writer.writerow([i['metka'], i['date'], i['from'], i['till'], i['zone']])
