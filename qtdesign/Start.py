import sys
from Functioning import Start_func
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Start_func.Main()
    ex.show()
    sys.exit(app.exec_())
