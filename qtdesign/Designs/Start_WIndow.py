from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Start_Window(object):
    def setupUi(self, Start_Window):
        Start_Window.setObjectName("Start_Window")
        Start_Window.resize(540, 400)
        font = QtGui.QFont()
        font.setPointSize(8)
        Start_Window.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Start_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_day = QtWidgets.QPushButton(self.centralwidget)
        self.btn_day.setGeometry(QtCore.QRect(165, 80, 210, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_day.setFont(font)
        self.btn_day.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_day.setObjectName("btn_day")
        self.btn_period = QtWidgets.QPushButton(self.centralwidget)
        self.btn_period.setGeometry(QtCore.QRect(165, 200, 210, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_period.setFont(font)
        self.btn_period.setObjectName("btn_period")
        Start_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Start_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 23))
        self.menubar.setObjectName("menubar")
        Start_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Start_Window)
        self.statusbar.setObjectName("statusbar")
        Start_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Start_Window)
        QtCore.QMetaObject.connectSlotsByName(Start_Window)

    def retranslateUi(self, Start_Window):
        _translate = QtCore.QCoreApplication.translate
        Start_Window.setWindowTitle(_translate("Start_Window", "ExcelParser"))
        self.btn_day.setText(_translate("Start_Window", "Информация за день"))
        self.btn_period.setText(_translate("Start_Window", "Информация за период"))
