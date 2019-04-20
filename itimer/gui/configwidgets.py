import sys
from PyQt5 import QtWidgets, QtCore


class OptionNameLabel(QtWidgets.QLabel):
    def __init__(self, *__args):
        super().__init__(*__args)


class SignalSelectionWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white")
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.btn1 = QtWidgets.QPushButton("1")
        self.btn2 = QtWidgets.QPushButton("2")
        self.btn3 = QtWidgets.QPushButton("+")
        self.user_signal_lb = QtWidgets.QLabel("metallica.mp3")
        self.lb = OptionNameLabel("сигнал")
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
        self.lb = OptionNameLabel("интервал")
        self.interval = QtWidgets.QTimeEdit()
        self.interval.setDisplayFormat("HH:mm:ss")

        self.hbox.addWidget(self.lb)
        self.hbox.addWidget(self.interval)

class DurationSignalWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white")
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.lb = OptionNameLabel("длительность")
        self.duration = QtWidgets.QSpinBox()


        self.hbox.addWidget(self.lb)
        self.hbox.addWidget(self.duration)

class AutostartWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white")
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.lb = OptionNameLabel("автостарт")
        self.autostar = QtWidgets.QCheckBox()


        self.hbox.addWidget(self.lb)
        self.hbox.addWidget(self.autostar)

class SelectingCyclingWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white")
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.lb = OptionNameLabel("зациклить")
        self.cycling = QtWidgets.QCheckBox()


        self.hbox.addWidget(self.lb)
        self.hbox.addWidget(self.cycling)

class VolumeWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white")
        self.hbox = QtWidgets.QHBoxLayout(self)
        self.lb = OptionNameLabel("громкость")
        self.volume = QtWidgets.QSlider(QtCore.Qt.Horizontal)


        self.hbox.addWidget(self.lb)
        self.hbox.addWidget(self.volume)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = SignalSelectionWidget()
    main.show()
    sys.exit(app.exec_())