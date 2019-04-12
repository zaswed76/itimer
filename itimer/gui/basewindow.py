import sys
from PyQt5 import QtWidgets, QtGui


class Widget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #E6E6E6")




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Widget()
    main.show()
    sys.exit(app.exec_())