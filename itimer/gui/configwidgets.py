import sys
from PyQt5 import QtWidgets



class SignalSelectionWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white")
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.btn1 = QtWidgets.QPushButton("1")
        self.btn2 = QtWidgets.QPushButton("2")
        self.btn3 = QtWidgets.QPushButton("+")
        self.user_signal_lb = QtWidgets.QLabel("3")
        self.lb = QtWidgets.QLabel("сигнал")
        self.hbox.addWidget(self.lb)
        self.hbox.addWidget(self.btn1)
        self.hbox.addWidget(self.btn2)
        self.hbox.addWidget(self.btn3)
        self.hbox.addWidget(self.user_signal_lb)

class IntervalSelectionWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white")
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.lb = QtWidgets.QLabel("сигнал")
        self.hbox.addWidget(self.lb)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = SignalSelectionWidget()
    main.show()
    sys.exit(app.exec_())