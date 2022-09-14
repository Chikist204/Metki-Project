from PyQt5.QtWidgets import QMainWindow
from bs4 import BeautifulSoup
from Designs import Day_Window
from Functioning import Start_func
from constants import HOST, URL1, FILE
import csv
import os
import requests as rq


class Day(QMainWindow, Day_Window.Ui_Day_WIndow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_back.clicked.connect(self.back)
        self.btn_compile.clicked.connect(self.compile)

    def back(self):
        self.close()
        self.win = Start_func.Main()
        self.win.show()

    def compile(self):
        try:
            self.get_date()
        except Exception as ex:
            print(ex)

    def get_date(self):
        metka = self.textEdit.toPlainText()
        s = list(reversed((str(self.calendarWidget.selectedDate())[19::])[:-1].split(', ')))
        self.date_day(metka, s)

    def date_day(self, m, d):
        day = d[0]
        month = d[1]
        year = d[2]
        metka = m
        url3 = HOST + '/demo6/devices.php?date=' + year + '-' + month + '-' + day + '&minor=' + str(metka)
        s = rq.Session()
        r = s.post(URL1, data={'login-email': '89052796658', 'login-password': '89052796658'})

        soup = BeautifulSoup(s.post(url3).text, "lxml")
        items = soup.find('table', id='example-datatables').find_all('tr')
        table = []
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
