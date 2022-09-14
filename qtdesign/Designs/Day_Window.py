from PyQt5 import QtCore, QtWidgets


class Ui_Day_WIndow(object):
    def setupUi(self, Day_WIndow):
        Day_WIndow.setObjectName("Day_WIndow")
        Day_WIndow.resize(630, 420)
        self.centralwidget = QtWidgets.QWidget(Day_WIndow)
        self.centralwidget.setObjectName("centralwidget")
        self.metka = QtWidgets.QLabel(self.centralwidget)
        self.metka.setGeometry(QtCore.QRect(185, 10, 70, 40))
        self.metka.setObjectName("metka")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(260, 10, 100, 31))
        self.textEdit.setObjectName("textEdit")
        self.date_lable = QtWidgets.QLabel(self.centralwidget)
        self.date_lable.setGeometry(QtCore.QRect(20, 60, 170, 40))
        self.date_lable.setObjectName("date_lable")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(200, 60, 400, 220))
        self.calendarWidget.setObjectName("calendarWidget")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(30, 310, 161, 61))
        self.btn_back.setObjectName("btn_back")
        self.btn_compile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_compile.setGeometry(QtCore.QRect(440, 310, 161, 61))
        self.btn_compile.setObjectName("btn_compile")
        Day_WIndow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Day_WIndow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 26))
        self.menubar.setObjectName("menubar")
        Day_WIndow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Day_WIndow)
        self.statusbar.setObjectName("statusbar")
        Day_WIndow.setStatusBar(self.statusbar)

        self.retranslateUi(Day_WIndow)
        QtCore.QMetaObject.connectSlotsByName(Day_WIndow)

    def retranslateUi(self, Day_WIndow):
        _translate = QtCore.QCoreApplication.translate
        Day_WIndow.setWindowTitle(_translate("Day_WIndow", "MainWindow"))
        self.metka.setText(_translate("Day_WIndow",
                                      "<html><head/><body><p><span style=\" font-size:14pt;\">Метка:</span></p></body></html>"))
        self.date_lable.setText(_translate("Day_WIndow",
                                           "<html><head/><body><p><span style=\" font-size:14pt;\">Выберите дату:</span></p></body></html>"))
        self.btn_back.setToolTip(_translate("Day_WIndow",
                                            "<html><head/><body><p><span style=\" font-size:12pt;\">Назад</span></p></body></html>"))
        self.btn_back.setText(_translate("Day_WIndow", "Назад"))
        self.btn_compile.setText(_translate("Day_WIndow", "Сформировать"))
