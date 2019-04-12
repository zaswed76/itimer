import sys
from PyQt5 import QtWidgets

class Widget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: grey")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Widget()
    main.show()
    sys.exit(app.exec_())