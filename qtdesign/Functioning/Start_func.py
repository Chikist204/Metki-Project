from Designs import Day_Window
from Designs import Period_Window
from PyQt5.QtWidgets import QApplication, QMainWindow
from Designs import Start_WIndow
from Functioning import Day_func, Period_func


class Main(Start_WIndow.Ui_Start_Window, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_day.clicked.connect(self.day)
        self.btn_period.clicked.connect(self.period)

    def day(self):
        self.hide()
        self.win = Day_func.Day()
        self.win.show()

    def period(self):
        try:
            self.hide()
            self.win = Period_func.Period()
            self.win.show()
        except Exception as ex:
            print(ex)
